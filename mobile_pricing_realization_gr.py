import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression,LogisticRegression,RandomForestClassifier
from sklearn.model_selection import KFold, cross_val_score,StratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score,roc_curve
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor,GradientBoostingClassifier
data=pd.read_csv(r"C:\JAY_python\RESOURCES\DL_Sep24\Datasets\project-intership\MOBILE_PRICING\Mobile Phone Pricing\dataset.csv")


X=data.drop('price_range',axis=1)
y=data['price_range']
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.3, random_state = 23)

data['price_range'].value_counts(normalization=True)

kfold = StratifiedKFold(n_splits=5,shuffle= True,random_state= 24)
params = {'learning_rate':[0.1,0.3,.5],
          'max_depth':[None,3],
          'n_estimators':[150,100,50]}
gbm = GradientBoostingClassifier(random_state=24)
gcv = GridSearchCV(gbm, param_grid = params, cv = kfold,verbose=3,
                   scoring='accuracy')

gcv.fit(X,y)
print(gcv.best_params_)
print(gcv.best_score_)

best_model = gcv.best_estimator_


###########

import pickle
filehandler = open("C:\JAY_python\pkl_file\mobile_price", 'wb') 
pickle.dump(best_model, file=filehandler)
filehandler.close()


###################