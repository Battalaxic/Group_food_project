import price
from datetime import date

def total_cost(cost_list):
    final_cost = 0
    for cost in cost_list:
        final_cost += cost
    return final_cost

def total_ingredient_determiner(list_of_recipes):
    # all_ingreds = []
    total_ingred_dict = {}  #the final amount of ingredients
    ingred_measure_dict = {}
    ingred_price_dict = {}
    for recipe in list_of_recipes:
        recipe_url = price.find_ingredients(recipe)
        price.complete_price_subroutine(recipe)
        ingreds, costs, measures, qty = price.ingredient_price_determiner(recipe_url, str(date.today()))
        #print(ingreds, costs, measures, qty)
        for i in range(len(ingreds)):
            ingredient = str(ingreds[i]).lower()
            total_ingred_dict[ingredient] = total_ingred_dict.get(ingredient, 0) + qty[i]
            ingred_measure_dict[ingredient] = measures[i]
            ingred_price_dict[ingredient] = ingred_price_dict.get(ingredient, 0) + costs[i]

    ingred_price_order = sorted(ingred_price_dict, key=lambda x: x[1], reverse=True)
    #print(total_ingred_dict, ingred_measure_dict, ingred_price_dict)
    text_list = []
    for ingred in ingred_price_order:
        text = ''
        text += f"{total_ingred_dict[ingred]} {ingred_measure_dict[ingred]}/s of {ingred}: ${ingred_price_dict[ingred]}"
        if ingred_measure_dict[ingred] == "<unit>" or ingred_measure_dict[ingred] == None:
            text = f"{ingred.title()}: ${ingred_price_dict[ingred]}"
        text_list.append(text)
    final_cost = total_cost(costs)
    return ((text_list, final_cost))

if __name__ == '__main__':
    print(total_ingredient_determiner(["chicken grilled sandwich"]))