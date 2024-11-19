from tkinter import *
import sqlite3
import os


class Window():
    def __init__ (self, title, header):
        self.window = Tk() # creates window 
        self.window.geometry("1200x630")# determines size of the window
        self.window.minsize(1200,630) # minsize and maxsize are equal to each other to lock the size in place to ensure everything is displayed correctly
        self.window.maxsize(1200,630)
        self.title = title # parameter passed through stored as variable
        self.window.title(self.title) # names the window what the variable title is called
        self.header = header # Header at the top is name 

        #list of colours i will be using( I have put them into variables so i do not need to remember the RGB/Hex code)
        #Colour List:
        self.gray = '#808080'
        self.blue = '#4472c4'
        self.red = '#FF0000'
        self.white = '#FFFFFF'
        self.black = '#000000'
        self.light_blue = 'light blue'
        self.burgundy = '#800020'
        self.magenta = '#FF00FF'
        self.turquoise = '#008080'#30D5C8
        self.teal = '#677FA3' # 008080
        self.livid = '#6699CC'
        self.orange = '#efa37f'
        self.lime_green = "#32CD32"
        self.yellow = '#FFCC00'

        self.lbl=Label(self.window, relief = 'raised', text= self.header , fg= self.white , padx = '65', pady = '25' ,background = self.blue, font=("Calibri", 28, 'bold'))
        self.lbl.place(x=475, y=20)
        # big title button at the top naming the page

        self.exit_button = Button(self.window, text = "x", font=("Calibri", 28,'bold'), command=self.Close, background = self.blue, fg = self.white, padx='25', pady = '15')
        self.exit_button.place ( x=1075, y = 20) 
        #button in the top right and Closes the program when pressed.

    '''def back_button(self,command_page):
        self.back_button = Button(self.window, text = "x", font=("Calibri", 28,'bold'), command=command_page, background = self.blue, fg = self.white, padx='25', pady = '15')
        self.back_button.place ( x=100, y = 100)'''
        
    def Close(self):
        self.window.destroy()
        #This function is the x button in the top right and will close the program when clicked.
    
def database_create():
    try:
        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the database file path in the same directory as the script
        db_path = os.path.join(script_dir, 'game.db')

        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()  # Connects to the database, creating it if it doesn't exist

        # Create Users table
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                            UserID INTEGER PRIMARY KEY AUTOINCREMENT,
                            Username STRING UNIQUE,
                            Hashed_Password BLOB,
                            Email STRING UNIQUE,
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

        connection.commit()  # Save changes
        connection.close()   # Close connection to the database
        print("Database created and tables initialized successfully.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")