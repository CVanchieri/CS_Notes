### Sklearn RandomForest Models Notes ###
''' The fundamental idea behind a random forest is to combine many decision trees into a single model. Individually, predictions made by 
    decision trees (or humans) may not be accurate, but combined together, the predictions will be closer to the mark on average. '''

### Pros ###
# can handle large datasets 
# less influenced by outliers in the data
# no assumptions about underlying distributions in the data
# can implicitly handle collinearity in features, highly similar features 
# work well with heterogeneous features, categorical and numerical, mixing different range values 

### Cons ###
# robust algorithm makes it more complex tougher to analyze small details 
# not best to determine feature and target relationships/effects due to working with highly similar features

''' model set up steps '''
### setup steps ###
# load the data
# determine regression or classification target
# clean and organize the data
# set features and target datasets
# train/test split the data 
# scale the data if necessary 
# build the model, fit on the data, run the model
# run metrics, analyze/view results, adjust parameters, repeat until satisfied...


''' scaling data is the process of increasing or decreasing the magnitude according to a fixed ratio '''
# good practice to scale data
# helps handling disparities in units
# improves performance reduces variability 
### scalar types ###
# StandardScalar, removes the mean and scales the data to unit variance. The scaling shrinks the range of the feature values, does not do well with outliers 
# MinMaxScalar, rescales the data set such that all feature values are in the range [0, 1], does not do well with outliers 
# MaxAbsScaler, similar to MinMaxScaler except that the values are mapped in the range [0, 1], positives only, does not do well with outliers 
# RobustScaler, based on percentiles and are therefore not influenced by a few number of very large marginal outliers, resulting range of the transformed feature values is larger
# PowerTransformer, a power transformation to each feature to make the data more Gaussian-like in order to stabilize variance and minimize skewness
# QuantileTransformer (uniform output), a non-linear transformation such that the probability density function of each feature will be mapped to a uniform or Gaussian distribution
# QuantileTransformer (uniform gaussian), map to a Gaussian distribution, set the parameter output_distribution='normal'
# Normalizer, rescales the vector for each sample to have unit norm, independently of the distribution of the samples


''' model hyperparameter tuning ''' 
### optional parameters ### 
# max_depth,  the longest path between the root node and the leaf node, limit up to what depth I want every tree in my random forest to grow, can overfit test data if to big, macro level
# min_sample_split, the minimum required number of observations in any given node in order to split it, increasing can minimized difference between train and test score, can underfit if to big 
# max_leaf_nodes, sets a condition on the splitting of the nodes, If after splitting we have more terminal nodes than the specified number of terminal nodes, it will stop the splitting and the tree
# min_samples_leaf, specifies the minimum number of samples that should be present in the leaf node after splitting a node, increasing can minimize overfitting, can underfit if to large 
# n_estimators, determines the number of 'trees' used in the model, increasing can improve results but time complexity also increases, start at 200
# max_sample (bootstrap sample), determines what fraction of the original dataset is given to any individual tree, will reduce the training time of the model, each tree does not need all the data
# max_features, resembles the number of maximum features provided to each tree, default value is set to square root of the number of features present in the dataset, helps with overfitting, can underfit if to large 


### model examples ###
''' RandomForestRegression model '''
### import ###
import pandas as pd
import numpy as np
import sklearn
### target is numerical float, no set category ###
### making a prediction of gas consumption for 48 US states ###

### read in the data file ###
df = pd.read_csv('petrol_consumption.csv')
### show the dataframe shape ###
print(df.shape)
### show the dataframe ###
df.head()

### divide the data into features & target sets ###
# target is column 4, Petrol_Consumption
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

### split the into training and testing data sets ###
### import ###
from sklearn.model_selection import train_test_split
### set the train test split parameters ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### feature scaling ### 
### import ###
from sklearn.preprocessing import StandardScaler
### set the scalar ###
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### train the RandomForest model ###
### import ###
from sklearn.ensemble import RandomForestRegressor
### set the regressor model with parameteres ###
regressor = RandomForestRegressor(n_estimators=20, # 20 estimators, # of trees used
                                  random_state=0)
# changing n_estimators # of trees decreased error, increasing to 200 was better
# fit the model on the X, Y train data
regressor.fit(X_train, y_train)
# set the y_pred prediction on the X test data
y_pred = regressor.predict(X_test)

### metrics to use for regression ###
# mean absolute error
# mean squared error
# root mean squared error
### import ###
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
### manipuate n_estimoars # of trees to reduce root mean squared error ###
# around 200 trees the decrease stops
### set the regressor model with parameteres ###
regressor = RandomForestRegressor(n_estimators=200, # 20 estimators, # of trees used
                                  random_state=0)
# fit the model on the X, Y train data
regressor.fit(X_train, y_train)
# set the y_pred prediction on the X test data
y_pred = regressor.predict(X_test)
### evaluate the model ### 
### metrics to use for regression ###
# mean absolute error
# mean squared error
# root mean squared error
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


''' RandomForest Classification model '''
### import ###
import pandas as pd
import numpy as np
import sklearn
### target is a set 'category', binary true or false ###
### making a prediction if a bank note is authentic or not ###

### read in the data file ###
df = pd.read_csv('bill_authentication.csv')
### show the dataframe shape ###
print(df.shape)
### show the dataframe ###
df.head()

### divide the data into features & target sets ###
# target is column 4, Class
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

### split the into training and testing data sets ###
### import ###
from sklearn.model_selection import train_test_split
### set the train test split parameters ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### feature scaling ### 
### import ###
from sklearn.preprocessing import StandardScaler
### set the scalar ###
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### train the RandomForest model ###
### import ###
from sklearn.ensemble import RandomForestClassifier
### set the classifier model with parameteres ###
classifier = RandomForestClassifier(n_estimators=20, # 20 estimators, # of trees used
                                  random_state=0)
# changing n_estimators # of trees did not incease accuracy, 20 was best
# fit the model on the X, Y train data
classifier.fit(X_train, y_train)
# set the y_pred prediction on the X test data
y_pred = classifier.predict(X_test)

### metrics to use for classification ###
# accuracy
# confusion matrix
# precision recall
# f1 
### import ###
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))


''' hyperparameter tuning ''' 
# sometimes a basic model will score high enough 
# tuning may not always help 

### RandomForest Classification model ###
### GridSearchCV ###
### import ###
import pandas as pd
import numpy as np
import sklearn
### target is a set 'category', binary true or false ###
### making a prediction if a bank note is authentic or not ###

### read in the data file ###
df = pd.read_csv('bill_authentication.csv')
### show the dataframe shape ###
print(df.shape)
### show the dataframe ###
df.head()

### divide the data into features & target sets ###
# target is column 4, Class
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

### split the into training and testing data sets ###
### import ###
from sklearn.model_selection import train_test_split
### set the train test split parameters ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### feature scaling ### 
### import ###
from sklearn.preprocessing import StandardScaler
### set the scalar ###
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### import ###
from sklearn.ensemble import RandomForestClassifier
### set the classifier model ###
classifier = RandomForestClassifier()

### create the param grid with the attributes wanted ###
param_grid = { 
    'n_estimators': [20, 100, 200], # 
    'max_features': ['auto', 'sqrt', 'log2'], # 
    'max_leaf_nodes' : [2, 6, 10], # 
    'max_depth' : [5, 15, 25], # 
    'min_samples_split' : [2, 10, 15], # 
    'bootstrap': [True, False], # 
    'criterion' :['gini', 'entropy'] # 
    }

### imports ###
from sklearn.model_selection import GridSearchCV
### initiate the GridSearchCV with the model, param grid, attributes 
CV_rfc = GridSearchCV(estimator=classifier, param_grid=param_grid, cv=3) 
### parameters ###
# estimator, estimator object, sklearn model to be used 
# param_grid, doct or list of dicts, keys and lists of parameter settings to try as values
# scoring, string, callable, list, tuple, dict, default none, strategy to evaluate the performance of the cross-validated model on the test set
# n_jobs, int, number of jobs to run in parallel
# pre_dispatch, int or str, default n_jobs, controls the number of jobs that get dispatched during parallel execution
# cv, int, cross-validation generator or an iterable, default None, determines the cross-validation splitting strategy
# refit, bool, str or callable, default True, Refit an estimator using the best found parameters on the whole dataset
# verbose, int, controls the verbosity, the higher, the more messages
# error_score, ‘raise’ or numeric, default np.nan, value to assign to the score if an error occurs in estimator fitting
# return_train_score, bool, default False, If False, the cv_results_ attribute will not include training scores
%time CV_rfc.fit(X_train, y_train)
CV_rfc.best_params_

### RandomForest Classification model ###
### RandomizedSearchCV ###
### import ###
import pandas as pd
import numpy as np
import sklearn
### target is a set 'category', binary true or false ###
### making a prediction if a bank note is authentic or not ###

### read in the data file ###
df = pd.read_csv('bill_authentication.csv')
### show the dataframe shape ###
print(df.shape)
### show the dataframe ###
df.head()

### divide the data into features & target sets ###
# target is column 4, Class
X = df.iloc[:, 0:4].values
y = df.iloc[:, 4].values

### split the into training and testing data sets ###
### import ###
from sklearn.model_selection import train_test_split
### set the train test split parameters ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### feature scaling ### 
### import ###
from sklearn.preprocessing import StandardScaler
### set the scalar ###
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

### import ###
from sklearn.ensemble import RandomForestClassifier
### set the classifier model ###
classifier = RandomForestClassifier()

### create the param grid with the attributes wanted ###
param_grid = { 
    'n_estimators': [20, 200], # 
    'max_features': ['auto', 'sqrt', 'log2'], # 
    'max_leaf_nodes': [2, 20], # 
    'max_depth': [5, 50], # 
    'min_samples_split': [2, 10, 20], # 
    'bootstrap': [True, False], # 
    'criterion': ['gini', 'entropy'] # 
    }

### imports ###
from sklearn.model_selection import RandomizedSearchCV
### initiate the RandomizedSearchCV with the model, param grid, attributes 
RCV_rfc = RandomizedSearchCV(classifier, param_grid, cv=3, n_jobs=2) 
### parameters ###
# estimator, estimator object, sklearn model to be used 
# param_grid, doct or list of dicts, keys and lists of parameter settings to try as values
# scoring, string, callable, list, tuple, dict, default none, strategy to evaluate the performance of the cross-validated model on the test set
# n_jobs, int, number of jobs to run in parallel
# pre_dispatch, int or str, default n_jobs, controls the number of jobs that get dispatched during parallel execution
# cv, int, cross-validation generator or an iterable, default None, determines the cross-validation splitting strategy
# refit, bool, str or callable, default True, Refit an estimator using the best found parameters on the whole dataset
# verbose, int, controls the verbosity, the higher, the more messages
# error_score, ‘raise’ or numeric, default np.nan, value to assign to the score if an error occurs in estimator fitting
# return_train_score, bool, default False, If False, the cv_results_ attribute will not include training scores
%time RCV_rfc.fit(X_train, y_train)
RCV_rfc.best_params_

