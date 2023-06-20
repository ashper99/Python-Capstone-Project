# This program will allow the user to insert the parameters required to determine the monthly mortgage
# rate based on a series of down payments from 5 - 20%.
# The user will also be given the opportunity to decide on a refinance option, early payoff, or sale
# proceeds.

import numpy as np, matplotlib.pyplot as plt, seaborn as sns, pandas as pd, tkinter as tk
def mortgage():
    #User inputs the purchase price

    print("Please follow the prompts and enter the correct information. \n")

    #purchase price as principal

    while True:
        try:
            principal = float(input('Please enter the total purchase price \n'))
        except ValueError:
            print("Please input a valid number amount")
            continue
        if principal > 0:
            break
        else:
            print("Please input a valid dollar amount")
    return principal

def interest():

    #Interest rate

    while True:
        try:
            interest_rate = float(input('Please enter the interest \n'))
        except ValueError:
            print("Please input as a percentage, for example, 3.9")
            continue
        if interest_rate > 0:
            break
        else:
            print("Please input a valid rate")
    return interest_rate

def mortgage_term():
    #mortgage term in years

    while True:
        try:
            term = int(input('Please enter the term in years \n'))
        except ValueError:
            print('Please enter a valid number')
            continue
        if term > 0:
            break
        else:
            print('Please enter a valid number')
    return term

def down_payment():
    #enter down payment as a percentage

    while True:
        try:
            pctdown = float(input('Please enter the down payment as a percentage \n'))
        except ValueError:
            print('Please enter a valid number')
            continue
        if pctdown > 0:
            break
        else:
            print('Please enter a valid number')
    return pctdown

def correction():
    #allows user to make corrections to chosen line item

    while True:
        change = str(input(
            'Please choose which item you would like to correct \n Purchase Price \n Interest Rate \n Terms \n Down Payment \n'))
        if change.lower() == 'purchase price':
           global a
           a = mortgage()
           break
        elif change.lower() == 'interest rate':
            global b
            b = interest()
            break
        elif change.lower() == 'terms':
            global c
            c = mortgage_term()
            break
        elif change.lower() == 'down payment':
            global d
            d = down_payment()
            break
        else:
            print('Please enter the item that you would like to correct \n')
            continue

def verify():
    # verify the information

    print('Please verify the information you entered \n \n')
    print('Purchase price $ ' + format(a, ',.2f'), '\n')
    print('Interest Rate ', b, '%\n')
    print('Mortgage Term ', c, 'years\n')
    print('Down Payment ', d, '%\n')

    #ask the user if the information is correct and give them the opportunity to make changes

    while True:
        correct = input("Is the information correct? (yes/no): \n")
        if correct.lower() == 'yes':

            break
        elif correct.lower() == 'no':

            correction()
            print('Purchase price $ ' + format(a, ',.2f'), '\n')
            print('Interest Rate ', b, '%\n')
            print('Mortgage Term ', c, 'years\n')
            print('Down Payment ', d, '%\n')

        else:
            print('Type yes or no')
            continue
def calculation():
    #this will make the calculations necessary to come up with the projected payments

    global a, b, c, d
    month_term = c*12 #years times 12 months
    monthly_interest = 1 + (b)/(12*100)

    mortgage_amount = a - (a*(d/100)) #total amount of loan


    #calculate monthly payment
    monthly_payment = (round(mortgage_amount*(monthly_interest**month_term)*(1-monthly_interest)/(1-monthly_interest**month_term), 2))


    # calculate the monthly interest and monthly principal remaining
    monthlyinterest = []
    monthly_principal = []

    for i in range(1, month_term + 1):
        monthint = mortgage_amount*(monthly_interest - 1)
        mortgage_amount = mortgage_amount - (monthly_payment - monthint)
        monthlyinterest = np.append(monthlyinterest, monthint)
        monthly_principal = np.append(monthly_principal, mortgage_amount)

    np.set_printoptions(suppress=True)

    
#main program

a = mortgage()
b = interest()
c = mortgage_term()
d = down_payment()
verify()
calculation()



