import customtkinter as ctk
from tkinter import ttk, messagebox
from database_manager import DatabaseManager
from utils.widgets import button_default, entry_label, entry_default, big_label, big_number
from utils.constants import BACKGROUND_COLOR, LABEL_REGULAR, LABEL_BOLD, BUTTON_COLOR1, BUTTON_COLOR3, BUTTON_COLOR2, \
    BLACK_COLOR


class HomeFrame(ctk.CTkFrame):
    """
    This class represents the home frame.
    It displays basic information about the system such as:
        Number of Products Registered
        Number of Suppliers Registered
        Number of Stocks Registered
        Treeview table of Expired Products
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

        # Top Frame contains summarized list and label
        self.info_frame = ctk.CTkFrame(self, fg_color=BUTTON_COLOR3, bg_color=BUTTON_COLOR3,height=256, width=768)
        self.info_frame.grid(row=0, column=0, sticky='nsew')
        big_label(self.info_frame, "HOME").pack(fill="x", expand=True, padx=5, pady=(10, 5))

        # Frame that contains all data displays
        self.info_fields_frame = ctk.CTkFrame(self.info_frame, fg_color="transparent")

        # Stock Label and Number
        self.stock_field_frame = ctk.CTkFrame(self.info_fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.stock_field_frame, "PRODUCTS IN-STOCK:").grid(row=0, column=0, pady=0)
        self.stock = self.db_manager.stock_count(self.user_id)
        self.stock_count = big_number(self.stock_field_frame, self.stock[0])
        self.stock_count.grid(row=1, column=0)

        # Product Label and Number
        self.product_field_frame = ctk.CTkFrame(self.info_fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.product_field_frame, "NO. OF PRODUCTS:").grid(row=0, column=0, pady=0)
        self.products = self.db_manager.product_count(self.user_id)
        self.products_count =  big_number(self.product_field_frame, self.products[0])
        self.products_count.grid(row=1, column=0)

        # Supplier Label and Number
        self.supplier_field_frame = ctk.CTkFrame(self.info_fields_frame,fg_color="transparent", bg_color="transparent")
        entry_label(self.supplier_field_frame,"NO. OF SUPPLIERS:").grid(row=0, column=0, pady=0)
        self.suppliers = self.db_manager.supplier_count(self.user_id)
        self.suppliers_count = big_number(self.supplier_field_frame, self.suppliers[0])
        self.suppliers_count.grid(row=1, column=0)

        # Info fields placement
        self.stock_field_frame.grid(row=0, column=0, padx=10)
        self.product_field_frame.grid(row=0, column=1, padx=24)
        self.supplier_field_frame.grid(row=0, column=2, padx=10)
        self.info_fields_frame.pack(expand=True, pady=(8, 24))

        ctk.CTkLabel(self.info_frame, text="EXPIRED STOCK", font=(LABEL_BOLD, 16), bg_color=BUTTON_COLOR1, text_color='white').pack(expand=True, fill="x")


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
        self.tree = ttk.Treeview(self.treeview_frame, columns=("ProductID", "ProductName", "ExpDate", "Quantity"),
                                 show="headings", height=25)
        self.tree.heading("ProductID", text="Product ID")
        self.tree.heading("ProductName", text="Product Name")
        self.tree.heading("ExpDate", text="Expiration Date")
        self.tree.heading("Quantity", text="Quantity")
        self.tree.column("ProductID", width=180, anchor="center")
        self.tree.column("ProductName", width=590)
        self.tree.column("ExpDate", width=200, anchor="center")
        self.tree.column("Quantity", width=150, anchor="center")
        self.tree.grid(row=0, column=0, sticky='nsew', padx=15, pady=(10, 0))


    # Fills the treeview table
    def populate_treeview(self):
        """
        This function essentially fills up the treeview table with the data in the database tables.
        It is also called to refresh the table every time an action is done.
        """
        self.rows = self.db_manager.treeview_expired(self.user_id)

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.rows:
            self.tree.insert('', 'end', values=row)
