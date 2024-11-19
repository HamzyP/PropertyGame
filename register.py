# Handles the register function
from window_template import Window
import re
import os
import hashlib
from tkinter import *
import sqlite3

class Register(Window):
    def __init__(self, title, header):
        super().__init__(title, header)

    def create_tables(self):
        """Create the necessary tables if they don't already exist."""
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, 'game.db')
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()

        # Create Users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Username TEXT UNIQUE,
                            Hashed_Password BLOB,
                            Email TEXT UNIQUE,
                            Money REAL DEFAULT 25000
                          )''')

        # Create IndustrialProperties table
        cursor.execute('''CREATE TABLE IF NOT EXISTS IndustrialProperties (
                            PropertyID INTEGER PRIMARY KEY AUTOINCREMENT,
                            UserID INTEGER,
                            Own BOOLEAN DEFAULT 0,
                            Value REAL DEFAULT 0,
                            forRent BOOLEAN DEFAULT 0,
                            FOREIGN KEY(UserID) REFERENCES Users(UserID)
                          )''')

        # Create ResidentialProperties table
        cursor.execute('''CREATE TABLE IF NOT EXISTS ResidentialProperties (
                            PropertyID INTEGER PRIMARY KEY AUTOINCREMENT,
                            UserID INTEGER,
                            Own BOOLEAN DEFAULT 0,
                            Value REAL DEFAULT 0,
                            forRent BOOLEAN DEFAULT 0,
                            FOREIGN KEY(UserID) REFERENCES Users(UserID)
                          )''')

        # Create CommercialProperties table
        cursor.execute('''CREATE TABLE IF NOT EXISTS CommercialProperties (
                            PropertyID INTEGER PRIMARY KEY AUTOINCREMENT,
                            UserID INTEGER,
                            Own BOOLEAN DEFAULT 0,
                            Value REAL DEFAULT 0,
                            forRent BOOLEAN DEFAULT 0,
                            FOREIGN KEY(UserID) REFERENCES Users(UserID)
                          )''')

        connection.commit()
        connection.close()

    def Register_on_click(self):
        """Handles user registration and initializes properties."""
        self.create_tables()  # Ensure tables exist

        work = True
        self.username_entered = self.Username_entry.get().lower()
        self.password_entered = self.Password1_Entry.get()
        self.confirm_password_entered = self.Password2_Entry.get()
        self.email_entered = self.Email_Entry.get().lower()

        # VALIDATION CHECKS
        regex = re.compile('[@!#$%^&*()<>?/\\\\|}{~:]')
        if self.password_entered != self.confirm_password_entered:
            work = False
            self.display_message("Your passwords aren't a match. Please re-enter them.")
            self.clear_password_fields()

        if len(self.password_entered) < 6:
            work = False
            self.display_message("Your password is too short. Please try again.")
            self.clear_password_fields()

        if len(self.username_entered) < 4 or len(self.username_entered) > 15:
            work = False
            self.display_message("Your username is an invalid length. Please try again.")
            self.clear_password_fields()

        if regex.search(self.username_entered) is not None:
            work = False
            self.display_message("Your username contains invalid characters. Please try again.")
            self.clear_password_fields()

        if self.email_entered[0] == "." or self.email_entered[-1] == "." or "@" not in self.email_entered:
            work = False
            self.display_message("Your email is invalid. Please try again.")
            self.clear_password_fields()

        # Check if the username or email is already taken
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, 'game.db')
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT Username FROM Users WHERE Username = ? OR Email = ?", 
                       (self.username_entered, self.email_entered))
        data = cursor.fetchone()

        if data is not None:
            work = False
            self.display_message("The username or email is already taken. Please try a different one.")
            self.clear_all_fields()

        if work:
            # Hash the password with a salt
            salt = os.urandom(32)
            self.password_entered = hashlib.pbkdf2_hmac('sha256',
                                                        self.password_entered.encode('utf-8'),
                                                        salt,
                                                        100000,
                                                        dklen=128)
            self.password_entered = salt + self.password_entered

            try:
                # Insert user into the Users table
                cursor.execute('''INSERT INTO Users (Username, Hashed_Password, Email) 
                                  VALUES (?, ?, ?)''', 
                               (self.username_entered, self.password_entered, self.email_entered))
                connection.commit()

                # Get the newly created UserID
                user_id = cursor.lastrowid

                # Initialize properties for the user
                for _ in range(7):  # 7 residential properties
                    cursor.execute("INSERT INTO ResidentialProperties (UserID) VALUES (?)", (user_id,))
                for _ in range(7):  # 7 industrial properties
                    cursor.execute("INSERT INTO IndustrialProperties (UserID) VALUES (?)", (user_id,))
                for _ in range(7):  # 7 commercial properties
                    cursor.execute("INSERT INTO CommercialProperties (UserID) VALUES (?)", (user_id,))
                connection.commit()

                self.display_message("Thank you for creating an account with us.")
                self.clear_all_fields()
            except sqlite3.IntegrityError:
                self.display_message("An error occurred while creating your account. Please try again.")
            finally:
                connection.close()

    def display_message(self, message):
        """Displays a message to the user."""
        Label(self.window, text=message, font=("Georgia", 22,), fg=self.white,
              background=self.blue, padx='11', pady='5').place(relx=0.3, rely=0.35, anchor='center')

    def clear_password_fields(self):
        """Clears the password fields."""
        self.Password1_Entry.delete(0, END)
        self.Password2_Entry.delete(0, END)

    def clear_all_fields(self):
        """Clears all input fields."""
        self.Username_entry.delete(0, END)
        self.Password1_Entry.delete(0, END)
        self.Password2_Entry.delete(0, END)
        self.Email_Entry.delete(0, END)

    def Login_page_on_click(self):
        """Switches to the login page."""
        self.Close()
        from login import Login
        Login_page = Login("Buying and Selling Properties Game - Login", "LOGIN PAGE")
        Login.login_function(Login_page)

    def Register_function(self):
        """Displays the registration form."""
        self.UsernameText = Label(self.window, text="Username:", font=("Georgia", 22,), fg=self.white,
                                  background=self.blue, padx='11', pady='5')
        self.UsernameText.place(relx=0.40, rely=0.45, anchor='center')
        self.Username_entry = Entry(self.window, width=18, bg="light blue", font=("Calibri", 28, 'bold'), fg='#000000')
        self.Username_entry.place(relx=0.61, rely=0.45, anchor='center')

        self.Password1 = Label(self.window, text="Password:", font=("Georgia", 22,), fg=self.white,
                               background=self.blue, padx='15', pady='5')
        self.Password1.place(relx=0.40, rely=0.55, anchor='center')
        self.Password1_Entry = Entry(self.window, show='*', width=18, bg="light blue", font=("Calibri", 28, 'bold'),
                                     fg='#000000')
        self.Password1_Entry.place(relx=0.61, rely=0.55, anchor='center')

        self.Password2 = Label(self.window, text="Confirm Password:", font=("Georgia", 22,), fg=self.white,
                               background=self.blue, padx='15', pady='5')
        self.Password2.place(relx=0.35, rely=0.65, anchor='center')
        self.Password2_Entry = Entry(self.window, show='*', width=18, bg="light blue", font=("Calibri", 28, 'bold'),
                                     fg='#000000')
        self.Password2_Entry.place(relx=0.61, rely=0.65, anchor='center')

        self.Email = Label(self.window, text="Email:", font=("Georgia", 22,), fg=self.white,
                           background=self.blue, padx='15', pady='5')
        self.Email.place(relx=0.4155, rely=0.75, anchor='center')
        self.Email_Entry = Entry(self.window, width=18, bg="light blue", font=("Calibri", 28, 'bold'), fg='#000000')
        self.Email_Entry.place(relx=0.61, rely=0.75, anchor='center')

        self.Register_button = Button(self.window, width=15, text="Register", command=self.Register_on_click,
                                      font=("Calibri", 18, 'bold'), fg=self.white, background=self.blue)
        self.Register_button.place(x=550, y=500)

        Login_page_button = Button(self.window, width=20, text="Login Here", command=self.Login_page_on_click,
                                   font=("Calibri", 18, 'bold'), fg=self.white, background=self.blue)
        Login_page_button.place(x=100, y=450)

        self.window.mainloop()
