import requests
from pprint import pprint
#mainfood = 'beef'
# The function below takes input from the HTML form and sets it to 'mainfoodvalue' variable
def input_mainfood(main_food):
    mainfoodvalue = str(main_food)
    api_response = mealplan_api(mainfoodvalue)
# Below is the function to call the api
def mealplan_api(mainfoodinput):
    mainfood = mainfoodinput
    Mealtype = 'Dinner'
    Cals = '1000-4000'
    Exclude = ' '
    headers = {
        'Accept': 'application/json',
    }
    params = {
        'type': 'public',
        'q': mainfood,
        'app_id': 'a908d81b',
        'app_key': '999c127f15867c0d167bd920f511a436',
        'ingr': '5-15',
        #'health': 'vegetarian',
        'mealType': Mealtype,
        'calories': Cals,
        'imageSize': 'REGULAR',
        'excluded': Exclude,
        'random': 'true',
    }
    # Left the line below as Michael left it, might be important
    #response = requests.get('https://api.edamam.com/api/recipes/v2', params=params, headers=headers)
    response = requests.get('https://api.edamam.com/api/recipes/v2', params=params, headers=headers)
    data = response.json()
    recipe = data.get('hits')[0].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

    recipe = data.get('hits')[1].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

    recipe = data.get('hits')[2].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

    recipe = data.get('hits')[3].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

    recipe = data.get('hits')[4].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

    recipe = data.get('hits')[5].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

    recipe = data.get('hits')[6].get('recipe')
    FoodName = recipe.get('label')
    FoodLink = recipe.get('url')
    pprint(FoodName)
    pprint(FoodLink)

# Input main food and it will work