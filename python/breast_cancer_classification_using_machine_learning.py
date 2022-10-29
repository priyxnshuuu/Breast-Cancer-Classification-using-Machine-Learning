# -*- coding: utf-8 -*-
"""Breast Cancer Classification using Machine Learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1qGtUJrGckkZAd3yvI8WzQQ2x9cSEVvsj

1. Import the lib
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""2. Load DataSet """

df = pd.read_csv('data.csv')

"""3. Analyzing Data"""

df.head(10)

df.tail(10)

df.info()

df.isnull().sum

df.head()

"""4. Lable encoding of categorical column"""

df.loc[df['diagnosis'] == 'M', 'diagnosis'] = 0
df.loc[df['diagnosis'] == 'B', 'diagnosis'] = 1

"""Malignant --> 0

Benign --> 1
"""

df.head()

df['diagnosis'].value_counts()

"""5. Split x and y"""

x = df.drop(columns = 'diagnosis')
y = df['diagnosis']

y=y.astype("int")

print(x)

print(y)

"""6. Split Train and Test """

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2,  stratify= y)
# stratify= y means split y evenly in train and test

print(x.shape, x_train.shape, x_test.shape)

print(y.shape, y_train.shape, y_test.shape)

"""7. Model Training"""

model = LogisticRegression()

# training the Logistic Regression model using Training data

model.fit(x_train, y_train)

"""8. Model Evaluation"""

# accuracy on train data

x_train_predict = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_predict, y_train)

print('training data accuracy: ',training_data_accuracy)

# accuracy on test data

x_test_predict = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_predict, y_test)

print('test data accuracy: ',test_data_accuracy)

"""9. Building System"""

input_data = [16.74,21.59,110.1,869.5,0.0961,0.1336,0.1348,0.06018,0.1896,0.05656,0.4615,0.9197,3.008,45.19,0.005776,0.02499,0.03695,0.01195,0.02789,0.002665,20.01,29.02,133.5,1229,0.1563,0.3835,0.5409,0.1813,0.4863,0.08633]

#convert input_data into array
input_data_array = np.asanyarray(input_data)

#reshaping array into 2d 
input_data_array_reshape = input_data_array.reshape(1,-1)

predict = model.predict(input_data_array_reshape)
print(predict)

if predict[0] == 0:
  print("you have brest cancer")
else:
  print("you do not have cancer")