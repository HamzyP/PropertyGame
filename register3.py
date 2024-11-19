# Handles the register function
# should be pretty simple register the user add the stuff to database if exists and this job is done.
from window_template import Window
import re
import os
import hashlib
from tkinter import *
import sqlite3

class Register(Window):
    def __init__ (self, title , header):
        super().__init__(title, header)
     
    def Register_on_click(self):
        work = True
        # self.database_create() # calls the function to create the database 
        #collects data entered through the entry fields
        self.username_entered = self.Username_entry.get()
        self.username_entered = self.username_entered.lower() # saves in lower case so when compared during login it can compare accurately
        self.password_entered = self.Password1_Entry.get()
        self.confirm_password_entered = self.Password2_Entry.get()
        self.email_entered = self.Email_Entry.get()
        self.email_entered = self.email_entered.lower()

        #VALIDATION CHECKS:
        regex = re.compile('[@!#$%^&*()<>?/\\\\|}{~:]')
        if self.password_entered != self.confirm_password_entered:# This checks that the password entries match to ensure that the user hasn't entered it incorrectly by accident.
            work = False # shouldnt work if the condition is met
            message=Label(self.window, text = "Your passwords aren't a match. Please re enter them", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.3, anchor ='center') # error that is shown through label to user.
            self.Password1_Entry.delete(0, END)
            self.Password2_Entry.delete(0, END)

        if len(self.password_entered) < 6: # validate the length of the password
            work = False # shouldnt work if the condition is met
            message=Label(self.window, text = "Your password is too short. Please try again.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')
            self.Password1_Entry.delete(0, END)
            self.Password2_Entry.delete(0, END)
        
        if len(self.username_entered) < 4 or len(self.username_entered) > 15: # validate the length of the username
            work = False # shouldnt work if the condition is met
            message=Label(self.window, text = "Your username is an invalid length. Please try again.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')
            self.Password1_Entry.delete(0, END)
            self.Password2_Entry.delete(0, END)

        if regex.search(self.username_entered) is not None: # validates the special characters - no special characters allowed in username
            work = False # shouldnt work if the condition is met
            message=Label(self.window, text = "Your email is invalid. Please try again.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')
            self.Password1_Entry.delete(0, END) # deletes password entries
            self.Password2_Entry.delete(0, END) 

        if self.email_entered[0] == "." or self.email_entered[-1] == ".":
            work = False # shouldnt work if the condition is met
            message=Label(self.window, text = "Your email is invalid. Please try again.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')
            self.Password1_Entry.delete(0, END) # deletes password entries
            self.Password2_Entry.delete(0, END) 


        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the database file path in the same directory as the script
        db_path = os.path.join(script_dir, 'game.db')
        #connects to database
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM Users WHERE username = ? ", (self.username_entered,))
        #checks if user already exists (in database)
        data = cursor.fetchone()

        if data is not None:
            work = False
            message=Label(self.window, text = "The username is already taken. Please try a different one.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')
            self.Username_entry.delete(0, END) # deletes the entry field
            self.Password1_Entry.delete(0, END) # deletes the entry field
            self.Password2_Entry.delete(0, END) # deletes the entry field
            self.Email_Entry.delete(0, END) # deletes the entry field

        connection.close()

        if work == True: # If it passes all the validation checks then it will be inputted into the database.
            salt = os.urandom(32) # comes up with something random to use as a salt

            self.password_entered = hashlib.pbkdf2_hmac('sha256',
            self.password_entered.encode('utf-8'), 
            salt, 
            100000,
            dklen=128
            )

            self.password_entered = salt + self.password_entered
           # print("salt:",salt)
           # print("password register:" , self.password_entered)

            # Get the absolute path of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Define the database file path in the same directory as the script
            db_path = os.path.join(script_dir, 'game.db')

            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            money_amount = 25000
            prop_ownership = False
            prop_value = 5000
            cursor.execute('''INSERT INTO Users (Username,Hashed_Password, Email, Money, OwnResi1, ValueResi1) VALUES (?, ?, ?, ?, ?, ?)''',
                            (self.username_entered, self.password_entered, self.email_entered,money_amount, prop_ownership, prop_value)) 
            #This inserts it into the database using SQL.
            connection.commit() # saves the changes in the database
            connection.close() # closes the connection to the database

            message=Label(self.window, text = "Thank you for creating an account with us.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')

            #the following input is in format:
            #username, data[1], own r prop 1, value of r prop 1, own r prop 2, value of r prop 2, own r prop 3, value of r prop 3, own r prop 3, value of r prop 3, and so on until prop7 then commercial prop1... after this its rentingRprop1 rentingrProp2 and so on
            # after 55000 is commercial prop 1
            # lines = [self.username_entered, 50000, "n", 25000, "n", 30000, "n", 35000, "n", 40000, "n", 45000, "n", 50000, "n", 55000, "n", 50000, "n", 55000, "n", 60000, "n", 65000, "n", 70000, "n", 75000, "n", 80000,  "n", 100000, "n", 110000, "n", 120000, "n", 130000, "n", 140000, "n", 150000, "n", 160000, "n" , "n", "n", "n" , "n", "n", "n", "n" , "n", "n", "n" , "n", "n", "n", "n" , "n", "n", "n" , "n", "n", "n"]
            # counter = 0
            # with open('game_data.txt', 'a') as f:
            #     for line in lines:
            #         counter = counter+1
            #         line = str(line)
            #         f.write(line)
            #         f.write(',')
            #         if counter == 65: # when the data has been entered, moves the cursor to the next line for the next user that will register.
            #             f.write('\n')

            self.Username_entry.delete(0, END)
            self.Password1_Entry.delete(0, END)
            self.Password2_Entry.delete(0, END)
            self.Email_Entry.delete(0, END)
    #This is what happens when you click the register button. It grabs the data entered into the entry fields and
    #stores them as entry fields.

    def Login_page_on_click(self):
        self.Close() # closes this (register) window
        from login import Login
        Login_page = Login("Buying and Selling Properties Game - Login ","LOGIN PAGE") #This is the title that appears right at the top that is the name of the program
        Login.login_function(Login_page) # opens the login page

    def Register_function(self):
        # Widgets:
        self.UsernameText=Label(self.window, text = "Username:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
        self.UsernameText.place(relx = 0.40, rely = 0.45, anchor ='center')#This determines where the text is place onscreen
        #This literally prints 'Username'
        self.Username_entry = Entry(self.window,width= 18 , bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Username_entry.place(relx = 0.61, rely = 0.45, anchor ='center')#This determines where the entry for the username is placed onscreen
        #The bit that you actually write the text into. Next to the username.

        self.Password1=Label(self.window, text = "Password:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.Password1.place(relx = 0.40, rely = 0.55, anchor ='center')
        #This literally displays 'Password:' on the screen
        self.Password1_Entry = Entry(self.window,show = '*',width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Password1_Entry.place(relx = 0.61, rely = 0.55, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says Password:.

        self.Password2=Label(self.window, text = "Confirm Password:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.Password2.place(relx = 0.35, rely = 0.65, anchor ='center')
        #This literally displays 'Password:' on the screen
        self.Password2_Entry = Entry(self.window,show = '*',width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Password2_Entry.place(relx = 0.61, rely = 0.65, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says Confirm Password:.


        self.Email=Label(self.window, text = "Email:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.Email.place(relx = 0.4155, rely = 0.75, anchor ='center')
        #This literally displays 'Email:' on the screen
        self.Email_Entry = Entry(self.window,width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Email_Entry.place(relx = 0.61, rely = 0.75, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says Email:.


        self.Register_button = Button(self.window, width = 15, text = "Register", command= self.Register_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        self.Register_button.place(x=550, y=500)
        #Register button that captures the data by taking the program into the on_click function

        Login_page_button = Button(self.window, width = 20, text = "Login Here", command= self.Login_page_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        Login_page_button.place(x=100, y=450)
        #Login page button in the bottom left - takes you to the login page

        self.window.mainloop()
