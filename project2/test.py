import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
import matplotlib.pyplot as plt


data = pd.read_csv('./data.csv')
feature = list(data)[:-1]
label = list(data)[-1]

X = data[feature].dropna().copy()
label_encoder = LabelEncoder()
X['Residence'] = label_encoder.fit_transform(X['Residence'])

# X = pd.get_dummies(X)
# robust = RobustScaler()
# X = robust.fit_transform(X)

x_tr, x_te, y_tr, y_te = train_test_split(X,data[label],test_size=0.25)
tr = DecisionTreeClassifier(max_depth=7)
tr.fit(x_tr,y_tr)
result = tr.predict(x_te)

# print("Accuracy:", metrics.accuracy_score(y_te, result))
print(classification_report(y_te,result))

fig = plt.figure(figsize=(10,8))
tree.plot_tree(tr, feature_names=feature, class_names='Risk')
fig.savefig('./Decision_fig.png',dpi=600)
plt.show()