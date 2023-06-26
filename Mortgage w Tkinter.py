#This is a mortgage program which will utilize Tkinter as the GUI.

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *

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



def verification():
    # add new window for the verification
    verify_info = Toplevel()
    verify_info.title("Verification")
    verify_info.geometry('800x400')

    # give user to make changes or keep existing

    verifylabelone = Label(verify_info, text = "Please verify the information provided", font = ('Arial', 20))
    verifylabelone.grid(row = 0, column = 1)
    verifylabeltwo = Label(verify_info, text = "If correct, press enter, otherwise choose", font = ('Arial', 20))
    verifylabeltwo.grid(row = 1, column = 1)
    verifylabelthree = Label(verify_info, text = "the item to change, then press enter",font = ('Arial', 20))
    verifylabelthree.grid(row = 2, column = 1)


    #show inputs with checkbox to change

    verify_choice1 = IntVar()
    verify_choice2 = IntVar()
    verify_choice3 = IntVar()
    verify_choice4 = IntVar()
    verify_choice5 = IntVar()


    update_principal = Checkbutton(verify_info, text = "Purchase Price   $ " + principal_main.get(), variable = verify_choice1)
    update_principal.grid(row = 3, column = 0, pady = (20, 0), sticky = 'W')
    update_interest = Checkbutton(verify_info, text="Interest Rate  " + interest_main.get() + "%",
                                   variable=verify_choice2)
    update_interest.grid(row=4, column=0,  sticky='W')
    update_term = Checkbutton(verify_info, text="Term in years  " + term_main.get(),
                                   variable=verify_choice3)
    update_term.grid(row=5, column=0, sticky='W')
    update_downpayment = Checkbutton(verify_info, text= "Down Payment Percentage  " + downpayment_main.get() + "%",
                                   variable=verify_choice4)
    update_downpayment.grid(row=6, column=0,  sticky='W')
    correct_info = Checkbutton(verify_info, text = "Everything looks good", variable = verify_choice5)
    correct_info.grid(row = 7, column = 0, sticky = 'W')


def mortgagecalc():

#this starts the function for the first mortgage calculation
#by creating a new window
    new_file.destroy()
    mortgage_calculator = Tk()
    mortgage_calculator.title("Mortgage Calculator")
    mortgage_calculator.geometry('800x400')


#introduction line
    mortgage_label1 = Label(mortgage_calculator, text = "Please enter the information", font = ('Arial', 20))
    mortgage_label2 = Label(mortgage_calculator, text = "to calculate your monthly payment", font = ('Arial', 20))
    mortgage_label1.grid(row = 0, column = 0, columnspan = 2, padx =40)
    mortgage_label2.grid(row=1, column=0, columnspan = 2, padx = 40, pady = (0,20))

#adding the input fields
    principal = StringVar()
    interest = StringVar()
    term = StringVar()
    downpayment = StringVar()

    principal = Entry(mortgage_calculator, width = 20)
    principal.grid(row = 3, column = 1, padx = 20, ipadx = 50)
    interest = Entry(mortgage_calculator, width = 20)
    interest.grid(row = 4, column = 1, ipadx = 50)
    term = Entry(mortgage_calculator, width = 20)
    term.grid(row = 5, column = 1, ipadx = 50)
    downpayment = Entry(mortgage_calculator, width = 20)
    downpayment.grid(row = 6, column =1, ipadx = 50)

#Create input labels

    principal_label = Label(mortgage_calculator, text = "Enter purchase price as a whole number  e.g 300000", padx = 40)
    principal_label.grid(row = 3, column = 0, padx = 40, pady = (0,5), sticky = "W")
    interest_label = Label(mortgage_calculator, text="Enter interest as a percentage  e.g 3.9 for 3.9%", padx=40)
    interest_label.grid(row = 4, column = 0, padx = 40, pady = (0,5), sticky = "W")
    term_label = Label(mortgage_calculator, text = "Enter the term in years  e.g 30 for 30 years", padx = 40)
    term_label.grid(row = 5, column = 0, padx = 40, pady = (0,5), sticky = "W")
    downpayment_label = Label(mortgage_calculator, text = "Enter down payment as a percentage e.g 5 for 5%", padx = 40)
    downpayment_label.grid(row = 6, column = 0, padx = 40, pady = (0,5), sticky = "W")

    global principal_main
    principal_main = principal
    global interest_main
    interest_main = interest
    global term_main
    term_main = term
    global downpayment_main
    downpayment_main = downpayment



#create submit button

    submit_info = Button(mortgage_calculator, text = "Enter", command = lambda: verification())
    submit_info.grid(row = 7, column = 0, sticky = 'E', pady = 10)


def refinancecalc():
    return

def extrapaycalc():
    return


def proceedscalc():
    return









new_file.mainloop()

# call to run the main program



