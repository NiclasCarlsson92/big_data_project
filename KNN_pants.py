import math
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from pants_data_male import pants_data_m
from pants_data_female import pants_data_f
from collections import Counter


def euclidian_distance(df_data, user_data):
    x1, y1 = df_data
    x2, y2 = user_data

    delta_x = x1 - x2
    delta_y = y1 - y2

    return math.sqrt((delta_x**2) + (delta_y**2))


user_sex = int(input("Male[0] or Female [1]\n"))
user_length = int(input("Enter length in mm:\n"))
user_weight = int(input("Enter weight in hg:\n"))
user_data = [user_length, user_weight]

distances = []
pants_data = []
sizes = []

if user_sex == 0:
    pants_data = list(zip(pants_data_m['stature'], pants_data_m['weightkg']))
    sizes = pants_data_m['size']
else:
    pants_data = list(zip(pants_data_f['stature'], pants_data_f['weightkg']))
    sizes = pants_data_f['size']

check_nearest = int(input('Enter K value: '))
for i, df in enumerate(pants_data):
    dist = euclidian_distance(df, user_data)
    distances.append({'dist': dist, 'size': sizes[i]})

distances.sort(key=lambda data: data['dist'])

distances = distances[:check_nearest]

counter = Counter([d['size'] for d in distances])
print('*'*40)
print(check_nearest, 'nearest neighbours')
print(counter.most_common(check_nearest))
print('*'*40)
print('My KNN predicts this pants size for you: ', counter.most_common(1)[0][0].upper())
print('*'*40)

X = None
y = None
if user_sex == 0:
    X = list(zip(pants_data_m['stature'], pants_data_m['weightkg']))
    y = list(pants_data_m['size'])
else:
    X = list(zip(pants_data_f['stature'], pants_data_f['weightkg']))
    y = list(pants_data_f['size'])

model = KNeighborsClassifier(n_neighbors=check_nearest)
model.fit(X, y)
predicted = model.predict([user_data])
print('SKlearn-KNN predicts this pants size for you: ', predicted)
print('*' * 40)
X_dt = None
y_dt = None
if user_sex == 0:
    X_dt = list(zip(pants_data_m['stature'], pants_data_m['weightkg']))
    y_dt = list(pants_data_m['size'])
else:
    X_dt = list(zip(pants_data_f['stature'], pants_data_f['weightkg']))
    y_dt = list(pants_data_f['size'])

X_train, X_test, y_train, y_test = train_test_split(X_dt, y_dt, test_size=0.3, random_state=1)
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)
y_pred = clf.predict([[user_length, user_weight]])
print('SKlearn Decision Tree Classifier predicts this t-shirt size for you:', y_pred)
print('*' * 40)
