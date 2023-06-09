# -*- coding: utf-8 -*-
"""titanic-problem.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hjzCrIpOr74TYfz2iyJwYGXWQLSzaFKI
"""

import numpy as np
import pandas as pd
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, ConfusionMatrixDisplay
from sklearn.linear_model import LinearRegression

for dirname, _, filenames in os.walk('/content/data/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

pd.options.mode.chained_assignment = None

train_data = pd.read_csv("/content/data/input/train.csv")
train_data.head()

train_data.describe()

print(train_data.isnull().sum())

#Linear regression approach for age
'''

data = pd.read_csv("/kaggle/input/titanic/train.csv")
datatest = pd.read_csv("/kaggle/input/titanic/test.csv")

data = data[["Survived", "Pclass", "Sex", "SibSp", "Parch", "Fare", "Age"]]

data["Sex"] = [1 if x=="male" else 0 for x in data["Sex"]]

test_data = data[data["Age"].isnull()]
data.dropna(inplace=True)

y_train = data["Age"]
X_train = data.drop("Age", axis=1)
X_test = test_data.drop("Age", axis=1)


model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(len(y_pred))
count=0
for i in range(len(train_data["Age"])):
    if np.isnan(train_data["Age"][i]):
        train_data["Age"][i]=y_pred[count]
        count+=1
print(train_data.isnull().sum())'''

#first approach
train_data["Age"]=train_data["Age"].replace(np.NaN,train_data["Age"].mean())
train_data["Cabin"]=train_data["Cabin"].fillna("U")
train_data["Embarked"] = train_data["Embarked"].fillna(train_data["Embarked"].mode()[0])

#second approach
#train_data["Age"] = train_data["Age"].fillna(method='ffill')
#train_data["Cabin"] = train_data["Cabin"].fillna(method='ffill')
#train_data["Cabin"] = train_data["Cabin"].fillna(method='bfill')

#third approach
#train_data["Age"] = train_data["Age"].interpolate(method='linear', limit_direction='forward', axis=0)


print(train_data.isnull().sum())

test_data = pd.read_csv("/content/data/input/test.csv")
test_data.head()

test_data.describe()

print(test_data.isnull().sum())

#first approach
test_data["Age"]=test_data["Age"].replace(np.NaN,test_data["Age"].mean())
test_data["Fare"]=test_data["Fare"].replace(np.NaN,test_data["Fare"].mean())
test_data["Cabin"]=test_data["Cabin"].fillna("U")


#second approach
#test_data["Age"] = test_data["Age"].fillna(method='ffill')
#test_data["Cabin"] = test_data["Cabin"].fillna(method='ffill')
#test_data["Cabin"] = test_data["Cabin"].fillna(method='bfill')
#test_data["Fare"] = test_data["Fare"].fillna(method='ffill')

#third approach
#test_data["Age"] = test_data["Age"].interpolate(method='linear', limit_direction='forward', axis=0)
#test_data["Fare"] = test_data["Fare"].interpolate(method='linear', limit_direction='forward', axis=0)

print(test_data.isnull().sum())

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
print("% of women who survived:", rate_women)

women = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_women = sum(women)/len(women)
print("% of men who survived:", rate_women)

women = train_data.loc[train_data.Pclass == 1]["Survived"]
rate_women = sum(women)/len(women)
print("% of Pclass 1 who survived:", rate_women)

women = train_data.loc[train_data.Pclass == 2]["Survived"]
rate_women = sum(women)/len(women)
print("% of Pclass 2 who survived:", rate_women)

women = train_data.loc[train_data.Pclass == 3]["Survived"]
rate_women = sum(women)/len(women)
print("% of Pclass 3 who survived:", rate_women)

women = train_data.loc[train_data.Age >= 30]["Survived"]
rate_women = sum(women)/len(women)
print("% of Age 30> who survived:", rate_women)

women = train_data.loc[train_data.Age < 30]["Survived"]
rate_women = sum(women)/len(women)
print("% of Age 30< who survived:", rate_women)

women = train_data.loc[train_data.Fare >= 33]["Survived"]
rate_women = sum(women)/len(women)
print("% of Fare 33> who survived:", rate_women)

women = train_data.loc[train_data.Fare < 33]["Survived"]
rate_women = sum(women)/len(women)
print("% of Fare 33< who survived:", rate_women)

y = train_data["Survived"]

#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked (Ticket,Cabin couldn't be added)

features = ["Pclass","Sex","Age","Fare","SibSp","Parch","Embarked"]#


#if decision tree
#train_data["Sex"] = [1 if x=="male" else 0 for x in train_data["Sex"]]
#test_data["Sex"] = [1 if x=="male" else 0 for x in test_data["Sex"]]
#train_data["Embarked"] = [1 if x=="S" else (2 if x=="C" else (3 if x=="Q" else 0)) for x in train_data["Embarked"]]
#test_data["Embarked"] = [1 if x=="S" else (2 if x=="C" else (3 if x=="Q" else 0)) for x in test_data["Embarked"]]

X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])

train_X, val_X, train_y, val_y = train_test_split(X, y,test_size=0.25, random_state = 0)


#trying to find best params
'''rfc=RandomForestClassifier(random_state=0)
param_grid = { 
    'n_estimators': [200, 500],
    'max_features': ['auto', 'sqrt', 'log2'],
    'max_depth' : [4,5,6,7,8],
    'criterion' :['gini', 'entropy']
}
CV_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5)
CV_rfc.fit(train_X, train_y)
CV_rfc.best_params_
'''
'''
{'criterion': 'entropy',
 'max_depth': 8,
 'max_features': 'auto',
 'n_estimators': 200}
'''

#Logistic Regression Part
#logreg = LogisticRegression(random_state=16, max_iter=3000)
#logreg.fit(train_X, train_y)
#predictions = logreg.predict(X_test)

#Random Forest Part
model = RandomForestClassifier(n_estimators=200, random_state=0,max_depth=8,max_features="auto",criterion="entropy")
model.fit(train_X, train_y)
predictions = model.predict(X_test)

#Decision Tree Part
#model=DecisionTreeRegressor(random_state=1)
#model.fit(train_X, train_y)
#predictions = model.predict(X_test)
#output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': np.array(predictions,int)})

#Naive Bayes Part
#model = GaussianNB()
#model.fit(train_X, train_y);
#predictions = model.predict(X_test)

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv('submission.csv', index=False)
print("Your submission was successfully saved!")
print(predictions)
#print(np.array(predictions,int))
print((predictions !=0).sum())

#Evaluate(later)
accuracy = accuracy_score(val_y, predictions[0:223])
print("Accuracy:%", accuracy*100)