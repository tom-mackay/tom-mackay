import json
import os
#& We could move this to a setup config also to mask Whats being imported
# from Login_UPE1 import UniqueENC1
# from Login_UPK import URPK_method
from Login_SCYE1 import UniqueSCYE1

def validate_login_func(username_input, password_input):
    
    try:
        #& This will likely be an api call to microsoft power platforms flows
        #! Assuming 'user_data.json' contains JSON data
        with open('user_data.json', 'r') as user_data_file: #& Change the name at some point
            user_dict = json.load(user_data_file)
            
        #! SCYE1 Config Stream - Collection of Variables First
        try:
            #! Collect Required Variables
            with open("scye1_config.json") as scye_config:
                syce_dict = json.load(scye_config)
            enc1_resonator = syce_dict["pc-scye1"]
        except:
            print("SCYE1 Variables Failed to Collect")
            return False

        #! ENCRYPTION/DECRYPTION - Step 2
        try:
            #! Encryption of Data
            None
            
        except:
            #! SCYE1 Error
            print('SCYE1 Failed: Security Notice Filed')
            #& This spot here has quite of a lot of intersting possibility as a deterrent
            return False # IGNORE UNTIL HERE

        #! Checks first if username is right - Step 3
        if user_dict[username_input]:
            user_login_info = user_dict[username_input]
            
            #! Then confirms password
            if user_login_info["password"] == password_input:
                return True
        else:
            return False
    
    except:
        return False
    