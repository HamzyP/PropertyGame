from window_template import Window
from tkinter import *


class MainMenu(Window):
    def __init__ (self, title , header):
        super().__init__(title, header) # inherits from the parent function
     
    def Game_on_click(self,username):
        self.Close()
        from game import Game
        game_page = Game("Buying and Selling Properties Game - Game ","GAME PAGE") #This is the title that appears right at the top that is the name of the program
        Game.game_function(game_page,username) # opens the game page

    def Settings_on_click(self,username):
        self.Close()
        from settings import Settings
        Settings_page= Settings("Buying and Selling Properties Game - Settings ","Settings") #This is the title that appears right at the top that is the name of the program
        Settings.settings_function(Settings_page,username) # opens the leaderboard page

    def logout_on_click(self):
        self.Close() # closes this (MainMenu) window
        from login import Login
        Login_page = Login("Buying and Selling Properties Game - Login ","LOGIN PAGE") #This is the title that appears right at the top that is the name of the program
        Login.login_function(Login_page) # opens the login page

    def Leaderboard_on_click(self,username):
        self.Close()
        from leaderboard import Leaderboard
        Leaderboard_page= Leaderboard("Buying and Selling Properties Game - Leaderboard ","Leaderboard") #This is the title that appears right at the top that is the name of the program
        Leaderboard.leaderboard_function(Leaderboard_page,username) # opens the leaderboard page
    
    def main_menu_function(self,username):
        # Widgets:
        Game_button = Button(self.window, width = 15, text = "Game", command= lambda: self.Game_on_click(username), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        Game_button.place(x=550, y=400)

        #Login button that captures the data by taking the program into the Game_on_click function
        Leaderboard_button = Button(self.window, width = 15, text = "Leaderboard", command= lambda: self.Leaderboard_on_click(username), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        Leaderboard_button.place(x=550, y=300)

        Settings_button = Button(self.window, width = 15, text = "Settings", command= lambda: self.Settings_on_click(username), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        Settings_button.place(x=550, y=200)
        #Login button that captures the data by taking the program into the Settings_on_click function

        logout_button = Button(self.window, width = 20, text = "Logout", command= self.logout_on_click, font = ("Calibri", 18, 'bold'),fg = self.white, background = self.blue)
        logout_button.place(x=100, y=450)

        #This is the title that appears right at the top that is the name of the program
        self.window.mainloop()
