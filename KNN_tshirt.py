import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import neighbors
from sklearn.metrics import f1_score
from tshirt_data_female import new_data_f
from tshirt_data_male import new_data_m


def main():
    user_sex = int(input("Male[0] or Female [1]\n"))
    user_length = int(input("Enter length in mm:\n"))
    user_weight = int(input("Enter weight in hg:\n"))

    nearest = []
    if user_sex == 0:
        for length, weight in zip(new_data_m['stature'], new_data_m['weightkg']):
            delta_y = abs(user_length) - abs(length)
            delta_x = abs(user_weight) - abs(weight)
            hypotenuse = delta_y ** 2 + delta_x ** 2
            nearest.append(math.sqrt(hypotenuse))
    else:
        for length, weight in zip(new_data_f['stature'], new_data_f['weightkg']):
            delta_y = abs(user_length) - abs(length)
            delta_x = abs(user_weight) - abs(weight)
            hypotenuse = delta_y ** 2 + delta_x ** 2
            nearest.append(math.sqrt(hypotenuse))

    if user_sex == 0:
        new_data_m['nearest'] = nearest
    else:
        new_data_f['nearest'] = nearest

    if user_sex == 0:
        X = new_data_m.drop(columns=['size', 'color'])
        Y = new_data_m['size']
    else:
        X = new_data_f.drop(columns=['size', 'color'])
        Y = new_data_f['size']

    X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=20)

    scaler = StandardScaler()
    scaler.fit_transform(X_train)
    scaler.transform(X_val)

    f1_list = []
    k_list = []

    print('*' * 50)

    for k in range(1, 22, 2):
        clf = neighbors.KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
        clf.fit(X_train, y_train)
        pred = clf.predict(X_val)
        f = f1_score(y_val, pred, average='macro')
        print('k)', k, '=>', f)
        f1_list.append(f)
        k_list.append(k)

    print('*' * 50)
    print('\n')

    best_f1_score = max(f1_list)
    best_k = k_list[f1_list.index(best_f1_score)]
    print("Optimum K value=", best_k, " with F1-Score=", best_f1_score, '\n')

    KNN_model = neighbors.KNeighborsClassifier(n_neighbors=best_k, n_jobs=-1)
    KNN_model.fit(X_train, y_train)
    pred = KNN_model.predict(X_val)
    accuracy = sum(y_val == pred) / (y_val.shape[0]) * 100

    print('Using the optimum K value', best_k)
    if user_sex == 0:
        print(f'Accuracy: {int(accuracy)}%\n')
        print(new_data_m.sort_values(by=['nearest']).head(best_k))
    else:
        print(f'Accuracy: {int(accuracy)}%\n')
        print(new_data_f.sort_values(by=['nearest']).head(best_k))


if __name__ == '__main__':
    main()
