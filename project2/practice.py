from sklearn import datasets
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

iris = datasets.load_iris()
x = iris['data']
y = iris['target']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=10)
# knn = KNeighborsClassifier()
# knn.fit(x_train,y_train)
# result = knn.predict(x_test)
dt = DecisionTreeClassifier()
dt.fit(x_train,y_train)
result = dt.predict(x_test)
for a,b in zip(result,y_test):
    print(a,b)