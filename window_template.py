from tkinter import *
import sqlite3


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

    def database_create(self):
        self.connection = sqlite3.connect('game.db')
        cursor = self.connection.cursor()# connects to the database, if it doesn't exist it will create one
        cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                            (UserID INTEGER NOT NULL PRIMARY KEY,
                            Username STRING,
                            Hashed_Password STRING,
                            Email STRING)''')
        self.connection.commit()# saves the changes in the database
        self.connection.close() # closes the connection to the database