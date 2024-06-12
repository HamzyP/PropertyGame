from window_template import Window
from tkinter import *
import sqlite3
import hashlib
import os

class Settings(Window):
    def __init__ (self, title , header):
        super().__init__(title, header)

    def back_on_click(self,username):
        self.Close()
        from menu import MainMenu
        Main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu ","MAIN MENU") #This is the title that appears right at the top that is the name of the program
        MainMenu.main_menu_function(Main_menu_page,username)

    def changing_password(self,username):
        self.connection = sqlite3.connect('game.db') # connects to the database
        cursor = self.connection.cursor()
        cursor.execute('''SELECT Hashed_Password FROM Users WHERE Username = ? ''', (username,) ) #finds the correlating password to the username entered
        data = cursor.fetchone()
        db_password = data[0]  
        self.connection.close()

        self.Old_Password=Label(self.window, text = "Old Password:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.Old_Password.place(relx = 0.38, rely = 0.45, anchor ='center')
        #This literally displays 'Old Password:' on the screen
        self.Old_Password_Entry = Entry(self.window,show = '*',width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Old_Password_Entry.place(relx = 0.61, rely = 0.45, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says 'Old Password:'

        self.New_Password=Label(self.window, text = "New Password:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.New_Password.place(relx = 0.37, rely = 0.55, anchor ='center')
        #This literally displays 'Password:' on the screen
        self.New_Password_Entry = Entry(self.window,show = '*',width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.New_Password_Entry.place(relx = 0.61, rely = 0.55, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says 'New Password:'

        self.Confirm_NewPassword=Label(self.window, text = "Confirm New Password:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.Confirm_NewPassword.place(relx = 0.33, rely = 0.65, anchor ='center')
        #This literally displays 'Password:' on the screen
        self.Confirm_NewPassword_Entry = Entry(self.window,show = '*',width= 18, bg = "light blue", font=("Calibri", 28,'bold'),fg = '#000000' )
        self.Confirm_NewPassword_Entry.place(relx = 0.61, rely = 0.65, anchor ='center')
        #Entry field that you actually write the text into. Next to where it says 'Confirm New Password:'

        change_password_button = Button(self.window, width = 15, text = "Change Password", command=lambda:[self.password_change_command(username,db_password)], font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        change_password_button.place(x=550, y=500)

        back_button = Button(self.window, width = 15, text = "Back", command=lambda:[self.Settings_on_click(username)], font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        back_button.place(x=40, y=30)
    
    def Settings_on_click(self,username):
        self.Close()
        Settings_page= Settings("Buying and Selling Properties Game - Settings ","Settings") #This is the title that appears right at the top that is the name of the program
        Settings.settings_function(Settings_page,username) # opens the leaderboard page



    def password_change_command(self,username,db_password):
        self.Old_Password = self.Old_Password_Entry.get() 
        self.New_Password = self.New_Password_Entry.get() 
        self.Confirm_New_Password = self.Confirm_NewPassword_Entry.get()
        
        salt_from_storage = db_password[:32] # 32 is the length of the salt
        key_from_storage = db_password[32:]

        self.Old_Password = hashlib.pbkdf2_hmac(
            'sha256', # The hash digest algorithm for HMAC
            self.Old_Password.encode('utf-8'), # Convert the password to bytes
            salt_from_storage, # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256 
            dklen=128 # Get a 128 byte key
            )


        if self.Old_Password == key_from_storage:
            if self.New_Password == self.Confirm_New_Password:
                salt = os.urandom(32) # comes up with something random to use as a salt

                self.New_Password = hashlib.pbkdf2_hmac('sha256',
                self.New_Password.encode('utf-8'), 
                salt, 
                100000,
                dklen=128
                )
                self.New_Password = salt + self.New_Password

                connection = sqlite3.connect('game.db')
                cursor = connection.cursor()
                
                
                cursor.execute('UPDATE Users SET Hashed_Password=? WHERE username=?', [self.New_Password, username])
                
                
                connection.commit() # saves the changes in the database
                connection.close() # closes the connection to the database
                
                
                self.Old_Password_Entry.delete(0, END) # deletes the entry field
                self.New_Password_Entry.delete(0, END) # deletes the entry field
                self.Confirm_NewPassword_Entry.delete(0, END) # deletes the entry field
                
                
                message=Label(self.window, text = "Your password has successfully changed.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
                message.place(relx = 0.3, rely = 0.35, anchor ='center')
            
            
            
            elif self.New_Password != self.Confirm_New_Password:
                self.Old_Password_Entry.delete(0, END) # deletes the entry field
                self.New_Password_Entry.delete(0, END) # deletes the entry field
                self.Confirm_NewPassword_Entry.delete(0, END) # deletes the entry field
                message=Label(self.window, text = "Your new passwords do not match.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
                message.place(relx = 0.3, rely = 0.35, anchor ='center')

        elif self.Old_Password != db_password:
            self.Old_Password_Entry.delete(0, END) # deletes the entry field
            self.New_Password_Entry.delete(0, END) # deletes the entry field
            self.Confirm_NewPassword_Entry.delete(0, END) # deletes the entry field
            message=Label(self.window, text = "Old Password does not match.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.3, rely = 0.35, anchor ='center')


    def main_changePassword(self,username):
        self.Close() # closes this (MainMenu) window
        change_password = Settings("Buying and Selling Properties Game - Change Password ","Change your password") #This is the title that appears right at the top that is the name of the program
        Settings.changing_password(change_password,username) # opens the login page

    def logout_on_click(self):
        self.Close() # closes this (MainMenu) window
        from login import Login
        Login_page = Login("Buying and Selling Properties Game - Login ","LOGIN PAGE") #This is the title that appears right at the top that is the name of the program
        Login.login_function(Login_page) # opens the login page

    def settings_function(self,username):
        self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command=lambda:self.back_on_click(username)
                                  , background = self.blue, fg = self.white, padx='25', pady = '5')
        self.back_button.place ( x=40, y = 30)

        change_Password_button = Button(self.window, width = 50, text = "Change your password", command=lambda:[self.main_changePassword(username)], font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        change_Password_button.place(x=300, y=300)

        logout_button = Button(self.window, width = 50, text = "Logout", command= self.logout_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        logout_button.place(x=300, y=450)

        self.window.mainloop()