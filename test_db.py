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
                                    ValueResi1 REAL,
                                    OwnResi2 BOOLEAN,
                                    ValueResi2 REAL,
                                    OwnResi3 BOOLEAN,
                                    ValueResi3 REAL,
                                    OwnResi4 BOOLEAN,
                                    ValueResi4 REAL,
                                    OwnResi5 BOOLEAN,
                                    ValueResi5 REAL,
                                    OwnResi6 BOOLEAN,
                                    ValueResi6 REAL,
                                    OwnResi7 BOOLEAN,
                                    ValueResi7 REAL,
                                    OwnComm1 BOOLEAN,
                                    ValueComm1 REAL,
                                    OwnComm2 BOOLEAN,
                                    ValueComm2 REAL,
                                    OwnComm3 BOOLEAN,
                                    ValueComm3 REAL,
                                    OwnComm4 BOOLEAN,
                                    ValueComm4 REAL,
                                    OwnComm5 BOOLEAN,
                                    ValueComm5 REAL,
                                    OwnComm6 BOOLEAN,
                                    ValueComm6 REAL,
                                    OwnComm7 BOOLEAN,
                                    ValueComm7 REAL,
                                    OwnIndus1 BOOLEAN,
                                    ValueIndus1 REAL,
                                    OwnIndus2 BOOLEAN,
                                    ValueIndus2 REAL,
                                    OwnIndus3 BOOLEAN,
                                    ValueIndus3 REAL,
                                    OwnIndus4 BOOLEAN,
                                    ValueIndus4 REAL,
                                    OwnIndus5 BOOLEAN,
                                    ValueIndus5 REAL,
                                    OwnIndus6 BOOLEAN,
                                    ValueIndus6 REAL,
                                    OwnIndus7 BOOLEAN,
                                    ValueIndus7 REAL)''')
            
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


