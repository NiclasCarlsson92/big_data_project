import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

data_frame = pd.read_csv('./stock_data/male.csv')
male_measures = data_frame[['stature', 'weightkg', 'chestcircumference', 'waistcircumference']]
#male_measures.to_csv('clean_data/clean_male.csv')
data_frame.dropna(inplace=True)
new_data_m = pd.read_csv('./clean_data/clean_male.csv')
new_data_m.drop(new_data_m.columns[0], axis=1, inplace=True)
new_data_m.insert(4, column="size", value="-")
new_data_m.insert(5, column="color", value="-")

size = []
color = []

for chest, waist in zip(new_data_m['chestcircumference'], new_data_m['waistcircumference']):
    if chest <= 1020:
        if waist >= 810:
            size.append('medium')
            color.append('lightsteelblue')
        else:
            size.append('small')
            color.append('slategrey')
    elif chest <= 1120:
        if waist >= 840:
            size.append('large')
            color.append('cornflowerblue')
        else:
            size.append('medium')
            color.append('lightsteelblue')
    elif chest <= 1220:
        if waist >= 870:
            size.append('xl')
            color.append('royalblue')
        else:
            size.append('large')
            color.append('cornflowerblue')
    elif chest <= 1270:
        if waist >= 970:
            size.append('xxl')
            color.append('blue')
        else:
            size.append('xl')
            color.append('royalblue')
    elif chest <= 1320:
        if waist >= 1070:
            size.append('xxxl')
            color.append('midnightblue')
        else:
            size.append('xxxxl')
            color.append('black')
    elif chest <= 1700:
        size.append('MegaXL')
        color.append('red')

new_data_m['size'] = size
new_data_m['color'] = color
