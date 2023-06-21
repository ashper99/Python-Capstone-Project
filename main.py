# This program will allow the user to insert the parameters required to determine the monthly mortgage
# rate based on a series of down payments from 5 - 20%.
# The user will also be given the opportunity to decide on a refinance option, early payoff, or sale
# proceeds.

import numpy as np, matplotlib.pyplot as plt, seaborn as sns, pandas as pd
import csv

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
        if interest_rate >= 0 and interest_rate <= 20:
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
        if pctdown >= 0 and pctdown <= 100:
            break
        else:
            print('Please enter a valid number')
    return pctdown
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

    totalamount = mortgage_amount #placeholder since mortgage_amount is modified below
    totalamount1 = mortgage_amount #another placeholder since I use totalamount

    for i in range(1, month_term + 1):
        monthint = mortgage_amount*(monthly_interest - 1)
        mortgage_amount = mortgage_amount - (monthly_payment - monthint)
        monthlyinterest = np.append(monthlyinterest, monthint)
        monthly_principal = np.append(monthly_principal, mortgage_amount)

    np.set_printoptions(suppress=True) #remove scientific notation from monthly_principal when printed

    #calculate the total interest paid
    total_interest = 0
    for i in monthlyinterest:
        total_interest += i

    #total amount paid for the mortgage
    total_mortgage = totalamount + total_interest

    # creating dataframe for results
    #formatting numbers for proper display
    a1 = ("${:0,.2f}".format(a))
    b1 = ("{:.2%}".format(b/100))
    d1 = ("{:.2%}".format(d/100))
    monthly_payment1 = ("${:0,.2f}".format(monthly_payment))
    total_interest1 = ("${:0,.2f}".format(total_interest))
    total_mortgage1 = ("${:0,.2f}".format(total_mortgage))

    label_values = ['Sales Price', 'Interest Rate', 'Mortgage Term', 'Down Payment', 'Monthly Payment', 'Total Interest', 'Total Paid']
    column_values = ["Totals"]
    mortgage_array = np.array([a1, b1, c, d1, monthly_payment1, total_interest1, total_mortgage1])

    mortgage_data = pd.DataFrame(data = mortgage_array, index = label_values, columns = column_values)

    print(mortgage_data)

    #create remainder of spreadsheet array
    months = np.arange(1, (month_term + 1))
    principal_paid = []
    principalamt = 0

    #create array for monthly principal
    for i in monthly_principal:
        principalamt = totalamount - i
        totalamount -= principalamt
        principal_paid = np.append(principal_paid, principalamt)

    #array for starting balance
    start_balance =[totalamount1]
    for i in monthly_principal[0:(month_term - 1)]:
        start_balance = np.append(start_balance, i)

    #ending balance should be zero

    monthly_principal[-1] = 0

    #create the dataframe

    payment_values = ['Starting Balance', 'Principal Paid', 'Interest Paid', 'Ending Balance']

    payment_data = pd.DataFrame(list(zip(start_balance, principal_paid, monthlyinterest, monthly_principal)), index = months, columns = payment_values)
    payment_data = payment_data.round(2)

    while True:
        hard_copy = input('Do you wish to save a copy of the monthly payment structure?  yes/no \n')
        if hard_copy == 'no':
            print('Thank you and have a wonderful day')
            break
        elif hard_copy == 'yes':

            payment_data.to_csv('mortgage.csv', index = True)
            print('Your file has been saved as mortgage.csv')
            break
        else:
            print('Please enter yes or no')
            continue

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
        if correct.lower() == 'no':
            correction()
            print('Purchase price $ ' + format(a, ',.2f'), '\n')
            print('Interest Rate ', b, '%\n')
            print('Mortgage Term ', c, 'years\n')
            print('Down Payment ', d, '%\n')
        elif correct.lower() == 'yes':
            calculation()
            break
        else:
            print('Enter yes or no')
            continue

#main program

a = mortgage()
b = interest()
c = mortgage_term()
d = down_payment()
verify()





