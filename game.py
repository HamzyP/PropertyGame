import os
import random
import sqlite3
from tkinter import *
from window_template import Window

class Game(Window):
    def __init__(self, title, header):
        super().__init__(title, header)
        # Connect to the game database located in the same directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(script_dir, 'game.db')
        self.connection = sqlite3.connect(db_path)
        # Use Row factory to access columns by name
        self.connection.row_factory = sqlite3.Row  
        self.cursor = self.connection.cursor()
        
        # Define some UI color/font variables (adjust as needed)
        self.blue = "#003366"
        self.livid = "#555555"
        self.white = "#FFFFFF"
        self.teal = "#008080"
        self.turquoise = "#40E0D0"
        self.lime_green = "#32CD32"
        self.red = "#FF0000"
        self.magenta = "#FF00FF"
        self.light_blue = "#ADD8E6"
        self.yellow = "#FFFF00"
        self.gray = "#888888"
    
    # -------------
    # Database Helpers
    # -------------
    def get_user_data(self, username):
        query = "SELECT * FROM Users WHERE Username = ?"
        self.cursor.execute(query, (username,))
        user = self.cursor.fetchone()
        if not user:
            print("User not found.")
        return user

    def get_properties(self, variant, user_id):
        table = variant.capitalize() + "Properties"  # e.g. "ResidentialProperties"
        query = f"SELECT * FROM {table} WHERE UserID = ? ORDER BY PropertyID ASC"
        self.cursor.execute(query, (user_id,))
        properties = self.cursor.fetchall()
        return properties

    def get_property_by_number(self, variant, user_id, prop_number):
        properties = self.get_properties(variant, user_id)
        if len(properties) >= prop_number:
            return properties[prop_number - 1]
        return None

    def update_user_money(self, user_id, new_money):
        query = "UPDATE Users SET Money = ? WHERE UserID = ?"
        self.cursor.execute(query, (new_money, user_id))
        self.connection.commit()

    def update_property(self, variant, property_id, own, value, forRent):
        table = variant.capitalize() + "Properties"
        query = f"UPDATE {table} SET Own = ?, Value = ?, forRent = ? WHERE PropertyID = ?"
        self.cursor.execute(query, (own, value, forRent, property_id))
        self.connection.commit()
    
    # -------------
    # Action Methods
    # -------------
    def buy_property(self, variant, prop_number, username):
        user = self.get_user_data(username)
        if not user: 
            return
        user_id = user["UserID"]
        prop = self.get_property_by_number(variant, user_id, int(prop_number))
        if not prop:
            self.display_message("Property not found.")
            return
        if prop["Own"]:
            self.display_message("You already own this property.")
            return

        prop_value = prop["Value"]
        if user["Money"] < prop_value:
            self.display_message("Insufficient funds to buy this property.")
            return
        
        new_money = user["Money"] - prop_value
        try:
            self.cursor.execute("BEGIN TRANSACTION")
            self.cursor.execute("UPDATE Users SET Money = ? WHERE UserID = ?", (new_money, user_id))
            table = variant.capitalize() + "Properties"
            self.cursor.execute(f"UPDATE {table} SET Own = 1 WHERE PropertyID = ?", (prop["PropertyID"],))
            self.connection.commit()
            self.display_message("Property successfully bought!")
        except Exception as e:
            self.connection.rollback()
            self.display_message(f"Error during purchase: {e}")
        
        self.refresh_actions(variant, username)

    def sell_property(self, variant, prop_number, username):
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        prop = self.get_property_by_number(variant, user_id, int(prop_number))
        if not prop:
            self.display_message("Property not found.")
            return
        if not prop["Own"]:
            self.display_message("You do not own this property.")
            return
        
        prop_value = prop["Value"]
        new_money = user["Money"] + prop_value
        try:
            self.cursor.execute("BEGIN TRANSACTION")
            self.cursor.execute("UPDATE Users SET Money = ? WHERE UserID = ?", (new_money, user_id))
            table = variant.capitalize() + "Properties"
            self.cursor.execute(f"UPDATE {table} SET Own = 0 WHERE PropertyID = ?", (prop["PropertyID"],))
            self.connection.commit()
            self.display_message("Property successfully sold!")
        except Exception as e:
            self.connection.rollback()
            self.display_message(f"Error during sale: {e}")
        
        self.refresh_actions(variant, username)

    def invest_property(self, variant, prop_number, username):
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        prop = self.get_property_by_number(variant, user_id, int(prop_number))
        if not prop:
            self.display_message("Property not found.")
            return
        if not prop["Own"]:
            self.display_message("You cannot invest in a property you do not own.")
            return
        
        prop_value = prop["Value"]
        investment_cost = round(prop_value * 0.10)
        if user["Money"] < investment_cost:
            self.display_message("Insufficient funds for investment.")
            return
        
        # Random success factor (for example, between 0.98 and 1.12)
        success_factor = 0.97 + (random.randint(1, 15) * 0.01)
        new_prop_value = round(prop_value * success_factor)
        new_money = user["Money"] - investment_cost
        try:
            self.cursor.execute("BEGIN TRANSACTION")
            self.cursor.execute("UPDATE Users SET Money = ? WHERE UserID = ?", (new_money, user_id))
            table = variant.capitalize() + "Properties"
            self.cursor.execute(f"UPDATE {table} SET Value = ? WHERE PropertyID = ?", (new_prop_value, prop["PropertyID"]))
            self.connection.commit()
            self.display_message(f"Investment successful! New property value: £{new_prop_value}")
        except Exception as e:
            self.connection.rollback()
            self.display_message(f"Error during investment: {e}")
        
        self.refresh_actions(variant, username)

    def rent_property(self, variant, prop_number, username):
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        prop = self.get_property_by_number(variant, user_id, int(prop_number))
        if not prop:
            self.display_message("Property not found.")
            return
        if not prop["Own"]:
            self.display_message("You do not own this property.")
            return
        if prop["forRent"]:
            self.display_message("Property is already rented.")
            return
        
        try:
            table = variant.capitalize() + "Properties"
            self.cursor.execute(f"UPDATE {table} SET forRent = 1 WHERE PropertyID = ?", (prop["PropertyID"],))
            self.connection.commit()
            self.display_message("Property successfully set to rent!")
        except Exception as e:
            self.connection.rollback()
            self.display_message(f"Error during renting: {e}")
        self.refresh_actions(variant, username)

    def evict_property(self, variant, prop_number, username):
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        prop = self.get_property_by_number(variant, user_id, int(prop_number))
        if not prop:
            self.display_message("Property not found.")
            return
        if not prop["forRent"]:
            self.display_message("Property is not rented.")
            return
        
        try:
            table = variant.capitalize() + "Properties"
            self.cursor.execute(f"UPDATE {table} SET forRent = 0 WHERE PropertyID = ?", (prop["PropertyID"],))
            self.connection.commit()
            self.display_message("Tenant evicted successfully!")
        except Exception as e:
            self.connection.rollback()
            self.display_message(f"Error during eviction: {e}")
        self.refresh_actions(variant, username)

    def next_month(self, username):
        # Process rent income and update property values for market changes.
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        total_rent_income = 0
        # Determine a market change factor (for example, between 0.99 and 1.07)
        market_factor = round(0.99 + random.randint(0, 8) * 0.01, 2)
        for variant in ["residential", "commercial", "industrial"]:
            table = variant.capitalize() + "Properties"
            query = f"SELECT * FROM {table} WHERE UserID = ?"
            self.cursor.execute(query, (user_id,))
            properties = self.cursor.fetchall()
            for prop in properties:
                # If the property is owned and is rented, calculate rent income
                if prop["Own"] and prop["forRent"]:
                    rent_income = round(prop["Value"] * 0.008)
                    total_rent_income += rent_income
                # Update the property value based on market change
                new_value = round(prop["Value"] * market_factor)
                update_query = f"UPDATE {table} SET Value = ? WHERE PropertyID = ?"
                self.cursor.execute(update_query, (new_value, prop["PropertyID"]))
        new_money = user["Money"] + total_rent_income
        try:
            self.cursor.execute("BEGIN TRANSACTION")
            self.cursor.execute("UPDATE Users SET Money = ? WHERE UserID = ?", (new_money, user_id))
            self.connection.commit()
            self.display_message(f"Next month processed! Rent income: £{total_rent_income}, Market factor: {market_factor}")
        except Exception as e:
            self.connection.rollback()
            self.display_message(f"Error processing next month: {e}")
        self.refresh_actions("all", username)
    
    # -------------
    # UI Helper Methods
    # -------------
    def display_message(self, msg):
        print(msg)
        # Display message on the UI (simple label in center)
        message = Label(self.window, text=msg, font=("Georgia", 22), fg=self.white, background=self.gray, padx=11, pady=5)
        message.place(relx=0.5, rely=0.9, anchor='center')
        # Remove the message after 2 seconds

        self.window.after(2000, message.destroy)

    def refresh_actions(self, variant, username):
        # Refresh the UI after an action. We close the current window and reopen the game page.
        print(variant)
        # self.Close()
        # new_game = Game("Buying and Selling Properties Game - Game", "GAME PAGE")
        # new_game.game_function(username)
        self.actions(variant,username)
    
    def manual_save(self, username):
        # Manual save button (though changes are auto-committed)
        self.connection.commit()
        self.display_message("Game saved successfully!")
    
    # -------------
    # UI Pages: Main Game, Actions, and Info
    # -------------
    def game_function(self, username):
        user = self.get_user_data(username)
        if not user:
            print("User data not found.")
            return
        user_id = user["UserID"]

        # Create background
        self.background_label = Label(self.window, relief='raised', font=("Georgia", 22), fg=self.white, background=self.blue, padx=470, pady=220)
        self.background_label.place(relx=0.5, rely=0.6, anchor='center')
        
        # Display user money
        self.capital_label = Label(self.window, relief='raised', text=f"Money: £{user['Money']}", font=("Times New Roman", 22), fg=self.white, background=self.teal, padx=25, pady=5)
        self.capital_label.place(relx=0.53, rely=0.20, anchor='center')
        
        # For each property type, show stats and add buttons for more info and actions.
        variants = [("Residential", "residential"), ("Commercial", "commercial"), ("Industrial", "industrial")]
        x_positions = [0.23, 0.51, 0.78]
        for idx, (dispName, variant) in enumerate(variants):
            props = self.get_properties(variant, user_id)
            owned_count = sum(1 for p in props if p["Own"])
            total_value = sum(p["Value"] for p in props if p["Own"])
            rent_income = sum(round(p["Value"] * 0.008) for p in props if p["Own"] and p["forRent"])
            Label(self.window, relief='raised', text=dispName, font=("Georgia", 22), fg=self.white, background=self.livid, padx=25, pady=15).place(relx=x_positions[idx], rely=0.30, anchor='center')
            Label(self.window, relief='raised', text=f"Props Owned: {owned_count}/7", font=("Times New Roman", 22), fg=self.white, background=self.teal, padx=25, pady=5).place(relx=x_positions[idx], rely=0.44, anchor='center')
            Label(self.window, relief='raised', text=f"Props Value: £{total_value}", font=("Times New Roman", 22), fg=self.white, background=self.teal, padx=25, pady=5).place(relx=x_positions[idx], rely=0.55, anchor='center')
            Label(self.window, relief='raised', text=f"Props Rent: £{rent_income}", font=("Times New Roman", 22), fg=self.white, background=self.teal, padx=25, pady=5).place(relx=x_positions[idx], rely=0.69, anchor='center')
            
            Button(self.window, width=15, text="VIEW MORE INFO",
                   command=lambda v=variant: self.call_view_more_info(v, username),
                   font=("Calibri", 18, 'bold'), fg=self.white, background=self.turquoise).place(relx=x_positions[idx], rely=0.8, anchor='center')
            Button(self.window, width=15, text="ACTIONS",
                   command=lambda v=variant: self.call_actions(v, username),
                   font=("Calibri", 18, 'bold'), fg=self.white, background=self.lime_green).place(relx=x_positions[idx], rely=0.91, anchor='center')
        
        Button(self.window, width=8, text="SAVE", command=lambda: self.manual_save(username), font=("Calibri", 18, 'bold'), fg=self.white, background=self.turquoise).place(relx=0.945, rely=0.938, anchor='center')
        Button(self.window, width=8, text="NEXT\nMONTH", command=lambda: self.next_month(username), font=("Calibri", 18, 'bold'), fg=self.white, background=self.turquoise).place(relx=0.945, rely=0.83, anchor='center')
        
        self.back_button = Button(self.window, relief='raised', text="BACK", font=("Calibri", 28, 'bold'),
                                  command=lambda: self.back_on_click(username), background=self.blue, fg=self.white, padx=25, pady=5)
        self.back_button.place(x=40, y=30)
        self.window.mainloop()

    def call_view_more_info(self, variant, username):
        self.Close()
        view_more_info_page = Game("Buying and Selling Properties Game - Info", "Information")
        view_more_info_page.view_more_info(variant, username)

    def call_actions(self, variant, username):
        self.Close()
        actions_page = Game(f"Buying and Selling Properties Game - {variant.capitalize()} Actions", "Actions")
        actions_page.actions(variant, username)

    def actions(self, variant, username):
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        props = self.get_properties(variant, user_id)
        
        # Background and header
        self.background_label = Label(
            self.window,
            relief='raised',
            font=("Georgia", 22),
            fg=self.white,
            background=self.blue,
            padx=575,
            pady=220
        )
        self.background_label.place(relx=0.5, rely=0.6, anchor='center')
        
        Label(
            self.window,
            relief='raised',
            text=f"{variant.capitalize()} Properties Actions",
            font=("Georgia", 22),
            fg=self.white,
            background=self.livid,
            padx=25,
            pady=15
        ).place(relx=0.53, rely=0.30, anchor='center')
        
        # Create a dedicated frame for the table.
        table_frame = Frame(self.window, background=self.livid)
        table_frame.place(relx=0.5, rely=0.65, anchor='center')
        
        # Add header row for the table.
        headers = ["Property No.", "Value", "Owned", "Buy/Sell", "Rent/Evict", "Invest"]
        for col, heading in enumerate(headers):
            header_label = Label(
                table_frame,
                text=heading,
                font=("Arial", 16, 'bold'),
                fg=self.white,
                bg=self.livid
            )
            header_label.grid(row=0, column=col, padx=5, pady=5)
        
        # Loop through each property and add a row (starting from row 1).
        for i, prop in enumerate(props):
            row_idx = i + 1
            prop_num = i + 1
            own_status = "Yes" if prop["Own"] else "No"
            prop_value = f"£{prop['Value']}"
            
            # Property number.
            e = Entry(
                table_frame,
                width=15,
                disabledbackground=self.livid,
                disabledforeground=self.white,
                fg=self.white,
                font=('Arial', 16, 'bold')
            )
            e.grid(row=row_idx, column=0, padx=5, pady=5)
            e.insert(END, prop_num)
            e.configure(state='disabled', justify='center')
            
            # Property value.
            e_val = Entry(
                table_frame,
                width=15,
                disabledbackground=self.livid,
                disabledforeground=self.white,
                fg=self.white,
                font=('Arial', 16, 'bold')
            )
            e_val.grid(row=row_idx, column=1, padx=5, pady=5)
            e_val.insert(END, prop_value)
            e_val.configure(state='disabled', justify='center')
            
            # Ownership status.
            e_own = Entry(
                table_frame,
                width=15,
                disabledbackground=self.livid,
                disabledforeground=self.white,
                fg=self.white,
                font=('Arial', 16, 'bold')
            )
            e_own.grid(row=row_idx, column=2, padx=5, pady=5)
            e_own.insert(END, own_status)
            e_own.configure(state='disabled', justify='center')
            
            # Buy/Sell button.
            if not prop["Own"]:
                Button(
                    table_frame,
                    text="BUY",
                    command=lambda p=prop_num: self.buy_property(variant, p, username),
                    font=("Calibri", 10, 'bold'),
                    fg="black",
                    background=self.lime_green,
                    width=10
                ).grid(row=row_idx, column=3, padx=5, pady=5)
            else:
                Button(
                    table_frame,
                    text="SELL",
                    command=lambda p=prop_num: self.sell_property(variant, p, username),
                    font=("Calibri", 10, 'bold'),
                    fg=self.white,
                    background=self.red,
                    width=10
                ).grid(row=row_idx, column=3, padx=5, pady=5)
            
            # Rent/Evict button.
            if prop["forRent"]:
                Button(
                    table_frame,
                    text="EVICT",
                    command=lambda p=prop_num: self.evict_property(variant, p, username),
                    font=("Calibri", 10, 'bold'),
                    fg=self.white,
                    background=self.magenta,
                    width=10
                ).grid(row=row_idx, column=4, padx=5, pady=5)
            else:
                Button(
                    table_frame,
                    text="RENT",
                    command=lambda p=prop_num: self.rent_property(variant, p, username),
                    font=("Calibri", 10, 'bold'),
                    fg="black",
                    background=self.light_blue,
                    width=10
                ).grid(row=row_idx, column=4, padx=5, pady=5)
            
            # Invest button – changed text color to black for better contrast.
            Button(
                table_frame,
                text="INVEST",
                command=lambda p=prop_num: self.invest_property(variant, p, username),
                font=("Calibri", 10, 'bold'),
                fg="black",
                background=self.yellow,
                width=10
            ).grid(row=row_idx, column=5, padx=5, pady=5)
        
        # Add a BACK button.
        self.back_button = Button(
            self.window,
            text="BACK",
            font=("Calibri", 28, 'bold'),
            command=lambda: self.back_on_click(username),
            background=self.blue,
            fg=self.white,
            padx=25,
            pady=5
        )
        self.back_button.place(relx=0.05, rely=0.05)
        self.window.mainloop()


    def view_more_info(self, variant, username):
        user = self.get_user_data(username)
        if not user:
            return
        user_id = user["UserID"]
        props = self.get_properties(variant, user_id)
        
        # Background and header
        self.background_label = Label(
            self.window,
            relief='raised',
            font=("Georgia", 22),
            fg=self.white,
            background=self.blue,
            padx=470,
            pady=220
        )
        self.background_label.place(relx=0.5, rely=0.6, anchor='center')
        
        Label(
            self.window,
            text=f"{variant.capitalize()} Properties Info",
            font=("Georgia", 22),
            fg=self.white,
            background=self.livid,
            padx=25,
            pady=15
        ).place(relx=0.53, rely=0.30, anchor='center')
        
        # Create a list of property details.
        a_list = []
        for i, prop in enumerate(props):
            own_status = "Yes" if prop["Own"] else "No"
            rent_val = f"£{round(prop['Value'] * 0.008)}" if prop["Own"] else "£0"
            a_list.append((i + 1, f"£{prop['Value']}", rent_val, own_status))
        
        total_rows = len(a_list)
        total_columns = len(a_list[0]) if total_rows > 0 else 0

        # Create a dedicated frame for the table.
        table_frame = Frame(self.window, background=self.livid)
        table_frame.place(relx=0.5, rely=0.65, anchor='center')
        
        # Create header row.
        headers = ["Property No.", "Value", "Rent", "Owned"]
        for col, heading in enumerate(headers):
            header_entry = Entry(
                table_frame,
                width=15,
                disabledbackground=self.livid,
                disabledforeground=self.white,
                fg=self.white,
                font=('Arial', 16, 'bold')
            )
            header_entry.grid(row=0, column=col, padx=5, pady=5)
            header_entry.insert(END, heading)
            header_entry.configure(state='disabled', justify='center')
        
        # Populate the table (offset by one row for headers).
        for row in range(total_rows):
            for col in range(total_columns):
                e = Entry(
                    table_frame,
                    width=15,
                    disabledbackground=self.livid,
                    disabledforeground=self.white,
                    fg=self.white,
                    font=('Arial', 16, 'bold')
                )
                e.grid(row=row + 1, column=col, padx=5, pady=5)
                e.insert(END, a_list[row][col])
                e.configure(state='disabled', justify='center')
        
        # Add a BACK button.
        self.back_button = Button(
            self.window,
            text="BACK",
            font=("Calibri", 28, 'bold'),
            command=lambda: self.back_on_click(username),
            background=self.blue,
            fg=self.white,
            padx=25,
            pady=5
        )
        self.back_button.place(relx=0.05, rely=0.05)
        self.window.mainloop()


    # -------------
    # Navigation Helpers
    # -------------
    def back_on_click(self, username):
        self.Close()
        from menu import MainMenu
        main_menu_page = MainMenu("Buying and Selling Properties Game - Main Menu", "MAIN MENU")
        MainMenu.main_menu_function(main_menu_page, username)

    def back_on_click_game(self, username):
        self.Close()
        game_page = Game("Buying and Selling Properties Game - Game", "GAME PAGE")
        game_page.game_function(username)

# Example usage:
# if __name__ == "__main__":
#     game = Game("Buying and Selling Properties Game - Game", "GAME PAGE")
#     game.game_function("example_username")
