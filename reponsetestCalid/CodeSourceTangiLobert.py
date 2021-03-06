#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.externals import joblib
import numpy as np

def predict(df):
    
    data = pd.read_csv('train.csv') #chargement des données
    Xenc = OneHotEncoder() #préparation des encodeurs
    Yenc = OneHotEncoder()

    X = data.drop(columns=['class']) # séparation des résultats des données
    Y = np.array(data['class']).reshape(-1,1)# passage a un tableau 2D car fit() n'accepte pas les listes
    Xenc.fit(X)#création des encodeurs
    Xenc.transform(X)#encodage
    Yenc.fit(Y)
    Yenc.transform(Y)
    X_train , X_test , Y_train , Y_test = train_test_split(X,Y, test_size=0.1)#séparation des données pour que 10% soit réserver aux tests


    model = DecisionTreeClassifier()#création du model
    model.fit(Xenc.transform(X_train).toarray(), Yenc.transform(Y_train).toarray())#entrainement du model
    predictions=model.predict(Xenc.transform(X_test).toarray())#prédiction pour tester la précision
    accuracy_score(Yenc.transform(Y_test),predictions)#test de la précision
    joblib.dump(model,'test2.joblib')#rend le model persistent mais ne fonctionne pas car les données apprentissage sont encodées ainsi que les réponses
    return pd.Series(Yenc.inverse_transform(model.predict(Xenc.transform(df).toarray())).tolist())
    #retourne une série Pandas mais il faut 1: encoder les données  2: prédire 3:inverser l'encodage de la réponse 4: en faire une liste


if __name__ == "__main__":
    df = pd.read_csv('evaluation.csv')
    y = predict(df)
    evaluate(y,true_y)

