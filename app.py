from flask import Flask, render_template, request, redirect, url_for
import graphing
import fetch_data
import price
import password_testing
import price_graphs
import history
import bmicalculator
import json
import os
import mealslogger
from mealplan import input_mainfood
import shopping_list

'''https://pythonbasics.org/flask-login/'''

app = Flask(__name__)

logged_in_flag = False
@app.route('/login', methods=['GET', 'POST'])
def login_and_register():  # put application's code here
    user_already_created = False
    if request.method == "POST":
        password = request.form.get("password")
        username = request.form.get("username")
        if request.form.get("user_function") == "Login":
            if password_testing.login_attempt(username, password) == True:
                logged_in_flag = True
                return redirect(url_for("recipe_query"))
            else:
                logged_in_flag = False
                return render_template('launch_page.html', failed_login=True)
        elif request.form.get("user_function") == "Register":
            new_user_file = f"static/{request.form.get('username')}.txt"
            password_testing.add_user(username, password)
            try:
                create_file = open(new_user_file, "x")
                return redirect(url_for("recipe_query"))
            except:
                user_already_created = True
                return render_template('launch_page.html', user_already_created=user_already_created)
    return render_template('launch_page.html')


@app.route('/', methods=['GET','POST'])
def recipe_query():
    title = "Recipe Search"
    if request.method =='POST':
        recipe_query1 = request.form.get('recipe_query')
        #print(recipe_query1)
        with open("static/recipe_query.txt", "w") as f:
            f.write(recipe_query1)
        diet_query = request.form.get('diet_query', '')
        health_query = request.form.get('health_query', '')
        cuisine_type_query = request.form.get('cuisine_type_query', '')
        meal_type_query = request.form.get('meal_type_query', '')
        dish_type_query = request.form.get('dish_type_query', '')
        recipe_list = fetch_data.call_recipe_search(recipe_query1, diet_query, health_query, cuisine_type_query, meal_type_query, dish_type_query)
        recipe_items = fetch_data.search_recipe_organise(recipe_list)
        recipe_labels = recipe_items['labels']
        recipe_thumbnails = recipe_items['thumbnails']
        recipe_ids = recipe_items['recipe_ids']
        return render_template('recipe_list.html',
                               recipe_list=recipe_list,
                               recipe_labels=recipe_labels,
                               recipe_thumbnails=recipe_thumbnails,
                               recipe_ids=recipe_ids,
                               title=title)
    return render_template("recipe_query.html", title=title)

#print(recipe_query1)

@app.route('/recipe_info', methods=['GET','POST'])
def recipe_info():
    title = "Recipe Info"
    recipe_id = request.args.get('id')
    print(f'Recipe id {recipe_id}')
    if recipe_id is None or recipe_id == '':
        return redirect('/')
    else:
        specific_recipe_data = fetch_data.search_specific_recipe(recipe_id)
        micronutrient_chart_JSON = graphing.micronutrient_chart(specific_recipe_data)
        macronutrient_chart_JSON = graphing.macronutrient_chart(specific_recipe_data)
        organised_recipe_data = fetch_data.specific_recipe_organise(specific_recipe_data)
        ingredients_list = organised_recipe_data['ingredients_list']
        name = organised_recipe_data['label'].lower().split()  # For Thomas' Module
        #history.get_history(name)
        #history.get_query()
        #print(output)
        #print(api_request_url, "POPOPOPOPOPOPOP")
        with open("static/recipe_query.txt") as f:
            for line in f:
                recipe_query1 = line
        print(recipe_query1)
        ingreds, costs, measures, qtys = price.complete_price_subroutine(recipe_query1)
        price_pie_chart = price_graphs.price_pie_chart(ingreds, costs)
        #text_list, final_cost = shopping_list.total_ingredient_determiner(recipe_query1)
        return render_template("recipe_info.html",
                               specific_recipe_data=specific_recipe_data,
                               micronutrient_chart_JSON=micronutrient_chart_JSON,
                               macronutrient_chart_JSON=macronutrient_chart_JSON,
                               organised_recipe_data=organised_recipe_data,
                               ingredients_list=ingredients_list,
                               price_pie_chart_JSON=price_pie_chart,
                               title=title)


if __name__ == '__main__':
    app.run()