import math
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import neighbors
from sklearn.metrics import f1_score, confusion_matrix, roc_auc_score


def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    # Create a data_frame by reading csv-files
    data_frame = pd.read_csv('./stock_data/female.csv')
    data_frame2 = pd.read_csv('./stock_data/male.csv')

    # Dropping null value columns
    data_frame.dropna(inplace=True)
    data_frame2.dropna(inplace=True)

    # Create a new folder
    # os.makedirs('clean_data', exist_ok=True)

    # DF with filtered data
    female_measures = data_frame[['stature', 'weightkg', 'chestcircumference', 'waistcircumference']]
    male_measures = data_frame[['stature', 'weightkg', 'chestcircumference', 'waistcircumference']]
    # Write to file
    female_measures.to_csv('clean_data/clean_female.csv')
    male_measures.to_csv('clean_data/clean_male.csv')

    # New data frame
    new_data_f = pd.read_csv('./clean_data/clean_female.csv')
    # new_data_m = pd.read_csv('./clean_data/clean_male.csv')

    new_data_f.drop(new_data_f.columns[0], axis=1, inplace=True)
    new_data_f.insert(4, column="size", value="-")
    new_data_f.insert(5, column="color", value="-")

    size = []
    color = []

    for chest, waist in zip(new_data_f['chestcircumference'], new_data_f['waistcircumference']):
        if chest <= 860:
            if waist >= 660:
                size.append('medium')
                color.append('lightsteelblue')
                # color.append(1.0)
            else:
                size.append('small')
                color.append('slategrey')
                # color.append(2.0)
        elif chest <= 970:
            if waist >= 720:
                size.append('large')
                color.append('cornflowerblue')
                # color.append(3.0)
            else:
                size.append('medium')
                color.append('lightsteelblue')
                # color.append(1.0)
        elif chest <= 1070:
            if waist >= 810:
                size.append('xl')
                color.append('royalblue')
                # color.append(4.0)
            else:
                size.append('large')
                color.append('cornflowerblue')
                # color.append(3.0)
        elif chest <= 1180:
            if waist >= 890:
                size.append('xxl')
                color.append('blue')
                # color.append(5.0)
            else:
                size.append('xl')
                color.append('royalblue')
                # color.append(4.0)
        elif chest < 1500:
            size.append('xxxl')
            color.append('midnightblue')
            # color.append(6.0)

    new_data_f['size'] = size
    new_data_f['color'] = color
    nearest = []

    # User input
    ask_length = int(input("Enter length in mm:\n"))
    ask_weight = int(input("Enter weight in hg:\n"))

    for length, weight in zip(new_data_f['stature'], new_data_f['weightkg']):
        delta_y = abs(ask_length) - abs(length)
        delta_x = abs(ask_weight) - abs(weight)
        hypotenuse = delta_y ** 2 + delta_x ** 2
        nearest.append(math.sqrt(hypotenuse))

    new_data_f['nearest'] = nearest

    # sns.set()
    # sns.scatterplot(y=new_data_f['stature'], x=new_data_f['weightkg'], c=new_data_f['color'])
    # plt.show()

    # KNN
    #################################################################################

    X = new_data_f.drop(columns=['size', 'color'])
    Y = new_data_f['size']
    X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=20)
    scaler = StandardScaler()
    scaler.fit_transform(X_train)
    scaler.transform(X_val)

    # Looking for the 20 closest neighbours
    KNN_model = neighbors.KNeighborsClassifier(n_neighbors=20, n_jobs=-1)
    KNN_model.fit(X_train, y_train)

    pred = KNN_model.predict(X_val)
    print("Accuracy={}%".format((sum(y_val == pred) / y_val.shape[0]) * 100))

    # F1-Score is a performance metric used for evaluating the model. Value of F1-Score is in range 0–1.
    f1_list = []
    k_list = []
    for k in range(1, 10):
        clf = neighbors.KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
        clf.fit(X_train, y_train)
        pred = clf.predict(X_val)
        f = f1_score(y_val, pred, average='macro')
        f1_list.append(f)
        k_list.append(k)

    best_f1_score = max(f1_list)
    best_k = k_list[f1_list.index(best_f1_score)]
    # Finds out what's the best K value for this equation
    print("Optimum K value=", best_k, " with F1-Score=", best_f1_score)

    KNN_model = neighbors.KNeighborsClassifier(n_neighbors=6, n_jobs=-1)
    KNN_model.fit(X_train, y_train)
    pred = KNN_model.predict(X_val)
    print("Accuracy={}%".format((sum(y_val == pred) / y_val.shape[0]) * 100))

    for k in range(1):
        print(new_data_f.sort_values(by=['nearest']).head(7))
    # print(new_data_f.sort_values(by=['nearest']).head(7))
    #################################################################################


if __name__ == '__main__':
    main()
