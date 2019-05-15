import pandas as pd
excel_data = pd.read_csv("my_excel_data.csv")

def get_macros(food):
    macros = []
    macros.extend(excel_data[excel_data.name == food].calories)
    macros.extend(excel_data[excel_data.name == food].fat)
    macros.extend(excel_data[excel_data.name == food].protein)
    macros.extend(excel_data[excel_data.name == food].carb)
    macros.extend(excel_data[excel_data.name == food].fiber)
    macros.extend(excel_data[excel_data.name == food].serving)
    return macros


totals = {
    'calories': 0,
    'protein': 0,
    'fat': 0,
    'carbs': 0,
    'fiber': 0,
    'net_carbs': 0
}

def add_food(food, grams):
    totals['calories'] += get_macros(food)[0] * grams / get_macros(food)[5]
    totals['fat'] += get_macros(food)[1] * grams / get_macros(food)[5]
    totals['protein'] += get_macros(food)[2] * grams / get_macros(food)[5]
    totals['carbs'] += get_macros(food)[3] * grams / get_macros(food)[5]
    totals['fiber'] += get_macros(food)[4] * grams / get_macros(food)[5]
    totals['net_carbs'] += (get_macros(food)[3] * grams / get_macros(food)[5]) - (get_macros(food)[4] * grams / get_macros(food)[5])
    if totals['net_carbs'] >= 20.0:
        print ("You're over your carb limit!!!")
    else:
        print ('You have {} net carbs left.'.format(20 - totals['net_carbs']))
    return totals


def clear_totals():
    for key in totals:
        totals[key] = 0
    return totals


def calculate_macro_percentages():
    calories = totals['protein']*4 + totals['fat']*9 + totals['net_carbs']*4
    protein_percent = str((totals['protein'] * 4 / calories)*100) + '%'
    fat_percent = str((totals['fat'] * 9 / calories)*100) + '%'
    carb_percent = str((totals['net_carbs'] * 4 / calories)*100) + '%'
    percentages = {
        'Fat': fat_percent,
        'Protein': protein_percent,
        'Carbs': carb_percent,
        'Net_Carbs': totals['net_carbs']}
    return percentages


def pie_chart_data():
    calories = totals['protein']*4 + totals['fat']*9 + totals['net_carbs']*4 + 1
    protein_percent = totals['protein'] * 4 / calories
    fat_percent = totals['fat'] * 9 / calories
    carb_percent = totals['net_carbs'] * 4 / calories
    percentages = {
        'Fat': fat_percent,
        'Protein': protein_percent,
        'Carb': carb_percent}
    return percentages


import matplotlib.pyplot as plt
from collections import Counter

# Data to plot
labels = list(Counter(pie_chart_data()))
sizes = list(Counter(pie_chart_data()).values())
colors = ['lightblue', 'lightcoral', 'yellowgreen']
explode = (.1, .1, .1)

# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()
