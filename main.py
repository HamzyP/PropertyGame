# Here we can quarterback all the operations

from login import *
# from register import *
def central():
    Login_page = Login("Buying and Selling Properties Game - Login ","LOGIN PAGE") #This is the title that appears right at the top that is the name of the program
    Login.login_function(Login_page)

central()