import json
import os
#& We could move this to a setup config also to mask Whats being imported
from Login_UPE1 import UniqueENC1
from Login_UPK import URPK_method
from Login_SCYE1 import UniqueSCYE1

def validate_login_func(username_input, password_input):
    
    enc1 = UniqueENC1()
    
    try:
        #& This will likely be an api call to microsoft power platforms flows
        #! Assuming 'user_data.json' contains JSON data
        with open('user_data.json', 'r') as user_data_file: #& Change the name at some point
            user_dict = json.load(user_data_file)
            
        #! SCYE1 Config Stream
        try:
            #! Collect Required Variables
            with open("scye1_config.json") as scye_config:
                syce_dict = json.load(scye_config)
            enc1_resonator = syce_dict["pc-scye1"]

            #! Pump Stream
            urpk, s_scye1 = URPK_method()
            print(urpk)
            print(s_scye1)
            scye1_required = enc1.decrypt(enc1_resonator, urpk)
            print(scye1_required)
            #! Stream Output
            scye1 = UniqueSCYE1(scye1_required, s_scye1)
            
        except Exception as e:
            print(f"SCYE1 Stream Failed: {e}")
        
        #! ENCRYPTION/DECRYPTION
        try:
            encrypt_stream = False
            if encrypt_stream:
                #stream_check = scye1.derive_key(scye1_required, s_scye1)
                stream_sum = scye1.encrypt(user_dict)
                #print(stream_sum)
                #! Save Encryption
                encrypted_json_data = json.dumps(stream_sum)
                with open('user_data.json', 'w') as encrypted_user_data:
                    encrypted_user_data.write(encrypted_json_data) 
            else:
                print("Passing Encryption")
                stream_result = scye1.decrypt(user_dict)
                #print(stream_result)
                pass
            
        except:
            #! SCYE1 Error
            print('SCYE1 Failed: Security Notice Filed')
            #& This spot here has quite of a lot of intersting possibility as a deterrent
            return False

        #! USERNAME CHECK
        if user_dict[username_input]:
            user_login_info = user_dict[username_input]
            
            #! Then confirms password
            if user_login_info["password"] == password_input:
                return True
        else:
            return False
    
    except:
        return False
    