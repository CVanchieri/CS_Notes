### Sklearn LinearRegression Model Notes ###
''' Regression searches for relationships among variables, you need regression to answer whether and how some 
    phenomenon influences the other or how several variables are related, also useful when you want to 
    forecast a response using a new set of predictors.  '''

### Pros ###
# very simple to work with 
# easy to interpret results

### Cons ###
# numerical values only, categorical will not work 

''' model types '''
### simple linear Rrgression ###
# simple or single-variate linear regression is the simplest case of linear regression with a single independent variable, 𝐱 = 𝑥
# a straight-line fit to data
# y=ax+b, where a is commonly known as the slope, and b is commonly known as the intercept

### multiple linear regression ###
# multiple or multivariate linear regression icd s a case of linear regression with two or more independent variables

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
# encode data if necessary 
# set features and target datasets
# train/test split the data 
# scale the data if necessary 
# build the model, fit on the data, run the model
# run metrics, analyze/view results, adjust parameters, repeat until satisfied...

''' encoding data is '''


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


### model examples ###
''' Single & Multi Linear Regression model '''
### import ###
import pandas as pd
import numpy as np
import sklearn
### target is numerical float, no set category ###
### making a prediction of medical charges ###

### read in the data file ###
df = pd.read_csv('medical_insurance.csv')
### show the dataframe shape ###
print(df.shape)
### show the dataframe ###
df.head()

### view, inspect,understand the data ### 
df.describe()
df.isna().sum()
df.dtypes
df.corr() 

### check for feature outliers ### 
### view correlation graphs for each features ### 
import seaborn as sns 
sns.heatmap(df.corr() , cmap = 'Wistia' , annot = True)
sns.pairplot(df)
### view correlation graphs for each feature vs. target 'charges' ###
import matplotlib.pyplot as plt 
x_col = "charges"
y_columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
for y_col in y_columns:
    figure = plt.figure
    ax = plt.gca()
    ax.scatter(df[x_col], df[y_col])
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.set_title(f'''{x_col} vs {y_col}''')
    plt.show()
### view 2 feature correlation with trendline ###
# regplot
plt.title('Regression line Between Age and Charges')
sns.regplot(x = df['age'], y= df['charges'])
plt.show()
# swarmplot
plt.title('Relation Between BMI and Charges')
sns.swarmplot(x=df['smoker'],y = df['charges'] )
plt.show()
# barplot 
plt.title('Relation between Children and Charges')
sns.barplot(x=df['children'], y=df['charges'])
### view 3+ feature correlation with trendline ###
# lmplot
sns.lmplot(x = 'bmi',y = 'charges', hue = 'smoker' , data=df)
plt.show()
# single feature outlier check
import seaborn as sns 
sns.boxplot(y = 'age', data = df)

### function to find outliers ###
def outlier_zscore(data):
    global outliers,zscore
    outliers = []
    zscore = []
    threshold = 3.5
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score= (i - mean)/std 
        zscore.append(z_score)
        if np.abs(z_score) > threshold:
            outliers.append(i)
    print(outliers)
    return len(outliers), outliers
### run each feature wanted through the function ### 
age_outliers_number, age_outliers = outlier_zscore(df.age)
sex_outliers_number, sex_outliers = outlier_zscore(df.sex)
bmi_outliers_number, bmi_outliers = outlier_zscore(df.bmi)
children_outliers_number, children_outliers = outlier_zscore(df.children)
smoker_outliers_number, smoker_outliers = outlier_zscore(df.smoker)
region_outliers_number, region_outliers = outlier_zscore(df.region)
charges_outliers_number, charges_outliers = outlier_zscore(df.charges)
### removal of outliers from each feature ###
# removing the outliers of bmi 
for num, i in enumerate(df['bmi']):
    if i in bmi_outliers:
        df['bmi'][num] = 48.5
# removing the outliers of charges
for num, i in enumerate(df['charges']):
    if i in charges_outliers:
        df['charges'][num] = 55000.00000

### divide the data into features & target sets ###
# target is column 4, Petrol_Consumption
X = df.iloc[:, 0:6].values
y = df.iloc[:, 6].values

### split the into training and testing data sets ###
### import ###
from sklearn.model_selection import train_test_split
### set the train test split parameters ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
print(" Shape of x_train = ", X_train.shape)
print(" Shape of x_test = ", X_test.shape)
print(" Shape of y_train = ", y_train.shape)
print(" Shape of y_test = ", y_test.shape)

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
# set the y_pred prediction on the X test data
y_pred = regressor.predict(X_test)
### create data frame of predictions and results ### 
y_pred_df = pd.DataFrame(y_pred, columns=["Predicted Values" ])
y_test_df = pd.DataFrame(np.array(y_test), columns=["Real Values"])
pd.concat([y_test_df , y_pred_df] , axis=1)
### metrics to use for regression ###
# r2score, model accuracy
### import ###
from sklearn import metrics
print('intercept:', regressor.intercept_)
print('coefficients:', regressor.coef_)
score = metrics.r2_score(y_test , y_pred)
print("R2 Score : {}".format(score))
print("Model Accuracy: {}%".format(score * 100))


''' Polynomial Linear Regression model '''
''' Polynomial Regression is a form of linear regression in which the relationship between the independent 
variable x and dependent variable y is modeled as an nth degree polynomial. Polynomial regression fits a 
nonlinear relationship between the value of x and the corresponding conditional mean of y, denoted E(y |x) '''
### import ###
import pandas as pd
import numpy as np
import sklearn

''' Linear RidgeRegression model '''
### import ###
import pandas as pd
import numpy as np
import sklearn
### target is numerical float, no set category ###
### making a prediction of gas consumption for 48 US states ###

### read in the data file ###
df = pd.read_csv('insurance.csv')
### show the dataframe shape ###
print(df.shape)
### show the dataframe ###
df.head()

### function to find outliers ###
def outlier_zscore(data):
    global outliers,zscore
    outliers = []
    zscore = []
    threshold = 3.5
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score= (i - mean)/std 
        zscore.append(z_score)
        if np.abs(z_score) > threshold:
            outliers.append(i)
    print(outliers)
    return len(outliers), outliers
### run each feature wanted through the function ### 
age_outliers_number, age_outliers = outlier_zscore(df.age)
sex_outliers_number, sex_outliers = outlier_zscore(df.sex)
bmi_outliers_number, bmi_outliers = outlier_zscore(df.bmi)
children_outliers_number, children_outliers = outlier_zscore(df.children)
smoker_outliers_number, smoker_outliers = outlier_zscore(df.smoker)
region_outliers_number, region_outliers = outlier_zscore(df.region)
charges_outliers_number, charges_outliers = outlier_zscore(df.charges)
### removal of outliers from each feature ###
# removing the outliers of bmi 
for num, i in enumerate(df['bmi']):
    if i in bmi_outliers:
        df['bmi'][num] = 48.5
# removing the outliers of charges
for num, i in enumerate(df['charges']):
    if i in charges_outliers:
        df['charges'][num] = 55000.00000

### divide the data into features & target sets ###
# target is column 4, Petrol_Consumption
X = df.iloc[:, 0:6].values
y = df.iloc[:, 6].values

### split the into training and testing data sets ###
### import ###
from sklearn.model_selection import train_test_split
### set the train test split parameters ###
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### feature scaling ### 
### import ###
from sklearn.preprocessing import StandardScalar
### set the scalar ###
sc = StandardScalar()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

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


