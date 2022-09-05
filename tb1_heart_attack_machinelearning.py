# -*- coding: utf-8 -*-
"""TB1_Heart_Attack_Machinelearning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dA7nfRyWidNmXy3zF3hCzIVgbj-_JnCo
"""

import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# Upload file dataset
from google.colab import files
uploaded = files.upload()

# Membaca file heart.csv
data = pd.read_csv('heart.csv')

# melihat informasi dataset pada 5 baris pertama
data.head()

# memisahkan atribut dan label
X = data.drop(["target"], axis=1)
X[0:5]

Y = data["target"].values
Y[0:5]

# split the dataset into the training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state=1)

# Untuk mengetahui panjang/jumldah data pada x_train , x_test, y_train, y_test
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)

"""# Naive Bayes Model"""

#Import Gaussian Naive Bayes model
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

#Create a Gaussian Classifier
model = GaussianNB()

# Train the model using the training sets
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)
print(acc)
print(cm)

# Melihat tingkat akurasi pada variable test
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred.round()))

"""# KNN"""

# membagi dataset menjadi training dan testing 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size= 0.2, random_state=3)

# Untuk mengetahui panjang/jumldah data pada x_train , x_test, y_train, y_test
print ('Train set:', X_train.shape,  y_train.shape)
print ('Test set:', X_test.shape,  y_test.shape)

from sklearn import preprocessing

X = preprocessing.StandardScaler().fit(X).transform(X.astype(float))
X[0:5]

from sklearn.model_selection import cross_val_score

k = 25
#Membuat model KNN  
neigh = KNeighborsClassifier(n_neighbors = k)

# Melakukan pelatihan model terhadap data
neigh.fit(X_train,y_train)

# prediksi model dengan neigh.predict
yhat = neigh.predict(X_test)
print(yhat[0:10]) #data prediksi
print(y_test[0:10]) #data test

# Menampilkan akurasi data train set dan test set
from sklearn import metrics
print("Test set Accuracy: ", metrics.accuracy_score(y_test, yhat))
print("Train set Accuracy: ", metrics.accuracy_score(y_train, neigh.predict(X_train)))

# Mencari nilai K yang paling optimal
Ks = 100
mean_acc = np.zeros((Ks-1))
std_acc = np.zeros((Ks-1))
ConfustionMx = [];
for n in range(1,Ks):
    
    #Train Model and Predict  
    neigh = KNeighborsClassifier(n_neighbors = n).fit(X_train,y_train)
    yhat=neigh.predict(X_test)
    mean_acc[n-1] = metrics.accuracy_score(y_test, yhat)

    
    std_acc[n-1]=np.std(yhat==y_test)/np.sqrt(yhat.shape[0])

mean_acc

plt.plot(range(1,Ks),mean_acc,'g')
plt.fill_between(range(1,Ks),mean_acc - 1 * std_acc,mean_acc + 1 * std_acc, alpha=0.10)
plt.legend(('Accuracy ', '+/- 3xstd'))
plt.ylabel('Accuracy ')
plt.xlabel('Number of Nabors (K)')
plt.tight_layout()
plt.show()

print( "The best accuracy was with", mean_acc.max(), "with k=", mean_acc.argmax()+1)

# Melihat tingkat akurasi pada variable test
from sklearn.metrics import classification_report
print(classification_report(y_test, yhat.round()))

"""# Decition tree"""

# membagi dataset menjadi training dan testing
X_trainset, X_testset, y_trainset, y_testset = train_test_split(X, Y, test_size=0.2, random_state = 5)

# Membuat model decision tree
treeModel = DecisionTreeClassifier(criterion="gini", max_depth=5)

# melakukan pelatihan model terhadap data
treeModel.fit(X_trainset,y_trainset)

# prediksi model dengan tree_model.predict
predTree = treeModel.predict(X_testset)

# Untuk melihat akurasi, sejauh mana predTree memenuhi jawaban yang sesungguhnya yaitu y_testset
print (predTree [0:10])
print (y_testset [0:10])

# Menampilkan akurasi data train set dan test set

print("DecisionTrees's Test set Accuracy: ", metrics.accuracy_score(y_testset, predTree))
print("DecisionTrees's Train set Accuracy: ", metrics.accuracy_score(y_trainset, treeModel.predict(X_trainset)))

# Melihat tingkat akurasi pada variable test
from sklearn.metrics import classification_report
print(classification_report(y_testset, predTree.round()))

