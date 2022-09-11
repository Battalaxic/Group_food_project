import requests
import os
from pprint import pprint

EDANAM_APP_ID="0e0f1be9"
EDANAM_API_KEY="881c76af2388a8ebb52475c2c10d24f5"

'''This function may not be needed'''
'''This function uses GraphQL, an API query language to query'''
def call_suggestic():
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://www.graphqlbin.com',
        'Authorization': f'Token {os.environ["SUGGESTIC_API_KEY"]}',
    }

    json_data = {'query':
    '''
    {
        restaurant(id: "UmVzdGF1cmFudDo1MzNhMTRjMC0zNmQ2LTQ4NWEtYmJhNC1mOTJmOTc5MWFjZTY=") {
            name
            databaseId
            country
            address1
        }
    }
    '''
    }
    response = requests.post('https://production.suggestic.com/graphql', headers=headers, json=json_data)
    data = response.json()
    # pprint(data)
    return data

# call_suggestic()


'''E.g. https://api.edamam.com/api/recipes/v2?type=public&q=chicken&app_id=0e0f1be9&app_key=881c76af2388a8ebb52475c2c10d24f5&diet=balanced&cuisineType=Asian'''
'''E.g. https://api.edamam.com/api/recipes/v2?type=public&q=chicken%20grilled%20sandwich&app_id=0e0f1be9&app_key=881c76af2388a8ebb52475c2c10d24f5&diet=low-fat&field=label&field=url&field=ingredients'''

endpoint = "https://api.edamam.com/api/recipes/v2"
path = "?type=public"


def call_recipe_search(recipe_query, diet_query='', health_query='', cuisine_type_query='', meal_type_query='', dish_type_query='', fields=[], calories='', protein='', random='true'):
    required_query_parameters = f'&q={recipe_query}&app_id={EDANAM_APP_ID}&app_key={EDANAM_API_KEY}'
    optional_parameters_dictionary = {
        'diet': diet_query,
        'health': health_query,
        'cuisineType': cuisine_type_query,
        'mealType': meal_type_query,
        'dishType': dish_type_query,
        'calories': calories,
        'nutrients%5BPROCNT%5D': protein,
        'random': random
    }
    optional_query_parameters = ''
    for parameter in optional_parameters_dictionary:
        if optional_parameters_dictionary[parameter] != '':
            optional_query_parameters += f'&{parameter}={optional_parameters_dictionary[parameter]}'
    if fields:  #Checks that fields is not an empty list
        for field_item in fields:
            optional_query_parameters += f'&field={field_item}'
    request = f'{endpoint}{path}{required_query_parameters}{optional_query_parameters}'
    response = requests.get(request)
    recipe_search = response.json()
    print(f'REQUEST IS {request}')
    # pprint(recipe_search)
    return recipe_search


def search_recipe_organise(recipe_search):
    labels = []
    label_set = []
    thumbnails = []
    thumbnail_set = []
    recipe_ids = []
    recipe_id_set = []
    items = {}
    counter = 0
    for recipe in recipe_search['hits']:
        counter += 1
        if counter % 4 != 0:
            label_set.append(recipe['recipe']['label'])
            thumbnail_set.append(recipe['recipe']['images']['SMALL']['url'])
            recipe_uri = (recipe['recipe']['uri']).split('#')  # All URIs seperate source and ID with a '#'
            recipe_id = recipe_uri[1]  # .split('#') creates a list, since only one '#' in the string, ID indexed at 1
            recipe_id_set.append(recipe_id)
        else:
            labels.append(label_set)
            thumbnails.append(thumbnail_set)
            recipe_ids.append(recipe_id_set)
            label_set = []
            thumbnail_set = []
            recipe_id_set = []
    items['labels'] = labels
    items['thumbnails'] = thumbnails
    items['recipe_ids'] = recipe_ids
    print(f'LABELS ARE {labels}')
    return items


'''E.g. https://api.edamam.com/api/recipes/v2/recipe_871096b92b8f0d49674a4d8c1935f9d0?type=public&app_id=0e0f1be9&app_key=881c76af2388a8ebb52475c2c10d24f5'''


def search_specific_recipe(recipe_id):
    required_query_parameters = f'&app_id={EDANAM_APP_ID}&app_key={EDANAM_API_KEY}'
    request = f'{endpoint}/{recipe_id}{path}{required_query_parameters}'
    print(f'SPECIFIC REQUEST IS {request}')
    response = requests.get(request)
    specific_recipe = response.json()
    return specific_recipe


def specific_recipe_organise(recipe_data):
    label = recipe_data['recipe']['label']
    image = recipe_data['recipe']['image']
    health_labels = recipe_data['recipe']['healthLabels']
    diet_labels = recipe_data['recipe']['dietLabels']
    cautions = recipe_data['recipe']['cautions']
    ingredients_list = recipe_data['recipe']['ingredientLines']
    ingredients_images = [] # TODO: show on hover
    for ingredient in recipe_data['recipe']['ingredients']:
        ingredients_images.append(ingredient['image'])
    organised_recipe_data = {
        'label': label,
        'image': image,
        'health_labels': health_labels,
        'diet_labels': diet_labels,
        'cautions': cautions,
        'ingredients_list': ingredients_list,
        'ingredients_images': ingredients_images}
    return organised_recipe_data


""" Function for Eric
endpoint = "https://api.edamam.com/api/recipes/v2"
def find_ingredients(recipe_query, fields=[]):
    path = "?type=public"
    required_query_parameters = f'&q={recipe_query}&app_id={os.environ["EDAMAM_APP_ID"]}&app_key={os.environ["EDAMAM_API_KEY"]}'
    optional_query_parameters = ''
    if fields:  #Checks that fields is not an empty list
        for field_item in fields:
            optional_query_parameters += f'&field={field_item}'
    request = f'{endpoint}{path}{required_query_parameters}{optional_query_parameters}'
    response = requests.get(request)
    ingredient_search = response.json()
    print(f'REQUEST IS {request}')
    pprint(ingredient_search)
    return ingredient_search
"""
"""
Example Query 1 - User Query:
recipe_query = 'chicken'
diet_query = 'balanced'
cuisine_type_query = 'Asian'
fields = [label, url, ingredients]  #fields should not be avaliable for users

call_recipe_search(recipe_query, diet_query=diet_query, cuisine_type_query=cuisine_type_query, fields)

Example Query 2 - Ingredient Query (Michael):
recipe_query = 'chicken grilled sandwich'
fields = ['label', 'url', 'ingredients']  #fields should not be avaliable for users

find_ingredients(recipe_query, fields)

Example Query 3 - Random Calorie & Protein Filtering (Michael)
recipe_query = 'chicken'
calories = '100-2000'
protein = '40-80'
random = 'true'
call_recipe_search(recipe_query, calories=calories, protein=protein, random=random)
"""
