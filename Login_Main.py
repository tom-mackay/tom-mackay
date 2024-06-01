import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# def create_gui():
#     # Create the main application window
#     root = ttk.Window(themename="vapor")
#     root.title("TTKBootstrap Example")

#     # Create and pack a label
#     label = ttk.Label(root, text="This is a Label", font=("Helvetica", 16))
#     label.pack(pady=10)

#     # Create and pack an entry (text input)
#     entry = ttk.Entry(root, font=("Helvetica", 16))
#     entry.pack(pady=10)

#     # Create and pack a button
#     button = ttk.Button(root, text="Click Me", command=on_button_click, bootstyle=PRIMARY)
#     button.pack(pady=10)

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

#     # Start the application
#     root.mainloop()

# def on_button_click():
#     selected_items = listbox.curselection()
#     selected_texts = [listbox.get(i) for i in selected_items]
#     print("Selected items:", selected_texts)

# if __name__ == "__main__":
#     create_gui()