from registration_window import RegistrationWindow
from utils.constants import BACKGROUND_COLOR, LABEL_FONT, LABEL_REGULAR
from database_manager import DatabaseManager
from main_window import MainWindow
from utils.widgets import create_label, create_frame, create_entry_usn, create_entry_pwd, create_button1, create_button2
import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from PIL import Image

class LoginWindow:
    # Login Window Constructor
    """
    First Window to appear and contains username and password fields.
    This window also contains a button that opens the registration window.
    """
    def __init__(self, root):
        self.root = root
        self.db_manager = DatabaseManager()

        self.setup_window()

    # Window Configurations
    def setup_window(self):
        self.root.title("Paninda Login")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.root.configure(fg_color=BACKGROUND_COLOR)

        self.create_widgets()

    # Creates widgets for Login Window
    def create_widgets(self):
        # Logo Frame
        """This contains the main logo of Paninda."""
        self.logo = ctk.CTkImage(light_image=Image.open("assets/Paninda400.png"), size=(269,65))
        self.logo_frame = tk.Frame(self.root,background=BACKGROUND_COLOR)

        self.logo_label = ctk.CTkLabel(self.logo_frame, image=self.logo, fg_color=BACKGROUND_COLOR, text="", bg_color=BACKGROUND_COLOR)
        self.logo_label.grid(row=0, column=0)
        self.logo_frame.pack(pady=(50, 4))

        # Login Label
        self.login_label = create_label(parent=self.root, text="LOGIN", font=(LABEL_FONT, 24))
        self.login_label.pack(pady=4)

        # Entry Frame
        """Contains both login and password fields."""
        self.entry_frame = create_frame(self.root,)
        self.entry_frame.pack(pady=8)

        # Username Frame within Entry Frame
        """Contains username label and field"""
        self.usern_frame = create_frame(self.entry_frame,)
        self.usern_label = create_label(parent=self.usern_frame, text="USERNAME", font=(LABEL_REGULAR, 12))
        self.entry_usern = create_entry_usn(self.usern_frame, (LABEL_REGULAR, 16), 1, 269)
        self.usern_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")
        self.entry_usern.grid(row=1, column=0, padx=10, pady=0)
        self.usern_frame.pack()

        # Password Frame within Entry Frame
        """Contains password label and field"""
        self.pwd_frame = create_frame(self.entry_frame,)
        self.pwd_label = create_label(parent=self.pwd_frame, text="PASSWORD", font=(LABEL_REGULAR, 12))
        self.entry_pwd = create_entry_pwd(self.pwd_frame, (LABEL_REGULAR, 16), 1, width=269)
        self.pwd_label.grid(row=0, column=0, padx=10, pady=0, sticky="w")
        self.entry_pwd.grid(row=1, column=0, padx=10, pady=0)
        self.pwd_frame.pack()

        # Login Button
        self.login_button = create_button1(self.root,"LOGIN",(LABEL_FONT, 18), command=self.login, height=36, width=100)
        self.login_button.pack()

        # Register Frame
        self.register_frame = create_frame(self.root,)
        self.register_label = create_label(parent=self.register_frame, text="Not registered yet?", font=(LABEL_REGULAR, 10))
        self.register_button = create_button2(self.register_frame,"REGISTER",(LABEL_REGULAR, 13), command=self.open_registration, height=20, width=80)
        self.register_label.pack()
        self.register_button.pack()
        self.register_frame.pack()

    # Login Function
    def login(self):
        """
        Calls an authentication method and logs the user in
        :parameter
            username (str)
            password (str)
        :return:
            user_id (int)
        """
        username = self.entry_usern.get()
        password = self.entry_pwd.get()
        user_id = self.db_manager.get_userid(username, password)
        if user_id:
            messagebox.showinfo("Login Successful", f"Welcome to Paninda, {username}!")
            self.root.destroy()
            self.open_main_window(user_id)
        else:
            messagebox.showerror("Login Failed", f"Username or password is incorrect")

    # Opens Main Window
    def open_main_window(self, user_id):
        main_app = ctk.CTk()
        MainWindow(self, main_app, user_id)
        main_app.mainloop()

    # Opens Registration Window
    def open_registration(self):
        registration_app = ctk.CTkToplevel(self.root)
        RegistrationWindow(registration_app)