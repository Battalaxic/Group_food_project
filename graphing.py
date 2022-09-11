import json
import plotly
import plotly.express as px


def find_chart_data(recipe_data, display_type):
    names = []
    values = []
    recipe_nutrients = recipe_data['recipe']['totalNutrients']
    for nutrient in recipe_nutrients:
        if display_type == 'micronutrient' and recipe_nutrients[nutrient]['unit'] == 'mg':
            names.append(recipe_nutrients[nutrient]['label'])
            values.append(round(recipe_nutrients[nutrient]['quantity'], 2))
        elif display_type == 'macronutrient' and recipe_nutrients[nutrient]['unit'] == 'g':
            names.append(recipe_nutrients[nutrient]['label'])
            values.append(round(recipe_nutrients[nutrient]['quantity'], 2))
    chart_data = {'names': names, 'values': values}
    return chart_data


def micronutrient_chart(recipe_data):
    display_type = 'micronutrient'
    chart_data = find_chart_data(recipe_data, display_type)
    fig = px.pie(values=chart_data['values'],
                 names=chart_data['names'],
                 color_discrete_sequence=px.colors.diverging.RdBu)              # Sets colour theme
    fig.update_traces(hovertemplate=" <b>%{label} </b><br><br> Quantity (mg): %{value} <br> Percentage: %{percent} ",
                      hoverinfo='label+percent',                                # Customises appearance
                      textposition='inside',
                      textinfo='percent+label',
                      marker=dict(line=dict(color='#ffffff', width=0.2)))
    fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')
    fig.update_layout(dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'))
    micronutrient_chart_JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return micronutrient_chart_JSON


def macronutrient_chart(recipe_data):
    display_type = 'macronutrient'
    chart_data = find_chart_data(recipe_data, display_type)
    fig = px.pie(values=chart_data['values'],
                 names=chart_data['names'],
                 color_discrete_sequence=px.colors.diverging.Geyser)
    fig.update_traces(hovertemplate=" <b>%{label} </b><br><br> Quantity (g): %{value} <br> Percentage: %{percent} ",
                      hoverinfo='label+percent',
                      textposition='inside',
                      textinfo='percent+label',
                      marker=dict(line=dict(color='#ffffff', width=0.2)))
    fig.update_layout(uniformtext_minsize=14, uniformtext_mode='hide')
    fig.update_layout(dict(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'))
    macronutrient_chart_JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return macronutrient_chart_JSON


