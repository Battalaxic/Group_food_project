import requests


endpoint = "https://api.edamam.com/api/food-database/v2/parser"
query_text = "chicken"
app_id = "f04b8e34"
food_database_api_key = "d7cb8481b59ac020d0867be9a0af752e"

def call_from_food_database(query="chicken"):
    query = f"{endpoint}?app_id={app_id}&app_key={food_database_api_key}&ingr={query}"
    JSON = requests.get(query).json()
    return JSON

if __name__ == '__main__':
    print(call_from_food_database())