import tkinter as tk
import ttkbootstrap as ttk

class LoginScreen(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        #! Screen Setup
        self.main_login_screen = master
        self.main_login_screen.title("Initialize User")
        self.main_login_screen.geometry("600x600")
        self.pack()

        #! Fonts
        self.title_font = ("Helvetica", 16)
    

        
        
        # Spacer
        self.spacer = ttk.Separator(self, orient="horizontal")
        self.spacer.pack(fill="x", pady=10)

        #! Login Title Label
        self.login_title_lbl = ttk.Label(self, text="Welcome Petty Fool", font=self.title_font)
        self.login_title_lbl.pack(pady=10)
        
        # Spacer
        self.spacer2 = ttk.Separator(self, orient="horizontal")
        self.spacer2.pack(fill="x", pady=10)
        
        #! Login Button
        self.login_button = ttk.Button(self, text="Login", command=self.login_action, takefocus=False, style='Primary.TButton')
        self.login_button.pack(side="right", pady=10)
        
        #! Info Button
        self.logininfo_button = ttk.Button(self, text="Info", command=self.info_action, takefocus=False, style='Secondary.TButton')
        self.logininfo_button.pack(side="left", padx=10, pady=10)

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
    app.mainloop()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def on_button_click():
#     selected_items = listbox.curselection()
#     selected_texts = [listbox.get(i) for i in selected_items]
#     print("Selected items:", selected_texts)

#     # Create and pack an entry (text input)
#     entry = ttk.Entry(root, font=("Helvetica", 16))
#     entry.pack(pady=10)

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