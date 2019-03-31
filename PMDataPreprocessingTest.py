import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_excel('PMinportTest.xlsx')
#Check for missing values
dataset.isnull().sum()
#Fill up missing values of categorical valriables

dataset['status'].fillna("Unknown",inplace=True)
dataset['Genre 1'].fillna("None",inplace=True)
dataset['Genre 2'].fillna("None",inplace=True)
dataset['Genre 3'].fillna("None",inplace=True)
dataset['Genre 4'].fillna("None",inplace=True)
dataset['Genre 5'].fillna("None",inplace=True)
dataset['Genre 6'].fillna("None",inplace=True)
dataset['Genre 7'].fillna("None",inplace=True)
dataset['Genre 8'].fillna("None",inplace=True)
dataset['Title'].fillna("Unknown",inplace=True)
X = dataset.iloc[:,0:21].values
Y=dataset.iloc[:,-1].values


#Taking care of missing data
from sklearn.preprocessing import Imputer

# Imputing the NUMERIC COLUMNS with mean
#Budget
imputer1=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer1=imputer1.fit(X[:,3:4])
X[:,3:4]=imputer1.transform(X[:,3:4])

#Popularity
imputer1=Imputer(missing_values="NaN",strategy='mean',axis=0)
imputer1=imputer1.fit(X[:,13:14])
X[:,13:14]=imputer1.transform(X[:,13:14])

#Revenue
imputer1=imputer1.fit(X[:,17:18])
X[:,17:18]=imputer1.transform(X[:,17:18])

#Runtime
imputer1=imputer1.fit(X[:,18:19])
X[:,18:19]=imputer1.transform(X[:,18:19])

#Handling Categorical Variables

D_Adult=pd.get_dummies(X[:,1])
D_Adult.columns=['Adult','Not Adult']
D_Collection=pd.get_dummies(X[:,2])
D_Collection.columns=['NotInCollection','InCollection']
D_Genre1=pd.get_dummies(X[:,5])
D_Genre2=pd.get_dummies(X[:,6])
D_Genre3=pd.get_dummies(X[:,7])
D_Genre4=pd.get_dummies(X[:,8])
D_Genre5=pd.get_dummies(X[:,9])
D_Genre6=pd.get_dummies(X[:,10])
D_Genre7=pd.get_dummies(X[:,11])
D_Genre8=pd.get_dummies(X[:,12])
D_Status=pd.get_dummies(X[:,19])




#Handling Categorical variables like ExYear , month and day
S_Year=dataset['ExYear']
S_Year=S_Year.astype('category')
S_Year=pd.DataFrame(S_Year)

S_Month=dataset['ExMonth']
S_Month=S_Month.astype('category')
S_Month=pd.DataFrame(S_Month)

S_Day=dataset['ExDay']
S_Day=S_Day.astype('category')
S_Day=pd.DataFrame(S_Day)


S_Eng=dataset['English /Non English']
S_Eng=S_Eng.astype('category')
S_Eng=pd.DataFrame(S_Eng)


# Feature scaling
# ---------------
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train.columns=['ID','Adult','Collection','budget','G1','G2','G3','G4','G5','G6','G7','G8','Eng','popularity','ExYear','ExMonth','ExDay','revenue','runtime','status','title']

xdf=pd.DataFrame(X)
xdf.columns=['ID','Adult','Collection','budget','G1','G2','G3','G4','G5','G6','G7','G8','Eng','popularity','ExYear','ExMonth','ExDay','revenue','runtime','status','title']
df=xdf[['budget','popularity','revenue','runtime']]

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
df=sc_X.fit_transform(df)
df=pd.DataFrame(df)
df.columns=['budget','popularity','revenue','runtime']


CleanedX=pd.DataFrame(xdf['ID'])
CleanedX=pd.concat([CleanedX,D_Adult,D_Collection,
                    S_Eng,
                    S_Year,S_Month,S_Day,
                    D_Status
                    ],axis=1)

CleanedX.to_csv('CleanedCategoricalTest.csv')
num=xdf[['budget','popularity','revenue','runtime']]


y=dataset['Target Success']
y.to_csv('CleanedYTest.csv')

df.to_csv('CleanedNumericTest.csv')











