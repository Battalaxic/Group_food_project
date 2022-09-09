import plotly
import plotly.express as px
import json
import pandas


def price_pie_chart(ingredients, prices):
    fig = px.pie(values=prices, names=ingredients)
    graph_JSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_JSON

def price_over_time_line_chart(dates, ingredients):             #ingredient can be overall
    fig = px.line(x=dates, y=ingredients)



'''TODO: line chart to track price over time for both overall and separate ingredients'''

if __name__ == '__main__':
    price_over_time_line_chart()