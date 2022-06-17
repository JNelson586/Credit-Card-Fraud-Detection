# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15qA7ky8Hyw96FgdEVMw7pDocb8NdJhYA
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Loading the dataset to a Pandas DataFrame
credit_card_data = pd.read_csv('/content/creditcard[1].csv')

credit_card_data.head()

credit_card_data.tail()

# Distriubtion of legit transactions & fradualent transactions
credit_card_data['Class'].value_counts()



"""This data set is highly unbalances. (via 284,315 legit transactions & 492 fradualent transactions)"""

# Separating data from fradualent transactions and legit transactions
legit = credit_card_data[credit_card_data.Class == 0]
fraud = credit_card_data[credit_card_data.Class == 1]

print(legit.shape)
print(fraud.shape)

# Statistical measures of the data
legit.Amount.describe()

fraud.Amount.describe()

# Compare values for both transactions
credit_card_data.groupby('Class').mean()



"""Under Sampling

Build a sample data set containg similar distriution of normal transactions and Fraudulent transactions
"""



"""Number of fraudaulent transactions = 492                                       
Number of legit transactions = 284315
"""

legit_sample = legit.sample(n=492)



"""Concatenating 2 DataFrameds"""

new_dataset = pd.concat([legit_sample, fraud], axis =0)

new_dataset.head()

new_dataset.tail()

new_dataset.groupby('Class').mean()



"""Splitting the data into Features & Target's"""

X = new_dataset.drop(columns = 'Class', axis =1)
Y = new_dataset['Class']

print(X)



"""Split the data into Training data & Testing data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape, X_train.shape, X_test.shape)



"""Model training

Logistic Regression
"""

model = LogisticRegression()

# Training the Logistic Regression Model with Training Data
model.fit(X_train, Y_train)



"""Model Evaluation"""



"""Accuracy Score"""

# accuracy on trainng data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

print('Accuracy on Training data : ', training_data_accuracy)

# Accuracy on Test Data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

print('Accuracy score on Test Data: ', test_data_accuracy)

