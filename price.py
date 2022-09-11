# Design the price data structure
import requests
from datetime import date
from random import randrange
import json
import os
from pprint import pprint

EDANAM_APP_ID="0e0f1be9"
EDANAM_API_KEY="881c76af2388a8ebb52475c2c10d24f5"

endpoint = "https://api.edamam.com/api/recipes/v2"
def find_ingredients(recipe_query, fields=[]):     #Jason's function (modified for my purposes)
    path = "?type=public"
    required_query_parameters = f'&q={recipe_query}&app_id={EDANAM_APP_ID}&app_key={EDANAM_API_KEY}'
    optional_query_parameters = ''
    if fields:  #Checks that fields is not an empty list
        for field_item in fields:
            optional_query_parameters += f'&field={field_item}'
    request = f'{endpoint}{path}{required_query_parameters}{optional_query_parameters}'
    return request

def ingredient_list_creator(request_url):
    JSON = requests.get(request_url).json()
    ingredients_JSON_list = JSON["hits"][0]["recipe"]["ingredients"]  #This is a list
    ingredient_list = []
    for ingredient_JSON in ingredients_JSON_list:
        #print(ingredient_JSON)
        ingredient_list.append(ingredient_JSON["food"])
    return ingredient_list

def dict_creator(ingredient_list):
    with open("static/ingredient_price.txt") as f:
        for line in f:
            dict = json.loads(line)
    for ingredient in ingredient_list:
        price_num = randrange(10, 100, 10) / 100
        dict[ingredient] = {f"{date.today()}": price_num}
    return dict

def dict_to_JSON_into_file(dict):             #dict is a python dictionary // Subroutine of subroutine below
    with open("static/ingredient_price.txt", "w") as outfile:
        json.dump(dict, outfile)

def check_file_for_empty_and_append():       #Only to add to an empty
    empty_flag = False
    with open("static/ingredient_price.txt") as f:
        if f.readline() == '':
            empty_flag = True
    if empty_flag == True:
        dict_to_JSON_into_file({})

def dict_updater(ingredient_list):
    with open("static/ingredient_price.txt") as f:
        for line in f:
            JSON = json.loads(line)
    #'''Redo going thru items of the dictionary'''
    for ingredient, prices in JSON.items():
        ingredient_prices = JSON[ingredient]
        price_num = randrange(50, 100, 10) / 100
        ingredient_prices[f"{date.today()}"] = price_num
    return JSON

def ingredient_price_determiner(request_url, date=str(date.today())):
    JSON_response = requests.get(request_url).json()
    ingredients_JSON_list = JSON_response["hits"][0]["recipe"]["ingredients"]  # This is a list
    ingredient_list = []
    ingred_qty_list = []
    measure_type_list = []
    for ingredient_JSON in ingredients_JSON_list:
        # print(ingredient_JSON)
        ingredient_list.append(ingredient_JSON["food"])
        ingred_qty_list.append(ingredient_JSON["quantity"])
        measure_type_list.append(ingredient_JSON["measure"])
    with open("static/ingredient_price.txt") as f:
        for line in f:
            price_dict = json.loads(line)
    ingred_cost_list = []
    for i in range(len(ingredient_list)):
        ingredient = ingredient_list[i]
        ingred_cost = ingred_qty_list[i] * price_dict[ingredient][date]
        ingred_cost_list.append(ingred_cost)
    return ((ingredient_list, ingred_cost_list, measure_type_list, ingred_qty_list))


def complete_price_subroutine(recipe_request):
    check_file_for_empty_and_append()
    url = find_ingredients(recipe_request)
    ingred_list = ingredient_list_creator(url)
    dict1 = dict_creator(ingred_list)
    dict_to_JSON_into_file(dict1)
    dict_to_JSON_into_file(dict_updater(ingred_list))
    return ingredient_price_determiner(url, str(date.today()))

if __name__ == '__main__':
    #print(check_file_for_empty_and_append())
    print(complete_price_subroutine("chicken grilled sandwich"))
    #print(ingredient_price_determiner(url, curr_date))