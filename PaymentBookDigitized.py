# -*- coding: utf-8 -*-
"""
Created on Mon Dec 6 2021
Payment Book
author: Dylan Smith
"""

#######################################IMPORTING##AND##OBLIGATORIES##################

customerindex = []
from datetime import datetime, timedelta #Imports pythons own dating system for use in finding the next date.
from calendar import monthrange #Imports the calender and days of the month, info like febuary has 28 days etc.

import tkinter as tk #Imports tkinter for use as tk
from PIL import Image, ImageTk #Imports a reall old image user program that let's the buttons be images
root = tk.Tk() #The root line
root.title("Payment Book") #Window title
root.geometry("600x350") #Geometry of the window

##############################Entry's##############################

# All Entries that are needed in order to add a customer to the database with
# their labels and where they are at in position within the window
# I could have moved all of the buttons here but I like the three line
# labeling thing I have going on.

tk.Label(root, text="Name:").grid(row=0, sticky='s') 
Customer = tk.Entry(root)
Customer.grid(row=0, column=1,sticky='s') 

tk.Label(root, text="Make/Model:").grid(row=1)
Vehicle = tk.Entry(root)
Vehicle.grid(row=1, column=1)

tk.Label(root, text="Last 4 VIN:").grid(row=2)
VIN = tk.Entry(root)
VIN.grid(row=2, column = 1)

tk.Label(root, text="Balance:").grid(row=3)
Balance =tk.Entry(root)
Balance.grid(row=3, column = 1)

tk.Label(root, text="Date (MM/DD/YY): ").grid(row=4)
Date = tk.Entry(root)
Date.grid(row=4, column = 1)

tk.Label(root, text="Enter name to find file").grid(row=8, column=0)
Search = tk.Entry(root)
Search.grid(row=8, column=1, pady=20) 

##############################DEFINITION'S############################

def FindPayDate(): #Uses datetime, timedelta, and monthrange in order to find on what day is the customer due.
    today_date = datetime.now().date() #Finds today's date.
    year = today_date.year #Finds Year
    month = today_date.month #Finds Month
    days_in_month = monthrange(year, month)[1] #Finds the days in said month
    global next_month #Allows next_month to be used outside of this function.
    
    if Date.get() == "": #this if statement allows the date to be found automatically if left unentered by user
        next_month = today_date + timedelta(days=days_in_month) #Finds next month's date.
    else:
        next_month = datetime.strptime(str(Date.get()), "%m-%d-%y") + timedelta(days=days_in_month) #uses input to find next month's date
    
def Bringfile(): #A search tool that takes the entry and find the txt file that has thaty name and the entry matches with.
    Name = Search.get()
    File = tk.Toplevel()
    File.title(Name+"'s File")
    global box #is needed in order for the data to be saved.
    box = tk.Text(File, width=50, height=5) #text window
    box.pack(pady=20) 
    BalBtn = tk.Button(File, text="Save All Changes", command = SaveChanges)
    BalBtn.pack(pady=20)
    OpenFile = Name.split(" ", 0) #takes the entry and splits it in to a list.
    OpenFile = [OpenFile[0]] #this is here because the file name was just going to include first names, so I had to use the first in the list

    Open_txt = open("Customerdata"+str(OpenFile).strip("['']")+".txt", "r") #takes the file name searched and finds the file with the name
    txt = Open_txt.read() #reads file
    box.insert(1.0, txt) #puts it in text box
    Open_txt.close() #closes file
    
def Addcustomer(): #Adds Customer to the database.
    AddCustomer = Customer.get() #These get all the entries on the main window
    AddVehicle = Vehicle.get()
    AddVIN = VIN.get()
    AddBalance = Balance.get()
    FindPayDate() #finds the pay date given the entry or not
    AddDate = next_month.strftime("%m""-""%d""-""%y") #Assigns the date in MM-DD-YY fashion
    NewFileName = AddCustomer.split(" ", 0) #explained above
    NewFileName = [NewFileName[0]] 
    
    with open("Customerdata"+str(NewFileName).strip("['']")+".txt", "w") as data: #Creates a text file and writes the entry's in them
        data.write(AddCustomer + "\n")
        data.write(AddVehicle + "\n")
        data.write(AddVIN + "\n")
        data.write(AddBalance + "\n")
        data.write(AddDate + "\n")
    
    Customer.delete(0, tk.END) #these lines delete the entry from the entry boxes when the add button is pressed
    Vehicle.delete(0, tk.END)
    VIN.delete(0, tk.END)
    Balance.delete(0, tk.END)
    Date.delete(0, tk.END)

def BalanceSubWindow():
    # This and the BalanceSubtractor go hand in hand, I am not sure how to edit a text file in the way that I am attempting
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
    # Every entry in the database is going to have the balance on line 4, so I have been trying to figure out a way to take the 
    # 4th line of the txt file and replace it, it has yet to work so I made a manual change and save system.
    # I think the problem is converting the line into a str and then doing math with it, I am not sure how to do that.

    global RunBalance

    Name = Search.get()
    OpenFile = Name.split(" ", 0)
    OpenFile = [OpenFile[0]] 
    
    custfile = open("Customerdata"+str(OpenFile).strip("['']")+".txt", "r")
    BalLine = custfile.readlines()
    BalLine[3] = int(RunBalance)-int(subent.get())+"\n"

    custfile = open("Customerdata"+str(OpenFile).strip("['']")+".txt", "w")
    custfile.writelines(BalLine)
    custfile.close()
    
    FindPayDate()
    
    custfile = open("Customerdata"+str(OpenFile).strip("['']")+".txt", "r")
    BalLine = custfile.readlines()
    BalLine[4] = next_month.strftime("%m""-""%d""-""%y")+"\n"

    custfile = open("Customerdata"+str(OpenFile).strip("['']")+".txt", "w")
    custfile.writelines(BalLine)
    custfile.close()
    
    Bringfile()
    
def SaveChanges(): #This takes what has been written in the text box provided and rewrites the txt file to that. 
    Name = Search.get()
    OpenFile = Name.split(" ", 0)
    OpenFile = [OpenFile[0]] 
    custfile = open("Customerdata"+str(OpenFile).strip("['']")+".txt", "w")
    custfile.write(box.get(1.0, tk.END))
    
def Exit(): #exits the program
    root.destroy()
######################################BUTTON'S###############################

# The buttons are mostly down here and they all have images, that was the hardest thing to figure out for 
# me for some reason. 


AddBtn = ImageTk.PhotoImage(Image.open('FlameSkeleton.png')) #Assigns an image to a variable to use
tk.Button(root, text='Add Customer to Database', font= 'Century', image=AddBtn, compound= tk.RIGHT, command=Addcustomer).grid(row=0, column=2)
SearchBtn = ImageTk.PhotoImage(Image.open('magni.png'))
tk.Button(root, text="Look Up File", image=SearchBtn, compound= tk.LEFT, command = Bringfile).grid(row=8, column=2)
ExitBtn = ImageTk.PhotoImage(Image.open('exitpng.png'))
tk.Button(root, text="Close Program", image=ExitBtn, compound= tk.TOP, command = Exit).grid(row=9, column=2, sticky='e')

root.mainloop()