from window_template import Window
from tkinter import *
import random
import sqlite3
import os


class Game(Window):#parent class Window is announced here.
    def __init__ (self, title , header):
        super().__init__(title, header)#inherits from parent class
        self.connection = sqlite3.connect('game.db')  # Connect to your existing database
        self.cursor = self.connection.cursor()

    def back_on_click(self,username):
        self.Close()
        from menu import MainMenu
        Main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu ","MAIN MENU") #This is the title that appears right at the top that is the name of the program
        MainMenu.main_menu_function(Main_menu_page,username)

    def back_on_click_game(self,username):
        self.Close()
        game_page = Game("Buying and Selling Properties Game - Game ","GAME PAGE") #This is the title that appears right at the top that is the name of the program
        Game.game_function(game_page,username) # opens the game page

    def call_actions(self,variant, header, title, data, username):
        self.Close()
        actionsR = Game(header,title) #This is the title that appears right at the top that is the name of the program
        Game.actions(actionsR, variant, data, username)


    def call_view_more_info(self, variant, header, title,data,username):
        self.Close()
        view_more_infoR = Game(header,title) #This is the title that appears right at the top that is the name of the program
        Game.view_more_info(view_more_infoR,variant,data,username)



    def actions(self, variant, data, username):
        # TABLE
            self.background_label = Label(self.window,relief='raised', font=("Georgia", 22,),fg = self.white, background = self.blue,padx='575',pady = '220')
            self.background_label.place(relx = 0.5, rely = 0.6,anchor ='center')# these two lines are the big blue background

            self.Residential_label = Label(self.window,relief='raised',text = variant.title() + " Properties", font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='25',pady = '15')
            self.Residential_label.place(relx = 0.53, rely = 0.30,anchor ='center')# label that says Residential Properties

            self.table_holder = Label(self.window, font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='330',pady = '160')
            self.table_holder.place(relx = 0.5, rely = 0.66,anchor ='center')# label that contains info about Industrial
            
            self.Property_Name_label = Label(self.window,relief='raised',text = "Property No.", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.Property_Name_label.place(relx = 0.195, rely = 0.45,anchor ='center')# label that says Property No.
            
            #label to show where the value column is
            self.value_label = Label(self.window,relief='raised',text = "Value", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.value_label.place(relx = 0.35, rely = 0.45,anchor ='center')# label that says VALUE
            
            #label to show what the yes and no represents
            self.owned_label = Label(self.window,relief='raised',text = "Owned", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.owned_label.place(relx = 0.5, rely = 0.45,anchor ='center')# label that says OWNED
            
            #lets the user go back
            self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command=lambda:[self.back_on_click_game(username)], background = self.blue, fg = self.white, padx='5', pady = '15')
            self.back_button.place ( x=40, y = 30)

            #data[1] is the liquid money a user has aka capital
            self.capital_label = Label(self.window,relief='raised',text = ("Money:","£", data[1]), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
            self.capital_label.place(relx = 0.53, rely = 0.20,anchor ='center')# label that displays the money a user has

            print("actions data:", data)
            own_Prop_1 = data[0][2]
            rent_1 = data[0][4]
            value_Prop_1 = data[0][3]

            own_Prop_2 = data[1][2]
            rent_1 = data[1][4]
            value_Prop_2 = data[1][3]

            own_Prop_3 = data[2][2]
            rent_1 = data[2][4]
            value_Prop_3 = data[2][3]

            own_Prop_4 = data[3][2]
            rent_1 = data[3][4]
            value_Prop_4 = data[3][3]

            own_Prop_5 = data[4][2]
            rent_1 = data[4][4]
            value_Prop_5 = data[4][3]

            own_Prop_6 = data[5][2]
            rent_1 = data[5][4]
            value_Prop_6 = data[5][3]

            own_Prop_7 = data[6][2]
            rent_1 = data[6][4]
            value_Prop_7 = data[6][3]


            #Buy/Sell Buttons:
            if own_Prop_1 == 0: # if user doesnt own prop 1 display buy button
                Buy1_button = Button(self.window, relief = 'flat' ,width = 25, text = "BUY", command=lambda:[self.main_buy(data,variant,"1", data)], font = ("Calibri", (10), 'bold'),fg = self.white, background = self.lime_green )
                Buy1_button.place(relx = 0.575, rely = 0.525,anchor ='center')
            elif own_Prop_1 == 1: # if user owns prop 1 display sell button
                SellOne_button = Button(self.window, relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"1", data)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
                SellOne_button.place(relx = 0.575, rely = 0.525,anchor ='center')
            
            if own_Prop_2 == 0:
                Buy2_button = Button(self.window, relief = 'flat' ,width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"2", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
                Buy2_button.place(relx = 0.575, rely = 0.57,anchor ='center')
            
            elif own_Prop_2 == 1:
                Sell2_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"2", data)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
                Sell2_button.place(relx = 0.575, rely = 0.57,anchor ='center')

            if own_Prop_3 == 0:
                Buy3_button = Button(self.window, relief = 'flat' , width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"3", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
                Buy3_button.place(relx = 0.575, rely = 0.615,anchor ='center')
            
            elif own_Prop_3 == 1:
                Sell3_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"3", data)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
                Sell3_button.place(relx = 0.575, rely = 0.615,anchor ='center')

            if own_Prop_4 == 0:
                Buy4_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"4", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
                Buy4_button.place(relx = 0.575, rely = 0.66,anchor ='center')
            
            elif own_Prop_4 == 1:
                Sell4_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"4", data)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
                Sell4_button.place(relx = 0.575, rely = 0.66,anchor ='center')

            if own_Prop_5 == 0:
                Buy5_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"5", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
                Buy5_button.place(relx = 0.575, rely = 0.705,anchor ='center')
            
            elif own_Prop_5 == 1:            
                Sell5_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"5", data)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
                Sell5_button.place(relx = 0.575, rely = 0.705,anchor ='center')
                
            
            if own_Prop_6 == 0:
                Buy6_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"6", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
                Buy6_button.place(relx = 0.575, rely = 0.75,anchor ='center')
            
            elif own_Prop_6 == 1:
                Sell6_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"6", data)],font = ("Calibri", 10, 'bold'), fg = self.white, background = self.red)
                Sell6_button.place(relx = 0.575, rely = 0.75,anchor ='center')

            if own_Prop_7 == 0:
                Buy7_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"7", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
                Buy7_button.place(relx = 0.575, rely = 0.795,anchor ='center')
            
            elif own_Prop_7 == 1:
                Sell7_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"7", data)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
                Sell7_button.place(relx = 0.575, rely = 0.795,anchor ='center')
            #0.73 is the mid column between invest and buy/sell
            
            #Rent buttons
            if rent_1 == 0: # if user isnt renting prop 1
                Rent1_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"1", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent1_button.place(relx = 0.73, rely = 0.525,anchor ='center')
            elif rent_1 == 1: #if user is renting prop 1
                Rent1_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"1", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent1_button.place(relx = 0.73, rely = 0.525,anchor ='center')
            
            if rent_1 == 0:
                Rent2_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"2", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent2_button.place(relx = 0.73, rely = 0.57,anchor ='center')
            if rent_1 == 1:
                Rent2_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"2", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent2_button.place(relx = 0.73, rely = 0.57,anchor ='center')

            if rent_1 == 0:
                Rent3_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"3", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent3_button.place(relx = 0.73, rely = 0.615,anchor ='center')
            elif rent_1 == 1:
                Rent3_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"3", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent3_button.place(relx = 0.73, rely = 0.615,anchor ='center')

            if rent_1 == 0:
                Rent4_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"4", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent4_button.place(relx = 0.73, rely = 0.66,anchor ='center')
            elif rent_1 == 1:
                Rent4_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"4", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent4_button.place(relx = 0.73, rely = 0.66,anchor ='center')

            if rent_1 == 0:
                Rent5_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"5", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent5_button.place(relx = 0.73, rely = 0.705,anchor ='center')
            elif rent_1 == 1:
                Rent5_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"5", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent5_button.place(relx = 0.73, rely = 0.705,anchor ='center')

            if rent_1 == 0:
                Rent6_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"6", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent6_button.place(relx = 0.73, rely = 0.75,anchor ='center')
            elif rent_1 == 1:
                Rent6_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"6", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent6_button.place(relx = 0.73, rely = 0.75,anchor ='center')

            if rent_1 == 0:
                Rent7_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"7", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
                Rent7_button.place(relx = 0.73, rely = 0.795,anchor ='center')
            elif rent_1 == 1:
                Rent7_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"7", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
                Rent7_button.place(relx = 0.73, rely = 0.795,anchor ='center')

            #Invest buttons:
            Invest1_button = Button(self.window, relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"1", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest1_button.place(relx = 0.884, rely = 0.525,anchor ='center')

            Invest2_button = Button(self.window,relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"2", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest2_button.place(relx = 0.884, rely = 0.57,anchor ='center')

            Invest3_button = Button(self.window,relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"3", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest3_button.place(relx = 0.884, rely = 0.615,anchor ='center')

            Invest4_button = Button(self.window,relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"4", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest4_button.place(relx = 0.884, rely = 0.66,anchor ='center')

            Invest5_button = Button(self.window,relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"5", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest5_button.place(relx = 0.884, rely = 0.705,anchor ='center')

            Invest6_button = Button(self.window,relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"6", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest6_button.place(relx = 0.884, rely = 0.75,anchor ='center')

            Invest7_button = Button(self.window,relief = 'flat' , width = 25, text = "Invest", command=lambda:[self.main_invest(data, variant,"7", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.yellow)
            Invest7_button.place(relx = 0.884, rely = 0.795,anchor ='center')

            own_Prop_1 = "Yes" if own_Prop_1 == 1  else "No"
            own_Prop_2 = "Yes" if own_Prop_2 == 1  else "No"
            own_Prop_3 = "Yes" if own_Prop_3 == 1  else "No"
            own_Prop_4 = "Yes" if own_Prop_4 == 1  else "No"
            own_Prop_5 = "Yes" if own_Prop_5 == 1  else "No"
            own_Prop_6 = "Yes" if own_Prop_6 == 1  else "No"
            own_Prop_7 = "Yes" if own_Prop_7 == 1  else "No"

            a_list = [(1,"£"+str(value_Prop_1), own_Prop_1, ' ', " ", " " ),
        (2,"£"+str(value_Prop_2) , own_Prop_2, " ", " ", " "),
        (3,"£"+str(value_Prop_3), own_Prop_3, " ", " ", " "),
        (4,"£"+str(value_Prop_4), own_Prop_4, " ", " ", " "),
        (5,"£"+str(value_Prop_5), own_Prop_5, " ", " ", " "),
            (6,"£"+str(value_Prop_6), own_Prop_6, " ", " ", " "),
            (7,"£"+str(value_Prop_7), own_Prop_7, " ", " ", " ")]

            

            total_rows = len(a_list)
            total_columns = len(a_list[0])
            for row in range(total_rows):
                for column in range(total_columns):
                    self.table = Entry(self.table_holder, width=15, disabledbackground = self.livid , disabledforeground = self.white, fg = self.white,  font=('Arial',16,'bold'))
                    self.table.grid(row = row, column= column)
                    self.table.insert(END, a_list[row][column])
                    self.table.configure(state='disabled', justify = 'center')
                    #if you want to move where the table is presented you have to go to self.table_holder and move that.
            return self,data

    def view_more_info(self, variant, data,username):
            # TABLE
            self.background_label = Label(self.window,relief='raised', font=("Georgia", 22,),fg = self.white, background = self.blue,padx='470',pady = '220')
            self.background_label.place(relx = 0.5, rely = 0.6,anchor ='center')# these two lines are the big blue background

            self.Residential_label = Label(self.window,relief='raised',text = variant.title() + " Properties", font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='25',pady = '15')
            self.Residential_label.place(relx = 0.53, rely = 0.30,anchor ='center')# label that says Residential Properties

            self.Industrial_info_label = Label(self.window, font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='330',pady = '160')
            self.Industrial_info_label.place(relx = 0.5, rely = 0.66,anchor ='center')# label that contains info about Industrial
            
            self.Property_Name_label = Label(self.window,relief='raised',text = "Property No.", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.Property_Name_label.place(relx = 0.195, rely = 0.45,anchor ='center')# label that says Property No.

            self.rent_label = Label(self.window,relief='raised',text = "Rent", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.rent_label.place(relx = 0.35, rely = 0.45,anchor ='center')# label that says RENT

            self.value_label = Label(self.window,relief='raised',text = "Value", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.value_label.place(relx = 0.5, rely = 0.45,anchor ='center')# label that says VALUE

            self.Revenue_label = Label(self.window,relief='raised',text = "Revenue"+"\n" +" Change", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.Revenue_label.place(relx = 0.65, rely = 0.43,anchor ='center')# label that says REVENUE CHANGE
            
            self.value_label = Label(self.window,relief='raised',text = "Owned", font=("Georgia", 18,),fg = self.white, background = self.livid ,padx='20',pady = '10')
            self.value_label.place(relx = 0.81, rely = 0.45,anchor ='center')# label that says OWNED

            self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command=lambda:[self.back_on_click_game(username)], background = self.blue, fg = self.white, padx='5', pady = '15')
            self.back_button.place ( x=40, y = 30)

            
            own_Prop_1 = data[0][2]
            value_Prop_1 = data[0][3]

            own_Prop_2 = data[1][2]
            value_Prop_2 = data[1][3]

            own_Prop_3 = data[2][2]
            value_Prop_3 = data[2][3]

            own_Prop_4 = data[3][2]
            value_Prop_4 = data[3][3]

            own_Prop_5 = data[4][2]
            value_Prop_5 = data[4][3]

            own_Prop_6 = data[5][2]
            value_Prop_6 = data[5][3]

            own_Prop_7 = data[6][2]
            value_Prop_7 = data[6][3]


            own_Prop_1 = "Yes" if own_Prop_1 == 1 or own_Prop_1 == "y" else "No"
            own_Prop_2 = "Yes" if own_Prop_2 == 1 or own_Prop_2 == "y" else "No"
            own_Prop_3 = "Yes" if own_Prop_3 == 1 or own_Prop_3 == "y" else "No"
            own_Prop_4 = "Yes" if own_Prop_4 == 1 or own_Prop_4 == "y" else "No"
            own_Prop_5 = "Yes" if own_Prop_5 == 1 or own_Prop_5 == "y" else "No"
            own_Prop_6 = "Yes" if own_Prop_6 == 1 or own_Prop_6 == "y" else "No"
            own_Prop_7 = "Yes" if own_Prop_7 == 1 or own_Prop_7 == "y" else "No"

            #This is the table that shows up
            a_list = [(1,"£"+str(round((int(value_Prop_1) *0.008))),"£"+str(value_Prop_1),'', own_Prop_1 ),
        (2,"£"+str(round((int(value_Prop_2) *0.008))),"£"+str(value_Prop_2) ,'', own_Prop_2),
        (3,"£"+str(round((int(value_Prop_3) *0.008))),"£"+str(value_Prop_3),'', own_Prop_3),
        (4,"£"+str(round((int(value_Prop_4) *0.008))),"£"+str(value_Prop_4),'', own_Prop_4),
        (5,"£"+str(round((int(value_Prop_5) *0.008))) ,"£"+str(value_Prop_5),'', own_Prop_5),
            (6,"£"+str(round((int(value_Prop_6) *0.008))),"£"+str(value_Prop_6),'', own_Prop_6),
            (7,"£"+str(round((int(value_Prop_7) *0.008))),"£"+str(value_Prop_7),'', own_Prop_7)]

            total_rows = len(a_list)
            total_columns = len(a_list[0])

            for i in range(total_rows):
                for j in range(total_columns):
                    self.e = Entry(self.Industrial_info_label, width=15, disabledbackground = self.livid , disabledforeground = self.white, fg = self.white,  font=('Arial',16,'bold'))
                    self.e.grid(row=i, column=j)
                    self.e.insert(END, a_list[i][j])
                    self.e.configure(state='disabled', justify='center')#disabled the entry box to stop user from typing - using an entry box to display info


    def get_user_data(self, username):
        """Fetch user data from the database."""
        query = "SELECT * FROM Users WHERE username = ?"
        self.cursor.execute(query, (username,))
        data = self.cursor.fetchone()
        if data:
            return data
        else:
            return None  # In case no data found for the username
    def get_resi_data(self,userID):
        """Fetch residential data from the database."""
        query = "SELECT * FROM ResidentialProperties WHERE userID = ?"
        self.cursor.execute(query, (userID,))
        data = self.cursor.fetchall()
        if data:
            return data
        else:
            return None  # In case no data found for the username
        
    def get_comm_data(self,userID):
        """Fetch Commercial data from the database."""
        query = "SELECT * FROM CommercialProperties WHERE userID = ?"
        self.cursor.execute(query, (userID,))
        data = self.cursor.fetchall()
        if data:
            return data
        else:
            return None  # In case no data found for the username

    def get_indu_data(self,userID):
        """Fetch industrial data from the database."""
        query = "SELECT * FROM IndustrialProperties WHERE userID = ?"
        self.cursor.execute(query, (userID,))
        data = self.cursor.fetchall()
        if data:
            return data
        else:
            return None  # In case no data found for the username
        
    def game_function(self,username):

        user_data = self.get_user_data(username)
        # user_Data [0] == userID
        # user_Data [1] == username
        # user_data [4] == money
        if user_data is None:
            print("User not found!")
            return


        # RESIDENTIAL SECTION
        resi_data = self.get_resi_data(user_data[0])
        print("resi_Data:", resi_data)

        # Extract the ownership status (third digit, index 2)
        resi_ownership_status = [entry[2] for entry in resi_data]
        print("resi_ownership_status:", resi_ownership_status)
        resi_value = [entry[3] for entry in resi_data]

        # Assuming 'resi_value' is a list with values corresponding to each property
        r_total = 0
        r_owned_counter = sum(resi_ownership_status)
        rent_rProps = [0] * 7  # List to store rent values for properties 1 to 7

        # Loop through the ownership status and calculate rent based on ownership
        for i, ownership in enumerate(resi_ownership_status):
            if ownership == 1:  # If property is owned (ownership is represented by 1)
                rent = resi_value[i]  # Get the rent from the resi_value list
                r_total += rent  # Add rent for the property
                rent_rProps[i] = round(rent * 0.008)  # Calculate rent for the property



        # Now rent_rProps will contain the rent values for all properties
        rent_rProp_1, rent_rProp_2, rent_rProp_3, rent_rProp_4, rent_rProp_5, rent_rProp_6, rent_rProp_7 = rent_rProps
        # END RESIDENTIAL SECTION
        
        # COMMERCIAL SECTION
        comm_data = self.get_comm_data(user_data[0])
        print("comm_data:", comm_data)

        # Extract the ownership status (third digit, index 2)
        comm_ownership_status = [entry[2] for entry in comm_data]
        print("comm_ownership_status:", comm_ownership_status)
        comm_value = [entry[3] for entry in comm_data]

        # Assuming 'comm_value' is a list with values corresponding to each property
        c_total = 0
        c_owned_counter = sum(comm_ownership_status)
        rent_cProps = [0] * 7  # List to store rent values for properties 1 to 7

        # Loop through the ownership status and calculate rent based on ownership
        for i, ownership in enumerate(comm_ownership_status):
            if ownership == 1:  # If property is owned (ownership is represented by 1)
                rent = comm_value[i]  # Get the rent from the resi_value list
                c_total += rent  # Add rent for the property
                rent_cProps[i] = round(rent * 0.008)  # Calculate rent for the property



        # Now rent_rProps will contain the rent values for all properties
        rent_cProp_1, rent_cProp_2, rent_cProp_3, rent_cProp_4, rent_cProp_5, rent_cProp_6, rent_cProp_7 = rent_cProps

        #END COMMERCIAL SECTION
        #INDUSTRIAL SECTION
        ind_data = self.get_indu_data(user_data[0])
        print("ind_data:", ind_data)

        # Extract the ownership status (third digit, index 2)
        ind_ownership_status = [entry[2] for entry in ind_data]
        print("ind_ownership_status:", ind_ownership_status)
        ind_value = [entry[3] for entry in ind_data]

        # Assuming 'comm_value' is a list with values corresponding to each property
        i_total = 0
        i_owned_counter = sum(ind_ownership_status)
        rent_iProps = [0] * 7  # List to store rent values for properties 1 to 7

        # Loop through the ownership status and calculate rent based on ownership
        for i, ownership in enumerate(comm_ownership_status):
            if ownership == 1:  # If property is owned (ownership is represented by 1)
                rent = ind_value[i]  # Get the rent from the resi_value list
                c_total += rent  # Add rent for the property
                rent_iProps[i] = round(rent * 0.008)  # Calculate rent for the property



        # Now rent_rProps will contain the rent values for all properties
        rent_iProp_1, rent_iProp_2, rent_iProp_3, rent_iProp_4, rent_iProp_5, rent_iProp_6, rent_iProp_7 = rent_iProps

        #END INDUSTRIAL SECTION


        rent_rProp = sum(rent_rProps)
        rent_cProp = sum(rent_cProps)
        rent_iProp = sum(rent_iProps)
        #print(data[1],data[2],data[3])
        #text = ("Properties owned:","\n",owned_counter,"/7")
        
        #Labels:
        self.background_label = Label(self.window,relief='raised', font=("Georgia", 22,),fg = self.white, background = self.blue,padx='470',pady = '220')
        self.background_label.place(relx = 0.5, rely = 0.6,anchor ='center')# these two lines are the big blue background

        self.Residential_label = Label(self.window,relief='raised',text = "Residential", font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='25',pady = '15')
        self.Residential_label.place(relx = 0.23, rely = 0.30,anchor ='center')# label that says Residential

        self.Residential_info_label = Label(self.window,relief='raised', font=("Arial", 22,),fg = self.white, background = self.livid ,padx='130',pady = '130')
        self.Residential_info_label.place(relx = 0.23, rely = 0.62,anchor ='center')# label that contains info about residential

        self.Commercial_label = Label(self.window,relief='raised',text = "Commercial", font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='25',pady = '15')
        self.Commercial_label.place(relx = 0.51, rely = 0.30,anchor ='center')# Label that says Commerical

        self.Commercial_info_label = Label(self.window,relief='raised', font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='130',pady = '130')
        self.Commercial_info_label.place(relx = 0.51, rely = 0.62,anchor ='center')# label that contains info about Commercial

        self.Industrial_label = Label(self.window,relief='raised',text = "Industrial", font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='25',pady = '15')
        self.Industrial_label.place(relx = 0.78, rely = 0.30,anchor ='center')# Label that says Industrial

        self.Industrial_info_label = Label(self.window,relief='raised', font=("Georgia", 22,),fg = self.white, background = self.livid ,padx='130',pady = '130')
        self.Industrial_info_label.place(relx = 0.78, rely = 0.62,anchor ='center')# label that contains info about Industrial

        self.capital_label = Label(self.window,relief='raised',text = ("Money:","£", user_data[4]), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.capital_label.place(relx = 0.53, rely = 0.20,anchor ='center')# label that displays data[1] they have

        #Residential Labels:
        self.r_prop_label = Label(self.window,relief='raised',text = ("Props Owned:"+str(r_owned_counter)+"/7"), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.r_prop_label.place(relx = 0.23, rely = 0.44,anchor ='center')# label that contains info about how many props are owned 

        self.r_propV_label = Label(self.window,relief='raised',text = ("Props Value:\n"+" £"+str(r_total)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.r_propV_label.place(relx = 0.23, rely = 0.55,anchor ='center')# label that contains info about props value

        self.r_propR_label = Label(self.window,relief='raised',text = ("Props Rent:\n"+" £"+str(rent_rProp)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.r_propR_label.place(relx = 0.23, rely = 0.69,anchor ='center')# label that contains info about props value

        #Commercial Labels:
        self.c_prop_label = Label(self.window,relief='raised',text = ("Props Owned:"+str(c_owned_counter)+"/7"), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.c_prop_label.place(relx = 0.51, rely = 0.44,anchor ='center')# label that contains info about how many props are owned 

        self.c_propV_label = Label(self.window,relief='raised',text = ("Props Value:\n"+" £"+str(c_total)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.c_propV_label.place(relx = 0.51, rely = 0.55,anchor ='center')# label that contains info about props value

        self.c_propR_label = Label(self.window,relief='raised',text = ("Props Rent:\n"+" £"+str(rent_cProp)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.c_propR_label.place(relx = 0.51, rely = 0.69,anchor ='center')# label that contains info about props value

        #Industrial Labels:
        self.i_prop_label = Label(self.window,relief='raised',text = ("Props Owned:"+str(i_owned_counter)+"/7"), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.i_prop_label.place(relx = 0.78, rely = 0.44,anchor ='center')# label that contains info about how many props are owned 

        self.i_propV_label = Label(self.window,relief='raised',text = ("Props Value:\n"+" £"+str(i_total)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.i_propV_label.place(relx = 0.78, rely = 0.55,anchor ='center')# label that contains info about props value

        self.i_propR_label = Label(self.window,relief='raised',text = ("Props Rent:\n"+" £"+str(rent_iProp)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.i_propR_label.place(relx = 0.78, rely = 0.69,anchor ='center')# label that contains info about props value

        #Buttons:
        save_button = Button(self.window, width = 8, text = "SAVE",command= lambda: self.save(user_data, user_data), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        save_button.place(relx = 0.945, rely = 0.938,anchor ='center')

        next_turn_button = Button(self.window, width = 8, text = ("NEXT"+"\n"+"MONTH"), command=  lambda: self.main_next_month(user_data, user_data), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        next_turn_button.place(relx = 0.945, rely = 0.83,anchor ='center')

        ViewMore_Residential_button = Button(self.window, width = 15, text = "VIEW MORE INFO",command= lambda: self.call_view_more_info("residential","Buying and Selling Properties Game - Commercial info", "Information", resi_data,user_data[1]),
                                                 font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        ViewMore_Residential_button.place(relx = 0.23, rely = 0.8,anchor ='center')

        ViewMore_Commercial_button = Button(self.window, width = 15, text = "VIEW MORE INFO",command= lambda: self.call_view_more_info("commercial","Buying and Selling Properties Game - Commercial info", "Information",comm_data, user_data[1]),
                                                 font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        ViewMore_Commercial_button.place(relx = 0.51, rely = 0.8,anchor ='center')

        ViewMore_Industrial_button = Button(self.window, width = 15, text = "VIEW MORE INFO",command= lambda: self.call_view_more_info("industrial","Buying and Selling Properties Game - Industrial info", "Information",ind_data, user_data[1]),
                                                 font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        ViewMore_Industrial_button.place(relx = 0.78, rely = 0.8,anchor ='center')

        Actions_Residential_button = Button(self.window, width = 15, text = "ACTIONS", command= lambda: self.call_actions("residential","Buying and Selling Properties Game - Residential Actions", "Actions",resi_data,user_data[1])  , font = ("Calibri", 18, 'bold'),fg = self.white, background = self.lime_green)
        Actions_Residential_button.place(relx = 0.23, rely = 0.91,anchor ='center')
        
        Actions_Commercial_button = Button(self.window, width = 15, text = "ACTIONS", command= lambda: self.call_actions("commercial","Buying and Selling Properties Game - Residential Actions", "Actions",comm_data,user_data[1]), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.lime_green)
        Actions_Commercial_button.place(relx = 0.51, rely = 0.91,anchor ='center')

        Actions_Industrial_button = Button(self.window, width = 15, text = "ACTIONS", command= lambda: self.call_actions("industrial","Buying and Selling Properties Game - Residential Actions", "Actions",ind_data,user_data[1]), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.lime_green)
        Actions_Industrial_button.place(relx = 0.78, rely = 0.91,anchor ='center')

        self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command= lambda: self.back_on_click(user_data[1]), background = self.blue, fg = self.white, padx='25', pady = '5')
        self.back_button.place ( x=40, y = 30)

        self.window.mainloop()