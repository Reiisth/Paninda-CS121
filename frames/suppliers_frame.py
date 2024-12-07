import customtkinter as ctk
from tkinter import ttk, messagebox
from database_manager import DatabaseManager
from frames.home_frame import HomeFrame
from utils.widgets import button_default, entry_label, entry_default, big_label
from utils.constants import BACKGROUND_COLOR, LABEL_REGULAR, LABEL_BOLD, BUTTON_COLOR1, BUTTON_COLOR3, BUTTON_COLOR2


class SuppliersFrame(ctk.CTkFrame):
    """
    This class represents the suppliers frame.
    It displays entry fields on the top for entries and editing.
    It also displays a treeview table that has 4 columns:
        Supplier ID
        Supplier Name
        Supplier Contact
        Supplier Address
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Top Frame contains entry fields and label
        self.entry_frame = ctk.CTkFrame(self, fg_color=BUTTON_COLOR3, bg_color=BUTTON_COLOR3,height=256, width=768)
        self.entry_frame.grid(row=0, column=0, sticky='nsew')
        big_label(self.entry_frame, "SUPPLIERS").pack(fill="x", expand=True, padx=5, pady=(10, 5))

        # Frame that contains all alterable fields
        """
        There are fields that are displayed in the treeview 
        that is not editable or alterable such as the Supplier ID column which is automatically assigned.
        That is because these columns contain foreign data that was derived from foreign keys.
        Thus they can only be altered within the table that they are entered.
        """
        self.fields_frame = ctk.CTkFrame(self.entry_frame, fg_color="transparent")

        # Name entry and label
        self.name_field_frame = ctk.CTkFrame(self.fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.name_field_frame, "SUPPLIER NAME").grid(row=0, column=0, sticky="w", pady=0)
        self.supplier_name_entry = entry_default(self.name_field_frame, 250, "ex: Lawson Marketing Inc.")
        self.supplier_name_entry.grid(row=1, column=0)

        # Contact entry and label
        self.contact_frame = ctk.CTkFrame(self.fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.contact_frame,"CONTACT").grid(row=0, column=0, sticky="w", pady=0)
        self.supplier_contact_entry = entry_default(self.contact_frame, 150, "ex: 09221106121")
        self.supplier_contact_entry.grid(row=1, column=0)

        # Address entry and label
        self.address_frame = ctk.CTkFrame(self.fields_frame,fg_color="transparent", bg_color="transparent")
        entry_label(self.address_frame,"ADDRESS").grid(row=0, column=0, sticky="w", pady=0)
        self.supplier_address_entry = entry_default(self.address_frame, 300, "ex: Illustre Ave. Lemery, Batangas")
        self.supplier_address_entry.grid(row=1, column=0)

        # Entry fields placement
        self.name_field_frame.grid(row=0, column=0, padx=10)
        self.contact_frame.grid(row=0, column=1, padx=10)
        self.address_frame.grid(row=0, column=2, padx=10)
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
        self.tree = ttk.Treeview(self.treeview_frame, columns=("SupplierID", "SupplierName", "SupplierContact", "SupplierAddress"), show="headings", height=25)
        self.tree.heading("SupplierID", text="Supplier ID")
        self.tree.heading("SupplierName", text="Name")
        self.tree.heading("SupplierContact", text="Contact")
        self.tree.heading("SupplierAddress", text="Address")
        self.tree.column("SupplierID", width=130, anchor="center")
        self.tree.column("SupplierName", width=360)
        self.tree.column("SupplierContact", width=180, anchor="center")
        self.tree.column("SupplierAddress", width=450)
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
        self.supplier_name_entry.delete(0, "end")
        self.supplier_name_entry.insert(0, row_values[1])
        self.supplier_contact_entry.delete(0, "end")
        self.supplier_contact_entry.insert(0, row_values[2])
        self.supplier_address_entry.delete(0, "end")
        self.supplier_address_entry.insert(0, row_values[3])

    # Fills the treeview table
    def populate_treeview(self):
        """
        This function essentially fills up the treeview table with the data in the database tables.
        It is also called to refresh the table every time an action is done.
        """
        self.rows = self.db_manager.treeview_supplier(self.user_id)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.rows:
            self.tree.insert('', 'end', values=row)

    # Adds Supplier
    def add_row(self):
        """Extracts data from the entry fields and calls a database manager function to insert a new record."""
        self.supplier_name = self.supplier_name_entry.get()
        self.supplier_contact = self.supplier_contact_entry.get()
        self.supplier_address = self.supplier_address_entry.get()

        """Rejects blank inputs"""
        if not self.supplier_name or not self.supplier_contact:
            messagebox.showerror(title="Error", message="Name and Contact are required fields")
            return

        # Exception catching
        try:
            self.db_manager.save_supplier(self.supplier_name, self.supplier_contact, self.supplier_address, self.user_id)
            messagebox.showinfo(title="Success", message="Supplier has been added")
            self.supplier_name_entry.delete(0, "end")
            self.supplier_contact_entry.delete(0, "end")
            self.supplier_address_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    # Deletes Supplier
    def delete_row(self):
        """Extracts data from the double click event and calls a database manager function to delete the selected record."""
        self.selected_item = self.tree.selection()

        """Rejects blank selections."""
        if not self.selected_item:
            messagebox.showerror(title="Error", message="No selected item")
            return

        item = self.tree.item(self.selected_item)
        row_values = item["values"]

        supplier_id = row_values[0]

        # Exception Catching
        try:
            self.db_manager.delete_supplier(supplier_id)
            messagebox.showinfo(title="Success", message="Supplier has been deleted")
            self.supplier_name_entry.delete(0, "end")
            self.supplier_contact_entry.delete(0, "end")
            self.supplier_address_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    # Updates Supplier Info
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
        supplier_id = row_values[0]

        # Updated values
        supplier_name = self.supplier_name_entry.get()
        supplier_contact = self.supplier_contact_entry.get()
        supplier_address = self.supplier_address_entry.get()

        """Rejects blank inputs."""
        if not supplier_name or not supplier_contact:
            messagebox.showerror(title="Error", message="Name and Contact are required fields")
            return

        # Exception catching
        try:
            self.db_manager.update_supplier(
                supplier_id, supplier_name, supplier_contact, supplier_address, self.user_id)
            messagebox.showinfo(title="Success", message="Supplier has been updated")
            self.supplier_name_entry.delete(0, "end")
            self.supplier_contact_entry.delete(0, "end")
            self.supplier_address_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))