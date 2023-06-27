#This is a mortgage program which will utilize Tkinter as the GUI.

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from tkinter import messagebox

#allow for use of different functions for different windows

def choice():
    if module.get() == 'Mortgage Calculation':
        mortgagecalc()
    elif module.get() == 'Refinance':
        refinancecalc()
    elif module.get() == 'extrapayment':
        extrapaycalc()
    elif module.get() == 'proceeds':
        proceedscalc()

# creating the window
new_file = Tk()
new_file.title("Finance Calculator")
new_file.geometry("800x400")

#create the welcome label and the choices
mortgage_label1 = Label(new_file, text = "Welcome to the mortgage calculator.", font=("Arial", 20))
mortgage_label2 = Label(new_file, text = "Please choose one of the options below.", font=("Arial", 20))
mortgage_label1.grid(row = 0, column = 0, columnspan = 2)
mortgage_label2.grid(row = 1, column = 0, columnspan = 2, padx = (40, 0), pady = (0, 20))

#Create buttons to choose the program
module = StringVar()
module.set(False)

mortgage = Radiobutton(new_file, text = 'Mortgage Calculator', variable = module, value = "Mortgage Calculation")
refinance = Radiobutton(new_file, text = 'Mortgage Loan Refinance', variable = module, value = "Refinance")
extra_payment = Radiobutton(new_file, text = 'Extra Payment', variable = module, value = "extrapayment")
proceedscalc = Radiobutton(new_file, text = 'Proceeds from sale', variable = module, value = "proceeds")

choose = Button(new_file, text = "Enter", command = choice)

#Insert Buttons

mortgage.grid(row = 2, column = 0, sticky = 'W')
refinance.grid(row = 3, column = 0, sticky = 'W')
extra_payment.grid(row = 4, column = 0, sticky = 'W')
proceedscalc.grid(row = 5, column = 0, sticky = 'W')
choose.grid(row = 6, column = 1, sticky = 'W', pady = 10)

def calculate_result():

    try:
        verify_principal1 = int(principal_verify.get())
        verify_interest1 = float(interest_verify.get())
        verify_term1 = int(term_verify.get())
        verify_downpayment1 = float(downpayment_verify.get())
        if verify_principal1 <= 0:
            messagebox.showerror("Principal Error", "Please enter a positive whole number")
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

    calculation.pack(fill='both', expand=1)
    verify_info.pack_forget()

    #creating lists for dataframe use

    monthly_principal = []
    interest_paid = []
    running_balance = []

    #making the calculations

    month_term = term_verify*12
    monthly_interest = 1 + (interest_verify)/(12*100)
    principal_amt = principal_verify*(downpayment_verify/100)






def verification():

    # verifying the values entered are correct

    try:
        verify_principal = int(principal_main.get())
        verify_interest = float(interest_main.get())
        verify_term = int(term_main.get())
        verify_downpayment = float(downpayment_main.get())
        if verify_principal <= 0:
            messagebox.showerror("Purchase Price Error", "Please enter a positive whole number")
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
            messagebox.showerror("Down Payment Error", "Please enter a valid down payment")
            return
        elif verify_downpayment > 50:
            messagebox.showerror("Down Payment Error", "Please enter a valid down payment")
            return
        else:
            pass
    except ValueError:
        messagebox.showerror("Value Error", "Please enter a valid number")
        return

    #open a new frame to verify information entered

    verify_info.pack(fill='both', expand = 1)
    close_mortgage_calc.pack_forget()

    # give user option to make changes or keep existing

    verifylabelone = Label(verify_info, text = "Please verify the information provided", font = ('Arial', 20))
    verifylabelone.grid(row = 0, column = 1)
    verifylabeltwo = Label(verify_info, text = "If correct, press submit, otherwise make", font = ('Arial', 20))
    verifylabeltwo.grid(row = 1, column = 1)
    verifylabelthree = Label(verify_info, text = "corrections and press submit",font = ('Arial', 20))
    verifylabelthree.grid(row = 2, column = 1)

    #create entry widget showing values entered

    update_principal = Entry(verify_info, width = 20)
    update_principal.grid(row = 3, column = 1, pady = (20, 0), padx = 20, ipadx = 50)
    update_interest = Entry(verify_info, width =20)
    update_interest.grid(row=4, column=1, padx = 20, ipadx = 50)
    update_term = Entry(verify_info, width=20)
    update_term.grid(row=5, column=1, padx=20, ipadx=50)
    update_downpayment = Entry(verify_info, width=20)
    update_downpayment.grid(row=6, column=1, padx=20, ipadx=50)

    #add labels to show on screen

    update_principal_label = Label(verify_info, text = "Verify Principal")
    update_principal_label.grid(row = 3, column = 0, pady = (20,0), padx = (80,0), sticky = 'W')
    update_interest_label = Label(verify_info, text = "Verify Interest")
    update_interest_label.grid(row = 4, column = 0, padx = (80,0), sticky = 'W')
    update_term_label = Label(verify_info, text = "Verify Yearly Terms")
    update_term_label.grid(row = 5, column = 0, padx = (80,0), sticky = 'W')
    update_downpayment_label = Label(verify_info, text = "Down Payment")
    update_downpayment_label.grid(row = 6, column = 0, padx = (80,0), sticky = 'W')

    #show the values within the entry fields

    update_principal.insert(5, principal_main.get())
    update_interest.insert(5, interest_main.get())
    update_term.insert(5, term_main.get())
    update_downpayment.insert(5, downpayment_main.get())

    #redo the gloabl variables

    global principal_verify
    principal_verify = update_principal
    global interest_verify
    interest_verify = update_interest
    global term_verify
    term_verify = update_term
    global downpayment_verify
    downpayment_verify = update_downpayment

    #create the submit button

    submit_button = Button(verify_info, text = "Submit", command = calculate_result)
    submit_button.grid(row = 7, column = 1, pady = (20,0))

# this starts the function for the first mortgage calculation
# by creating a new window
def mortgagecalc():

#this starts the function for the first mortgage calculation
#by creating a new window
    new_file.destroy()
    mortgage_calculator = Tk()
    mortgage_calculator.title("Mortgage Calculator")
    mortgage_calculator.geometry('800x400')

    mortgage_calculator1 = LabelFrame(mortgage_calculator)
    mortgage_calculator1.pack(fill='both', expand = 1)

#introduction line
    mortgage_label1 = Label(mortgage_calculator1, text = "Please enter the information", font = ('Arial', 20))
    mortgage_label2 = Label(mortgage_calculator1, text = "to calculate your monthly payment", font = ('Arial', 20))
    mortgage_label1.grid(row = 0, column = 0, columnspan = 2, padx =40)
    mortgage_label2.grid(row=1, column=0, columnspan = 2, padx = 40, pady = (0,20))

#adding the input fields
    principal = IntVar()
    interest = DoubleVar()
    term = IntVar()
    downpayment = DoubleVar()

    principal = Entry(mortgage_calculator1, width = 20)
    principal.grid(row = 3, column = 1, padx = 20, ipadx = 50)
    interest = Entry(mortgage_calculator1, width = 20)
    interest.grid(row = 4, column = 1, ipadx = 50)
    term = Entry(mortgage_calculator1, width = 20)
    term.grid(row = 5, column = 1, ipadx = 50)
    downpayment = Entry(mortgage_calculator1, width = 20)
    downpayment.grid(row = 6, column =1, ipadx = 50)

#Create input labels

    principal_label = Label(mortgage_calculator1, text = "Enter purchase price as a whole number  e.g 300000", padx = 40)
    principal_label.grid(row = 3, column = 0, padx = 40, pady = (0,5), sticky = "W")
    interest_label = Label(mortgage_calculator1, text="Enter interest as a percentage  e.g 3.9 for 3.9%", padx=40)
    interest_label.grid(row = 4, column = 0, padx = 40, pady = (0,5), sticky = "W")
    term_label = Label(mortgage_calculator1, text = "Enter the term in years  e.g 30 for 30 years", padx = 40)
    term_label.grid(row = 5, column = 0, padx = 40, pady = (0,5), sticky = "W")
    downpayment_label = Label(mortgage_calculator1, text = "Enter down payment as a percentage e.g 5 for 5%", padx = 40)
    downpayment_label.grid(row = 6, column = 0, padx = 40, pady = (0,5), sticky = "W")

    #assign values as global

    global principal_main
    principal_main = principal
    global interest_main
    interest_main = interest
    global term_main
    term_main = term
    global downpayment_main
    downpayment_main = downpayment

    #creating frames and assigning global variables

    verify_frame = LabelFrame(mortgage_calculator)
    global verify_info
    verify_info = verify_frame
    global close_mortgage_calc
    close_mortgage_calc = mortgage_calculator1
    calculate_frame = LabelFrame(mortgage_calculator)
    global calculation
    calculation = calculate_frame

#create submit button

    submit_info = Button(mortgage_calculator1, text = "Submit", command = verification)
    submit_info.grid(row = 7, column = 0, sticky = 'E', pady = 10)




def refinancecalc():
    return

def extrapaycalc():
    return


def proceedscalc():
    return









new_file.mainloop()

# call to run the main program



