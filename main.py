# Here we can quarterback all the operations

from login import *
import os
#from register import *
def central():
        check_database()
        #Loads the login page.
        Login_page = Login("Buying and Selling Properties Game - Login ","LOGIN PAGE") #This is the title that appears right at the top that is the name of the program
        Login.login_function(Login_page)


def check_database():
        # Get the absolute path of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Define the database file path in the same directory as the script
        db_path = os.path.join(script_dir, 'game.db')
        if os.path.exists(db_path):
        #      print("Database file 'game.db' exists.")
             pass
        else:
            from window_template import database_create
            database_create()
            



central()