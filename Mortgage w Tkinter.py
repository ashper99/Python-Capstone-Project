#This is a mortgage program which will utilize Tkinter as the GUI.

import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *

#allow for use of different functions for different windows
class MortgageCalculator:
    def __init__(self):


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
        self.module = StringVar()
        self.module.set(False)

        mortgage = Radiobutton(new_file, text = 'Mortgage Calculator', variable = self.module, value = "Mortgage Calculation")
        refinance = Radiobutton(new_file, text = 'Mortgage Loan Refinance', variable = self.module, value = "Refinance")
        extra_payment = Radiobutton(new_file, text = 'Extra Payment', variable = self.module, value = "extrapayment")
        proceedscalc = Radiobutton(new_file, text = 'Proceeds from sale', variable = self.module, value = "proceeds")

        choose = Button(new_file, text = "Enter", command = self.choice)



    #Insert Buttons

        mortgage.grid(row = 2, column = 0, sticky = 'W')
        refinance.grid(row = 3, column = 0, sticky = 'W')
        extra_payment.grid(row = 4, column = 0, sticky = 'W')
        proceedscalc.grid(row = 5, column = 0, sticky = 'W')
        choose.grid(row = 6, column = 1, sticky = 'W', pady = 10)

    def choice(self):
        if self.module.get() == 'Mortgage Calculation':
            mortgagecalc()
        elif self.module.get() == 'Refinance':
            refinancecalc()
        elif self.module.get() == 'extrapayment':
            extrapaycalc()
        elif self.module.get() == 'proceeds':
            proceedscalc()

    def verification(self):
        return

    def mortgagecalc(self):

        #this starts the function for the first mortgage calculation
        #by creating a new window

        mortgage_calculator = Toplevel()
        mortgage_calculator.title("Mortgage Calculator")
        mortgage_calculator.geometry('800x400')

        #introduction line
        mortgage_label1 = Label(mortgage_calculator, text = "Please enter the information", font = ('Arial', 20))
        mortgage_label2 = Label(mortgage_calculator, text = "to calculate your monthly payment", font = ('Arial', 20))
        mortgage_label1.grid(row = 0, column = 0, columnspan = 2, padx =40)
        mortgage_label2.grid(row=1, column=0, columnspan = 2, padx = 40, pady = (0,20))

        #adding the input fields
        self.principal = StringVar()
        self.interest = StringVar()
        self.term = StringVar()
        self.downpayment = StringVar()

        self.principal = Entry(mortgage_calculator, width = 20)
        self.principal.grid(row = 3, column = 1, padx = 20, ipadx = 50)
        self.interest = Entry(mortgage_calculator, width = 20)
        self.interest.grid(row = 4, column = 1, ipadx = 50)
        self.term = Entry(mortgage_calculator, width = 20)
        self.term.grid(row = 5, column = 1, ipadx = 50)
        self.downpayment = Entry(mortgage_calculator, width = 20)
        self.downpayment.grid(row = 6, column =1, ipadx = 50)

        #Create input labels

        principal_label = Label(mortgage_calculator, text = "Enter purchase price as a whole number  e.g 300000", padx = 40)
        principal_label.grid(row = 3, column = 0, padx = 40, pady = (0,5), sticky = "W")
        interest_label = Label(mortgage_calculator, text="Enter interest as a percentage  e.g 3.9 for 3.9%", padx=40)
        interest_label.grid(row = 4, column = 0, padx = 40, pady = (0,5), sticky = "W")
        term_label = Label(mortgage_calculator, text = "Enter the term in years  e.g 30 for 30 years", padx = 40)
        term_label.grid(row = 5, column = 0, padx = 40, pady = (0,5), sticky = "W")
        downpayment_label = Label(mortgage_calculator, text = "Enter down payment as a percentage e.g 5 for 5%", padx = 40)
        downpayment_label.grid(row = 6, column = 0, padx = 40, pady = (0,5), sticky = "W")





    #create submit button

        self.submit_info = Button(mortgage_calculator, text = "Enter", command = self.verification)
        submit_info.grid(row = 7, column = 0, sticky = 'E', pady = 10)









    def refinancecalc(self):
        return

    def extrapaycalc(self):
        return


    def proceedscalc(self):
        return








        root = Tk()
        newfile.mainloop()

# call to run the main program
MortgageCalculator()


