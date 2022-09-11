import hashlib
import os
import json
import base64

'''users = {} # A simple demo storage'''

def add_empty_dict_if_empty():
    empty_flag = False
    with open("static/user_ids.txt") as f:
        for line in f:
            if line == '':
                empty_flag = True
    if empty_flag == True:
        with open("static/user_ids.txt", "w") as f:
            f.write('{}')

def update_user_ids_file(users):
    with open("static/user_ids.txt", "w") as outfile:
        json.dump(users, outfile)

def add_user(username, password):
    with open("static/user_ids.txt") as f:
        for line in f:
            users = json.loads(line)
    salt = os.urandom(32) # A new salt for this user
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    salt = base64.b64encode(salt).decode('ascii')
    key = base64.b64encode(key).decode('ascii')
    users[username] = { # Store the salt and key
        'salt': salt,
        'key': key
    }
    update_user_ids_file(users)
    return users

def login_attempt(username, entered_password):
    with open("static/user_ids.txt") as f:
        for line in f:
            users = json.loads(line)
    if users.get(username) != None:
        salt = base64.b64decode(users[username]['salt']) # Get the salt
        key = users[username]['key'] # Get the correct key
        new_key = hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), salt, 100000)
        new_key = base64.b64encode(new_key).decode('ascii')
        if key == new_key:
            return True
        return False
    else:
        return None

def delete_user(username, password):
    login_status = login_attempt(username, password)
    if login_status == True:
        with open("static/user_ids.txt") as f:
            for line in f:
                users = json.loads(line)
        del users[username]
        update_user_ids_file(users)

def change_password(username, password, new_password):
    if login_attempt(username, password) == True:
        add_user(username, new_password)
        return True
    else:
        return False


if __name__ == '__main__':
    add_empty_dict_if_empty()
    add_user("Test", "blood")
    print(login_attempt("Test", "bloo"))