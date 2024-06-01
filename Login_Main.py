import tkinter as tk
import ttkbootstrap as ttk
import os
import logging
from Login_Validate import validate_login_func

class LoginScreen(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.relative_path = os.path.abspath(__file__)
        print(self.relative_path)
        
        #! Screen Setup
        self.main_login_screen = master
        self.main_login_screen.title("Initialize User")
        
        #! Get screen width and height
        screen_width = self.main_login_screen.winfo_screenwidth()
        screen_height = self.main_login_screen.winfo_screenheight()
        #! Calculate x and y positions for the window to be centered
        x = (screen_width - 600) // 2  # 600 is the window width
        y = (screen_height - 230) // 2  # 230 is the window height
        #! Set the window position
        #self.main_login_screen.geometry(f"600x230+{x}+{y}")
        self.main_login_screen.geometry("600x230") #^ WidthxHeight
        self.main_login_screen.resizable(False, False) 
        self.pack()
        #self.grid(row=0, column=0) #& Review another time
        
        #! Fonts
        self.title_font = ("Helvetica", 16)
        self.input_font = ("Helvetica", 12)
 
        #! Create a Login Canvas widget
        self.login_canvas = tk.Canvas(self)
        self.login_canvas.pack(fill=tk.BOTH, expand=True)
        
        # Spacer
        self.spacer = ttk.Label(self.login_canvas, text="")
        self.spacer.pack()

        #! Login Title Label
        self.login_title_lbl = ttk.Label(self.login_canvas, text="Welcome PETTY Fool", font=self.title_font)
        self.login_title_lbl.pack(anchor=tk.CENTER)
        
        # Spacer
        self.spacer2 = ttk.Label(self.login_canvas, text="")
        self.spacer2.pack()
        
        #! Main Login Frame
        self.login_frame = ttk.Frame(self.login_canvas)
        self.login_frame.pack(anchor=tk.CENTER)
        
        #! Username Input and Label
        self.username_lbl = ttk.Label(self.login_frame, text="Username:", font=self.input_font)
        self.username_lbl.grid(padx=5, row=0, column=0)
        self.username_input = ttk.Entry(self.login_frame, font=self.input_font)
        self.username_input.grid(padx=5, row=0, column=1)
        # Spacer
        self.spacer3 = ttk.Label(self.login_frame, text="")
        self.spacer3.grid(row=1, column=0)
        #! Password Input and Label
        self.password_lbl = ttk.Label(self.login_frame, text="Password:", font=self.input_font)
        self.password_lbl.grid(padx=5, row=2, column=0)
        self.password_input = ttk.Entry(self.login_frame, font=self.input_font, show="*")
        self.password_input.grid(padx=5, row=2, column=1)
        
        # Spacer
        self.spacer4 = ttk.Label(self.login_canvas, text="")
        self.spacer4.pack()
        
        #! Frame for Buttons
        self.login_buttons_frame = ttk.Frame(self.login_canvas)
        self.login_buttons_frame.pack(anchor=tk.CENTER)
        #! Login Button
        self.login_button = ttk.Button(self.login_buttons_frame, text="Login", command=self.login_action, takefocus=False, style='Primary.TButton')
        self.login_button.grid(padx=20, row=0, column=1)
        #! Info Button
        self.logininfo_button = ttk.Button(self.login_buttons_frame, text="Info", command=self.info_action, takefocus=False, style='Secondary.TButton')
        self.logininfo_button.grid(padx=20, row=0, column=0)

        #& Signup Button
        #& self.signup_button = ttk.Button(self.login_canvas, text="Sign Up", takefocus=True, style='info.Link.TButton')
             
             
             
             
             
             
             
             
             
    def login_action(self):
        
        self.user_input_value = self.username_input.get()
        #print(self.user_input_value)
        self.password_input_value = self.password_input.get()
        #print(self.password_input_value)
        validation_status = validate_login_func(self.user_input_value, self.password_input_value)
        #print(login_validation_status)
        
        if validation_status:
            print("Logging Successful")
        else:
            print("Login Failed, Check Credentials")


    def info_action(self):
        # Define the action to be taken when the info button is clicked
        pass







if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("vapor")  # Set the theme to "vapor"    
    app = LoginScreen(master=root)
    app.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    

# Listbox Details
#     # Create and pack a listbox with a scrollbar
#     listbox_frame = ttk.Frame(root)
#     listbox_frame.pack(pady=10)
#     listbox_scrollbar = ttk.Scrollbar(listbox_frame)
#     listbox_scrollbar.pack(side=RIGHT, fill=Y)
#     listbox = ttk.Listbox(listbox_frame, yscrollcommand=listbox_scrollbar.set, font=("Helvetica", 16))
#     listbox.pack()
#     listbox_scrollbar.config(command=listbox.yview)
#     # Add items to the listbox
#     for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
#         listbox.insert(END, item)