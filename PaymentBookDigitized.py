# -*- coding: utf-8 -*-
"""
Created on Mon Dec 6 2021
Payment Book
author: Dylan Smith
"""

#######################################IMPORTING##AND##OBLIGATORIES##################

customerindex = []
from datetime import datetime, timedelta
from calendar import monthrange

import tkinter as tk
root = tk.Tk()
root.title("Payment Book")
root.geometry("600x300")

##############################Entry's##############################

tk.Label(root, text="Customer Name:").grid(row=0)
Customer = tk.Entry(root)
Customer.grid(row=0, column=1) 

tk.Label(root, text="Vehicle Name:").grid(row=1)
Vehicle = tk.Entry(root)
Vehicle.grid(row=1, column=1)

tk.Label(root, text="Last 4 VIN:").grid(row=2)
VIN = tk.Entry(root)
VIN.grid(row=2, column = 1)

tk.Label(root, text="Enter Their Balance").grid(row=3)
Balance =tk.Entry(root)
Balance.grid(row=3, column = 1)

tk.Label(root, text="Today's Date: ").grid(row=4)
Date = tk.Entry(root)
Date.grid(row=4, column = 1)

##############################DEFINITION'S############################

def FindPayDate():
    today_date = datetime.now().date()
    year = today_date.year
    month = today_date.month
    days_in_month = monthrange(year, month)[1]
    global next_month
    
    if Date.get() == "":
        next_month = today_date + timedelta(days=days_in_month)
    else:
        next_month = datetime.strptime(str(Date.get()), "%m-%d-%y") + timedelta(days=days_in_month)        
    
    #pay_date = datetime.datetime.strptime(next_month, "%d/%m/%Y %H:%M")
    #if today_date > pay_date:
        #tk.Label(root, text = "Time is up!").grid(row=3, column = 2)

    tk.Label(root, text = next_month.strftime("%m"" - ""%d"" - ""%y")).grid(row=3, column = 2)
def Addcustomer():
    Customer.get()
    Vehicle.get()
    VIN.get()
    Balance.get()
    Date.get()
    
    customerindex.append([Customer.get(), VIN.get(), Balance.get(), FindPayDate()])
    tk.Label(root, text = customerindex).grid(row=2, column = 2)
    
    Customer.delete(0, tk.END)
    Vehicle.delete(0, tk.END)
    VIN.delete(0, tk.END)
    Balance.delete(0, tk.END)
    Date.delete(0, tk.END)

def BalanceSubWindow():
    global subent
    global RunBalance
    RunBalance = Balance.get()
    Pay = tk.Toplevel()
    Pay.title("This is so difficult")
    
    labia = tk.Label(Pay, text="What did they pay today?")
    labia.grid(row=0, column=0)

    subent = tk.Entry(Pay)
    subent.grid(row=1, column=0)

    subbut = tk.Button(Pay, text="Subtract from Balance", command=BalanceSubtractor)
    subbut.grid(row=1, column=1)

def BalanceSubtractor():
    global RunBalance
    RunBalance = int(RunBalance)-int(subent.get())
    Result = tk.Label(root, text=RunBalance)
    Result.grid(row=2, column=3)

######################################BUTTON'S###############################

tk.Button(root, text='Add Customer to Database', command=Addcustomer).grid(row=0, column=2)
tk.Button(root, text='Date Tester', command=FindPayDate).grid(row=1, column=2)
tk.Button(root, text="Subtract Balance Button", command = BalanceSubWindow).grid(row=0, column=3)

root.mainloop()