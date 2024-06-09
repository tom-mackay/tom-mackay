import tkinter as tk
import ttkbootstrap as ttk
import os
import logging
from datetime import datetime
from Login_Validate import validate_login_func
    
#^ START READING HERE: 
#! From James
#^ If you're not seeing color when reading this, install the vscode extension colorful comments.
    
#^ This color is for general discussion in the code, like how devs will user specific colors to annotate their code.
#^ David if you want to use this color we can change it also.
#! James
#? Tamokai
#*  David - #^Choose a color (I'm guessing youd want green) - you NEED the vscode extensions "colorful comments"

#& This color is used to discuss possible development changes: Speicifically, this color will be used to start a development thread. 
#& For example, I think we setup an automation that creates a thread on slack with the #& tag.This will make automated checks possible later.
#& David if you want this color we can change it also.

#^ Background Project - Ai Documentation Generation
#^ We are going to be using docstrings and black formatting based on the standard documentation templates
#^ to train an LLM to generate business documentation. This can be used to do validation and if we get a good model,
#^ and learn to review the output, we could apply to be a software validation company. 

#^ Unfortunately the google dev competition requires the app to be in a web/android based application. I think we keep
#^ this python project aimed at software (SW) validation. In the meantime there is about 2 and a bit months for the competition.
#^ Im going to start learning Android studio for the dev comp, I encourage you do also.

#^ Lets continue discussion like this in threads commenting downwards from here: (Continue to write in your color below, will keep yellow for breakdowns like this)
# From 
    
    
    
    
    
    
    
#^ Code Start!
    
class LoginScreen(ttk.Frame):
    #! Parent __Init__, Runs First (initializes core functions)
    def __init__(self, master=None): 
        
        #! ^ Initializes First (Functions/CLasses/Objects can be loaded here)
        
        #! CHILD INIT STARTS HERE
        super().__init__(master)
        #! This is a child ("super()."") __init__() (instance and is run AFTER __init__), it can allow us to run 
        
        #! setup functions in an order in try loops to catch and document errors at specific stages in the app.
        #! Initializing Logging
        self.initialize_Logging()
        #! Launch Login GUI
        self.initializeUI(master)
        
        
        
        
        
        
        
        
        
    #! PARENT INIT STARTS HERE - Notice how these functions are aligned with the parent __init__ class***
    def initialize_Logging(self):
        #! Try Loop to Attempt Logging       
        try:
            #! Generate the timestamp
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            #! Get Relative System Path
            self.relative_path = os.path.dirname(os.path.abspath(__file__))
            logs_path = os.path.join(self.relative_path, "system_logs")
            #print(self.relative_path)
            #! Log Filepath Creation
            log_filename = f"system_log_file_{timestamp}.log"
            self.full_log_file_path = os.path.join(logs_path, log_filename)
            print(self.full_log_file_path)
            
            if not os.path.exists(logs_path):
                print("No Log Directory Exists -> Creating Log Directory")  #& Make Logging Later
                os.makedirs(logs_path)
                print("Directory Created -> Initializing Log")
            else:
                print("Log Directory Exists -> Initializing Log")
                
            #! Configure logging
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                handlers=[
                                    logging.FileHandler(self.full_log_file_path),
                                    logging.StreamHandler()
                                ])
            # Create a logger instance
            self.logger = logging.getLogger(__name__)
            logging.info("<LOGIN MAIN> Log Initialized Successfully")
            return True
        
        except Exception as e:
            raise ValueError(f"Log Initialization Failed: {e}")
                       
         
         
         
    #! Launch GUI                                      
    def initializeUI(self, master):
        logging.info("<LOGIN MAIN> Starting Brisbane Columbia GUI")
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
        self.spacer4 = ttk.Label(self.main_login_screen, text="")
        self.spacer4.pack()

        #! Frame for Buttons
        self.login_buttons_frame = ttk.Frame(self.main_login_screen)
        self.login_buttons_frame.pack(anchor=tk.CENTER)
        #! Login Button
        self.login_button = ttk.Button(self.login_buttons_frame, text="Login", command=self.login_action, takefocus=False, style='Primary.TButton')
        self.login_button.grid(padx=20, row=0, column=1)
        #! Info Button
        self.logininfo_button = ttk.Button(self.login_buttons_frame, text="Info", command=self.info_action, takefocus=False, style='Secondary.TButton')
        self.logininfo_button.grid(padx=20, row=0, column=0)

        # Spacer
        self.spacer5 = ttk.Label(self.main_login_screen, text="")
        self.spacer5.pack()

        #? Frame for Signup Buttons 
        self.signup_button_frame = ttk.Frame(self.main_login_screen)
        self.signup_button_frame.pack(anchor="se")          #? Aight so turns out this anchor uses cardinal directions fyi 
        logging.info("<LOGIN MAIN> All Widgets Loaded Successfully")



            
             
             
             
             
             
    #! Button Functions Listed Below - Alignd with the parent __init__ instance 
    #! Question Time: Because it's aligned with the parent __init, when is this function initialized? (first/second)?   
             
    def login_action(self):
        
        self.user_input_value = self.username_input.get()
        #print(self.user_input_value)
        self.password_input_value = self.password_input.get()
        #print(self.password_input_value)
        validation_status = validate_login_func(self, self.user_input_value, self.password_input_value)
        #print(login_validation_status)
        
        if validation_status:
            print("Login Successful")
            #! Start the program
        else:
            print("Login Failed, Check Credentials")

    def info_action(self):
        # Define the action to be taken when the info button is clicked
        pass









#! Main Loop Master for Program - This will be the executable
if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("vapor")  #! Set the theme to "vapor" - We selected from documentation on the web and using this theme allows us to recolor and distribute the SW very quickly.
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