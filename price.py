# Design the price data structure
import requests
from datetime import date
from random import randrange
from pprint import pprint

url = "https://api.edamam.com/api/recipes/v2?type=public&q=chicken%20grilled%20sandwich&app_id=0e0f1be9&app_key=881c76af2388a8ebb52475c2c10d24f5&diet=low-fat&field=label&field=url&field=ingredients"

def check_file_for_empty_and_append(dict_to_add='testing'):       #Only to add to an empty
    empty_flag = False
    with open("static/ingredient_price.txt") as f:
        if f.readline() == '':
            empty_flag = True
    if empty_flag == True:
        with open("static/ingredient_price.txt", "w") as empty_f:
            empty_f.write(dict_to_add)

def ingredient_list_creator(request_url):
    JSON = requests.get(request_url).json()
    ingredients_JSON_list = JSON["hits"][0]["recipe"]["ingredients"]  #This is a list
    ingredient_list = []
    for ingredient_JSON in ingredients_JSON_list:
        #print(ingredient_JSON)
        ingredient_list.append(ingredient_JSON["food"])
    return ingredient_list

def dict_creator(ingredient_list):
    result_string = ''
    ingredient_keys = ''
    for ingredient in ingredient_list:
        price_num = randrange(10, 100, 10)
        ingredient_keys += f'"{ingredient}": ' + '{' + f"{date.today()}: {price_num / 100}" + '}, '
    result_string += '{' + ingredient_keys + "}"
    #d = {}
    #for ingredient in ingredient_list:
    return result_string

#def dict_to_JSON(string):


if __name__ == '__main__':
    #print(check_file_for_empty_and_append())
    ingred_list = ingredient_list_creator(url)
    print(dict_creator(ingred_list))