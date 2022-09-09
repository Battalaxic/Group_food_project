import hashlib
import os
import json
import base64

users = {} # A simple demo storage

# Add a user
username = 'Brent' # The users username
password = 'mypassword' # The users password

salt = os.urandom(32) # A new salt for this user
key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
salt = base64.b64encode(salt).decode('ascii')
key = base64.b64encode(key).decode('ascii')
users[username] = { # Store the salt and key
    'salt': salt,
    'key': key
}

# Verification attempt 1 (incorrect password)
username = 'Brent'
password = 'notmypassword'

salt = base64.b64decode(users[username]['salt']) # Get the salt
key = users[username]['key'] # Get the correct key
new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

print(key == new_key, key, "==", new_key)

print(users)

with open("static/user_ids.txt", "w") as outfile:
    json.dump(users, outfile)