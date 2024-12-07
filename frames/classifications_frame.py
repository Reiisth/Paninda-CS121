import customtkinter as ctk
from tkinter import ttk, messagebox
from database_manager import DatabaseManager
from utils.widgets import button_default, entry_label, entry_default, big_label
from utils.constants import BACKGROUND_COLOR, LABEL_FONT, LABEL_REGULAR, LABEL_BOLD, BUTTON_COLOR1, BUTTON_COLOR3, \
    BLACK_COLOR, BUTTON_COLOR2


class ClassificationsFrame(ctk.CTkFrame):
    """
    This class represents the classifications frame.
    It displays entry fields on the top for entries and editing.
    It also displays a treeview table that has 2 columns:
        Class ID
        Class Name
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
        big_label(self.entry_frame,"CLASSIFICATIONS").pack(fill="x", expand=True, padx=5, pady=(10, 5))

        # Frame that contains all alterable fields
        self.fields_frame = ctk.CTkFrame(self.entry_frame, fg_color="transparent")

        # Name entry and label
        self.class_id_field_frame = ctk.CTkFrame(self.fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.class_id_field_frame, "CLASS ID").grid(row=0, column=0, sticky="w", pady=0)
        self.class_id_entry = entry_default(self.class_id_field_frame, 150, "ex: ICC")
        self.class_id_entry.grid(row=1, column=0)

        # Contact entry and label
        self.class_name_frame = ctk.CTkFrame(self.fields_frame, fg_color="transparent", bg_color="transparent")
        entry_label(self.class_name_frame,"CLASS NAME").grid(row=0, column=0, sticky="w", pady=0)
        self.class_name_entry = entry_default(self.class_name_frame, 250, "ex: Ice Creams")
        self.class_name_entry.grid(row=1, column=0)

        # Entry fields placement
        self.class_id_field_frame.grid(row=0, column=0, padx=10)
        self.class_name_frame.grid(row=0, column=1, padx=10)
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
        self.tree = ttk.Treeview(self.treeview_frame, columns=("ClassID", "ClassName"), show="headings", height=25)
        self.tree.heading("ClassID", text="Class ID")
        self.tree.heading("ClassName", text="Class Name")
        self.tree.column("ClassID", width=130, anchor="center")
        self.tree.column("ClassName", width=360)
        self.tree.grid(row=0, column=0, sticky='nsew', padx=330, pady=(10, 0))

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
        self.class_id_entry.delete(0, "end")
        self.class_id_entry.insert(0, row_values[0])
        self.class_name_entry.delete(0, "end")
        self.class_name_entry.insert(0, row_values[1])

    # Fills the treeview table
    def populate_treeview(self):
        """
        This function essentially fills up the treeview table with the data in the database tables.
        It is also called to refresh the table every time an action is done.
        """
        self.rows = self.db_manager.treeview_classification()

        for row in self.tree.get_children():
            self.tree.delete(row)

        for row in self.rows:
            self.tree.insert('', 'end', values=row)

    # Adds Classification
    def add_row(self):
        """Extracts data from the entry fields and calls a database manager function to insert a new record."""
        self.class_id = self.class_id_entry.get()
        self.class_name = self.class_name_entry.get()

        """Rejects blank inputs."""
        if not self.class_id or not self.class_name:
            messagebox.showerror(title="Error", message="Class ID and Class Name are required fields")
            return

        # Exception catching
        try:
            self.db_manager.save_classification(self.class_id, self.class_name)
            messagebox.showinfo(title="Success", message="Class has been added")
            self.class_id_entry.delete(0, "end")
            self.class_name_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    # Deletes Classification
    def delete_row(self):
        """Extracts data from the double click event and calls a database manager function to delete the selected record."""
        self.selected_item = self.tree.selection()

        """Rejects blank selections."""
        if not self.selected_item:
            messagebox.showerror(title="Error", message="No selected item")
            return

        item = self.tree.item(self.selected_item)
        row_values = item["values"]

        class_id = row_values[0]

        # Exception catching
        try:
            self.db_manager.delete_classification(class_id)
            messagebox.showinfo(title="Success", message="Class has been deleted")
            self.class_id_entry.delete(0, "end")
            self.class_name_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))

    # Updates Classification Info
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
        class_id = row_values[0]

        # Updated values
        new_class_id = self.class_id_entry.get()
        class_name = self.class_name_entry.get()

        """Rejects blank inputs."""
        if not class_id or not class_name:
            messagebox.showerror(title="Error", message="Name and Contact are required fields")
            return

        # Exception catching
        try:
            self.db_manager.update_classification(class_id, new_class_id, class_name)
            messagebox.showinfo(title="Success", message="Class has been updated")
            self.class_id_entry.delete(0, "end")
            self.class_name_entry.delete(0, "end")
            self.populate_treeview()

        except Exception as e:
            messagebox.showerror(title="Error", message=str(e))