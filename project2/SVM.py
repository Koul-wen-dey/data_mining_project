import pandas as pd
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import RobustScaler
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 讀取資料並提取特徵欄位和標籤欄位
data = pd.read_csv('./data.csv')
feature = list(data)[:-1]
label = list(data)[-1]

# 將特徵欄位中的非數值轉換為數值
x = data[feature].copy()
label_encoder = LabelEncoder()
x['Residence'] = label_encoder.fit_transform(x['Residence'])

# 中位數和四分位數標準化，有效減少outlier
robust = RobustScaler()
x = robust.fit_transform(x)

# 將資料與標籤分割成訓練集和測試集，並輸入模型預測
x_tr, x_te, y_tr, y_te = train_test_split(x,data[label],test_size=0.25)
tr = SVC(probability=True)
tr.fit(x_tr,y_tr)
result = tr.predict(x_te)

# print("Accuracy:", metrics.accuracy_score(y_te, result))
print(classification_report(y_te,result))
mtx = confusion_matrix(y_te,result)
print(mtx)
sns.heatmap(mtx/np.sum(mtx), square=True, annot=True, fmt='.2%',
            xticklabels=[0, 1], yticklabels=[0,1])
plt.xlabel('predicted label')
plt.ylabel('true label')

plt.show()