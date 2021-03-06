# -*- coding: utf-8 -*-
"""Load_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HWX_7F1HS9Z5JGN9obQWcBmK2wRUl15A

### Loan Prediction Using Niave_Bayes Algorithm  and  Decesion Tree Algorithm
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

dataset = pd.read_csv('/content/sample_data/data.csv')

dataset.head()

"""For finding row and column"""

dataset.shape

dataset.info()

dataset.describe()

pd.crosstab(dataset['Credit_History'] , dataset['Loan_Status'] , margins = True)

dataset.boxplot(column = "ApplicantIncome")

dataset["ApplicantIncome"].hist(bins = 20)

dataset["CoapplicantIncome"].hist(bins = 20)

dataset.boxplot(column = "ApplicantIncome" , by="Education")

dataset. boxplot(column='LoanAmount')

dataset['LoanAmount'].hist(bins=20)

dataset['LoanAmount_log']= np.log(dataset['LoanAmount'])
dataset['LoanAmount_log'].hist(bins=30)

dataset.isnull().sum()

dataset.isnull()

dataset['Gender'].fillna(dataset['Gender'].mode()[0] , inplace = True)

dataset['Married'].fillna(dataset['Married'].mode()[0] , inplace = True)

dataset['Dependents'].fillna(dataset['Dependents'].mode()[0] , inplace = True)

dataset['Self_Employed'].fillna(dataset['Self_Employed'].mode()[0] , inplace = True)

dataset.LoanAmount = dataset.LoanAmount.fillna(dataset.LoanAmount.mean())
dataset.LoanAmount_log = dataset.LoanAmount_log.fillna(dataset.LoanAmount_log.mean())

dataset['Loan_Amount_Term'].fillna(dataset['Loan_Amount_Term'].mode()[0] , inplace = True)

dataset['Credit_History'].fillna(dataset['Credit_History'].mode()[0] , inplace = True)

dataset.isnull().sum()

dataset['TotalIncome'] = dataset['ApplicantIncome'] + dataset['CoapplicantIncome']
dataset['TotalIncome_log'] = np.log(dataset['TotalIncome'])

dataset['TotalIncome_log'].hist(bins=20)

dataset.head()

X = dataset.iloc[:,np.r_[1:5,9:11,13:15]].values
Y = dataset.iloc[:,12].values

X

Y

"""Splitting **train** **dataset** **using** **sklearn** **bold text**"""

from sklearn.model_selection import train_test_split

X_train,X_test , Y_train,Y_test = train_test_split(X,Y , test_size=0.2 , random_state = 0)

"""20 percent testing data ---- 80percent training data"""

print(X_train)

print(Y_train)

"""converting to 1s and 0s using label encoder"""

from sklearn.preprocessing import LabelEncoder 
labelencoder_X = LabelEncoder()

for i in range(0,5):
  X_train[:,i] = labelencoder_X.fit_transform( X_train[:,i])

X_train[:,7] = labelencoder_X.fit_transform( X_train[:,7])

X_train

labelencoder_Y = LabelEncoder()
Y_train=labelencoder_Y.fit_transform(Y_train)

Y_train

Y_test

for i in range(0,5):
  X_test[:,i] = labelencoder_X.fit_transform( X_test[:,i])

X_test[:,7] = labelencoder_X.fit_transform(X_test[:,7])

labelencoder_Y = LabelEncoder()
Y_test= labelencoder_Y.fit_transform(Y_test)

Y_test

X_test

from sklearn.preprocessing import StandardScaler
ss = StandardScaler() 
X_train = ss.fit_transform(X_train)
X_test = ss.fit_transform(X_test)

"""

---



---


## Using Decision Tree Algorithm

---

"""

from sklearn.tree import DecisionTreeClassifier
DTClassifier = DecisionTreeClassifier(criterion="entropy" , random_state =0 )
DTClassifier.fit(X_train, Y_train)

y_pred = DTClassifier.predict(X_test)
y_pred

from sklearn import metrics
print("The accuracy of decision tree is :" , metrics.accuracy_score(y_pred , Y_test))

"""---

## Decision Tree we got 70 percent accuracy




---

---


### Naive_Bayes algorithm

---
"""

from sklearn.naive_bayes import GaussianNB
NBClassifier = GaussianNB()
NBClassifier.fit(X_train , Y_train)

y_pred1 = NBClassifier.predict(X_test)

y_pred1

print("The accuracy of decision tree is :" , metrics.accuracy_score(y_pred1 , Y_test))

testdata = pd.read_csv('/content/sample_data/data.csv')

testdata.head()

testdata.info()

testdata.isnull().sum()

dataset.isnull().sum()

dataset.boxplot(column='LoanAmount')

#dataset['TotalIncome'] = dataset['ApplicantIncome'] + testdata['CoapplicantIncome']
#dataset['TotalIncome_log'] = np.log(testdata['TotalIncome'])

"""---
Used full dataset to test
---

---





"""

test = dataset.iloc[:,np.r_[1:5,9:11,13:15]].values

for i in range(0,5):
  test[:,i] = labelencoder_X.fit_transform(test[:,7])

test

test = ss.fit_transform(test)

pred = NBClassifier.predict(test)

pred

"""1 represents customer is eligible and ) represents customer is not eligible """

