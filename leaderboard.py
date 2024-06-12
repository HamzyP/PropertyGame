from window_template import Window
from tkinter import *

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
        
        self.text=Label(self.window, text = "This is something to display:", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='15',pady = '5')
        self.text.place(relx = 0.38, rely = 0.45, anchor ='center')
        self.window.mainloop()