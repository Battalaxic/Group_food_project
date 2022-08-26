import requests

API_key = "3946116677a6b3799a544432c54e9371db10713a"

def user_initialise_JSON(name, email, query="user_id"):
    user = {"name": name, "email": email}
    response = requests.post(
    "https://api.suggestic.com/users",
    headers={"Authorization": "Token 3946116677a6b3799a544432c54e9371db10713a"},
    data=user)
    return response.json()[query]

def delete_user(user_id):
    headers = {
        'Authorization': f'Token {API_key}',
        'SG-User': user_id,
        'Content-Type': 'application/json',
    }

    data = '{"query":"mutation { deleteMyProfile { success  } }"}'

    response = requests.post('https://production.suggestic.com/graphql', headers=headers, data=data)
    return response.content

def user_id_file_appender(user_id):
    with open("static/user_ids.txt") as f:
        f.append(f"{user_id};")

if __name__ == '__main__':
    print(delete_user("1c8843e5-9c3f-4faf-96b4-837b27d71a2e"))