import ttkbootstrap as ttk


#! LoginScreen 
class LoginScreen(ttk.Frame):
    def __init__(self, loginmaster=None):
        super().__init__(loginmaster, themename="vapor")
        
        self.login_screen = loginmaster
        self.login_screen.title("Initialize User")  # Set the screen name
        self.login_screen.geometry("600x600")    # Set the screen geometry (width x height)
        self.pack()

        #! Fonts Variables
        self.title_font = ("Helvetica", 16)

        #! Create a spacer (separator)
        self.spacer = ttk.Separator(self, orient="horizontal")
        self.spacer.pack(fill="x", pady=10)  # Add padding around the spacer

        #! Create Title Label
        self.login_title_lbl = ttk.Label(self, text="Welcome Petty Fool", font=self.title_font)
        self.login_title_lbl.pack(pady=10)





if __name__ == "__main__":
    root = ttk.Window()
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