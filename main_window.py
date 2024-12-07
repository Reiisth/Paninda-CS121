from tkinter import messagebox
from PIL import Image
import customtkinter as ctk
from database_manager import DatabaseManager
from frames.home_frame import HomeFrame
from frames.suppliers_frame import SuppliersFrame
from frames.classifications_frame import ClassificationsFrame
from frames.products_frame import ProductsFrame
from frames.stock_frame import StockFrame
from utils.constants import BUTTON_COLOR1, LABEL_FONT, HOVER_COLOR_1, BACKGROUND_COLOR, BLACK_COLOR, BUTTON_COLOR3, HOVER_COLOR_3

# Main Window
class MainWindow:
    """
    This class contains the main window of the application.
    It is split into two parts:
        Dashboard panel/frame
        Content panel/frame

    The Dashboard Panel contains tabs(buttons) that allow users to navigate the contents panel.
    Each tab is configured to show a different content panel and each panel has different functionality and contents.
    It provides an easy way to navigate a large database while conserving memory and optimizing performance.
    Because of its modularity, this setup is expandable and can accommodate more content frames if it is necessary.
    """
    userid: object
    def __init__(self, parent, main_app, userid):
        self.parent = parent
        self.app = main_app
        self.userid = userid
        self.db_manager = DatabaseManager()

        self.setup_window()

    # Window Configurations
    def setup_window(self):
        print(f"Logged in with UserID: {self.userid}")
        self.app.title("Paninda Dashboard")
        self.app.geometry("1024x768")
        self.app.resizable(False, False)

        self.create_widgets()

    # Creates Widgets
    def create_widgets(self):
        # Create the Dashboard panel
        self.dashboard_panel = ctk.CTkFrame(self.app, width=256, corner_radius=0, fg_color=BUTTON_COLOR1, bg_color=BUTTON_COLOR1)
        self.dashboard_panel.pack(side="left", fill="y")

        # Logo
        """Paninda logo on the dashboard panel."""
        self.logo = ctk.CTkImage(light_image=Image.open("assets/MainLogo.png"), size=(256, 144))
        self.logo_frame = ctk.CTkFrame(self.dashboard_panel, fg_color="transparent")
        self.logo_label = ctk.CTkLabel(self.logo_frame, image=self.logo, fg_color=BUTTON_COLOR1, text="", bg_color=BUTTON_COLOR1)
        self.logo_label.grid(row=0, column=0)
        self.logo_frame.pack()

        # Tabs
        """Creates the tabs(buttons) and packs it in the dashboard panel."""
        self.create_dashboard_buttons()

        # Create the main content panel
        """Creates the frame or the content panel. This frame is a placeholder only and is used as a master of the content frames."""
        self.content_panel = ctk.CTkFrame(self.app, width=768, corner_radius=0, fg_color=BACKGROUND_COLOR, bg_color=BACKGROUND_COLOR)
        self.content_panel.pack(side="left", fill="y", expand=True)

        # Dictionary to hold content frames
        """
        This program uses dictionary as a way to index the content panel.
        Each panel is linked to a tab within this dictionary. 
        """
        self.frames = {}

        # Creates content frames
        self.create_content_frames()

        # Show the default frame
        """The default frame is the one shown upon logging in"""
        self.show_frame("Home")

    def create_dashboard_buttons(self):
        """
        This function creates the buttons on the dashboard panel.
        It uses a list of dictionaries to traverse the configurations of the buttons/tabs.
        And it uses a for loop to pack them into the dashboard panel.
        :return: none
        """
        # Button configurations
        """
        A list of dictionaries to traverse the configurations of the buttons/tabs.
        Each dictionary has the text and command keys as those are the button parameters that differ among the buttons/tabs.
        """
        button_config = [
            {"text": "   HOME", "command": lambda:self.show_frame("Home")},
            {"text": "   STOCK", "command": lambda: self.show_frame("Stock")},
            {"text": "   PRODUCTS", "command": lambda: self.show_frame("Products")},
            {"text": "   CLASSIFICATIONS", "command": lambda: self.show_frame("Classifications")},
            {"text": "   SUPPLIERS", "command": lambda: self.show_frame("Suppliers")},
        ]

        # Button configurations
        """
        This for loop traverses the configurations of the buttons/tabs and uses them to create buttons.
        Each button created is packed into the dashboard panel.
        """
        for config in button_config:
            button = ctk.CTkButton(
                self.dashboard_panel,
                text=config["text"],
                command=config["command"],
                text_color="white",
                font=(LABEL_FONT, 24),
                width=256,
                fg_color=BUTTON_COLOR1,
                anchor="w",
                corner_radius=0,
                hover_color=HOVER_COLOR_1
            )
            button.pack()

        # Logout Button
        """This button is the last button on the dashboard panel. Clicking it destroys the main window."""
        self.log_out_button = ctk.CTkButton(self.dashboard_panel, text="LOG OUT", command=self.log_out, font=(LABEL_FONT, 20), width=200, text_color=BLACK_COLOR, fg_color=BUTTON_COLOR3, hover_color=HOVER_COLOR_3)
        self.log_out_button.pack(side="bottom", pady=24)

    # Closes the Program
    def log_out(self):
        messagebox.showinfo("Logged Out", "You have been logged out.")
        self.app.destroy()

    # Creates Frames to display in the content frame slot
    def create_content_frames(self):
        """Creates the content frames and stores them in a dictionary."""
        # Add frames
        self.frames["Home"] = HomeFrame(self.content_panel, self.userid)
        self.frames["Stock"] = StockFrame(self.content_panel, self.userid)
        self.frames["Products"] = ProductsFrame(self.content_panel, self.userid)
        self.frames["Classifications"] = ClassificationsFrame(self.content_panel, self.userid)
        self.frames["Suppliers"] = SuppliersFrame(self.content_panel, self.userid)

    def show_frame(self, frame_name):
        """Switches the visible content frame."""
        # Clear current content
        for frame in self.frames.values():
            frame.grid_forget()

        # Show the selected frame
        frame = self.frames[frame_name]
        frame.grid(row=0, column=0, sticky="nswe")