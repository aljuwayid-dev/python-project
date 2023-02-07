from tkinter import *
import tkinter
import tkinter as tk
import sqlite3
from datetime import datetime
from tkinter import messagebox


class Login:
    def __init__(self):
        self.window = tk.Tk()
        self.window.iconbitmap("myIcon.ico")
        self.window.title("Login")
        self.window.geometry('800x350')
        self.window.geometry("+600+200")
        self.window.config(bg="lightblue")
        # student information
        self.ID = StringVar()
        self.Password = StringVar()
        # we use --> textvariable=self.

        #logo
        self.logo_label = tkinter.Label(self.window, text='KsuPay', font=("arial", 30, "bold"), bg="lightblue")
        self.logo_label.grid(column=2, row=0)

        #id
        self.label_ID = tkinter.Label(self.window, text='ID',font=("arial", 20), bg="lightblue")
        self.label_ID.grid(column=1, row=3)

        #id entery
        self.id_enter = tkinter.Entry(self.window , width="80",textvariable=self.ID)
        self.id_enter.grid(column=2, row=3)

        # password lable
        self.Password_label = tkinter.Label(self.window, text='Password',font=("arial", 20), bg="lightblue")
        self.Password_label.grid(column=1, row=4)

        # password entery
        self.Password_enter = tkinter.Entry(self.window, textvariable=self.Password , width="80")
        self.Password_enter.grid(column=2, row=4)

        #login button
        self.button_login_now = tkinter.Button(self.window, text="    login    ",font=("arial", 10),command=self.login_now, height = 3, width = 10)
        self.button_login_now.grid(column=1, row=5,pady=10,ipadx=10)

        #go to singup
        self.buttonBack = tk.Button(self.window, text=' go to Sign up',font=("arial", 10), command=self.go_signup, height = 3, width = 10)
        self.buttonBack.grid(column=1, row=6,pady=10,ipadx=10)

        self.window.mainloop()

        # FOR TIME:
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        conn = sqlite3.connect('test.db')



    # FOR GOING TO SINGUP
    def go_signup(self):
        self.window.destroy()
        from project import Signup
        Signup.Signup()

    #  for student wallet
    def go_Wallet(self , n , k , l):
        self.window.destroy()
        import Wallet
        Wallet.Wallet(n,k,l)

    #  for Admin
    def go_Admin(self):
        self.window.destroy()
        from project import Admin
        Admin.Admin()



    def login_now(self):
        # check for ID
        if len(self.ID.get()) < 10 or len(self.ID.get()) > 10 :
            messagebox.showinfo("Error", "   Please enter your ID")
            self.window.destroy()
            Login()
            return
        # check for password
        if len(self.Password.get()) < 6:
            messagebox.showinfo("Error", "   Please enter your passwrod")
            self.window.destroy()
            Login()
            return



        #FOR LOINGIN TO CHECK IF ADMIN OR STUDENT
        conn = sqlite3.connect('test.db')
        cursor2 = conn.execute(" SELECT *  from st1 ")

        k = 0
        for row in cursor2:
            #IF ADMIN
            if (str(row[0]) == self.ID.get() and str(row[4]) == self.Password.get())and str(row[7]) =='admin':
                conn.close()
                self.go_Admin()
                k=1
                break
            #IF STUDENT
            if (str(row[0]) == self.ID.get() and str(row[4]) == self.Password.get())and str(row[7]) =='Student':
               conn.close()
               self.go_Wallet(row[0],row[1],row[8])
               k=1
               break
        #for not in the db as an Error check we use a (k) to make sure
        if k == 0:
            messagebox.showinfo("Error", "   wrong password or id ")
            k = 0
            self.window.destroy()
            Login()
            return
        k = 0
