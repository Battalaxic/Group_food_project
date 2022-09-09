import os
import hashlib
import json

salt = os.urandom(32)

def dict_into_user_ids_txt(dict1={}):        #dict is a python dictionary // often used in tandem with user_ids_dict_updater()
    with open("static/user_ids.txt", "w") as outfile:
        json.dump(dict1, outfile)

def hash_plain_text_password(username, password):
    """Following tutorial from https://nitratine.net/blog/post/how-to-hash-passwords-in-python/"""

    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    storage = salt + key
    salt_from_storage = storage[:32]  # 32 is the length of the salt
    key_from_storage = storage[32:]
    return ((username, storage))

def user_ids_dict_updater(username, hashed_password):    #hased_password is storage (64)
    with open("static/user_ids.txt") as f:
        for line in f:
            JSON = json.loads(line)

    JSON[username] = str(hashed_password)
    return JSON

def check_file_for_empty_and_append(dict_to_add=''):       #Only to add to an empty
    empty_flag = False
    with open("static/user_ids.txt") as f:
        if f.readline() == '':
            empty_flag = True
    if empty_flag == True:
        dict_into_user_ids_txt()

def password_hash_comparer(username, entered_password):
    with open("static/user_ids.txt") as f:
        for line in f:
            dict1 = json.loads(line)
            print(dict1)
    username_storage = dict1[username]
    key = username_storage[32:]
    new_key = str(hashlib.pbkdf2_hmac('sha256', entered_password.encode('utf-8'), salt, 100000))
    print(salt)
    print(new_key, key)
    if key == new_key:
        return True
    else:
        return False


if __name__ == '__main__':
    #bundle = hash_plain_text_password("Tester", "password123")
    #check_file_for_empty_and_append()
    #dictionary = user_ids_dict_updater(bundle[0], bundle[1])
    #dict_into_user_ids_txt(dictionary)
    password_hash_comparer("Tester", "password123")
