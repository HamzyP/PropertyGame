from window_template import Window
from tkinter import *
from tkinter import ttk
import os 
import sqlite3

class Leaderboard(Window):
    def __init__ (self, title , header):
        super().__init__(title, header)

    def back_on_click(self,username):
        self.Close()
        from menu import MainMenu
        Main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu ","MAIN MENU") #This is the title that appears right at the top that is the name of the program
        MainMenu.main_menu_function(Main_menu_page,username)

    def leaderboard_function(self,username):
        self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command= lambda: self.back_on_click(username), background = self.blue, fg = self.white, padx='25', pady = '5')
        self.back_button.place ( x=40, y = 30)
        
        # Create Treeview widget
        
        # Create a style for the Treeview widget
        self.style = ttk.Style()
        self.style.configure('Treeview', background='#e1d8b9', foreground='black')

        self.tree = ttk.Treeview(self.window, columns=('Position','Username', 'Money'), show='headings')
        self.tree.heading('Position', text = 'Position')
        self.tree.heading('Username', text='Username')
        self.tree.heading('Money', text='Money')
        self.tree.pack(pady=20)
        self.tree.place(x=350, y=200)


         # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the database file path in the same directory as the script
        db_path = os.path.join(script_dir, 'game.db')

        connection = sqlite3.connect(db_path)

        cursor = connection.cursor()
        cursor.execute('''SELECT Username,Money FROM Users''') #finds the correlating password to the username entered
        data = cursor.fetchall()
        print(data)
        connection.close()

        leader_data = []
        for entries in data:
            leader_data.append(entries)
        
        # Sort leaderboard data by money (score) in descending order
        leader_data.sort(key=lambda x: x[1], reverse=True)
        # print("leader data", leader_data) # line used for testing.
        # Insert data into the Treeview with row numbers

        for index, (username, Money) in enumerate(leader_data, start=1):
            formatted_username = username.capitalize() #makes user start with a capital ( stored in database as all lowercase so it is case insensitive when logging in)
            formatted_money = f"${Money:.2f}" # Formats the Money variable with a dollar sign ($) and two decimal places (e.g., $25000.00)

            '''Inserts a row into the Treeview widget with the following values:
            - index: The position of the row (starting from 1)
            - formatted_username
            - formatted_money
            
            Parameters:
            - '' (empty string): Specifies the parent item to insert the new row under. Using an empty string ('') means the row will be inserted at the top level.
            - END: Indicates that the new row should be inserted at the end of the Treeview widget's current items.'''

            self.tree.insert('', END, values=(index, formatted_username, formatted_money))

        self.window.mainloop()