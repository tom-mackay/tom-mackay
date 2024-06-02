import json


def validate_login_func(username_input, password_input):
    
    try:
        
        #& This will likely be an api call to microsoft power platforms flows
        #! Assuming 'user_data.json' contains JSON data
        with open('user_data.json', 'r') as user_data_file: #& Change the name at some point
            user_dict = json.load(user_data_file)











        #! ENCRYPTION/DECRYPTION
        try:
            #! Encryption of Data
            None
        except:
            #! SCYE1 Error
            print('SCYE1 Failed: Security Notice Filed')
            #& This spot here has quite of a lot of intersting possibility as a deterrent
            return False

        #! Checks first if username is right
        if user_dict[username_input]:
            user_login_info = user_dict[username_input]
            #! Then confirms password
            if user_login_info["password"] == password_input:
                return True
        else:
            return False
    
    except:
        return False
    