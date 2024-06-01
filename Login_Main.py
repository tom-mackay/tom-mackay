import tkinter as tk
import ttkbootstrap as ttk
import logging

class LoginScreen(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        #! Screen Setup
        self.main_login_screen = master
        self.main_login_screen.title("Initialize User")
        self.main_login_screen.geometry("600x230") #^ HxW

        #! Login Screen Frame
        self.login_screen_frame = ttk.Frame(self, relief="solid", borderwidth=2)
        self.login_screen_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        #! Fonts
        self.title_font = ("Helvetica", 16)
        self.input_font = ("Helvetica", 12)
    
        # Spacer
        self.spacer = ttk.Label(self, text="")
        self.spacer.grid(row=0, column=0)

        #! Login Title Label
        self.login_title_lbl = ttk.Label(self, text="Welcome PETTY Fool", font=self.title_font)
        self.login_title_lbl.grid(row=1, column=0)
        
        # Spacer
        self.spacer2 = ttk.Label(self, text="")
        self.spacer2.grid(row=2, column=0)
        
        #! Main Login Frame
        self.login_frame = self.login_frame = ttk.Frame(self)
        self.login_frame.grid(row=3, column=0)
        
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
        self.password_input = ttk.Entry(self.login_frame, font=self.input_font)
        self.password_input.grid(padx=5, row=2, column=1)
        
        # Spacer
        self.spacer4 = ttk.Label(self, text="")
        self.spacer4.grid(row=4, column=0)
        
        #! Frame for Buttons
        self.login_buttons_frame = ttk.Frame(self)
        self.login_buttons_frame.grid(row=5, column=0)
        #! Login Button
        self.login_button = ttk.Button(self.login_buttons_frame, text="Login", command=self.login_action, takefocus=False, style='Primary.TButton')
        self.login_button.grid(padx=20, row=0, column=0)
        #! Info Button
        self.logininfo_button = ttk.Button(self.login_buttons_frame, text="Info", command=self.info_action, takefocus=False, style='Secondary.TButton')
        self.logininfo_button.grid(padx=20, row=0, column=2)
        
        # # Spacer
        # self.spacer5 = ttk.Label(self, text="")
        # self.spacer5.grid(row=7, column=4)











    def login_action(self):
        # Define the action to be taken when the login button is clicked
        pass

    def info_action(self):
        # Define the action to be taken when the info button is clicked
        pass

if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("vapor")  # Set the theme to "vapor"
    
    app = LoginScreen(master=root)
    app.grid(row=0, column=0, sticky="nsew")  # Grid the main application frame
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    app.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def on_button_click():
#     selected_items = listbox.curselection()
#     selected_texts = [listbox.get(i) for i in selected_items]
#     print("Selected items:", selected_texts)



#     # Create and pack a button
#     button = ttk.Button(root, text="Click Me", command=on_button_click, bootstyle=PRIMARY)
#     button.pack(pady=10)









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