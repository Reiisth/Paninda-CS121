import customtkinter as ctk
from utils.constants import *

"""
This file contains no class. It only contains functions that are called most often. 
More specifically, these are widget related functions that are used in the GUI.
"""

def create_label(parent, text, font, **kwargs):
    return ctk.CTkLabel(parent, text=text, font=font, bg_color=BACKGROUND_COLOR, fg_color=BACKGROUND_COLOR, **kwargs)

def create_sized_frame (parent, width, bg_color=BACKGROUND_COLOR, **kwargs):
    return ctk.CTkFrame(parent, width=width, bg_color=bg_color, fg_color=bg_color, **kwargs)

def create_frame(parent, bg_color=BACKGROUND_COLOR, **kwargs):
    return ctk.CTkFrame(parent, fg_color=bg_color,bg_color=bg_color, **kwargs)

def create_button1(parent, text, font, command, height, width, color=BUTTON_COLOR1, bg_color=BACKGROUND_COLOR,**kwargs):
    return ctk.CTkButton(parent, text=text, font=font,  command=command, height=height, width=width, text_color="white", fg_color= color, bg_color=bg_color,hover_color=HOVER_COLOR_1, corner_radius=100, **kwargs)

def create_button2(parent, text, font, command, height, width, corner_radius=50, color=BUTTON_COLOR2, bg_color=BACKGROUND_COLOR,**kwargs):
    return ctk.CTkButton(parent, text=text, font=font, command=command, height=height, width=width, text_color="white",fg_color=color, bg_color=bg_color, hover_color=HOVER_COLOR_2, corner_radius=corner_radius, **kwargs)

def create_button3(parent, text, font, command, height, width, corner_radius=50, color=BUTTON_COLOR3, bg_color=BACKGROUND_COLOR,**kwargs):
    return ctk.CTkButton(parent, text=text, font=font, command=command, height=height, width=width,text_color="white", fg_color=color, bg_color=bg_color, hover_color=HOVER_COLOR_3,corner_radius=corner_radius, **kwargs)

def create_entry_usn(parent, font, border_width,  width, bg_color=BACKGROUND_COLOR, **kwargs):
    return ctk.CTkEntry(parent,
                        font=font,
                        border_width=border_width,
                        width=width,
                        placeholder_text="ex: AlingNena",
                        placeholder_text_color="grey",
                        bg_color=bg_color,
                        fg_color="white",
                        corner_radius=10,
                        border_color=BUTTON_COLOR3,
                        **kwargs)

def create_entry_pwd(parent, font, border_width,  width, bg_color=BACKGROUND_COLOR, **kwargs):
    return ctk.CTkEntry(parent,
                        font=font,
                        border_width=border_width,
                        width=width,
                        bg_color=bg_color,
                        fg_color="white",
                        corner_radius=10,
                        show="*",
                        border_color=BUTTON_COLOR3,
                        **kwargs)

def entry_label(parent, text):
    return ctk.CTkLabel(parent, text=text, font=(LABEL_BOLD, 12), bg_color="transparent")

def entry_default(parent, width, p_holder):
    return ctk.CTkEntry(parent, width=width, placeholder_text=p_holder, placeholder_text_color="grey", border_color=BACKGROUND_COLOR, fg_color="white",font=(LABEL_REGULAR,13))

def button_default(parent, text, command, width=100, font=(LABEL_FONT, 16), text_color="white", corner_radius=100, bg_color="transparent", fg_color=BUTTON_COLOR1, **kwargs):
    return ctk.CTkButton(parent,
                         text=text,
                         command=command,
                         width=width,
                         font=font,
                         text_color=text_color,
                         corner_radius=corner_radius,
                         bg_color=bg_color,
                         hover_color=HOVER_COLOR_1,
                         fg_color=fg_color,
                         **kwargs)

def big_label(parent, text):
    return ctk.CTkLabel(parent, text=text, font=(LABEL_FONT, 40), text_color=BLACK_COLOR, bg_color="transparent")

def big_number(parent, text):
    return ctk.CTkLabel(parent, text=text, font=(LABEL_BOLD, 36), text_color=BUTTON_COLOR1, fg_color="transparent", bg_color="transparent")
