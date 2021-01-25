### Sklearn LinearRegression Model Notes ###
''' Regression searches for relationships among variables, you need regression to answer whether and how some 
    phenomenon influences the other or how several variables are related, also useful when you want to 
    forecast a response using a new set of predictors.  '''

### Pros ###
# very simple to work with 
# easy to interpret results

### Cons ###

''' model types '''
### simple linear Rrgression ###
# simple or single-variate linear regression is the simplest case of linear regression with a single independent variable, 𝐱 = 𝑥

### multiple linear regression ###
# multiple or multivariate linear regression is a case of linear regression with two or more independent variables

### polynomial regression ###
# you can regard polynomial regression as a generalized case of linear regression. You assume the polynomial dependence between the output and inputs and, consequently, the polynomial estimated regression function

### ridge regression ###
# 

### lasso regression ###
#

### elasticnet regression ###
#

''' model set up steps '''
### setup steps ###
# load the data
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
''' Single & Multi Linear Regression model '''
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

### train the Single/Multi LinearRegression model ###
### import ###
from sklearn.linear_model import LinearRegression
### set the regressor model with parameteres ###
regressor = LinearRegression()
# fit the model on the X, Y train data
regressor.fit(X_train, y_train)
### best intercet & slope 
print(regressor.intercept_)
print(regressor.coef_)
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
### best intercet & slope 
r_sq = regressor.score(x_, y_train)
print('coefficient of determination:', r_sq)
print('intercept:', regressor.intercept_)
print('coefficients:', regressor.coef_)
from sklearn.model_selection import cross_val_score
# storing the ten scores in an object called mse
mse = cross_val_score(regressor,X_train,y_train,scoring='neg_mean_squared_error',cv=10)
print('mse', mse.mean())

''' Polynomial Linear Regression model '''
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
from sklearn.preprocessing import Normalizer
### set the scalar ###
nm = Normalizer()
X_train = nm.fit_transform(X_train)
X_test = nm.transform(X_test)

### train the PolynomialRegression model ###
### import ###
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
### initiate the Polynomial and fit transform the data ###
x_ = PolynomialFeatures(degree=2, include_bias=False).fit_transform(X_train)
### set the regressor model ###
regressor = LinearRegression().fit(x_, y_train)
# set the y_pred prediction on the X test data
y_pred = regressor.predict(x_)
### import ###
from sklearn import metrics
### metrics to use for regression ###
# mean absolute error
# mean squared error
# root mean squared error
print('Mean Absolute Error:', metrics.mean_absolute_error(y_train, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_train, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_train, y_pred)))
### best intercet & slope 
r_sq = regressor.score(x_, y_train)
print('coefficient of determination:', r_sq)
print('intercept:', regressor.intercept_)
print('coefficients:', regressor.coef_)
from sklearn.model_selection import cross_val_score
# storing the ten scores in an object called mse
mse = cross_val_score(regressor,x_, y_train,scoring='neg_mean_squared_error',cv=10)
print('mse', mse.mean())


''' Linear RidgeRegression model '''
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
from sklearn.preprocessing import Normalizer
### set the scalar ###
nm = Normalizer()
X_train = nm.fit_transform(X_train)
X_test = nm.transform(X_test)

### train the Linear Ridge model ###
### import ###
from sklearn.linear_model import Ridge
from sklearn.model_selection import GridSearchCV
### set the regressor model with parameteres ###

alpha_values = {'alpha':[0.001, 0.01,0.02,0.03,0.04, 0.05, 0.06, 0.08, 1, 2, 3, 5, 8, 10, 20, 50, 100]}
ridge = GridSearchCV(Ridge(), alpha_values, scoring='neg_mean_squared_error', cv=10)
ridge.fit(X_train,y_train)

print(ridge.best_params_)
print(ridge.best_score_)

''' Linear LassoRegression model '''
### train the Linear Lasso model ###
### import ###
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
### set the regressor model with parameteres ###

alpha_values = {'alpha':[0.001, 0.01,0.02,0.03,0.04, 0.05, 0.06, 0.08, 1, 2, 3, 5, 8, 10, 20, 50, 100]}
lasso = GridSearchCV(Lasso(), alpha_values, scoring='neg_mean_squared_error', cv=10)
lasso.fit(X_train,y_train)

print(lasso.best_params_)# fit the model on the X, Y train data
print(lasso.best_score_)

''' Linear ElasticnetRegression model '''
### train the Linear ElasticNet model ###
### import ###
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import GridSearchCV
### set the regressor model with parameteres ###

alpha_values = {'alpha':[0.001, 0.01,0.02,0.03,0.04, 0.05, 0.06, 0.08, 1, 2, 3, 5, 8, 10, 20, 50, 100]}
elastic = GridSearchCV(ElasticNet(), alpha_values, scoring='neg_mean_squared_error', cv=10)
elastic.fit(X_train,y_train)

print(elastic.best_params_)# fit the model on the X, Y train data
print(elastic.best_score_)







### scaling ### 
# standardization, standardizing the features around the center and 0 with a standard deviation of 1 is important when we compare measurements that have different units, useful when your data has varying scales and the algorithm you are using does make assumptions about your data having a Gaussian distribution
# normalization, normalization is to change the values of numeric columns in the dataset to a common scale, without distorting differences in the ranges of values, use when you do not know the distribution of your data or when you know the distribution is not Gaussian (a bell curve)
# 
# 
# 


