import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

new_data_f = pd.read_csv('./clean_data/tshirt_female.csv')
new_data_f.dropna(inplace=True)
new_data_f.drop(new_data_f.columns[0], axis=1, inplace=True)
# new_data_f.insert(4, column="size", value="-")
# new_data_f.insert(5, column="color", value="-")

size = []
color = []

for chest, waist in zip(new_data_f['chestcircumference'], new_data_f['waistcircumference']):
    if chest <= 860:
        if waist >= 660:
            size.append('medium')
            color.append('lightsteelblue')
        else:
            size.append('small')
            color.append('slategrey')
    elif chest <= 970:
        if waist >= 720:
            size.append('large')
            color.append('cornflowerblue')
        else:
            size.append('medium')
            color.append('lightsteelblue')
    elif chest <= 1070:
        if waist >= 810:
            size.append('xl')
            color.append('royalblue')
        else:
            size.append('large')
            color.append('cornflowerblue')
    elif chest <= 1180:
        if waist >= 890:
            size.append('xxl')
            color.append('blue')
        else:
            size.append('xl')
            color.append('royalblue')
    elif chest < 1500:
        size.append('xxxl')
        color.append('midnightblue')

new_data_f['size'] = size
new_data_f['color'] = color

