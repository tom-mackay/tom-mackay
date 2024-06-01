import json

def validate_login_func(username_input, password_input):
    
    # Assuming 'user_data.json' contains JSON data
    with open('user_data.json', 'r') as user_data_file:
        user_dict = json.load(user_data_file)

    if user_dict[username_input]:
        user_login_info = user_dict[username_input]
        if user_login_info["password"] == password_input:
            return True
    else:
        return False