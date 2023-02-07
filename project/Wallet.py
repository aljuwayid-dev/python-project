import sqlite3
import tkinter as tk
import tkinter
from datetime import datetime
from tkinter import *
from tkinter import messagebox


class Wallet:
    def __init__(self, id ,wn , bl):
        self.window = tk.Tk()
        self.window.iconbitmap("myIcon.ico")
        self.window.title("Student Wallet")
        self.window.geometry('800x350')
        self.window.geometry("+600+200")
        self.window.config(bg="lightblue")
        self.target = StringVar()
        self.amount = StringVar()
        self.ID = id
        self.wallet_number = wn
        self.balance = bl


        # logo
        self.label2 = tkinter.Label(self.window, text='KsuPay', font=("arial", 30, "bold"), bg="lightblue")
        self.label2.grid(column=2, row=0)

        #label wallet number
        self.wallet_number_label = tkinter.Label(self.window, text=f'wallet number :{self.wallet_number}', font=("arial", 20, "bold"),bg="lightblue")
        self.wallet_number_label.grid(column=2, row=6)

        #label balance
        self.balance_label = tkinter.Label(self.window, text=f'balance :{self.balance}', font=("arial", 20, "bold"), bg="lightblue")
        self.balance_label.grid(column=2, row=5)

        # send money label
        self.send_money_label = tkinter.Label(self.window, text='send money:', font=("arial",20, "bold"), bg="lightblue")
        self.send_money_label.grid(column=1, row=1)

        # target label
        self.target_label = tkinter.Label(self.window, text='wallet number',font=("arial", 20), bg="lightblue")
        self.target_label.grid(column=1, row=3)

        # target entery
        self.target_enter = tkinter.Entry(self.window, textvariable=self.target, width="60")
        self.target_enter.grid(column=1 + 1, row=3)

        # amount label
        self.amount_label = tkinter.Label(self.window, text='amount',font=("arial", 20), bg="lightblue")
        self.amount_label.grid(column=1, row=4)

        # amount entery
        self.amount_enter = tkinter.Entry(self.window,textvariable=self.amount, width="60")
        self.amount_enter.grid(column=2, row=4)

        #pay button
        self.paynow_button = tk.Button(self.window, text="    Pay    ",command=self.paynow,font=("arial", 10), height = 3, width = 10)
        self.paynow_button.grid(column=0, row=5,pady=5,ipadx=10)

        #logout
        self.buttonBack = tk.Button(self.window, text=' Logout ', command=self.logout,font=("arial", 10), height = 3, width = 10)
        self.buttonBack.grid(column=0, row=6,pady=5,ipadx=10)

        self.window.mainloop()

    def logout(self):
        self.window.destroy()
        from project import Signup
        Signup.Signup()

    def paynow(self):
        w = 0
        conn = sqlite3.connect('test.db')

        #check the wallte number  before going to the db
        if len(str(self.target.get())) < 10 or len(str(self.target.get())) > 10:
            messagebox.showinfo("Error", "   Please enter the wallet number")
            self.window.destroy()
            Wallet(self.ID,self.wallet_number ,self.balance)

        # check the amount  before going to the db
        if  str(self.amount.get()) == '' or int(self.balance) < int(self.amount.get()) or int(self.balance) == 0:
            messagebox.showinfo("Error", " There is not enough money ")
            self.window.destroy()
            Wallet(self.ID,self.wallet_number ,self.balance)

        cursor22 = conn.execute(" SELECT  * from st1 ")
        for row22 in cursor22:

            # chack the wallet number if not in  db
            if str(self.target.get()) == str(row22[1]):
                 w=1

        if w ==0 :
            messagebox.showinfo("Error", "  Please enter the wallet number ")
            self.window.destroy()
            Wallet(self.ID,self.wallet_number ,self.balance)



        # for loging the transactions part 1
        file_log = open('transactions.txt', 'a')
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        #for going to the db
        cursor22 = conn.execute(" SELECT  * from st1 ")
        for row2 in cursor22:
            if str(self.target.get()) == str(row2[1]):

                #for takeing the money from the balance
                conn.execute(f'UPDATE st1  SET balance = balance - {str(self.amount.get())}  where wallet_number = {int(self.wallet_number)} and balance > 0')
                conn.commit()

                # to add the amout to the target
                conn.execute(f'UPDATE st1  SET balance = balance + {str(self.amount.get())}  where wallet_number = {int(self.target.get())} ')
                conn.commit()

                conn.close()

                # for loging the transactions part 2
                file_log.write(f"[time = {dt_string} / the amount = {str(self.amount.get())} / the Wallet number of the sender = {int(self.wallet_number)} /  and the Wallet number of the receiver = {int(self.target.get())}]")
                file_log.close()

                break

        # to open the window agine and show the new data
        conn = sqlite3.connect('test.db')
        cursor22 = conn.execute(f" SELECT  balance from st1 where ID = {int(self.ID)}  ")
        for row2 in cursor22:
            self.window.destroy()
            conn.close()
            Wallet(self.ID, self.wallet_number, row2[0])
            return
