from window_template import Window
from tkinter import *
import random


class Game(Window):#parent class Window is announced here.
    def __init__ (self, title , header):
        super().__init__(title, header)#inherits from parent class

    def back_on_click(self,username):
        self.Close()
        from menu import MainMenu
        Main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu ","MAIN MENU") #This is the title that appears right at the top that is the name of the program
        MainMenu.main_menu_function(Main_menu_page,username)

    def back_on_click_game(self,username):
        self.Close()
        game_page = Game("Buying and Selling Properties Game - Game ","GAME PAGE") #This is the title that appears right at the top that is the name of the program
        Game.game_function(game_page,username) # opens the game page

    # def data(self,username):
    #     flag=0
    #     with open('game_data.txt', 'r') as f: # opens the textfile, withopen means i don't have to close the connection myself.
    #         for line in f:
    #             oldData = line
    #             line = line.split(',') # separates the data with the comma
    #             user_data = line # puts all the data into a list
    #             #index= index + 1 #was used to found out what line the users data is on 
    #             if username in user_data[0]: # when username matches the user's username in the textfile it breaks 
    #                 flag = 1
    #                 break
    #         if flag == 0:
    #             print(username, 'not found') # this is an error which shouldn't occur as all usernames
    #             #should have a corresponding line in the textfile as it is made when registered
    #         else:   
    #             #print(user_data)
    #             #print(user_data[1])
            
    #             return user_data, oldData # returns all the user data into the variable assigned when calling the function

    def data(self,username):
        # print("this is username" , username)
        with open('game_data.txt', 'r') as f:
            for line in f:
                old_data = line.strip()  # Store the entire line as old data
                user_data = old_data.split(',')
                if username == user_data[0]:
                    return user_data, old_data  # Return both user data and old data
            else:
                print(username, 'not found')
                return None, None  # Return None for both values if username is not found

    def buy(self, data, variant, Prop_Number):
        #Finds the relevant pieces of data
        if variant == "residential":
            if Prop_Number == "1":
                own_Prop = data[2]
                value_Prop = data[3]
            elif Prop_Number == "2":
                own_Prop = data[4]
                value_Prop = data[5]
            elif Prop_Number == "3":
                own_Prop = data[6]
                value_Prop = data[7] 
            elif Prop_Number == "4":
                own_Prop = data[8]
                value_Prop = data[9] 
            elif Prop_Number == "5":
                own_Prop = data[10]
                value_Prop = data[11] 
            elif Prop_Number == "6":
                own_Prop = data[12]
                value_Prop = data[13]
            elif Prop_Number == "7":
                own_Prop = data[14]   
                value_Prop = data[15]
        if variant == "commercial":
            if Prop_Number == "1":
                own_Prop = data[16]
                value_Prop = data[17]
            elif Prop_Number == "2":
                own_Prop = data[18]
                value_Prop = data[19]
            elif Prop_Number == "3":
                own_Prop = data[20] 
                value_Prop = data[21]
            elif Prop_Number == "4":
                own_Prop = data[22] 
                value_Prop = data[23]
            elif Prop_Number == "5":
                own_Prop = data[24] 
                value_Prop = data[25]
            elif Prop_Number == "6":
                own_Prop = data[26]
                value_Prop = data[27]
            elif Prop_Number == "7":
                own_Prop = data[28]
                value_Prop = data[29] 
        if variant == "industrial":
            if Prop_Number == "1":
                own_Prop = data[30]
                value_Prop = data[31]
            elif Prop_Number == "2":
                own_Prop = data[32]
                value_Prop = data[33]
            elif Prop_Number == "3":
                own_Prop = data[34] 
                value_Prop = data[35]
            elif Prop_Number == "4":
                own_Prop = data[36] 
                value_Prop = data[37]
            elif Prop_Number == "5":
                own_Prop = data[38] 
                value_Prop = data[39]
            elif Prop_Number == "6":
                own_Prop = data[40]
                value_Prop = data[41]
            elif Prop_Number == "7":
                own_Prop = data[42]
                value_Prop = data[43] 

        if own_Prop == 'n' or "No": # if you don't own the property
            data[1] = int(data[1]) # makes string an integer so we can compare values
            value_Prop = int(value_Prop) # makes string an integer so we can compare values
            if int(data[1]) > int(value_Prop): # checks you have more money than the property is worth
                data[1] = data[1] - value_Prop # takes the value of the property from the users money
                # changes relvant piece of data to yes
                if variant == "residential":
                    if Prop_Number == "1":
                        data[2] = "y"          
                    elif Prop_Number == "2":
                        data[4] = "y"                        
                    elif Prop_Number == "3":
                        data[6] = "y"                        
                    elif Prop_Number == "4":
                        data[8] = "y"                        
                    elif Prop_Number == "5":
                        data[10] = "y"                        
                    elif Prop_Number == "6":
                        data[12] = "y"                        
                    elif Prop_Number == "7":
                        data[14] = "y"                           
                if variant == "commercial":
                    if Prop_Number == "1":
                        data[16] = "y"                        
                    elif Prop_Number == "2":
                        data[18] = "y"                        
                    elif Prop_Number == "3":
                        data[20] = "y"                       
                    elif Prop_Number == "4":
                        data[22] = "y"                         
                    elif Prop_Number == "5":
                        data[24] = "y"                         
                    elif Prop_Number == "6":
                        data[26] = "y"                      
                    elif Prop_Number == "7":
                        data[28] = "y"                        
                if variant == "industrial":
                    if Prop_Number == "1":
                        data[30] = "y"
                    elif Prop_Number == "2":
                        data[32]  = "y"
                    elif Prop_Number == "3":
                        data[34]  = "y"
                    elif Prop_Number == "4":
                        data[36]  = "y"
                    elif Prop_Number == "5":
                        data[38]  = "y"
                    elif Prop_Number == "6":
                        data[40] = "y"
                    elif Prop_Number == "7":
                        data[42] = "y"
                message=Label(self.window, text = "Property successfully bought!", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
                message.place(relx = 0.5, rely = 0.9, anchor ='center') #places message
                return data
            elif data[1] < value_Prop: # if the user doesnt have enough money
                message=Label(self.window, text = "You don't have enough money to buy this property.", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
                message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
                return data
            else:
                return data
        elif own_Prop == "y": # if user owns property and theyre trying to buy it still
            message=Label(self.window, text = "You already own this property.", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
            return data
        
    def main_buy(self, data,variant, Prop_Number, oldData):
        data = self.buy(data,variant,Prop_Number) # buys prop and stores the new data with the prop bought
        oldData = self.save(oldData ,data) # saves the new data, func updates oldData with the new data
        #next line refreshes the page so it shows 'sell' now user owns prop
        self.call_actions(variant,"Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData) 
    
    def main_invest(self, data,variant, Prop_Number, oldData):
        data = self.invest(data,variant,Prop_Number)
        oldData = self.save(oldData ,data)
        self.call_actions(variant,"Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData) 
    
    def invest(self, data, variant, Prop_Number):
        #Finds the relevant pieces of data
        if variant == "residential":
            if Prop_Number == "1":
                own_Prop = data[2]
                value_Prop = data[3]
            elif Prop_Number == "2":
                own_Prop = data[4]
                value_Prop = data[5]
            elif Prop_Number == "3":
                own_Prop = data[6]
                value_Prop = data[7] 
            elif Prop_Number == "4":
                own_Prop = data[8]
                value_Prop = data[9] 
            elif Prop_Number == "5":
                own_Prop = data[10]
                value_Prop = data[11] 
            elif Prop_Number == "6":
                own_Prop = data[12]
                value_Prop = data[13]
            elif Prop_Number == "7":
                own_Prop = data[14]   
                value_Prop = data[15]
        if variant == "commercial":
            if Prop_Number == "1":
                own_Prop = data[16]
                value_Prop = data[17]
            elif Prop_Number == "2":
                own_Prop = data[18]
                value_Prop = data[19]
            elif Prop_Number == "3":
                own_Prop = data[20] 
                value_Prop = data[21]
            elif Prop_Number == "4":
                own_Prop = data[22] 
                value_Prop = data[23]
            elif Prop_Number == "5":
                own_Prop = data[24] 
                value_Prop = data[25]
            elif Prop_Number == "6":
                own_Prop = data[26]
                value_Prop = data[27]
            elif Prop_Number == "7":
                own_Prop = data[28]
                value_Prop = data[29] 
        if variant == "industrial":
            if Prop_Number == "1":
                own_Prop = data[30]
                value_Prop = data[31]
            elif Prop_Number == "2":
                own_Prop = data[32]
                value_Prop = data[33]
            elif Prop_Number == "3":
                own_Prop = data[34] 
                value_Prop = data[35]
            elif Prop_Number == "4":
                own_Prop = data[36] 
                value_Prop = data[37]
            elif Prop_Number == "5":
                own_Prop = data[38] 
                value_Prop = data[39]
            elif Prop_Number == "6":
                own_Prop = data[40]
                value_Prop = data[41]
            elif Prop_Number == "7":
                own_Prop = data[42]
                value_Prop = data[43]
        if own_Prop == 'y' or 'Yes':
            data[1] = int(data[1]) - round(int(value_Prop)*0.1)
            data[1] = str(data[1])
            investment_success = random.randint(1,15)
            #print(investment_success)
            investment_success = int(investment_success) * 0.01
            investment_success = 0.97 + investment_success
            round(investment_success,2)
            value_Prop = int(value_Prop) * float(investment_success)
            value_Prop = str(value_Prop)
            message=Label(self.window, text = ("You have successfully invested!"+"\n"+ "Your property has increased in value by"+str(investment_success)), font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
        elif own_Prop == 'n':
            message=Label(self.window, text = "You cannot invest in a property you do not own.", font=("Georgia", 22,),fg = self.white, background = self.blue,padx='11',pady='5')
            message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
        return data
            
    def sell(self, data, variant, Prop_Number):
        #Finds the relevant pieces of data
        if variant == "residential":
            if Prop_Number == "1":
                own_Prop = data[2]
                value_Prop = data[3]
            elif Prop_Number == "2":
                own_Prop = data[4]
                value_Prop = data[5]
            elif Prop_Number == "3":
                own_Prop = data[6]
                value_Prop = data[7] 
            elif Prop_Number == "4":
                own_Prop = data[8]
                value_Prop = data[9] 
            elif Prop_Number == "5":
                own_Prop = data[10]
                value_Prop = data[11] 
            elif Prop_Number == "6":
                own_Prop = data[12]
                value_Prop = data[13]
            elif Prop_Number == "7":
                own_Prop = data[14]   
                value_Prop = data[15]
        if variant == "commercial":
            if Prop_Number == "1":
                own_Prop = data[16]
                value_Prop = data[17]
            elif Prop_Number == "2":
                own_Prop = data[18]
                value_Prop = data[19]
            elif Prop_Number == "3":
                own_Prop = data[20] 
                value_Prop = data[21]
            elif Prop_Number == "4":
                own_Prop = data[22] 
                value_Prop = data[23]
            elif Prop_Number == "5":
                own_Prop = data[24] 
                value_Prop = data[25]
            elif Prop_Number == "6":
                own_Prop = data[26]
                value_Prop = data[27]
            elif Prop_Number == "7":
                own_Prop = data[28]
                value_Prop = data[29] 
        if variant == "industrial":
            if Prop_Number == "1":
                own_Prop = data[30]
                value_Prop = data[31]
            elif Prop_Number == "2":
                own_Prop = data[32]
                value_Prop = data[33]
            elif Prop_Number == "3":
                own_Prop = data[34] 
                value_Prop = data[35]
            elif Prop_Number == "4":
                own_Prop = data[36] 
                value_Prop = data[37]
            elif Prop_Number == "5":
                own_Prop = data[38] 
                value_Prop = data[39]
            elif Prop_Number == "6":
                own_Prop = data[40]
                value_Prop = data[41]
            elif Prop_Number == "7":
                own_Prop = data[42]
                value_Prop = data[43]

        if own_Prop == 'y' or own_Prop == "Yes": # if you own the property
            data[1] = int(data[1]) # makes string an integer 
            value_Prop = int(value_Prop) # makes string an integer 
            data[1] = data[1] + value_Prop # adds the value of the property to the users money
            # changes relvant piece of data to no so they no longer own the property
            if variant == "residential":
                if Prop_Number == "1":
                    data[2] = "n"          
                elif Prop_Number == "2":
                    data[4] = "n"                        
                elif Prop_Number == "3":
                    data[6] = "n"                        
                elif Prop_Number == "4":
                    data[8] = "n"                        
                elif Prop_Number == "5":
                    data[10] = "n"                        
                elif Prop_Number == "6":
                    data[12] = "n"                        
                elif Prop_Number == "7":
                    data[14] = "n"                           
            if variant == "commercial":
                if Prop_Number == "1":
                    data[16] = "n"                        
                elif Prop_Number == "2":
                    data[18] = "n"                        
                elif Prop_Number == "3":
                    data[20] = "n"                       
                elif Prop_Number == "4":
                    data[22] = "n"                         
                elif Prop_Number == "5":
                    data[24] = "n"                         
                elif Prop_Number == "6":
                    data[26] = "n"                      
                elif Prop_Number == "7":
                    data[28] = "n"                        
            if variant == "industrial":
                if Prop_Number == "1":
                    data[30] = "n"
                elif Prop_Number == "2":
                    data[32]  = "n"
                elif Prop_Number == "3":
                    data[34]  = "n"
                elif Prop_Number == "4":
                    data[36]  = "n"
                elif Prop_Number == "5":
                    data[38]  = "n"
                elif Prop_Number == "6":
                    data[40] = "n"
                elif Prop_Number == "7":
                    data[42] = "n"
            message=Label(self.window, text = "Property successfully sold!", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') #places message
            return data
        elif own_Prop == "n":
            message=Label(self.window, text = "You do not own this property.", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
            return data
        
    def main_sell(self, data,variant, Prop_Number, oldData):
        data = self.sell(data,variant,Prop_Number) # sells prop and stores the new data with the prop sold and money added
        oldData = self.save(oldData ,data) # saves the new data, func updates oldData with the new data
        #next line refreshes the page so it shows 'buy' now that the user owns prop and updates money on screen
        self.call_actions(variant,"Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData) 

    def call_view_more_info(self, variant, header, title,data):
        self.Close()
        view_more_infoR = Game(header,title) #This is the title that appears right at the top that is the name of the program
        Game.view_more_info(view_more_infoR,variant,data)
        
    def view_more_info(self, variant, data):
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

        self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command=lambda:[self.back_on_click_game(data[0])], background = self.blue, fg = self.white, padx='5', pady = '15')
        self.back_button.place ( x=40, y = 30)

        if variant == "residential":
            own_Prop_1 = data[2]
            value_Prop_1 = data[3]
            own_Prop_2 = data[4]
            value_Prop_2 = data[5]
            own_Prop_3 = data[6]
            value_Prop_3 = data[7] 
            own_Prop_4 = data[8]
            value_Prop_4 = data[9] 
            own_Prop_5 = data[10]
            value_Prop_5 = data[11] 
            own_Prop_6 = data[12]
            value_Prop_6 = data[13]
            own_Prop_7 = data[14]   
            value_Prop_7 = data[15]
        if variant == "commercial":
            own_Prop_1 = data[16]
            value_Prop_1 = data[17]
            own_Prop_2 = data[18]
            value_Prop_2 = data[19]
            own_Prop_3 = data[20] 
            value_Prop_3 = data[21]
            own_Prop_4 = data[22] 
            value_Prop_4 = data[23]
            own_Prop_5 = data[24] 
            value_Prop_5 = data[25]
            own_Prop_6 = data[26]
            value_Prop_6 = data[27]
            own_Prop_7 = data[28]
            value_Prop_7 = data[29] 
        if variant == "industrial":
            own_Prop_1 = data[30]
            value_Prop_1 = data[31]
            own_Prop_2 = data[32]
            value_Prop_2 = data[33]
            own_Prop_3 = data[34] 
            value_Prop_3 = data[35]
            own_Prop_4 = data[36] 
            value_Prop_4 = data[37]
            own_Prop_5 = data[38] 
            value_Prop_5 = data[39]
            own_Prop_6 = data[40]
            value_Prop_6 = data[41]
            own_Prop_7 = data[42]
            value_Prop_7 = data[43] 

        if own_Prop_1 == "y":
            own_Prop_1 = "Yes"
        elif own_Prop_1 == "n":
            own_Prop_1 = "No"
        
        if own_Prop_2 == "y":
            own_Prop_2 = "Yes"
        elif own_Prop_2 == "n":
            own_Prop_2 = "No"
        
        if own_Prop_3 == "y":
            own_Prop_3 = "Yes"
        elif own_Prop_3 == "n":
            own_Prop_3 = "No"
        
        if own_Prop_4 == "y":
            own_Prop_4 = "Yes"
        elif own_Prop_4 == "n":
            own_Prop_4 = "No"
        
        if own_Prop_5 == "y":
            own_Prop_5 = "Yes"
        elif own_Prop_5 == "n":
            own_Prop_5 = "No"
        
        if own_Prop_6 == "y":
            own_Prop_6 = "Yes"
        elif own_Prop_6 == "n":
            own_Prop_6 = "No"

        if own_Prop_7 == "y":
            own_Prop_7 = "Yes"
        elif own_Prop_7 == "n":
            own_Prop_7 = "No"
        #This is the table that shows up
        a_list = [(1,"£"+str(round((int(value_Prop_1) *0.008))),"£"+value_Prop_1,'', own_Prop_1 ),
       (2,"£"+str(round((int(value_Prop_2) *0.008))),"£"+value_Prop_2 ,'', own_Prop_2),
       (3,"£"+str(round((int(value_Prop_3) *0.008))),"£"+value_Prop_3,'', own_Prop_3),
       (4,"£"+str(round((int(value_Prop_4) *0.008))),"£"+value_Prop_4,'', own_Prop_4),
       (5,"£"+str(round((int(value_Prop_5) *0.008))) ,"£"+value_Prop_5,'', own_Prop_5),
        (6,"£"+str(round((int(value_Prop_6) *0.008))),"£"+value_Prop_6,'', own_Prop_6),
        (7,"£"+str(round((int(value_Prop_7) *0.008))),"£"+value_Prop_7,'', own_Prop_7)]

        total_rows = len(a_list)
        total_columns = len(a_list[0])

        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(self.Industrial_info_label, width=15, disabledbackground = self.livid , disabledforeground = self.white, fg = self.white,  font=('Arial',16,'bold'))
                self.e.grid(row=i, column=j)
                self.e.insert(END, a_list[i][j])
                self.e.configure(state='disabled', justify='center')#disabled the entry box to stop user from typing - using an entry box to display info

    def convert(self, list):
        return tuple(list)
    
    # def save (self, oldData, data):
    #     #print("saved")
    #     counter = 0
    #     new_data = ''
    #     # makes the data a string from a list
    #     for index in range(len(data)):
    #         counter = counter + 1
    #         text = data[index]
    #         if counter < 66:
    #             new_data = str(new_data) + str(text) +","  
    #     #new_data is data but a string version
    #     #print("NEW_DATA:"+ "\n" + new_data)
    #     #print("OLD_DATA:"+ "\n" + oldData)
    #     with open("game_data.txt", 'r') as f:
    #         a_list = f.readline()
    #     text = a_list.replace(oldData, new_data)
    #     os.remove('game_data.txt')
    #     with open("game_data.txt", 'a') as f:
    #         #print("TEXT: " +"\n" +text)        
    #         f.write(text)
    #     #print(text)
    #     return new_data

    def save (self, username, data):
        try:
            # read the contents of the game data file
            with open("game_data.txt", "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            print("Error: game data file not found.")
            return
        
        # print the current file content (for review)
        print("Current file content:\n", file_content)

        print("current data variable", data)

        # find and replace old data 

    def call_actions(self,variant, header, title, data, oldData):
        self.Close()
        actionsR = Game(header,title) #This is the title that appears right at the top that is the name of the program
        Game.actions(actionsR, variant, data, oldData)

    def main_next_month(self, oldData, data):
        data = self.next_month(data) # calls next month and stores the return as 'data'
        print("main next month OLDdata: \n", oldData)
        print("main next month data: \n", data)
        oldData = self.save(oldData ,data) # saves the new data
        self.Close()
        game_page = Game("Buying and Selling Properties Game - Game ","GAME PAGE")
        Game.game_function(game_page,data[0]) # opens the game page

    def next_month(self,data):
        #data = data.split(",")
        #print("next_month data" , data)
        new_money = 0
        #THIS SECTION CHECKS IF THE PROPERTY IS ON RENT AND ADDS THE RENT MONEY TO USERS MONEY IF IT IS
        #residential:
        if data[2] == 'y'and data[44] =='y': # if they own the prop and its on rent, give them the rent money
            new_money = round((int(data[3]) * 0.08)) + int(new_money)

        if data[4] == 'y'and data[45] =='y':
            new_money = round((int(data[5]) * 0.08)) + int(new_money)

        if data[6] == 'y' and data[46] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[8] == 'y' and data[47] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[10] == 'y' and data[48] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)

        if data[12] == 'y' and data[49] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[14] == 'y' and data[50] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        #commercial:
        if data[16] == 'y' and data[51] =='y':
            new_money = round((int(data[3]) * 0.08)) + int(new_money)

        if data[18] == 'y' and data[52] =='y':
            new_money = round((int(data[5]) * 0.08)) + int(new_money)

        if data[20] == 'y' and data[53] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[22] == 'y' and data[54] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[24] == 'y' and data[55] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)

        if data[26] == 'y' and data[56] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[28] == 'y' and data[57] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        #industrial:
        if data[30] == 'y' and data[58] =='y':
            new_money = round((int(data[3]) * 0.08)) + int(new_money)

        if data[32] == 'y' and data[59] =='y':
            new_money = round((int(data[5]) * 0.08)) + int(new_money)

        if data[34] == 'y' and data[60] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[36] == 'y' and data[61] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[38] == 'y' and data[62] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)

        if data[40] == 'y' and data[63] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        
        if data[42] == 'y' and data[64] =='y':
            new_money = round((int(data[7]) * 0.08)) + int(new_money)
        #END OF SECTION

        #THIS SECTION CHANGES THE PRICES OF THE HOUSES DEPENDING IF THE 'HOUSING MARKET' GOES UP OR DOWN
        market_Change = random.randint(0,8) # gets random integer between 0 and 8 inc.
        market_Change = market_Change * 0.01 
        market_Change = 0.99 + market_Change
        round(market_Change,2)
        houses = [] # declare a list to append to
        for house in range(3,44,2): # this adds the place where the house prices are in the 'data' string
            houses.append(house)
        for integer in range(len(houses)):    
            data[houses[integer]] = float(data[houses[integer]]) * float(market_Change)
            data[houses[integer]] = int(data[houses[integer]])
            data[houses[integer]] = str(data[houses[integer]])
        #END OF SECTION
            
        data [ 1 ] = int(data[1]) + int(new_money)
        #print("new money data[1]:::",data[1])
        return data
        
    def rent(self, data, variant, Prop_Number):
        #Finds the relevant pieces of data
        if variant == "residential":
            if Prop_Number == "1":
                own_Prop = data[2]
            elif Prop_Number == "2":
                own_Prop = data[4]
            elif Prop_Number == "3":
                own_Prop = data[6]
            elif Prop_Number == "4":
                own_Prop = data[8]
            elif Prop_Number == "5":
                own_Prop = data[10]
            elif Prop_Number == "6":
                own_Prop = data[12]
            elif Prop_Number == "7":
                own_Prop = data[14]   
        if variant == "commercial":
            if Prop_Number == "1":
                own_Prop = data[16]
            elif Prop_Number == "2":
                own_Prop = data[18]
            elif Prop_Number == "3":
                own_Prop = data[20] 
            elif Prop_Number == "4":
                own_Prop = data[22] 
            elif Prop_Number == "5":
                own_Prop = data[24] 
            elif Prop_Number == "6":
                own_Prop = data[26]
            elif Prop_Number == "7":
                own_Prop = data[28]
        if variant == "industrial":
            if Prop_Number == "1":
                own_Prop = data[30]
            elif Prop_Number == "2":
                own_Prop = data[32]
            elif Prop_Number == "3":
                own_Prop = data[34] 
            elif Prop_Number == "4":
                own_Prop = data[36] 
            elif Prop_Number == "5":
                own_Prop = data[38] 
            elif Prop_Number == "6":
                own_Prop = data[40]
            elif Prop_Number == "7":
                own_Prop = data[42] 

        if own_Prop == 'y' or own_Prop == "Yes": # if you own the property
            # changes relvant piece of data so the property is stored as on rent
            if variant == "residential":
                if Prop_Number == "1":
                    data[44] = "y"          
                elif Prop_Number == "2":
                    data[45] = "y"                        
                elif Prop_Number == "3":
                    data[46] = "y"                        
                elif Prop_Number == "4":
                    data[47] = "y"                        
                elif Prop_Number == "5":
                    data[48] = "y"                        
                elif Prop_Number == "6":
                    data[49] = "y"                        
                elif Prop_Number == "7":
                    data[50] = "y"                           
            if variant == "commercial":
                if Prop_Number == "1":
                    data[51] = "y"                        
                elif Prop_Number == "2":
                    data[52] = "y"                        
                elif Prop_Number == "3":
                    data[53] = "y"                       
                elif Prop_Number == "4":
                    data[54] = "y"                         
                elif Prop_Number == "5":
                    data[55] = "y"                         
                elif Prop_Number == "6":
                    data[56] = "y"                      
                elif Prop_Number == "7":
                    data[57] = "y"                        
            if variant == "industrial":
                if Prop_Number == "1":
                    data[58] = "y"
                elif Prop_Number == "2":
                    data[59]  = "y"
                elif Prop_Number == "3":
                    data[60]  = "y"
                elif Prop_Number == "4":
                    data[61]  = "y"
                elif Prop_Number == "5":
                    data[62]  = "y"
                elif Prop_Number == "6":
                    data[63] = "y"
                elif Prop_Number == "7":
                    data[64] = "y"
            message=Label(self.window, text = "Property successfully rented!", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') #places message
            return data
        elif own_Prop == "n":
            message=Label(self.window, text = "You do not own this property.", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
            return data

    def main_rent(self, data,variant, Prop_Number, oldData):
        data = self.rent(data,variant,Prop_Number) # rents prop and stores the new data with the prop rented 
        oldData = self.save(oldData ,data) # saves the new data, func updates oldData with the new data
        #next line refreshes the page so it shows 'buy' now that the user owns prop and updates money on screen
        self.call_actions(variant,"Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData) 
    
    def evict(self, data, variant, Prop_Number):
        #Finds the relevant pieces of data
        if variant == "residential":
            if Prop_Number == "1":
                own_Prop = data[2]
            elif Prop_Number == "2":
                own_Prop = data[4]
            elif Prop_Number == "3":
                own_Prop = data[6]
            elif Prop_Number == "4":
                own_Prop = data[8]
            elif Prop_Number == "5":
                own_Prop = data[10]
            elif Prop_Number == "6":
                own_Prop = data[12]
            elif Prop_Number == "7":
                own_Prop = data[14]   
        if variant == "commercial":
            if Prop_Number == "1":
                own_Prop = data[16]
            elif Prop_Number == "2":
                own_Prop = data[18]
            elif Prop_Number == "3":
                own_Prop = data[20] 
            elif Prop_Number == "4":
                own_Prop = data[22] 
            elif Prop_Number == "5":
                own_Prop = data[24] 
            elif Prop_Number == "6":
                own_Prop = data[26]
            elif Prop_Number == "7":
                own_Prop = data[28]
        if variant == "industrial":
            if Prop_Number == "1":
                own_Prop = data[30]
            elif Prop_Number == "2":
                own_Prop = data[32]
            elif Prop_Number == "3":
                own_Prop = data[34] 
            elif Prop_Number == "4":
                own_Prop = data[36] 
            elif Prop_Number == "5":
                own_Prop = data[38] 
            elif Prop_Number == "6":
                own_Prop = data[40]
            elif Prop_Number == "7":
                own_Prop = data[42] 

        if own_Prop == 'y' or own_Prop == "Yes": # if you own the property
            # changes relvant piece of data so the property is stored as on rent
            if variant == "residential":
                if Prop_Number == "1":
                    data[44] = "n"          
                elif Prop_Number == "2":
                    data[45] = "n"                        
                elif Prop_Number == "3":
                    data[46] = "n"                        
                elif Prop_Number == "4":
                    data[47] = "n"                       
                elif Prop_Number == "5":
                    data[48] = "n"                       
                elif Prop_Number == "6":
                    data[49] = "n"                        
                elif Prop_Number == "7":
                    data[50] = "n"                          
            if variant == "commercial":
                if Prop_Number == "1":
                    data[51] = "n"                       
                elif Prop_Number == "2":
                    data[52] = "n"                       
                elif Prop_Number == "3":
                    data[53] = "n"                      
                elif Prop_Number == "4":
                    data[54] = "n"                       
                elif Prop_Number == "5":
                    data[55] = "n"                       
                elif Prop_Number == "6":
                    data[56] = "n"                     
                elif Prop_Number == "7":
                    data[57] = "n"                        
            if variant == "industrial":
                if Prop_Number == "1":
                    data[58] = "n"
                elif Prop_Number == "2":
                    data[59]  = "n"
                elif Prop_Number == "3":
                    data[60]  = "n"
                elif Prop_Number == "4":
                    data[61]  = "n"
                elif Prop_Number == "5":
                    data[62]  = "n"
                elif Prop_Number == "6":
                    data[63] = "n"
                elif Prop_Number == "7":
                    data[64] = "n"
            message=Label(self.window, text = "Property successfully rented!", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') #places message
            return data
        elif own_Prop == "n":
            message=Label(self.window, text = "You do not own this property.", font=("Georgia", 22,),fg = self.white, background = self.gray,padx='11',pady='5')#displays message to user.
            message.place(relx = 0.5, rely = 0.9, anchor ='center') # places message
            return data
    
    def main_evict(self, data,variant, Prop_Number, oldData):
        data = self.evict(data,variant,Prop_Number) # evicts the tenant from prop and stores the new data with the prop empty 
        oldData = self.save(oldData ,data) # saves the new data, func updates oldData with the new data
        #next line refreshes the page so it shows 'rent' 
        self.call_actions(variant,"Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData) 

    def actions(self, variant, data, oldData):
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
        self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command=lambda:[self.back_on_click_game(data[0])], background = self.blue, fg = self.white, padx='5', pady = '15')
        self.back_button.place ( x=40, y = 30)

        #data[1] is the liquid money a user has aka capital
        self.capital_label = Label(self.window,relief='raised',text = ("Money:","£", data[1]), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.capital_label.place(relx = 0.53, rely = 0.20,anchor ='center')# label that displays the money a user has

        if variant == "residential":
            own_Prop_1 = data[2]
            rentR_1 = data[44]
            value_Prop_1 = data[3]

            own_Prop_2 = data[4]
            rentR_2 = data[45]
            value_Prop_2 = data[5]

            own_Prop_3 = data[6]
            rentR_3 = data[46]
            value_Prop_3 = data[7] 

            own_Prop_4 = data[8]
            rentR_4 = data[47]
            value_Prop_4 = data[9] 

            own_Prop_5 = data[10]
            rentR_5 = data[48]
            value_Prop_5 = data[11] 

            own_Prop_6 = data[12]
            rentR_6 = data[49]
            value_Prop_6 = data[13]

            own_Prop_7 = data[14]
            rentR_7 = data[50]
            value_Prop_7 = data[15]
        if variant == "commercial":
            own_Prop_1 = data[16]
            rentR_1 = data[51]
            value_Prop_1 = data[17]

            own_Prop_2 = data[18]
            rentR_2 = data[52]
            value_Prop_2 = data[19]

            own_Prop_3 = data[20] 
            rentR_3 = data[53]
            value_Prop_3 = data[21]

            own_Prop_4 = data[22] 
            rentR_4 = data[54]
            value_Prop_4 = data[23]

            own_Prop_5 = data[24] 
            rentR_5 = data[55]
            value_Prop_5 = data[25]

            own_Prop_6 = data[26]
            rentR_6 = data[56]
            value_Prop_6 = data[27]

            own_Prop_7 = data[28]
            rentR_7 = data[57]
            value_Prop_7 = data[29] 
        if variant == "industrial":
            own_Prop_1 = data[30]
            rentR_1 = data[58]
            value_Prop_1 = data[31]

            own_Prop_2 = data[32]
            rentR_2 = data[59]
            value_Prop_2 = data[33]

            own_Prop_3 = data[34] 
            rentR_3 = data[60]
            value_Prop_3 = data[35]

            own_Prop_4 = data[36] 
            rentR_4 = data[61]
            value_Prop_4 = data[37]

            own_Prop_5 = data[38] 
            rentR_5 = data[62]
            value_Prop_5 = data[39]

            own_Prop_6 = data[40]
            rentR_6 = data[63]
            value_Prop_6 = data[41]

            own_Prop_7 = data[42]
            rentR_7 = data[64]
            value_Prop_7 = data[43] 
        #Buy/Sell Buttons:
        if own_Prop_1 == 'n': # if user doesnt own prop 1 display buy button
            Buy1_button = Button(self.window, relief = 'flat' ,width = 25, text = "BUY", command=lambda:[self.main_buy(data,variant,"1", oldData)], font = ("Calibri", (10), 'bold'),fg = self.white, background = self.lime_green )
            Buy1_button.place(relx = 0.575, rely = 0.525,anchor ='center')
        elif own_Prop_1 == 'y': # if user owns prop 1 display sell button
            SellOne_button = Button(self.window, relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"1", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
            SellOne_button.place(relx = 0.575, rely = 0.525,anchor ='center')
        
        if own_Prop_2 == 'n':
            Buy2_button = Button(self.window, relief = 'flat' ,width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"2", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
            Buy2_button.place(relx = 0.575, rely = 0.57,anchor ='center')
           
        elif own_Prop_2 == 'y':
            Sell2_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"2", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
            Sell2_button.place(relx = 0.575, rely = 0.57,anchor ='center')

        if own_Prop_3 == 'n':
            Buy3_button = Button(self.window, relief = 'flat' , width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"3", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
            Buy3_button.place(relx = 0.575, rely = 0.615,anchor ='center')
           
        elif own_Prop_3 == 'y':
            Sell3_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"3", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
            Sell3_button.place(relx = 0.575, rely = 0.615,anchor ='center')

        if own_Prop_4 == 'n':
            Buy4_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"4", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
            Buy4_button.place(relx = 0.575, rely = 0.66,anchor ='center')
           
        elif own_Prop_4 == 'y':
            Sell4_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"4", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
            Sell4_button.place(relx = 0.575, rely = 0.66,anchor ='center')

        if own_Prop_5 == 'n':
            Buy5_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"5", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
            Buy5_button.place(relx = 0.575, rely = 0.705,anchor ='center')
           
        elif own_Prop_5 == 'y':            
            Sell5_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"5", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
            Sell5_button.place(relx = 0.575, rely = 0.705,anchor ='center')
            
        
        if own_Prop_6 == 'n':
            Buy6_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"6", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
            Buy6_button.place(relx = 0.575, rely = 0.75,anchor ='center')
           
        elif own_Prop_6 == 'y':
            Sell6_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"6", oldData)],font = ("Calibri", 10, 'bold'), fg = self.white, background = self.red)
            Sell6_button.place(relx = 0.575, rely = 0.75,anchor ='center')

        if own_Prop_7 == 'n':
            Buy7_button = Button(self.window, relief = 'flat' ,  width = 25, text = "BUY", command=lambda:[self.main_buy(data, variant,"7", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.lime_green)
            Buy7_button.place(relx = 0.575, rely = 0.795,anchor ='center')
           
        elif own_Prop_7 == 'y':
            Sell7_button = Button(self.window,relief = 'flat' , width = 25, text = "SELL", command=lambda:[self.main_sell(data, variant,"7", oldData)], font = ("Calibri", 10, 'bold'),fg = self.white, background = self.red)
            Sell7_button.place(relx = 0.575, rely = 0.795,anchor ='center')
        #0.73 is the mid column between invest and buy/sell
        
        #Rent buttons
        if rentR_1 == 'n': # if user isnt renting prop 1
            Rent1_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"1", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent1_button.place(relx = 0.73, rely = 0.525,anchor ='center')
        elif rentR_1 == 'y': #if user is renting prop 1
            Rent1_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"1", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
            Rent1_button.place(relx = 0.73, rely = 0.525,anchor ='center')
        
        if rentR_2 == 'n':
            Rent2_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"2", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent2_button.place(relx = 0.73, rely = 0.57,anchor ='center')
        if rentR_2 == 'y':
            Rent2_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"2", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
            Rent2_button.place(relx = 0.73, rely = 0.57,anchor ='center')

        if rentR_3 == 'n':
            Rent3_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"3", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent3_button.place(relx = 0.73, rely = 0.615,anchor ='center')
        elif rentR_3 == 'y':
            Rent3_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"3", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
            Rent3_button.place(relx = 0.73, rely = 0.615,anchor ='center')

        if rentR_4 == 'n':
            Rent4_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"4", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent4_button.place(relx = 0.73, rely = 0.66,anchor ='center')
        elif rentR_4 == 'y':
            Rent4_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"4", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
            Rent4_button.place(relx = 0.73, rely = 0.66,anchor ='center')

        if rentR_5 == 'n':
            Rent5_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"5", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent5_button.place(relx = 0.73, rely = 0.705,anchor ='center')
        elif rentR_5 == 'y':
            Rent5_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"5", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
            Rent5_button.place(relx = 0.73, rely = 0.705,anchor ='center')

        if rentR_6 == 'n':
            Rent6_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"6", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent6_button.place(relx = 0.73, rely = 0.75,anchor ='center')
        elif rentR_6 == 'y':
            Rent6_button = Button(self.window,relief = 'flat' , width = 25, text = "EVICT", command=lambda:[self.main_evict(data, variant,"6", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.magenta)
            Rent6_button.place(relx = 0.73, rely = 0.75,anchor ='center')

        if rentR_7 == 'n':
            Rent7_button = Button(self.window,relief = 'flat' , width = 25, text = "RENT", command=lambda:[self.main_rent(data, variant,"7", oldData)],font = ("Calibri", 10, 'bold'),fg = self.white, background = self.light_blue)
            Rent7_button.place(relx = 0.73, rely = 0.795,anchor ='center')
        elif rentR_7 == 'y':
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

        if own_Prop_1 == "y":
            own_Prop_1 = "Yes"
        elif own_Prop_1 == "n":
            own_Prop_1 = "No"
        
        if own_Prop_2 == "y":
            own_Prop_2 = "Yes"
        elif own_Prop_2 == "n":
            own_Prop_2 = "No"
        
        if own_Prop_3 == "y":
            own_Prop_3 = "Yes"
        elif own_Prop_3 == "n":
            own_Prop_3 = "No"
        
        if own_Prop_4 == "y":
            own_Prop_4 = "Yes"
        elif own_Prop_4 == "n":
            own_Prop_4 = "No"
        
        if own_Prop_5 == "y":
            own_Prop_5 = "Yes"
        elif own_Prop_5 == "n":
            own_Prop_5 = "No"
        
        if own_Prop_6 == "y":
            own_Prop_6 = "Yes"
        elif own_Prop_6 == "n":
            own_Prop_6 = "No"

        if own_Prop_7 == "y":
            own_Prop_7 = "Yes"
        elif own_Prop_7 == "n":
            own_Prop_7 = "No"

        a_list = [(1,"£"+value_Prop_1, own_Prop_1, ' ', " ", " " ),
       (2,"£"+value_Prop_2 , own_Prop_2, " ", " ", " "),
       (3,"£"+value_Prop_3, own_Prop_3, " ", " ", " "),
       (4,"£"+value_Prop_4, own_Prop_4, " ", " ", " "),
       (5,"£"+value_Prop_5, own_Prop_5, " ", " ", " "),
        (6,"£"+value_Prop_6, own_Prop_6, " ", " ", " "),
        (7,"£"+value_Prop_7, own_Prop_7, " ", " ", " ")]

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

    def game_function(self,data):
        #username, data[1], own r prop 1, value of r prop 1, own r prop 2, value of r prop 2, own r prop 3, value of r prop 3, own r prop 3, value of r prop 3, and so on until prop7
        # print("game_function data", data)
        # data here is = to the username
        data, oldData = self.data(data) # data will be all the data stored in the text file for the username used to login.
        r_total = 0
        owned_counter =0
        rent_rProp_1 = 0
        rent_rProp_2 = 0
        rent_rProp_3 = 0
        rent_rProp_4 = 0
        rent_rProp_5 = 0
        rent_rProp_6 = 0
        rent_rProp_7 = 0
        rent_rProp = 0
        if data[2] == 'y':
            r_total = r_total + int(data[3])
            rent_rProp_1 = round((int(data[3]) *0.008))
            owned_counter = owned_counter + 1
        if data[4] == 'y':
            r_total = r_total + int(data[5])
            rent_rProp_2 = round((int(data[5]) *0.008))
            owned_counter = owned_counter + 1
        if data[6] == 'y':
            r_total = r_total + int(data[7])
            rent_rProp_3 = round((int(data[7]) *0.008))
            owned_counter = owned_counter + 1
        if data[8] == 'y':
            r_total = r_total + int(data[9])
            rent_rProp_4 = round((int(data[9]) *0.008))
            owned_counter = owned_counter + 1
        if data[10] == 'y':
            r_total = r_total + int(data[11])
            rent_rProp_5 = round((int(data[11]) *0.008))
            owned_counter = owned_counter + 1
        if data[12] == 'y':
            r_total = r_total + int(data[13])
            rent_rProp_6 = round((int(data[13]) *0.008))
            owned_counter = owned_counter + 1
        if data[14] == 'y':
            r_total = r_total + int(data[15])
            rent_rProp_7 = round((int(data[15]) *0.008))
            owned_counter = owned_counter + 1

        c_total = 0
        owned_counter_c =0
        rent_cProp_1 = 0
        rent_cProp_2 = 0
        rent_cProp_3 = 0
        rent_cProp_4 = 0
        rent_cProp_5 = 0
        rent_cProp_6 = 0
        rent_cProp_7 = 0
        rent_cProp = 0
        if data[16] == 'y':
            c_total = c_total + int(data[17])
            rent_cProp_1 = round((int(data[17]) *0.008))
            owned_counter_c = owned_counter_c + 1
        if data[18] == 'y':
            c_total = c_total + int(data[19])
            rent_rProp_2 = round((int(data[19]) *0.008))
            owned_counter_c = owned_counter_c + 1
        if data[20] == 'y':
            c_total = c_total + int(data[21])
            rent_rProp_3 = round((int(data[21]) *0.008))
            owned_counter_c = owned_counter_c + 1
        if data[22] == 'y':
            c_total = c_total + int(data[23])
            rent_rProp_4 = round((int(data[9]) *0.008))
            owned_counter_c = owned_counter_c + 1
        if data[24] == 'y':
            c_total = c_total + int(data[25])
            rent_cProp_5 = round((int(data[11]) *0.008))
            owned_counter_c = owned_counter_c + 1
        if data[26] == 'y':
            c_total = c_total + int(data[27])
            rent_cProp_6 = round((int(data[27]) *0.008))
            owned_counter_c = owned_counter_c + 1
        if data[28] == 'y':
            c_total = c_total + int(data[29])
            rent_cProp_7 = round((int(data[29]) *0.008))
            owned_counter_c = owned_counter_c + 1

        i_total = 0
        owned_counter_i =0
        rent_iProp_1 = 0
        rent_iProp_2 = 0
        rent_iProp_3 = 0
        rent_iProp_4 = 0
        rent_iProp_5 = 0
        rent_iProp_6 = 0
        rent_iProp_7 = 0
        rent_iProp = 0
        if data[30] == 'y':
            i_total = i_total + int(data[31])
            rent_iProp_1 = round((int(data[31]) *0.008))
            owned_counter_i = owned_counter_i + 1
        if data[32] == 'y':
            i_total = i_total + int(data[33])
            rent_rProp_2 = round((int(data[33]) *0.008))
            owned_counter_i = owned_counter_i + 1
        if data[34] == 'y':
            i_total = i_total + int(data[35])
            rent_rProp_3 = round((int(data[35]) *0.008))
            owned_counter_i = owned_counter_i + 1
        if data[36] == 'y':
            i_total = i_total + int(data[37])
            rent_rProp_4 = round((int(data[9]) *0.008))
            owned_counter_i = owned_counter_i + 1
        if data[38] == 'y':
            i_total = i_total + int(data[39])
            rent_iProp_5 = round((int(data[11]) *0.008))
            owned_counter_i = owned_counter_i + 1
        if data[40] == 'y':
            i_total = i_total + int(data[41])
            rent_iProp_6 = round((int(data[41]) *0.008))
            owned_counter_i = owned_counter_i + 1
        if data[42] == 'y':
            i_total = i_total + int(data[43])
            rent_iProp_7 = round((int(data[43]) *0.008))
            owned_counter_i = owned_counter_i + 1

        rent_rProp = rent_rProp_1 + rent_rProp_2 + rent_rProp_3 + rent_rProp_4 + rent_rProp_5 + rent_rProp_6 + rent_rProp_7
        rent_cProp = rent_cProp_1 + rent_cProp_2 + rent_cProp_3 + rent_cProp_4 + rent_cProp_5 + rent_cProp_6 + rent_cProp_7
        rent_iProp = rent_iProp_1 + rent_iProp_2 + rent_iProp_3 + rent_iProp_4 + rent_iProp_5 + rent_iProp_6 + rent_iProp_7
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

        self.capital_label = Label(self.window,relief='raised',text = ("Money:","£", data[1]), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.capital_label.place(relx = 0.53, rely = 0.20,anchor ='center')# label that displays data[1] they have

        #Residential Labels:
        self.r_prop_label = Label(self.window,relief='raised',text = ("Props Owned:"+str(owned_counter)+"/7"), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.r_prop_label.place(relx = 0.23, rely = 0.44,anchor ='center')# label that contains info about how many props are owned 

        self.r_propV_label = Label(self.window,relief='raised',text = ("Props Value:\n"+" £"+str(r_total)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.r_propV_label.place(relx = 0.23, rely = 0.55,anchor ='center')# label that contains info about props value

        self.r_propR_label = Label(self.window,relief='raised',text = ("Props Rent:\n"+" £"+str(rent_rProp)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.r_propR_label.place(relx = 0.23, rely = 0.69,anchor ='center')# label that contains info about props value

        #Commercial Labels:
        self.c_prop_label = Label(self.window,relief='raised',text = ("Props Owned:"+str(owned_counter_c)+"/7"), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.c_prop_label.place(relx = 0.51, rely = 0.44,anchor ='center')# label that contains info about how many props are owned 

        self.c_propV_label = Label(self.window,relief='raised',text = ("Props Value:\n"+" £"+str(c_total)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.c_propV_label.place(relx = 0.51, rely = 0.55,anchor ='center')# label that contains info about props value

        self.c_propR_label = Label(self.window,relief='raised',text = ("Props Rent:\n"+" £"+str(rent_cProp)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.c_propR_label.place(relx = 0.51, rely = 0.69,anchor ='center')# label that contains info about props value

        #Industrial Labels:
        self.i_prop_label = Label(self.window,relief='raised',text = ("Props Owned:"+str(owned_counter_i)+"/7"), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.i_prop_label.place(relx = 0.78, rely = 0.44,anchor ='center')# label that contains info about how many props are owned 

        self.i_propV_label = Label(self.window,relief='raised',text = ("Props Value:\n"+" £"+str(i_total)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.i_propV_label.place(relx = 0.78, rely = 0.55,anchor ='center')# label that contains info about props value

        self.i_propR_label = Label(self.window,relief='raised',text = ("Props Rent:\n"+" £"+str(rent_iProp)), font=("Times New Roman", 22,),fg = self.white, background = self.teal ,padx='25',pady = '5')
        self.i_propR_label.place(relx = 0.78, rely = 0.69,anchor ='center')# label that contains info about props value

        #Buttons:
        save_button = Button(self.window, width = 8, text = "SAVE",command= lambda: self.save(oldData, data), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        save_button.place(relx = 0.945, rely = 0.938,anchor ='center')

        next_turn_button = Button(self.window, width = 8, text = ("NEXT"+"\n"+"MONTH"), command=  lambda: self.main_next_month(oldData, data), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        next_turn_button.place(relx = 0.945, rely = 0.83,anchor ='center')

        ViewMore_Residential_button = Button(self.window, width = 15, text = "VIEW MORE INFO",command= lambda: self.call_view_more_info("residential","Buying and Selling Properties Game - Residential info", "Information",data),
                                                 font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        ViewMore_Residential_button.place(relx = 0.23, rely = 0.8,anchor ='center')

        ViewMore_Commercial_button = Button(self.window, width = 15, text = "VIEW MORE INFO",command= lambda: self.call_view_more_info("commercial","Buying and Selling Properties Game - Commercial info", "Information",data),
                                                 font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        ViewMore_Commercial_button.place(relx = 0.51, rely = 0.8,anchor ='center')

        ViewMore_Industrial_button = Button(self.window, width = 15, text = "VIEW MORE INFO",command= lambda: self.call_view_more_info("industrial","Buying and Selling Properties Game - Industrial info", "Information",data),
                                                 font = ("Calibri", 18, 'bold'),fg = self.white, background = self.turquoise)
        ViewMore_Industrial_button.place(relx = 0.78, rely = 0.8,anchor ='center')

        Actions_Residential_button = Button(self.window, width = 15, text = "ACTIONS", command= lambda: self.call_actions("residential","Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData)  , font = ("Calibri", 18, 'bold'),fg = self.white, background = self.lime_green)
        Actions_Residential_button.place(relx = 0.23, rely = 0.91,anchor ='center')
        
        Actions_Commercial_button = Button(self.window, width = 15, text = "ACTIONS", command= lambda: self.call_actions("commercial","Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.lime_green)
        Actions_Commercial_button.place(relx = 0.51, rely = 0.91,anchor ='center')

        Actions_Industrial_button = Button(self.window, width = 15, text = "ACTIONS", command= lambda: self.call_actions("industrial","Buying and Selling Properties Game - Residential Actions", "Actions",data,oldData), font = ("Calibri", 18, 'bold'),fg = self.white, background = self.lime_green)
        Actions_Industrial_button.place(relx = 0.78, rely = 0.91,anchor ='center')

        self.back_button = Button(self.window,relief='raised', text = "BACK", font=("Calibri", 28,'bold'), command= lambda: self.back_on_click(data[0]), background = self.blue, fg = self.white, padx='25', pady = '5')
        self.back_button.place ( x=40, y = 30)

        self.window.mainloop()