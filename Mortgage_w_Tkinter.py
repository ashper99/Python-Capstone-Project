# This is a mortgage program which will utilize Tkinter as the GUI.

import numpy as np
import pandas as pd
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog, Tk
import locale


from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib


def choice():
    """This give the user the options for the direction of the program"""

    if module.get() == "Mortgage Calculation":
        mortgagecalc()
    elif module.get() == "Refinance":
        refinancecalc()
    elif module.get() == "extrapayment":
        extrapaycalc()
    elif module.get() == "proceeds":
        proceedscalc()


def end_program1():
    """This ends the program"""
    new_file.destroy()


# Main program

""" This is the first window the user encounters.  The window gives one of four options to choose"""

new_file = Tk()
new_file.title("Finance Calculator")
new_file.geometry("800x400")

# add formatting for currency

locale.setlocale(locale.LC_ALL, "en_US.UTF-8")

# create the welcome label and the choices
mortgage_label1 = Label(
    new_file, text="Welcome to the mortgage calculator.", font=("Arial", 20)
)
mortgage_label2 = Label(
    new_file, text="Please choose one of the options below.", font=("Arial", 20)
)
mortgage_label1.grid(row=0, column=0, columnspan=2)
mortgage_label2.grid(row=1, column=0, columnspan=2, padx=(40, 0), pady=(0, 20))

# Create buttons to choose the program
module = StringVar()
module.set(False)

mortgage = Radiobutton(
    new_file, text="Mortgage Calculator", variable=module, value="Mortgage Calculation"
)
refinance = Radiobutton(
    new_file, text="Mortgage Loan Refinance", variable=module, value="Refinance"
)
extra_payment = Radiobutton(
    new_file, text="Extra Payment", variable=module, value="extrapayment"
)
proceedscalc = Radiobutton(
    new_file, text="Proceeds from sale", variable=module, value="proceeds"
)

choose = Button(new_file, text="Enter", command=choice)

# Insert Buttons

mortgage.grid(row=2, column=0, padx=10, sticky="W")
refinance.grid(row=3, column=0, padx=10, sticky="W")
extra_payment.grid(row=4, column=0, padx=10, sticky="W")
proceedscalc.grid(row=5, column=0, padx=10, sticky="W")
choose.grid(row=6, column=1, pady=20, ipadx=20, sticky="W")

# button used to end program

end_program = Button(new_file, text="Close", command=end_program1)
end_program.grid(row=6, column=1, pady=20, ipadx=20, sticky="E")


def save(mortgage_result):
    """The user is given the option to save the ammortization file"""

    file_path = filedialog.asksaveasfilename(
        filetypes=[("Excel file", ".xlsx"), ("CSV file", ".csv")],
        defaultextension=".xlsx",
    )
    if file_path:
        if file_path.endswith(".csv"):
            mortgage_result.to_csv(file_path, index=False)
        else:
            mortgage_result.to_excel(file_path, index=False)
        messagebox.showinfo("showinfo", "File Saved")


def return_file(mortgage_calculator):
    """This is the action completed when the user clicks close on the result frame"""

    mortgage_calculator.withdraw()
    new_file.deiconify()


def calculate_result(
    mortgage_calculator,
    verify_frame,
    update_principal,
    update_interest,
    update_term,
    update_downpayment,
    calculate_frame,
):
    """The call to calculate and show the results"""

    # Verfies the correct formatting is input

    try:
        verify_principal1 = int(update_principal.get())
        verify_interest1 = float(update_interest.get())
        verify_term1 = int(update_term.get())
        verify_downpayment1 = float(update_downpayment.get())
        if verify_principal1 <= 0:
            messagebox.showerror(
                "Principal Error", "Please enter a positive whole number"
            )
            return
        elif verify_interest1 < 0:
            messagebox.showerror("Interest Error", "Please enter a valid interest rate")
            return
        elif verify_interest1 > 20:
            messagebox.showerror("error", "Please enter a valid interest rate")
            return
        elif verify_term1 <= 0:
            messagebox.showerror("error", "Please enter a valid term in years")
            return
        elif verify_term1 >= 51:
            messagebox.showerror("error", "Please enter a valid term in years")
            return
        elif verify_downpayment1 < 0:
            messagebox.showerror("error", "Please enter a valid down payment")
            return
        elif verify_downpayment1 > 50:
            messagebox.showerror("error", "Please enter a valid down payment")
            return
        else:
            pass
    except ValueError:
        messagebox.showerror("error", "Please enter a whole number")
        return

    calculate_frame.pack(fill="both", expand=1)
    verify_frame.pack_forget()

    # creating lists for dataframe use

    monthly_principal = []
    interest_paid = []
    running_balance = []

    # making the calculations

    month_term = verify_term1 * 12
    monthly_interest = 1 + (verify_interest1) / (12 * 100)
    principal_amt = verify_principal1 - (
        verify_principal1 * (verify_downpayment1 / 100)
    )
    monthly_payment = (
        principal_amt
        * (monthly_interest**month_term)
        * (1 - monthly_interest)
        / (1 - monthly_interest**month_term)
    )

    # calculate monthly interest and principal

    totalamount = principal_amt  # placeholder

    for i in range(1, month_term + 1):
        monthint = totalamount * (monthly_interest - 1)
        totalamount = round(totalamount - (monthly_payment - monthint), 2)
        interest_paid = np.append(interest_paid, monthint)
        running_balance = np.append(running_balance, totalamount)
    running_balance[-1] = 0

    np.set_printoptions(suppress=True)

    # calculate total interest paid

    totalinterest = 0
    for i in interest_paid:
        totalinterest += i

    # calculate total principal paid

    total_mortgage = principal_amt + totalinterest

    # calculate monthly principal payment

    for j in interest_paid:
        monthly_principal1 = monthly_payment - j
        monthly_principal = np.append(monthly_principal, monthly_principal1)

    # calculate beginning balance

    begin_balance = [285000]

    for i in running_balance[:-1]:
        begin_balance = np.append(begin_balance, i)

    # adding formatting

    verify_principal1 = locale.currency(verify_principal1, grouping=True)
    monthly_payment = locale.currency(monthly_payment, grouping=True)
    totalinterest = locale.currency(totalinterest, grouping=True)
    total_mortgage = locale.currency(total_mortgage, grouping=True)

    # creating the DataFrame

    results = LabelFrame(calculate_frame, width=100, height=100)
    results.pack(pady=(0, 70), padx=20, side=LEFT)
    results1 = Label(results, text="Mortgage Results", font=("Arial", 12))
    results1.grid(row=0, column=0, columnspan=2)
    saleprice = Label(results, text="Sales Price")
    saleprice.grid(row=1, column=0, pady=(10, 0), sticky="W")
    saleprice2 = Label(results, text=verify_principal1)
    saleprice2.grid(row=1, column=1, pady=(10, 0), sticky="E")
    int_result = Label(results, text="Interest Rate")
    int_result.grid(row=2, column=0, sticky="W")
    int_result1 = Label(results, text=str(verify_interest1) + "%")
    int_result1.grid(row=2, column=1, sticky="E")
    term_result = Label(results, text="Mortgage Term")
    term_result.grid(row=3, column=0, sticky="W")
    term_result1 = Label(results, text=verify_term1)
    term_result1.grid(row=3, column=1, sticky="E")
    downpayment_result = Label(results, text="Down Payment")
    downpayment_result.grid(row=4, column=0, sticky="W")
    downpayment_result1 = Label(results, text=str(verify_downpayment1) + "%")
    downpayment_result1.grid(row=4, column=1, sticky="E")
    monthlypayment_result = Label(results, text="Monthly Payment")
    monthlypayment_result.grid(row=5, column=0, sticky="W")
    monthlypayment1_result = Label(results, text=monthly_payment)
    monthlypayment1_result.grid(row=5, column=1, sticky="E")
    totalinterest_result = Label(results, text="Total Interest")
    totalinterest_result.grid(row=6, column=0, sticky="W")
    totalinterest_result1 = Label(results, text=totalinterest)
    totalinterest_result1.grid(row=6, column=1, sticky="E")
    totalpaid_result = Label(results, text="Total Paid")
    totalpaid_result.grid(row=7, column=0, sticky="W")
    totalpaid_result1 = Label(results, text=total_mortgage)
    totalpaid_result1.grid(row=7, column=1, sticky="E")
    result_title1 = Label(
        calculate_frame, text="Mortgage Calculated", font=("Arial", 20)
    )
    result_title1.pack(anchor="nw", padx=(60, 0), pady=(10, 60))

    # create DataFrame

    month_num = []
    for months in range(1, month_term + 1):
        month_num = np.append(month_num, months)
    month_num = month_num.astype(int)

    # columns array

    result_data = {
        "Beginning Balance": begin_balance,
        "Principal Paid": monthly_principal,
        "Interest Paid": interest_paid,
        "Ending Balance": running_balance,
    }

    # format currency for dataframe

    mortgage_result = pd.DataFrame(result_data)
    for i in result_data.keys():
        mortgage_result[i] = mortgage_result[i].map(locale.currency)
    mortgage_result = mortgage_result.set_index(month_num)

    # create graph

    y1 = result_data["Principal Paid"]
    y2 = result_data["Interest Paid"]
    x = month_num
    graph = Figure(figsize=(6, 4))
    ax = graph.add_subplot(111)
    ax.set_title("Principal vs Interest Over Life of Loan")
    ax.set_ylabel("Principal and Interest")
    ax.set_xlabel("Months")
    ax.plot(x, y1, y2)
    ax.legend(["Principal", "Interest"], fontsize=10)
    matplotlib.rcParams["figure.autolayout"] = True
    chart = FigureCanvasTkAgg(graph, calculate_frame)
    chart.get_tk_widget().pack(pady=(20, 0))

    # create save and close buttons

    save_button = Label(
        calculate_frame,
        text="Press Save to save to Excel or CSV.  Press Close to return to main screen",
    )
    save_button.pack(side=BOTTOM, padx=(0, 120))
    btnsave = Button(
        calculate_frame, text="Save", command=lambda: save(mortgage_result)
    )
    btnsave.pack(side=LEFT, padx=200, pady=(10, 10), ipadx=20)
    btnclose = Button(
        calculate_frame, text="Close", command=lambda: return_file(mortgage_calculator)
    )
    btnclose.pack(side=LEFT, padx=(0, 150), ipadx=(20), pady=(10, 10))


def verification(
    mortgage_calculator,
    verify_frame,
    principal,
    interest,
    term,
    downpayment,
    mortgage_calculator1,
    calculate_frame,
):
    """The verification frame to ensure that the values the user entered are corect and no changes need to be made"""

    # checking for errors

    try:
        verify_principal = int(principal.get())
        verify_interest = float(interest.get())
        verify_term = int(term.get())
        verify_downpayment = float(downpayment.get())
        if verify_principal <= 0:
            messagebox.showerror(
                "Purchase Price Error", "Please enter a positive whole number"
            )
            return
        elif verify_interest < 0:
            messagebox.showerror("Interest Error", "Please enter a valid interest rate")
            return
        elif verify_interest > 20:
            messagebox.showerror("Interest Error", "Please enter a valid interest rate")
            return
        elif verify_term <= 0:
            messagebox.showerror("Term Error", "Please enter a valid term in years")
            return
        elif verify_term >= 51:
            messagebox.showerror("Term Error", "Please enter a valid term in years")
            return
        elif verify_downpayment < 0:
            messagebox.showerror(
                "Down Payment Error", "Please enter a valid down payment"
            )
            return
        elif verify_downpayment > 50:
            messagebox.showerror(
                "Down Payment Error", "Please enter a valid down payment"
            )
            return
        else:
            pass
    except ValueError:
        messagebox.showerror("Value Error", "Please enter a valid number")
        return

    # open a new frame to verify information entered

    verify_frame.pack(fill="both", expand=1)
    mortgage_calculator1.pack_forget()

    # give user option to make changes or keep existing

    verifylabelone = Label(
        verify_frame, text="Please verify the information provided", font=("Arial", 20)
    )
    verifylabelone.grid(row=0, column=1)
    verifylabeltwo = Label(
        verify_frame,
        text="If correct, press submit, otherwise make",
        font=("Arial", 20),
    )
    verifylabeltwo.grid(row=1, column=1)
    verifylabelthree = Label(
        verify_frame, text="corrections and press submit", font=("Arial", 20)
    )
    verifylabelthree.grid(row=2, column=1)

    # create entry widget showing values entered

    update_principal = Entry(verify_frame, width=20)
    update_principal.grid(row=3, column=1, pady=(20, 0), padx=20, ipadx=50)
    update_interest = Entry(verify_frame, width=20)
    update_interest.grid(row=4, column=1, padx=20, pady=(5, 0), ipadx=50)
    update_term = Entry(verify_frame, width=20)
    update_term.grid(row=5, column=1, padx=20, pady=(5, 0), ipadx=50)
    update_downpayment = Entry(verify_frame, width=20)
    update_downpayment.grid(row=6, column=1, padx=20, pady=(5, 0), ipadx=50)

    # add labels to show on screen

    update_principal_label = Label(verify_frame, text="Verify Purchase Price")
    update_principal_label.grid(row=3, column=0, pady=(20, 0), padx=(80, 0), sticky="W")
    update_interest_label = Label(verify_frame, text="Verify Interest")
    update_interest_label.grid(row=4, column=0, padx=(80, 0), pady=(5, 0), sticky="W")
    update_term_label = Label(verify_frame, text="Verify Yearly Terms")
    update_term_label.grid(row=5, column=0, padx=(80, 0), pady=(5, 0), sticky="W")
    update_downpayment_label = Label(verify_frame, text="Down Payment")
    update_downpayment_label.grid(
        row=6, column=0, padx=(80, 0), pady=(5, 0), sticky="W"
    )

    # show the values within the entry fields

    update_principal.insert(5, principal.get())
    update_interest.insert(5, interest.get())
    update_term.insert(5, term.get())
    update_downpayment.insert(5, downpayment.get())

    # create the submit button

    submit_button = Button(
        verify_frame,
        text="Submit",
        command=lambda: calculate_result(
            mortgage_calculator,
            verify_frame,
            update_principal,
            update_interest,
            update_term,
            update_downpayment,
            calculate_frame,
        ),
    )
    submit_button.grid(row=7, column=1, pady=(20, 0))


def mortgagecalc():
    """The new window is opened when the user chooses the first mortgage option from the main window"""

    new_file.withdraw()
    mortgage_calculator = Toplevel()
    mortgage_calculator.title("Mortgage Calculator")
    mortgage_calculator.geometry("1000x600")

    mortgage_calculator1 = LabelFrame(mortgage_calculator)
    mortgage_calculator1.pack(fill="both", expand=1)

    # introduction line
    mortgage_label1 = Label(
        mortgage_calculator1, text="Please enter the information", font=("Arial", 20)
    )
    mortgage_label2 = Label(
        mortgage_calculator1,
        text="to calculate your monthly payment",
        font=("Arial", 20),
    )
    mortgage_label1.grid(row=0, column=0, columnspan=2, padx=40)
    mortgage_label2.grid(row=1, column=0, columnspan=2, padx=40, pady=(0, 20))

    # adding the input fields
    principal = IntVar()
    interest = DoubleVar()
    term = IntVar()
    downpayment = DoubleVar()

    principal = Entry(mortgage_calculator1, width=20)
    principal.grid(row=3, column=1, padx=20, pady=(0, 5), ipadx=50)
    interest = Entry(mortgage_calculator1, width=20)
    interest.grid(row=4, column=1, pady=(0, 5), ipadx=50)
    term = Entry(mortgage_calculator1, width=20)
    term.grid(row=5, column=1, pady=(0, 5), ipadx=50)
    downpayment = Entry(mortgage_calculator1, width=20)
    downpayment.grid(row=6, column=1, pady=(0, 5), ipadx=50)

    # Create input labels

    principal_label = Label(
        mortgage_calculator1,
        text="Enter purchase price as a whole number",
        padx=40,
    )
    principal_label.grid(row=3, column=0, padx=40, pady=(0, 5), sticky="W")
    principal.insert(1, "example 300000")
    interest_label = Label(
        mortgage_calculator1,
        text="Enter interest as a percentage",
        padx=40,
    )
    interest_label.grid(row=4, column=0, padx=40, pady=(0, 5), sticky="W")
    interest.insert(1, "example 3.9 for 3.9%")
    term_label = Label(
        mortgage_calculator1,
        text="Enter the term in years",
        padx=40,
    )
    term_label.grid(row=5, column=0, padx=40, pady=(0, 5), sticky="W")
    term.insert(1, "Years")
    downpayment_label = Label(
        mortgage_calculator1,
        text="Enter down payment as a percentage",
        padx=40,
    )
    downpayment_label.grid(row=6, column=0, padx=40, pady=(0, 5), sticky="W")
    downpayment.insert(1, "example 5 for 5%")

    # creating frames

    verify_frame = LabelFrame(mortgage_calculator)
    calculate_frame = LabelFrame(mortgage_calculator)

    # create submit button

    submit_info = Button(
        mortgage_calculator1,
        text="Submit",
        command=lambda: verification(
            mortgage_calculator,
            verify_frame,
            principal,
            interest,
            term,
            downpayment,
            mortgage_calculator1,
            calculate_frame,
        ),
    )
    submit_info.grid(row=7, column=0, sticky="E", pady=10)


def calculate_result1(
    refinance_calc,
    verify_frame1,
    update_original_amount,
    update_original_interest,
    update_original_term,
    update_years_remain,
    update_months_remain,
    update_current_payment,
    update_new_interest,
    update_new_term,
    update_close_costs,
    calculate_frame1,
):
    return


def remaining_balance(
    original_amount, original_interest, original_term, years_remain, months_remain
):
    """Formula to calculate remaining loan balance"""

    # check for errors

    try:
        verify_original_amount = int(original_amount.get())
        verify_original_interest = float(original_interest.get())
        verify_original_term = int(original_term.get())
        verify_years_remain = int(years_remain.get())
        verify_months_remain = int(months_remain.get())

        if verify_original_amount <= 0:
            messagebox.showerror(
                "Original Price Error", "Please enter a positive whole number"
            )
            return
        elif verify_original_interest < 0:
            messagebox.showerror("Interest Error", "Please enter a valid interest rate")
            return
        elif verify_original_interest > 20:
            messagebox.showerror("Interest Error", "Please enter a valid interest rate")
            return
        elif verify_original_term <= 0:
            messagebox.showerror("Term Error", "Please enter a valid term in years")
            return
        elif verify_original_term >= 51:
            messagebox.showerror("Term Error", "Please enter a valid term in years")
            return
        elif verify_years_remain <= 0:
            messagebox.showerror("Years Error", "Please enter a valid number")
            return
        elif verify_years_remain >= verify_original_term:
            messagebox.showerror("Years Error", "Years must be less than original term")
            return
        elif verify_months_remain < 0:
            messagebox.showerror("Months Error", "Please enter a valid number")
            return
        elif verify_months_remain > 11:
            messagebox.showerror("Months Error", "Months must be less than 12")
            return
        else:
            pass
    except ValueError:
        messagebox.showerror("Value Error", "Please enter a valid number")
        return

    month_int1 = (verify_original_interest / 12) / 100

    original_month_term = verify_original_term * 12
    payment_made = original_month_term - (
        (verify_years_remain * 12) + verify_months_remain
    )
    balance_remain = (
        (verify_original_amount)
        * (
            ((1 + month_int1) ** original_month_term)
            - ((1 + month_int1) ** payment_made)
        )
        / (((1 + month_int1) ** original_month_term) - 1)
    )
    return balance_remain


def refi_verification(
    refinance_calc,
    verify_frame1,
    original_amount,
    original_interest,
    original_term,
    years_remain,
    months_remain,
    current_payment,
    new_interest,
    new_term,
    close_costs,
    refinance_calc1,
    calculate_frame1,
):
    """Verification frame to allow for opportunity to make changes or keep existing values"""

    # function called to calculate remaining balance of loan to complete further error verifications

    balance = remaining_balance(
        original_amount, original_interest, original_term, years_remain, months_remain
    )

    # checking for errors

    try:
        verify_current_payment = float(current_payment.get())
        verify_new_interest = float(new_interest.get())
        verify_new_term = int(new_term.get())
        verify_close_costs = int(close_costs.get())

        if verify_current_payment <= 0:
            messagebox.showerror("Payment Error", "Please enter a valid payment amount")
            return
        elif verify_current_payment >= balance:
            messagebox.showerror(
                "Payment Error", "Payment must be less than remaining balance"
            )
            return
        elif verify_new_interest < 0:
            messagebox.showerror(
                "New Interest Error", "Please enter a valid interest rate"
            )
            return
        elif verify_new_interest > 20:
            messagebox.showerror(
                "New Interest Error", "Please enter a valid interest rate"
            )
            return
        elif verify_new_term <= 0:
            messagebox.showerror("New Term Error", "Please enter a valid term in years")
            return
        elif verify_new_term > 50:
            messagebox.showerror("New Term Error", "Please enter a valid term in years")
            return
        elif verify_close_costs < 0:
            messagebox.showerror(
                "Closing Costs Error", "Please enter estimated closing costs"
            )
            return
        elif verify_close_costs >= balance:
            messagebox.showerror(
                "Closing Costs Error",
                "Closing Costs must be less than remaining balance",
            )
            return
        else:
            pass
    except ValueError:
        messagebox.showerror("Value Error", "Please enter a valid number")
        return

    # open a new frame to verify information entered

    verify_frame1.pack(fill="both", expand=1)
    refinance_calc1.pack_forget()

    # give user option to make changes or keep existing

    verifylabelone1 = Label(
        verify_frame1, text="Please verify the information provided", font=("Arial", 20)
    )
    verifylabelone1.grid(row=0, column=1)
    verifylabeltwo1 = Label(
        verify_frame1,
        text="If correct, press submit, otherwise make",
        font=("Arial", 20),
    )
    verifylabeltwo1.grid(row=1, column=1)
    verifylabelthree1 = Label(
        verify_frame1, text="corrections and press submit", font=("Arial", 20)
    )
    verifylabelthree1.grid(row=2, column=1)

    verifylabeloriginalloan = Label(
        verify_frame1, text="Original Loan", font=("Arial", 14)
    )
    verifylabeloriginalloan.grid(row=3, column=0, columnspan=2, pady=5)

    verifylabelnewloan = Label(verify_frame1, text="New Loan", font=("Arial", 14))
    verifylabelnewloan.grid(row=10, column=0, columnspan=2, pady=5)

    # create entry widget showing values entered

    update_original_amount = Entry(verify_frame1, width=20)
    update_original_amount.grid(row=4, column=1, pady=(20, 2), padx=20, ipadx=40)
    update_original_interest = Entry(verify_frame1, width=20)
    update_original_interest.grid(row=5, column=1, padx=20, pady=2, ipadx=40)
    update_original_term = Entry(verify_frame1, width=20)
    update_original_term.grid(row=6, column=1, padx=20, pady=2, ipadx=40)
    update_years_remain = Entry(verify_frame1, width=20)
    update_years_remain.grid(row=7, column=1, padx=20, pady=2, ipadx=40)
    update_months_remain = Entry(verify_frame1, width=20)
    update_months_remain.grid(row=8, column=1, padx=20, pady=2, ipadx=40)
    update_current_payment = Entry(verify_frame1, width=20)
    update_current_payment.grid(row=9, column=1, padx=20, pady=2, ipadx=40)
    update_new_interest = Entry(verify_frame1, width=20)
    update_new_interest.grid(row=11, column=1, padx=20, pady=2, ipadx=40)
    update_new_term = Entry(verify_frame1, width=20)
    update_new_term.grid(row=12, column=1, padx=20, pady=2, ipadx=40)
    update_close_costs = Entry(verify_frame1, width=20)
    update_close_costs.grid(row=13, column=1, padx=20, pady=2, ipadx=40)

    # add labels to show on screen

    update_original_amount_label = Label(verify_frame1, text="Verify Purchase Price")
    update_original_amount_label.grid(
        row=4, column=0, pady=(20, 2), padx=(80, 0), sticky="W"
    )
    update_original_interest_label = Label(verify_frame1, text="Verify Interest")
    update_original_interest_label.grid(
        row=5, column=0, padx=(80, 0), pady=2, sticky="W"
    )
    update_original_term_label = Label(verify_frame1, text="Verify Yearly Term")
    update_original_term_label.grid(row=6, column=0, padx=(80, 0), pady=2, sticky="W")
    update_years_remain_label = Label(verify_frame1, text="Years Remain")
    update_years_remain_label.grid(row=7, column=0, padx=(80, 0), pady=2, sticky="W")
    update_months_remain_label = Label(verify_frame1, text="Months Remain")
    update_months_remain_label.grid(row=8, column=0, padx=(80, 0), pady=2, sticky="W")
    update_current_payment_label = Label(verify_frame1, text="Monthly Payment")
    update_current_payment_label.grid(row=9, column=0, padx=(80, 0), pady=2, sticky="W")
    update_new_interest_label = Label(verify_frame1, text="New Interest Rate")
    update_new_interest_label.grid(row=11, column=0, padx=(80, 0), pady=2, sticky="W")
    update_new_term_label = Label(verify_frame1, text="New Term")
    update_new_term_label.grid(row=12, column=0, padx=(80, 0), pady=2, sticky="W")
    update_close_costs_label = Label(verify_frame1, text="Estimated Closing Costs")
    update_close_costs_label.grid(row=13, column=0, padx=(80, 0), pady=2, sticky="W")

    # show the values within the entry fields

    update_original_amount.insert(5, original_amount.get())
    update_original_interest.insert(5, original_interest.get())
    update_original_term.insert(5, original_term.get())
    update_years_remain.insert(5, years_remain.get())
    update_months_remain.insert(5, months_remain.get())
    update_current_payment.insert(5, current_payment.get())
    update_new_interest.insert(5, new_interest.get())
    update_new_term.insert(5, new_term.get())
    update_close_costs.insert(5, close_costs.get())

    # create the submit button

    submit_button = Button(
        verify_frame1,
        text="Submit",
        command=lambda: calculate_result1(
            refinance_calc,
            verify_frame1,
            update_original_amount,
            update_original_interest,
            update_original_term,
            update_years_remain,
            update_months_remain,
            update_current_payment,
            update_new_interest,
            update_new_term,
            update_close_costs,
            calculate_frame1,
        ),
    )
    submit_button.grid(row=14, column=1, pady=(20, 0))


def refinancecalc():
    # Future option for refinancing
    new_file.withdraw()
    refinance_calc = Toplevel()
    refinance_calc.title("Refinance Calculator")
    refinance_calc.geometry("1000x600")

    refinance_calc1 = LabelFrame(refinance_calc)
    refinance_calc1.pack(fill="both", expand=1)

    # introduction line
    refinance_label1 = Label(
        refinance_calc1, text="Please enter the information", font=("Arial", 20)
    )
    refinance_label2 = Label(
        refinance_calc1,
        text="to calculate your refinance option",
        font=("Arial", 20),
    )
    refinance_label1.grid(row=0, column=0, columnspan=2, padx=40)
    refinance_label2.grid(row=1, column=0, columnspan=2, padx=40, pady=(0, 20))

    # input fields

    original_amount = IntVar()
    original_interest = DoubleVar()
    original_term = IntVar()
    years_remain = IntVar()
    months_remain = IntVar()
    new_interest = DoubleVar()
    new_term = IntVar()
    current_payment = DoubleVar()
    close_costs = IntVar()

    # original amounts

    original_amount = Entry(refinance_calc1, width=20)
    original_amount.grid(row=4, column=1, padx=20, pady=(5, 0), ipadx=40)
    original_interest = Entry(refinance_calc1, width=20)
    original_interest.grid(row=5, column=1, pady=(5, 0), ipadx=40)
    original_term = Entry(refinance_calc1, width=20)
    original_term.grid(row=6, column=1, pady=(5, 0), ipadx=40)
    years_remain = Entry(refinance_calc1, width=20)
    years_remain.grid(row=7, column=1, pady=(5, 0), ipadx=40)
    months_remain = Entry(refinance_calc1, width=20)
    months_remain.grid(row=8, column=1, pady=(5, 0), ipadx=40)
    current_payment = Entry(refinance_calc1, width=20)
    current_payment.grid(row=9, column=1, padx=20, pady=(5, 0), ipadx=40)

    # new amounts
    new_term = Entry(refinance_calc1, width=20)
    new_term.grid(row=11, column=1, padx=20, pady=(5, 0), ipadx=50)
    new_interest = Entry(refinance_calc1, width=20)
    new_interest.grid(row=12, column=1, padx=20, pady=(5, 0), ipadx=50)
    close_costs = Entry(refinance_calc1, width=20)
    close_costs.grid(row=13, column=1, padx=20, pady=(5, 0), ipadx=50)

    # create the labels

    original_loan_label = Label(
        refinance_calc1, text="Current Loan", font=("Arial", 14), padx=40, pady=20
    )
    original_loan_label.grid(
        row=3,
        column=0,
        padx=40,
        pady=(0, 5),
        columnspan=2,
    )
    original_amount_label = Label(
        refinance_calc1,
        text="Enter original purchase price as a whole number",
        padx=40,
    )
    original_amount_label.grid(row=4, column=0, padx=40, pady=(0, 5), sticky="W")
    original_amount.insert(1, "example 300000")
    original_interest_label = Label(
        refinance_calc1,
        text="Enter original interest rate as a percentage",
        padx=40,
    )
    original_interest_label.grid(row=5, column=0, padx=40, pady=(0, 5), sticky="W")
    original_interest.insert(1, "example 3.9 for 3.9%")
    original_term_label = Label(
        refinance_calc1,
        text="Enter original loan term in years",
        padx=40,
    )
    original_term_label.grid(row=6, column=0, padx=40, pady=(0, 5), sticky="W")
    original_term.insert(1, "Years")
    years_remain_label = Label(
        refinance_calc1,
        text="Enter the number of years and months remaining",
        padx=40,
    )
    years_remain_label.grid(row=7, column=0, padx=40, pady=(0, 5), sticky="W")
    months_remain_label = Label(refinance_calc1, text="", padx=40)
    months_remain_label.grid(row=8, column=0, padx=40, pady=(0, 5), sticky="W")
    years_remain.insert(1, "Years")
    months_remain.insert(1, "Months")
    current_payment_label = Label(
        refinance_calc1,
        text="Enter the monthly payment of principal and interest only",
        padx=40,
    )
    current_payment_label.grid(row=9, column=0, padx=40, pady=(0, 5), sticky="W")
    current_payment.insert(1, "example 1,501.12")

    # insert labels for new loan amounts

    new_loan_label = Label(
        refinance_calc1, text="New Loan", font=("Arial", 14), padx=40, pady=20
    )
    new_loan_label.grid(
        row=10,
        column=0,
        padx=40,
        pady=(0, 5),
        columnspan=2,
    )
    new_term_label = Label(
        refinance_calc1,
        text="Enter the new loan term in years",
        padx=40,
    )
    new_term_label.grid(row=11, column=0, padx=40, pady=(0, 5), sticky="W")
    new_term.insert(1, "Years")

    new_interest_label = Label(
        refinance_calc1,
        text="Enter the new interest rate as a percentage",
        padx=40,
    )
    new_interest_label.grid(row=12, column=0, padx=40, pady=(0, 5), sticky="W")
    new_interest.insert(1, "example 3.9 for 3.9%")

    close_costs_label = Label(
        refinance_calc1,
        text="Enter estimated closing costs",
        padx=40,
    )
    close_costs_label.grid(row=13, column=0, padx=40, pady=(0, 5), sticky="W")
    close_costs.insert(1, "5000 is average")

    # creating frames

    verify_frame1 = LabelFrame(refinance_calc)
    calculate_frame1 = LabelFrame(refinance_calc)

    # create submit button

    submit_info1 = Button(
        refinance_calc1,
        text="Submit",
        command=lambda: refi_verification(
            refinance_calc,
            verify_frame1,
            original_amount,
            original_interest,
            original_term,
            years_remain,
            months_remain,
            current_payment,
            new_interest,
            new_term,
            close_costs,
            refinance_calc1,
            calculate_frame1,
        ),
    )
    submit_info1.grid(row=14, column=0, sticky="E", pady=10)


def extrapaycalc():
    """Future option to calculate additional payments"""

    return


def proceedscalc():
    """Future option to display proceeds from sale"""

    return


# closes the mainloop for Tkinter

new_file.mainloop()
