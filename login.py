from window_template import Window
import sqlite3
from tkinter import *
import hashlib
import os

class Login(Window):
    def __init__ (self, title , header):
        super().__init__(title, header)

    def Login_on_click(self):
        #self.database_create()
        self.username_entered = self.Username_entry.get()
        self.username_entered = self.username_entered.lower()# makes the username entered lowercase so it can match it with the database
        self.password_entered = self.Password_Entry.get()
    #This is what happens when you click the login button. It grabs the data entered into the entry fields and
    #stores them as entry fields.

        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the database file path in the same directory as the script
        db_path = os.path.join(script_dir, 'game.db')

        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute('''SELECT Hashed_Password FROM Users WHERE Username = ? ''', (self.username_entered,) ) #finds the correlating password to the username entered
        data = cursor.fetchone()

        if data is None and len(self.username_entered) == 0:# if there is no username or pasword entered, dont do anything
            pass
        elif data is None: # if the user entered isnt in the database, there is no password either so tell them there was an issue with the credentials
            self.errorLbl=Label(self.window, text="There was a problem authenticating your credentials. Please try again.", fg= self.black ,background = self.gray, font=("Calibri", 22,))
            self.errorLbl.place(x=50, y=175)
            self.Username_entry.delete(0, END) #deletes the entry field
            self.Password_Entry.delete(0, END) #deletes the entry field

        else:
            db_password = data[0] # This gets the password on its own without the additional tuple writing
            salt_from_storage = db_password[:32] # 32 is the length of the salt
            key_from_storage = db_password[32:]
            #print(db_password) # This prints the password it has found, useful for debugging and creating the program
            #hashing +salt process
            #print("salt in login:" , salt_from_storage)

            self.password_entered = hashlib.pbkdf2_hmac(
                'sha256', # The hash digest algorithm for HMAC
                self.password_entered.encode('utf-8'), # Convert the password to bytes
                salt_from_storage, # Provide the salt
                100000, # It is recommended to use at least 100,000 iterations of SHA-256 
                dklen=128 # Get a 128 byte key
                )
        
            #end hash+salt process
            #print("Login password:" ,self.password_entered)
            if self.password_entered == key_from_storage: # When password matches, let the user in
                self.Close()
                from menu import MainMenu
                Main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu ","MAIN MENU") #This is the title that appears right at the top that is the name of the program
                MainMenu.main_menu_function(Main_menu_page,self.username_entered)
            elif self.password_entered != db_password: # When the password is typed wrong, show user an error and clear the entry fields
                errorLbl=Label(self.window, text="There was a problem authenticating your credentials. Please try again.", fg= self.black ,background = self.gray, font=("Calibri", 22,)) #shows the user the issue using a label
                errorLbl.place(x=50, y=175)
                self.Username_entry.delete(0, END) #deletes the entry field
                self.Password_Entry.delete(0, END) #deletes the entry field
        connection.close()

    def Login_override_on_click(self):
        self.Close()
        from menu import MainMenu
        Main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu ","MAIN MENU") #This is the title that appears right at the top that is the name of the program
        MainMenu.main_menu_function(Main_menu_page,"hamzy")  # login override that helps for testing - saves me time from typing my user and password in each time

    def Register_page_on_click(self):
        self.Close()# closes this (login) window
        from register import Register
        Register_page = Register("Buying and Selling Properties Game - Register", "REGISTER PAGE")
        Register.Register_function(Register_page)# opens the register page    

    def login_function(self):
        self.UsernameText=Label(self.window, text = "Username:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
        self.UsernameText.place(relx = 0.40, rely = 0.45, anchor ='center')#This determines where the text is place onscreen
        #This literally prints 'Username'
        self.Username_entry = Entry(self.window,width= 18 , bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Username_entry.place(relx = 0.61, rely = 0.45, anchor ='center')#This determines where the entry for the username is placed onscreen
        #The bit that you actually write the text into. Next to the username.

        self.Password=Label(self.window, text = "Password:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.Password.place(relx = 0.40, rely = 0.55, anchor ='center')
        #This literally displays 'Password:' on the screen
        self.Password_Entry = Entry(self.window,show = '*',width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Password_Entry.place(relx = 0.61, rely = 0.55, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says 'Password:'

        # Buttons:
        Login_button = Button(self.window, width = 15, text = "Login", command= self.Login_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        Login_button.place(x=550, y=400)
        #Login button that captures the data by taking the program into the Login_on_click function

        Login_override_button = Button(self.window, width = 15, text = "Login override", command= self.Login_override_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        Login_override_button.place(x=900, y=400)
        #Login button that captures the data by taking the program into the Login_on_click function

        self.Register_page_button = Button(self.window, width = 20, text = "Register Here", command= self.Register_page_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        self.Register_page_button.place(x=100, y=450) # button that takes user to the register page
        self.window.mainloop()