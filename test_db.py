# this file is for testing the creation of the database to make sure all the fields are inputted correctly
# once verified it works it can be integrated into the main application
import sqlite3
import os

def database_create():
        try:
            # Get the absolute path of the current script
            script_dir = os.path.dirname(os.path.abspath(__file__))
            # Define the database file path in the same directory as the script
            db_path = os.path.join(script_dir, 'game.db')

            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()# connects to the database, if it doesn't exist it will create one
            cursor.execute('''CREATE TABLE IF NOT EXISTS Users
                                (UserID INTEGER NOT NULL PRIMARY KEY,
                                Username STRING,
                                Hashed_Password STRING,
                                Email STRING,
                                Money REAL,
                                OwnResi1 BOOLEAN,
                                ValueResi1 REAL)''')
            
            connection.commit()# saves the changes in the database
            connection.close() # closes the connection to the database
            print("Database created and table initialized successfully.")
        except sqlite3.Error as e:
              print(f"An error occurred: {e}")
        
        # For testing purposes.
        # if os.path.exists(db_path):
        #     print("Database file 'game.db' was created successfully.")
        # else:
        #     print("Failed to create the database file 'game.db'.")

#username, data[1], own r prop 1, value of r prop 1, own r prop 2, value of r prop 2, own r prop 3, value of r prop 3, own r prop 3, value of r prop 3, and so on until prop7

database_create()


