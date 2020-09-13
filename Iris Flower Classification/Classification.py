import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
#loading data
names= ['sepal-length','sepal-width','petal-length','petal-width','class']
df=pd.read_csv('iris.data',names=names)
print(df)
#summerizing data
print(df.isnull().sum())
print(df.shape)
print(df.describe())
scatter_matrix(df)
plt.show()
y=df['class'].values
print(y)
df.drop('class',axis=1,inplace=True)
x=df.values
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3,random_state=42)
#training modfel
clf=KNeighborsClassifier()
clf.fit(x_train, y_train)
#predicting
predictions=clf.predict(x_test)
print(accuracy_score(y_test, predictions))