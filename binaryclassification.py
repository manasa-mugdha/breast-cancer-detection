from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns

data=load_breast_cancer()
X=data['data']
y=data['target']

X_train, X_test, y_train, y_test=train_test_split(X,y, test_size=0.2) 
clf=KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
print(len(data['feature_names']))
X_new=np.array(random.sample(range(0,50), 30))
print(data['target_names'][clf.predict([X_new])[0]]) 

column_data=np.concatenate([data['data'], data['target'][:, None]], axis=1)
column_names=np.concatenate([data['feature_names'],["class"]])
df=pd.DataFrame(column_data, columns=column_names)
print(df)
sns.heatmap(df.corr(), cmap="coolwarm", annot=True, annot_kws={"fontsize":8})
plt.show()
