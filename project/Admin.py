import sqlite3
import tkinter
import tkinter as tk
import random
import csv
from tkinter import messagebox
from datetime import datetime

class Admin:
   def __init__(self):
      self.window = tk.Tk()
      self.window.iconbitmap("myIcon.ico")
      self.window.title("Admin")
      self.window.geometry('800x450')
      self.window.geometry("+600+200")
      self.window.config(bg="lightblue")
      self.Name = tkinter.StringVar()
      balance =0

      # for gating the total balance of all KSU entities wallets
      conn = sqlite3.connect('test.db')
      blc = conn.execute("select balance from st1  where type_of = 'KSU' ")
      for row in blc:
         balance = int(row[0]) + balance

      # logo
      self.label2 = tkinter.Label(self.window, text='KsuPay', font=("arial", 30, "bold"), bg="lightblue")
      self.label2.grid(column=2, row=0)

      # name
      self.label1 = tkinter.Label(self.window, text='name',font=("arial", 15), bg="lightblue")
      self.label1.grid(column=1, row=3)

      # name entery
      self.name_enter = tkinter.Entry(self.window, textvariable=self.Name, width="70")
      self.name_enter.grid(column=2, row=3)

      # for total balance of all KSU entities wallet
      self.label1 = tkinter.Label(self.window, text=f' total balance is {balance} SAR ', font=("arial", 15), bg="lightblue")
      self.label1.grid(column=1, row=5)

      #submit button
      self.submit_button = tkinter.Button(self.window, text="  Submit  ",font=("arial", 10),command=self.do_Submit, height = 3, width = 10)
      self.submit_button.grid(column=0, row=3,pady=5, ipadx=10)

      # stipends button
      self.Stipends_button = tkinter.Button(self.window, text="Pay Stipends",font=("arial", 10),command=self.Pay_Stipends, height = 3, width = 10)
      self.Stipends_button.grid(column=0, row=4,pady=5, ipadx=10)

      # cash outts button
      self.Cash_Outs_button_2 = tkinter.Button(self.window, text="     Cash Out    ",font=("arial", 10),command=self.Cash_Out_button, height = 3, width = 10)
      self.Cash_Outs_button_2.grid(column=0, row=5,pady=5, ipadx=10)

      # backup button
      self.backup_button_2 = tkinter.Button(self.window, text="     Backup    ", font=("arial", 10),command=self.back_up, height=3, width=10)
      self.backup_button_2.grid(column=0, row=6, pady=5, ipadx=10)

      #go to logout
      self.buttonBack = tkinter.Button(self.window, text='     Logout    ',font=("arial", 10), command=self.logout, height = 3, width = 10)
      self.buttonBack.grid(column=0, row=7,pady=5, ipadx=10)






      self.window.mainloop()

   def logout(self):
      self.window.destroy()
      from project import Signup
      Signup.Signup()
   def do_Submit(self):
      conn = sqlite3.connect('test.db')
      now = datetime.now()
      dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
      wallet_number = random.randint(0000000000, 9999999999)
      # FOR ADD TO THE DATA BESA
      conn.execute(f" INSERT  INTO st1 (ID,wallet_number,First_Name,last_Name,Password,Email_address,Phone_number,type_of , balance, datetime) \
             VALUES  ( 'null', '{int(wallet_number)}', '{str(self.Name.get())}' , 'null' , 'null','null' , 'null' , 'KSU' ,'0' , '{str(dt_string)}' ); ")
      conn.commit()
      # TO SHOW YOUR Wallet number
      messagebox.showinfo("DONE", f"   the entitie is  registered now the  wallet number is {wallet_number}", icon='info')
      self.window.destroy()
      Admin()


   def Pay_Stipends(self):
      conn = sqlite3.connect('test.db')
      conn.execute("UPDATE st1  SET balance = balance + 1000  where type_of = 'Student' ")
      conn.commit()

   def Cash_Out_button(self):
      conn = sqlite3.connect('test.db')
      conn.execute("UPDATE st1  SET balance = 0  where type_of = 'KSU' ")
      conn.commit()
      self.window.destroy()
      Admin()
   def back_up(self):
      conn = sqlite3.connect('test.db')
      cursor22 = conn.execute(" SELECT  * from st1")
      for row in cursor22:
         file_back = open("backup.csv", 'a')
         csvwriter = csv.writer(file_back)
         csvwriter.writerow(row)

      file_back.close()


