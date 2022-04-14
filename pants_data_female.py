import pandas as pd

pants_data_f = pd.read_csv('./clean_data/pants_female.csv')
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pants_data_f.dropna(inplace=True)
pants_data_f.drop(pants_data_f.columns[0], axis=1, inplace=True)

size = []
color = []

for butt, waist in zip(pants_data_f['buttockcircumference'], pants_data_f['waistcircumference']):
    if waist <= 640:
        if butt >= 880:
            size.append('small')
            color.append('slategrey')
        else:
            size.append('xs')
            color.append('pink')
    elif waist <= 720:
        if butt >= 960:
            size.append('medium')
            color.append('lightsteelblue')
        else:
            size.append('small')
            color.append('slategrey')
    elif waist <= 800:
        if butt >= 1040:
            size.append('large')
            color.append('cornflowerblue')
        else:
            size.append('medium')
            color.append('lightsteelblue')
    elif waist <= 880:
        if butt >= 1120:
            size.append('xl')
            color.append('royalblue')
        else:
            size.append('large')
            color.append('cornflowerblue')
    elif waist <= 1000:
        if butt >= 1220:
            size.append('xxl')
            color.append('blue')
        else:
            size.append('xl')
            color.append('royalblue')
    elif waist <= 1120:
        if butt >= 1320:
            size.append('xxxl')
            color.append('midnightblue')
        else:
            size.append('xxl')
            color.append('blue')
    elif waist < 1500:
        size.append('xxxxl')
        color.append('red')

pants_data_f['size'] = size
pants_data_f['color'] = color
