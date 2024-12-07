from tkinter import messagebox

import customtkinter as ctk
from PIL import Image
from database_manager import DatabaseManager
from utils.widgets import create_frame, create_label, create_button1, create_button3, create_entry_usn, create_entry_pwd
from utils.constants import BACKGROUND_COLOR, LABEL_FONT, LABEL_REGULAR, LABEL_BOLD


class RegistrationWindow:
    # Registration window constructor
    """
    This window contains username and password fields.
    Once entered, the user will be registered within the user database.
    """
    def __init__(self, root):
        self.root = root
        self.db_manager = DatabaseManager()

        self.setup_window()

    # Window Configurations
    def setup_window(self):
        self.root.title("Paninda User Registration")
        self.root.geometry("665x480")
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)
        self.root.iconbitmap("assets/icon.ico.ico")

        self.create_widgets()

    # Creates Widgets
    def create_widgets(self):
        # Window grid configurations
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=2)
        self.root.grid_rowconfigure(0, weight=1)
        ctk.CTkFrame(self.root, width=221, height=480, fg_color="green").grid(row=0, column=0, sticky="nsew")

        # Background Image
        self.bg_img = ctk.CTkImage(light_image=Image.open("assets/SignUp.png"), size=(665, 480))
        self.signup_bg = ctk.CTkLabel(self.root, image=self.bg_img, text="")
        self.signup_bg.place(x=0, y=0, relwidth=1, relheight=1)


        # Signup Widget Frame
        """Separates the sign up field from the logo and panel on the right"""
        self.signup_frame = create_frame(self.root,)
        self.signup_frame.grid(row=0, column=1, sticky="nesw", padx=(30, 10), pady=24)

        # Sign Up Label within Signup Frame
        self.signup_label = create_label(self.signup_frame, text="SIGN UP", font=(LABEL_FONT, 48))
        self.signup_label.grid(row=0, column=0)

        # Signup Entry Frame (for username and password)
        """Contains username and password entry boxes."""
        self.signup_entry_frame = create_frame(self.signup_frame,)
        self.signup_entry_frame.grid(row=1, column=0, pady=32)

        # Username Entry Frame
        """Contains username entry box and its label."""
        self.new_un_frame = create_frame(self.signup_entry_frame)
        self.new_un_frame.pack(pady=4)
        # Username Label and Entry
        self.new_un_label = create_label(self.new_un_frame, text="NEW USERNAME", font=(LABEL_REGULAR, 12))
        self.new_un_entry = create_entry_usn(self.new_un_frame, font=(LABEL_REGULAR, 20), border_width=2, width=320)
        self.new_un_label.grid(row=0, column=0, sticky="w")
        self.new_un_entry.grid(row=1, column=0)

        # Password Entry Frame
        """Contains password entry box and its label."""
        self.new_pw_frame = create_frame(self.signup_entry_frame)
        self.new_pw_frame.pack(pady=4)
        # Password Label and Entry
        self.new_pw_label = create_label(self.new_pw_frame, text="NEW PASSWORD", font=(LABEL_REGULAR, 12))
        self.new_pw_entry = create_entry_pwd(self.new_pw_frame, font=(LABEL_REGULAR, 20), border_width=2, width=320)
        self.new_pw_label.grid(row=0, column=0, sticky="w")
        self.new_pw_entry.grid(row=1, column=0)

        # Signup Buttons Frame
        """Contains signup button and cancel button."""
        self.signup_buttons_frame = create_frame(self.signup_frame,)
        self.signup_buttons_frame.grid(row=2, column=0)
        # Signup & Cancel Buttons
        self.signup_button = create_button1(self.signup_buttons_frame,
                                            text="SIGN UP",
                                            font=(LABEL_FONT, 20),
                                            command=self.register,
                                            height=40,
                                            width=152)
        self.cancel_button = create_button3(self.signup_buttons_frame,
                                            text="CANCEL",
                                            font=(LABEL_FONT, 20),
                                            command=self.root.destroy,
                                            height=40,
                                            width=152)
        self.cancel_button.grid(row=0, column=0, padx=10)
        self.signup_button.grid(row=0, column=1, padx=10)

        # Signup Bottom Message
        self.message_frame = create_frame(self.signup_frame)
        self.message1 = create_label(self.message_frame, text="Paninda is an easy and convenient way to manage", font=(LABEL_BOLD, 12),)
        self.message2 = create_label(self.message_frame, text="your sari-sari store inventory!", font=(LABEL_BOLD, 12),)
        self.message1.pack(pady=0)
        self.message2.pack(pady=0)
        self.message_frame.grid(row=3, column=0, pady=(48, 24))

    # Registers the user
    def register(self):
        """
        This method is called when the user clicks the sign up button.
        This extracts the entered username and password and then passes it to a couple of database manager functions.
        The functions check if the username already exists in the database.
        If the username already exists in the database, it will result in an error message.
        If the username is not a duplicate, it is registered in the database
        :parameters
            new_username: str
            new_password: str
        :return:
            messagebox
        """
        new_username = self.new_un_entry.get()
        new_password = self.new_pw_entry.get()
        if new_username == "" or new_password == "":
            messagebox.showerror(title="ERROR", message="Please enter all fields", parent=self.root)
        elif self.db_manager.check_duplicate(new_username):
            messagebox.showerror(title="ERROR", message="Username already exists", parent=self.root)
        else:
            self.db_manager.save_user(new_username, new_password)
            messagebox.showinfo(title="Registration Successful", message=f"We're glad to welcome you, {new_username}!", parent=self.root)