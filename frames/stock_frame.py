import customtkinter as ctk
from tkinter import ttk, messagebox
from database_manager import DatabaseManager
from utils.widgets import button_default, entry_label, entry_default, big_label
from utils.constants import BACKGROUND_COLOR, LABEL_FONT, LABEL_REGULAR, LABEL_BOLD, BUTTON_COLOR1, BUTTON_COLOR3, \
    BLACK_COLOR, BUTTON_COLOR2


class StockFrame(ctk.CTkFrame):
    """
    This class represents the stock frame.
    It displays entry fields on the top for entries and editing.
    It also displays a treeview table that has 4 columns:
        Product ID
        Product Name
        Expiration Date
        Quantity
    """
    def __init__(self, master, user_id):
        """
        This class accepts the user's user id in order to cater a user-exclusive
        experience and display only data that the user is concerned.
        :param master: content frame
        :param user_id: int
        """
        super().__init__(master, corner_radius=10)
        self.selected_item = None
        self.user_id = user_id
        self.db_manager = DatabaseManager()

        self.create_widgets()
        self.populate_treeview()

    # Creates widgets within the frame
    def create_widgets(self):
        # Frame grid configurations
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Top Frame contains entry fields and label
        self.entry_frame = ctk.CTkFrame(self, fg_color=BUTTON_COLOR3, bg_color=BUTTON_COLOR3,height=256, width=768)
        self.entry_frame.grid(row=0, column=0, sticky='nsew')
        big_label(self.entry_frame,"STOCK").pack(fill="x", expand=True, padx=5, pady=(10, 5))


        # Frame that contains all alterable fields
        """
        There are fields that are displayed in the treeview 
        that is not editable or alterable such as the product name column.
        That is because these columns contain foreign data that was derived from foreign keys.
        Thus they can only be altered within the table that they are entered.
        """
        self.fields_frame = ctk.CTkFrame(self.entry_frame, fg_color="transparent")

        # Product ID entry and label
        self.product_id_frame = ctk.CTkFrame(self.fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.product_id_frame, "PRODUCT ID").grid(row=0, column=0, sticky="w", pady=0)
        self.product_id_entry = entry_default(self.product_id_frame, 150, "ex: 1")
        self.product_id_entry.grid(row=1, column=0)

        # Contact entry and label
        self.exp_date_frame = ctk.CTkFrame(self.fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.exp_date_frame,"EXPIRATION DATE").grid(row=0, column=0, sticky="w", pady=0)
        self.exp_date_entry = entry_default(self.exp_date_frame, 200, "ex: 2022-11-06")
        self.exp_date_entry.grid(row=1, column=0)

        # Address entry and label
        self.quantity_frame = ctk.CTkFrame(self.fields_frame,fg_color="transparent", bg_color="transparent")
        entry_label(self.quantity_frame,"QUANTITY").grid(row=0, column=0, sticky="w", pady=0)
        self.quantity_entry = entry_default(self.quantity_frame, 150, "")
        self.quantity_entry.grid(row=1, column=0)

        # Entry fields placement
        self.product_id_frame.grid(row=0, column=0, padx=10)
        self.exp_date_frame.grid(row=0, column=1, padx=10)
        self.quantity_frame.grid(row=0, column=2, padx=10)
        self.fields_frame.pack(expand=True, pady=(8, 24))

        # Button Frame
        self.button_frame = ctk.CTkFrame(self.entry_frame, fg_color="transparent", bg_color="transparent")
        self.add_button = button_default(self.button_frame, "ADD", command=self.add_row)
        self.update_button = button_default(self.button_frame, "UPDATE", command=self.update_row)
        self.delete_button = button_default(self.button_frame, "DELETE", command=self.delete_row)
        # Button Placement
        self.add_button.grid(row=0, column=0, padx=10)
        self.update_button.grid(row=0, column=1, padx=10)
        self.delete_button.grid(row=0, column=2, padx=10)
        self.button_frame.pack(expand=True, pady=(0, 24))

        # Treeview Styling
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview.Heading", font=(LABEL_BOLD, 16), foreground="white", background=BUTTON_COLOR2)
        style.configure("Treeview",
                        font=(LABEL_REGULAR, 14),
                        rowheight=30)
        style.map("Treeview", background=[("selected", BUTTON_COLOR1)], foreground=[("selected", "white")])

        # Treeview Creation
        self.treeview_frame = ctk.CTkFrame(self, fg_color=BACKGROUND_COLOR, corner_radius=0)
        self.treeview_frame.grid(row=1, column=0, sticky='nsew')
        self.treeview_frame.grid_columnconfigure(0, weight=1)
        self.treeview_frame.grid_rowconfigure(0, weight=1)
        self.tree = ttk.Treeview(self.treeview_frame, columns=("ProductID", "ProductName", "ExpDate", "Quantity"), show="headings", height=25)
        self.tree.heading("ProductID", text="Product ID")
        self.tree.heading("ProductName", text="Product Name")
        self.tree.heading("ExpDate", text="Expiration Date")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.column("ProductID", width=180, anchor="center")
        self.tree.column("ProductName", width=590)
        self.tree.column("ExpDate", width=200, anchor="center")
        self.tree.column("Quantity", width=150, anchor="center")
        self.tree.grid(row=0, column=0, sticky='nsew', padx=15, pady=(10, 0))

        # Binding to double-click event
        self.tree.bind("<Double-1>", self.on_row_double_click)

    # Double click fetcher
    def on_row_double_click(self, event):
        """
        This defines an event that the treeview is bound to.
        It allows users to click the treeview to enter data within the fields.
        """
        self.selected_item = self.tree.selection()
        if not self.selected_item:
            return

        item = self.tree.item(self.selected_item)
        row_values = item["values"]

        """Clears the entry fields and populates it with the selected values."""
        self.product_id_entry.delete(0, "end")
        self.product_id_entry.insert(0, row_values[0])
        self.exp_date_entry.delete(0, "end")
        self.exp_date_entry.insert(0, row_values[2])
        self.quantity_entry.delete(0, "end")
        self.quantity_entry.insert(0, row_values[3])

    # Fills the treeview table
    def populate_treeview(self):
        """
        This function essentially fills up the treeview table with the data in the database tables.
        It is also called to refresh the table every time an action is done.
        """
        self.rows = self.db_manager.treeview_stock(self.user_id)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.rows:
            self.tree.insert('', 'end', values=row)

    # Adds Stock
    def add_row(self):
        """Extracts data from the entry fields and calls a database manager function to insert a new record."""
        product_id = self.product_id_entry.get()
        exp_date = self.exp_date_entry.get()
        quantity = self.quantity_entry.get()

        """Rejects blank inputs."""
        if not product_id or not exp_date or not quantity:
            messagebox.showerror(title="Error", message="Name and Contact are required fields")
            return

        # Exception catching
        try:
            self.db_manager.save_stock(product_id, exp_date, quantity, self.user_id)
            messagebox.showinfo(title="Success", message="Stock has been added")
            self.product_id_entry.delete(0, "end")
            self.exp_date_entry.delete(0, "end")
            self.quantity_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    # Deletes Stock
    def delete_row(self):
        """Extracts data from the double click event and calls a database manager function to delete the selected record."""
        selected_item = self.tree.selection()

        """Rejects blank selections."""
        if not self.selected_item:
            messagebox.showerror(title="Error", message="No selected item")
            return

        item = self.tree.item(selected_item)
        row_values = item["values"]

        product_id = row_values[0]
        exp_date = row_values[2]

        # Exception catching
        try:
            self.db_manager.delete_stock(product_id, exp_date, self.user_id)
            messagebox.showinfo(title="Success", message="Stock has been deleted")
            self.product_id_entry.delete(0, "end")
            self.exp_date_entry.delete(0, "end")
            self.quantity_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    # Updates Stock Info
    def update_row(self):
        """Extracts data from entry fields and calls a database manager function to update the selected record."""
        selected_item = self.tree.selection()

        """Rejects blank selection"""
        if not selected_item:
            messagebox.showerror(title="Error", message="No selected item")
            return
        item = self.tree.item(selected_item)
        # Recorded values within the database
        row_values = item["values"]
        product_id = row_values[0]
        exp_date = row_values[2]

        # Updated values
        product_id_new = self.product_id_entry.get()
        exp_date_new = self.exp_date_entry.get()
        quantity = self.quantity_entry.get()

        """Rejects blank inputs."""
        if not product_id or not exp_date:
            messagebox.showerror(title="Error", message="Name and Contact are required fields")
            return

        # Exception catching
        try:
            self.db_manager.update_stock(
                product_id, exp_date, product_id_new, exp_date_new, quantity, self.user_id)
            messagebox.showinfo(title="Success", message="Stock has been updated")
            self.product_id_entry.delete(0, "end")
            self.exp_date_entry.delete(0, "end")
            self.quantity_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))