import sqlite3
from tkinter import *
import tkinter
import tkinter as tk
import random
from tkinter import messagebox
from datetime import datetime

class Signup:

    def __init__(self):
        self.window = tk.Tk()
        self.window.iconbitmap("myIcon.ico")
        self.window.title("Sign up")
        self.window.geometry('800x450')
        self.window.geometry("+600+200") # to position the window in the center
        self.window.config( bg="lightblue")
        self.top_frame= tkinter.Frame(self.window)
        self.bottom_frame= tkinter.Frame(self.window)
        #student information
        self.First_Name = StringVar()
        self.Last_name = StringVar()
        self.ID = StringVar()
        self.Password = StringVar()
        self.Email_address = StringVar()
        self.Phone_number = StringVar()
        #we use --> textvariable=self.

        #logo
        self.logo_label = tkinter.Label(self.window, text='KsuPay',font=("arial", 30, "bold"), bg="lightblue")
        self.logo_label.grid(column=1,row=0)


        #first name label
        self.First_Name_label = tkinter.Label(self.window, text='First Name' ,font=("arial", 20), bg="lightblue")
        self.First_Name_label.grid(column=0,row=1)

        # first name entery
        self.First_Name_enter = tkinter.Entry(self.window,textvariable=self.First_Name, width="80")
        self.First_Name_enter.grid(column=1,row=1)

        # last name label
        self.Last_Name_label = tkinter.Label(self.window, text='Last Name',font=("arial", 20) ,bg="lightblue")
        self.Last_Name_label.grid(column=0, row=2)

        # last name entery
        self.Last_Name_enter = tkinter.Entry(self.window,textvariable=self.Last_name, width="80")
        self.Last_Name_enter.grid(column=1, row=2)

        #id label
        self.ID_label = tkinter.Label(self.window, text='ID',font=("arial", 20), bg="lightblue")
        self.ID_label.grid(column=0,row=3)

        #id entery
        self.Id_enter = tkinter.Entry(self.window,textvariable=self.ID, width="80")
        self.Id_enter.grid(column=1,row=3)

        #password lable
        self.Password_label = tkinter.Label(self.window, text='Password',font=("arial", 20), bg="lightblue")
        self.Password_label.grid(column=0,row=4)

        #password entery
        self.Password_enter = tkinter.Entry(self.window,textvariable=self.Password, width="80")
        self.Password_enter.grid(column=1,row=4)

        #Email address label
        self.Email_address_label = tkinter.Label(self.window, text='Email address ',font=("arial", 20), bg="lightblue")
        self.Email_address_label.grid(column=0,row=5)

        #Email address entery
        self.Email_address_enter = tkinter.Entry(self.window,textvariable=self.Email_address, width="80")
        self.Email_address_enter.grid(column=1,row=5)


        #phone number label
        self.Phone_number_label = tkinter.Label(self.window, text='Phone number ',font=("arial", 20), bg="lightblue")
        self.Phone_number_label.grid(column=0,row=6)

        #phone number entery
        self.Phone_number_enter = tkinter.Entry(self.window,textvariable=self.Phone_number, width="80")
        self.Phone_number_enter.grid(column=1,row=6)

        #singup button
        self.button_s2 = tk.Button(self.window,text="    signup    ",font=("arial", 10),command=self.singup_in_db, height = 3, width = 10)
        self.button_s2.grid(column=0, row=7, pady=10, ipadx=10)

        # GO TO Login button
        self.buttonBack = tk.Button(self.window, text='go to Login',font=("arial", 10), command=self.go_Login, height = 3, width = 10)
        self.buttonBack.grid(column=0, row=9, pady=5, ipadx=10)

        # FOR TIME:
        now = datetime.now()
        dt_string2 = now.strftime("%d/%m/%Y %H:%M:%S")

        # makeing the DB
        conn = sqlite3.connect('test.db')
        conn.execute('''CREATE TABLE if not exists st1 (
                    ID         int(10) NOT NULL , 
                    wallet_number         int(10) NOT NULL,
                    First_Name varchar(255) NOT NULL,
                    last_Name varchar(255) NOT NULL,
                    Password  varchar(255) NOT NULL,
                    Email_address  varchar(255) NOT NULL,
                    Phone_number  varchar(255) NOT NULL,
                    type_of     varchar(255),
                    balance  varchar(255)   ,
                    datetime  varchar(255)     );''')
        conn.commit()
        # ADDING AN ADMIN
        conn.execute(
            f"insert  INTO  st1 (ID,wallet_number,First_Name,last_Name,Password,Email_address,Phone_number,type_of , balance, datetime) VALUES  ('4411026730', '0000000000' , 'abdulkrem' , 'aljeawd' , 'admin11','441102673@ksu.edu.sa' , '0000000000' , 'admin' ,'0' , '{str(dt_string2)}' ); ")
        conn.commit()
        conn.execute(
            f"insert  INTO  st1 (ID,wallet_number,First_Name,last_Name,Password,Email_address,Phone_number,type_of , balance, datetime) VALUES  ('4411027650', '0000000000' , 'abdullah' , 'almusned' , 'admin22','441102765@ksu.edu.sa' , '0000000000' , 'admin' ,'0' , '{str(dt_string2)}' ); ")
        conn.commit()

        self.window.mainloop()




    # for admin  command=self.go_Admin    |||||  # for student wallet   command=self.go_Wallet

    #FOR LOGIN
    def go_Login(self):
        self.window.destroy()
        import Login
        Login.Login()

    #  for student wallet
    def go_Wallet(self):
         self.window.destroy()
         import Wallet
         Wallet.Wallet()

    #  for Admin
    def go_Admin(self):
         self.window.destroy()
         import Admin
         Admin.Admin()

    #for singup button
    def singup_in_db(self):
        conn = sqlite3.connect('test.db')
        #check for First name
        if self.First_Name.get() == '' or  self.First_Name.get().isdigit():
            messagebox.showinfo("Error", "   Please enter your First name")
            self.window.destroy()
            conn.close()
            Signup()
            return

        #  check for Last name
        if self.Last_name.get() == '' or self.Last_name.get().isdigit():
            messagebox.showinfo("Error", "   Please enter your Last name")
            self.window.destroy()
            conn.close()
            Signup()
            return

        # check for ID
        if len(self.ID.get()) < 10 or len(self.ID.get()) > 10 or  len(self.ID.get()) == '' or not(self.ID.get().isdigit()):
            messagebox.showinfo("Error", "   Please enter your ID")
            self.window.destroy()
            conn.close()
            Signup()
            return

        # check for password
        if len(self.Password.get()) <6:
            messagebox.showinfo("Error", "   Please enter your passwrod")
            self.window.destroy()
            conn.close()
            Signup()
            return

        #  check for Email
        if not( self.Email_address.get().endswith("@ksu.edu.sa")):
            messagebox.showinfo("Error", "   Please enter your email")
            self.window.destroy()
            conn.close()
            Signup()
            return

        #  check for phone
        if (not (self.Phone_number.get().startswith("05")) or  not (len(self.Phone_number.get()) == 10)) and self.Phone_number.get().isdigit():
            messagebox.showinfo("Error", "   Please enter your phone")
            self.window.destroy()
            conn.close()
            Signup()
            return

        #makeing wallet_numbe  and chacking
        wallet_number = random.randint(0000000000, 9999999999)

        # chack the ID if in db

        #cheking the db
        cursor22 = conn.execute(" SELECT  * from st1 ")
        for row2 in cursor22:

            #chack the email if in db
            if str(self.Email_address.get()) == str(row2[5]):
                messagebox.showinfo("Error", "   you are registered")
                self.window.destroy()
                conn.close()
                Signup()
                return

            # chack the phone if in db
            if str(self.Phone_number.get()) == str(row2[6]):
                messagebox.showinfo("Error", "   you are registered")
                self.window.destroy()
                conn.close()
                Signup()
                return

            # chack the ID if in db
            if str(self.ID.get()) == str(row2[0]):
                messagebox.showinfo("Error", "  you are registered")
                self.window.destroy()
                conn.close()
                Signup()
                return

        #FOR TIME:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # FOR ADDING TO THE DB
        conn.execute(f" INSERT  INTO st1 (ID,wallet_number,First_Name,last_Name,Password,Email_address,Phone_number,type_of , balance, datetime) \
        VALUES  ( '{int(self.ID.get())} ', '{int(wallet_number)}', '{str(self.First_Name.get())}' , '{str(self.Last_name.get())}' , '{str(self.Password.get())}','{str(self.Email_address.get())}' , '{str(self.Phone_number.get())}' , 'Student' ,'1000' , '{str(dt_string)}' ); ")
        conn.commit()

        #TO SHOW YOUR Wallet number
        conn = sqlite3.connect('test.db')
        messagebox.showinfo("DONE", f"   you are registered now your wallet number is {wallet_number}", icon='info')
        conn.close()
        self.window.destroy()
        Signup()
        return
Signup()