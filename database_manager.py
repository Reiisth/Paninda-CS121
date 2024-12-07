from tkinter import messagebox

import mysql.connector
from mysql.connector import Error


class DatabaseManager:
    """
    This is the database manager class that handles database connections and queries.
    This class is divided into subclasses but not implemented in code.
    The subclasses are as follows:
        Generic Functions
        Login Functions
        Signup Functions
        Frame Functions
            Stock
            Product
            Supplier
            Classification

    Each subclass contains its own methods that are utilized within their namesake classes/windows.
    This class was done for modularity, ease of implementation, and optimized debugging.
    """
    def __init__(self):
        """Every time the database manager is called, a connection is created."""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="paninda_db"
            )
            if self.connection.is_connected():
                print("Connected to MySQL server.")
        except Error as e:
            print(f"Error connecting to MySQL server: {e}")
            self.connection = None

# Generic Functions
    """
    These functions are called generic because they apply to all windows/classes and are utilized in them.
    These functions can be called as foundational functions because they are used in other functions.
    These are created to lessen the lines of code by automating or modularizing actions that are done often.
    """
    # Executes queries
    def execute_query(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            cursor.close()
            print("Query executed successfully.")
        except Error as e:
            print(f"Error executing query: {e}")

    # Fetches one row
    def fetch_one(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            result = cursor.fetchone()
            cursor.close()
            return result
        except Error as e:
            print(f"Error fetching data: {e}")
            return None

    # Fetches multiple rows
    def fetch_all(self, query, params=None):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return []

    # Closes database connection
    def close_connection(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed.")

# Login Function
    """These function is only called by the login class/window."""
    # Returns user id of the logged in account
    def get_userid(self, username, password):
        query = "SELECT userid FROM users WHERE username = %s AND password = %s"
        result = self.fetch_one(query, (username, password))
        if result is not None:
            return result[0]
        else:
            return False

# Frame Functions
    """
    It is not practical to use this subclass structure because each class performs 
    the same add, delete, and update, function but are grouped into separate functions here.
    This is done to have a clearer division between functions and classes.
    And also to easily spot functions/structures that are not well defined.
    """
# Signup Functions
    """These functions are only called by the signup class/window."""
    # Saves user within the database
    def save_user(self, username, password):
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        self.execute_query(query, (username, password))
        print("Record saved.")

    # Checks for duplicate usernames
    def check_duplicate(self, username):
        query = "SELECT userid FROM users WHERE username = %s"
        return self.fetch_one(query, (username,))

 # Supplier Functions (For Supplier Frame only)
    """These functions are only called by the Supplier class."""
    # Retrieves all data from supplier table
    def treeview_supplier(self, user_id):
        try:
            query = "SELECT * FROM suppliers WHERE UserID = %s"
            return self.fetch_all(query, (user_id,))
        except Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    # Saves supplier info
    def save_supplier(self, supplier_name, supplier_contact, supplier_address, user_id):
        query = 'INSERT INTO suppliers (SupplierName, SupplierContact, SupplierAddress, UserID) VALUES (%s, %s, %s, %s)'
        self.execute_query(query, (supplier_name, supplier_contact, supplier_address, user_id))

    # Deletes supplier info
    def delete_supplier(self, supplier_id):
        query = "DELETE FROM suppliers WHERE SupplierID = %s"
        self.execute_query(query, (supplier_id,))

    # Updates supplier info
    def update_supplier(self, supplier_id, supplier_name, supplier_contact, supplier_address, user_id):
        query = "UPDATE suppliers SET SupplierName = %s, SupplierContact = %s, SupplierAddress = %s WHERE SupplierID = %s and UserID = %s"
        self.execute_query(query, (supplier_name, supplier_contact, supplier_address, supplier_id, user_id))

# Classification Functions (For Classification Frame only)
    """These functions are only called by the Classifications class."""
    # Retrieves all data from classifications table
    def treeview_classification(self):
        try:
            query = "SELECT * FROM classifications"
            return self.fetch_all(query)
        except Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    # Saves classification info
    def save_classification(self, class_id, class_name):
        query = 'INSERT INTO classifications (ClassID, ClassName) VALUES (%s, %s)'
        self.execute_query(query, (class_id, class_name))

    # Deletes classification info
    def delete_classification(self, class_id):
        query = "DELETE FROM classifications WHERE ClassID = %s"
        self.execute_query(query, (class_id,))

    # Updates classification info
    def update_classification(self, class_id, new_class_id, class_name):
        query = "UPDATE classifications SET ClassID = %s, ClassName = %s WHERE ClassID = %s"
        self.execute_query(query, (new_class_id, class_name, class_id))

# Products Functions (For Products Frame only)
    """These functions are only called by the Products class."""
    # Retrieves all data from products table
    def treeview_product(self, user_id):
        try:
            query = "SELECT * FROM products WHERE UserID = %s"
            return self.fetch_all(query, (user_id,))
        except Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    # Saves product info
    def save_product(self, product_name, class_id, supplier_id, user_id):
        query = 'INSERT INTO products (ProductName, ClassID, SupplierID, UserID) VALUES (%s, %s, %s, %s)'
        self.execute_query(query, (product_name, class_id, supplier_id, user_id))

    # Deletes product info
    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE ProductID = %s"
        self.execute_query(query, (product_id,))

    # Updates product info
    def update_product(self, product_id, product_name, class_id, supplier_id, user_id):
        query = "UPDATE products SET ProductName = %s, ClassID = %s, SupplierID = %s WHERE ProductID = %s AND UserID = %s"
        self.execute_query(query, (product_name, class_id, supplier_id, product_id, user_id))

# Stock Functions (For Stock Frame only)
    """These functions are only called by the Stock class."""
    # Retrieves all data from products table
    def treeview_stock(self, user_id):
        try:
            query = "SELECT * FROM stock_with_names WHERE UserID = %s ORDER BY ExpDate ASC, Quantity ASC"
            return self.fetch_all(query, (user_id,))
        except Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    # Saves stock info
    def save_stock(self, product_id, exp_date, quantity, user_id):
        query = "INSERT INTO stock (ProductID, ExpDate, Quantity, UserID) VALUES (%s, %s, %s, %s)"
        self.execute_query(query, (product_id, exp_date, quantity, user_id))

    # Deletes stock info
    def delete_stock(self, product_id, exp_date, user_id):
        query = "DELETE FROM stock WHERE ProductID = %s AND ExpDate = %s AND UserID = %s"
        self.execute_query(query, (product_id, exp_date, user_id))

    # Updates stock info
    def update_stock(self, product_id, exp_date, product_id_new, exp_date_new, quantity, user_id):
        query = "UPDATE stock SET ProductID = %s, ExpDate = %s, Quantity = %s WHERE ProductID = %s AND ExpDate = %s AND UserID = %s "
        self.execute_query(query, (product_id_new, exp_date_new, quantity,  product_id, exp_date, user_id))


# Aggregate Functions
    def treeview_expired(self, user_id):
        query = "SELECT * FROM expired_stock WHERE UserID = %s ORDER BY ExpDate ASC, Quantity ASC"
        return self.fetch_all(query, (user_id,))

    def stock_count(self, user_id):
        query = "SELECT COUNT(*) FROM stock WHERE UserID = %s"
        return self.fetch_one(query, (user_id,))

    def product_count(self, user_id):
        query = "SELECT COUNT(*) FROM products WHERE UserID = %s"
        return self.fetch_one(query, (user_id,))

    def supplier_count(self, user_id):
        query = "SELECT COUNT(*) FROM suppliers WHERE UserID = %s"
        return self.fetch_one(query, (user_id,))

