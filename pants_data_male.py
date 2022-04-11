import pandas as pd

pants_data_m = pd.read_csv('./clean_data/pants_male.csv')

size = []
color = []

for crotch, waist in zip(pants_data_m['crotchheight'], pants_data_m['waistcircumference']):
    if crotch <= 810:
        if waist >= 800:
            size.append('medium')
            color.append('slategrey')
        else:
            size.append('small')
            color.append('asd')
    elif crotch <= 860:
        if waist >= 850:
            size.append('large')
            color.append('lightsteelblue')
        else:
            size.append('medium')
            color.append('slategrey')
    elif crotch <= 910:
        if waist >= 900:
            size.append('xl')
            color.append('cornflowerblue')
        else:
            size.append('large')
            color.append('lightsteelblue')
    elif crotch <= 960:
        if waist >= 950:
            size.append('xxl')
            color.append('royalblue')
        else:
            size.append('xl')
            color.append('cornflowerblue')
    elif crotch <= 1010:
        if waist >= 1000:
            size.append('xxxl')
            color.append('blue')
        else:
            size.append('xxl')
            color.append('royalblue')
    elif crotch <= 1060:
        if waist >= 1050:
            size.append('xxxxl')
            color.append('midnightblue')
        else:
            size.append('xxxl')
            color.append('blue')
    elif crotch < 1500:
        size.append('xxxxl')
        color.append('red')

# pants_data_m.dropna(inplace=True)
# pants_data_m.drop(pants_data_m.columns[0], axis=1, inplace=True)
# pants_data_m['size'] = size
# pants_data_m['color'] = color

