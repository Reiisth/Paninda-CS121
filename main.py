import customtkinter as ctk
from login_window import LoginWindow
ctk.set_appearance_mode("light")

if __name__ == "__main__":
    login_app = ctk.CTk()
    login_app.iconbitmap("assets/icon.ico.ico")
    LoginWindow = LoginWindow(login_app)
    login_app.mainloop()