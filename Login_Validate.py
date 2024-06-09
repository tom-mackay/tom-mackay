import json
import logging
#& We could move this to a setup config also to mask Whats being imported
from Login_SCYE1 import DictionaryEncryptor

def validate_login_func(self, username_input, password_input):
    
    self.logger = logging.getLogger(__name__)
    
    try:
        logging.info("<LOGIN VALIDATE> Commencing User Login Validation Process")
        #& This will likely be an api call to microsoft power platforms flows
        #! Assuming 'user_data.json' contains JSON data
        try: 
            with open('user_data.json', 'r') as user_data_file: #& Change the name at some point
                user_dict = json.load(user_data_file)
        #? Except and try block to catch any errors that may occur during json and user fetch
        except:
            logging.info("<LOGIN VALIDATE> User Login Process Failed or User Data Not Found")
            return False
            
        #! Encryption Information Required to Encrypt
        salt = b'\x02\xf4\x1b\xdd=\x04\x96j\x12.\x1e\xc5=~\xe6\xb2'
        passphrase = "isnt this cool and fresh"
        encryptor = DictionaryEncryptor(passphrase, salt) #! Initialize encryptor with both passphrase and salt to set the parameters for encryption
        encryption_flag = False
        decrption_flag = False
            
        try:
            #? inserting case for try and except block to catch any errors that may occur during encryption and decryption
            logging.info("<LOGIN VALIDATE> Commencing Encrypt/Decrypt User Process")
            if encryption_flag:
                encrypted_user_data = encryptor.encrypt(user_dict)
                print(encrypted_user_data)
                with open('user_data.json', 'w') as enc_user_data:
                    json.dump(encrypted_user_data, enc_user_data, indent=4)
                print("Encyrption Sucessfull")         
            else:
                decrypted_user_data = encryptor.decrypt(user_dict)
                #print(decrypted_user_data)
                decrption_flag = True
                print("Decryption Successful")
        except:
            logging.info("<LOGIN VALIDATE> The Encryption/Decryption Process Failed you Silly Goose!")
            decrption_flag = False
            print("Encryption/Decryption Process Failed")
            decrption_flag = False
                
        if decrption_flag:
            #! Checks first if username is right - Step 3
            if decrypted_user_data[username_input]:
                user_login_info = decrypted_user_data[username_input]
                #! Then confirms password
                if user_login_info["password"] == password_input:
                    return True
            else:
                return False
        else:
            print("User data decryption failed")
    
    except Exception as e:
        logging.error(f"<LOGIN VALIDATE> Validation Process Failed")
        return False
    