import plotly
import plotly.graph_objects as go
import json

# Function to calculate BMI and determine rating
def bmi_calculate(weight, height):
    weightPart = round(weight, 2)
    heightPart = round(height, 2)
    bmi = weightPart / (heightPart ** 2)
    bmi = round(bmi, 1)
    if 0 < bmi < 18.5:
        rating = "Underweight"
    elif 18.5 <= bmi < 24.9:
        rating = 'Healthy'
    elif 24.9 <= bmi < 30:
        rating = 'Overweight'
    else:
        rating = "Obese"
    return bmi, rating


# Function to display gauge meter with plotly
def bmi_meter(rating):
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=rating,
        mode="gauge+number",
        title={'text': 'BMI Meter'},
        gauge={'axis': {'range': [None, 100]},
               'bar': {'color': "black", 'thickness': 0.60},
               'steps': [
                   {'range': [0, 18.5], 'color': "cornflowerblue"},
                   {'range': [18.5, 24.9], 'color': "forestgreen"},
                   {'range': [24.9, 30], 'color': "darkorange"},
                   {'range': [30, 100], 'color': "red"}]}))
    bmi_meter_rating = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return bmi_meter_rating