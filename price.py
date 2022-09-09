# Design the price data structure
import requests
from datetime import date
from random import randrange
import json
from pprint import pprint

url = "https://api.edamam.com/api/recipes/v2?type=public&q=chicken%20grilled%20sandwich&app_id=0e0f1be9&app_key=881c76af2388a8ebb52475c2c10d24f5&diet=low-fat&field=label&field=url&field=ingredients"

def ingredient_list_creator(request_url):
    JSON = requests.get(request_url).json()
    ingredients_JSON_list = JSON["hits"][0]["recipe"]["ingredients"]  #This is a list
    ingredient_list = []
    for ingredient_JSON in ingredients_JSON_list:
        #print(ingredient_JSON)
        ingredient_list.append(ingredient_JSON["food"])
    return ingredient_list

def dict_creator(ingredient_list):
    dict = {}
    for ingredient in ingredient_list:
        price_num = randrange(10, 100, 10) / 100
        dict[ingredient] = {f"{date.today()}": price_num}
    return dict

def dict_to_JSON_into_file(dict):             #dict is a python dictionary // Subroutine of subroutine below
    with open("static/ingredient_price.txt", "w") as outfile:
        json.dump(dict, outfile)

def check_file_for_empty_and_append(dict_to_add):       #Only to add to an empty
    empty_flag = False
    with open("static/ingredient_price.txt") as f:
        if f.readline() == '':
            empty_flag = True
    if empty_flag == True:
        dict_to_JSON_into_file(dict_to_add)

def dict_updater(ingredient_list):
    with open("static/ingredient_price.txt") as f:
        for line in f:
            JSON = json.loads(line)

    for ingredient in ingredient_list:
        ingredient_prices = JSON[ingredient]
        price_num = randrange(50, 100, 10) / 100
        ingredient_prices[f"{date.today()}"] = price_num
    return JSON

def ingredient_price_determiner(request_url, date):
    JSON_response = requests.get(request_url).json()
    ingredients_JSON_list = JSON_response["hits"][0]["recipe"]["ingredients"]  # This is a list
    ingredient_list = []
    ingred_qty_list = []
    for ingredient_JSON in ingredients_JSON_list:
        # print(ingredient_JSON)
        ingredient_list.append(ingredient_JSON["food"])
        ingred_qty_list.append(ingredient_JSON["quantity"])
    with open("static/ingredient_price.txt") as f:
        for line in f:
            price_dict = json.loads(line)
    ingred_cost_list = []
    for i in range(len(ingredient_list)):
        ingredient = ingredient_list[i]
        ingred_cost = ingred_qty_list[i] * price_dict[ingredient][date]
        ingred_cost_list.append(ingred_cost)
    return ((ingredient_list, ingred_cost_list))

if __name__ == '__main__':
    #print(check_file_for_empty_and_append())
    curr_date = str(date.today())
    ingred_list = ingredient_list_creator(url)
    dict = dict_creator(ingred_list)
    check_file_for_empty_and_append(dict)
    dict_to_JSON_into_file(dict_updater(ingred_list))
    print(ingredient_price_determiner(url, curr_date))