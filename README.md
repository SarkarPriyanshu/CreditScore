<!-- <img src="https://rxresu.me/images/logos/logo.png" alt="Reactive Resume" width="256px" height="256px" /> -->

# Credit score classification Predictor

## [Summary] | [Problem Statement]

### Summary :
Given a person’s credit-related information, build a machine learning model that.

### Problem Statement :
You are working as a data scientist in a global finance company. Over the years, the company has collected basic bank details and gathered a lot of credit-related information. The management wants to build an intelligent system to segregate the people into credit score brackets to reduce the manual efforts.

## Table of Contents
  - [Basic Analysis](#basic-analysis)
  - [Data Cleaning](#data-cleaning)
  - [Data Preprocessing](#data-preprocessing)
  - [Model Selection](#model-selection-and-evaluations)
  - [Putting it Together](#putting-it-together)
  - [Flask and Api](#flask-and-api)
  - [Api Testing](#api-testing)

## Basic Analysis
### Asking basic question related to data
 
>>
    * What dimention we are working on?
        df.shape
    * How data looks?
        df.sample(5)
    * What datatype we are working with?
        df.info()
    * Is there any duplicated data present?
        df.duplicated().sum()
    * Is there any null value present in data?
        df.isnull().mean() * 100
    * On What scales different feature have and what distribution each feature have?
        df.describe()
    * What are the correlation between different features?
        df.cov() and df.corr()
>
> ### Observation
>> 
    * Having missing data in multiple features.
    * Skewed distribution.
    * Outliers.
    * categorical encoding required in multiple features.
    * Scaling required if working with linear models
    * Required lots of cleaning and data preprocessing 
      * Noisy data in various features
      
## Data Cleaning
>   After analying have to deal with multiple sub problems
> ### Sub Problems we faced working with this data
>>
    * Having special charecters on numeric feature and type conversion of data required.
    * Instead of null value special symbols are present in data to represent null entry.
    * Type of loan are stacked up in type of loan column so retrieve unique values and split them into n columns required
    * Type conversion required on various features
>

## Data Preprocessing
## Preprocessing steps

>   After analying have to deal with multiple sub problems
> ### Sub Problems we faced working with this data
>>
    * Data is missing not at random for many features as well as more than 5% of total population data are missing for various features
        We handle those kind of misssin value using missing indicator imputation technique
    * Missin data that are less than 5% of total population?
         We handle those kind of feature using median imputaion techniques due to skewed nature in distribution
    * Dealing with outlier?
        We had use IQR outlier technique due to skewed nature of ditribution of feature
    * Handling Skewed Nature in distribution
        Yoe johnson tranformations and square root tranformation give us sort of normal distribution so used this two techniques in various feature in our data.
    * Handling categorical data
        Label encoding for target column and one hot for 2 features and ordinal on 1 feature
    * On scales feature 
        We applied Standard scaler for scaling down feature std,max and mix values

## Model Selection and Evaluations
> ### Logistic Model and evaluation
>>
        Observation Logistic Regression:
          * Accuracy Score : 0.6378

          * GridSeachCV:
              - params : {'penalty':['l1','l2',None]}
              - best_score_: 0.62

          * Precision Score : 
               macro avg :      0.62
              - weighted avg:       0.64 
          * Recall Score :
              - macro avg :      0.58
              - weighted avg:       0.64
          * f1-score:
              - macro avg :      0.60
              - weighted avg:       0.63
        
> ### Support Vector Classifier Model and evaluation
>>
     Observation Support Vector Machine Classifier:
      * Accuracy Score : 0.69

      * GridSeachCV:
          - params :
                  {'C': 1, 'degree': 3, 'kernel': 'poly', 'max_iter': 200, 'verbose': True}
                  best_score_: 0.5342874999999999

                  {'gamma': 'scale', 'kernel': 'rbf', 'max_iter': 500, 'verbose': True}
                  best_score_: 0.43763749999999996

                  {'gamma': 'scale', 'kernel': 'rbf', 'max_iter': 1500, 'verbose': True}
                  best_score_ : 0.4786125

                  {'C': 1, 'kernel': 'rbf', 'max_iter': 5000, 'verbose': True}
                  best_score_ : 0.5951125
            
> ### AdaBoost Classifier and evaluation         
>>
     Observation of Adaboost
      * best Score :0.65255
      * best parameters : n_estimators=500,learning_rate=0.2,algorithm='SAMME.R'
      * training data : 0.653025
      * testing data : 0.6539
      - Auc_score : 0.7912295312807393
  
> ### XG boost Classifier and evaluation (Best Performer)
>>
     Observation of XgBoost
      * best parameters : n_estimators=200,reg_lambda=0.3,subsample=0.4,max_depth=6, gamma=3,booster='dart'
      * training data : 0.83975
      * testing data : 0.75025
      * Auc_score : 0.8911927496273545

> ### Random forest Classifier and evaluation
>>
     Observation of Random forest
      * best parameters : criterion='gini',max_depth=6,max_leaf_nodes=4,min_samples_leaf=2,min_samples_split=3,n_estimators=150
      * training data : 0.588925
      * testing data : 0.587
      * Auc_score : 0.7844111229987435
  
## Putting it Together
> ### We used pipeline and [feature_engine](https://feature-engine.readthedocs.io/en/latest/) for building whole work flow.
>>
    * Missing data imputation Observation
             - Occupation : missing indicator + Mode imputation
             - Monthly_Inhand_Salary: Missing indicator + median imputation
             - Type_of_Loan : Not decided add a feature if missing indicator (missing indicator + Mode imputation)
             - Num_of_Delayed_Payment: End of distribution imputation
             - Changed_Credit_Limit: Median imputation
             - Num_Credit_Inquiries: Median imputation
             - Credit_Mix: missing indicator + Mode imputation
             - Credit_History_Age : missing indicator + Mode imputation
             - Amount_invested_monthly : Median imputation
             - Payment_Behaviour : Add a missing indicator
             - Monthly_Balance : Median imputation
             - Credit_History_Age_years: missing indicator + Mode imputation
             - Credit_History_Age_months: missing indicator + Mode imputation
    * Handling Outliers
             - Month : No outliers
             - Age : IQR Capping
             - Anual Income : IQR Capping
             - Monthly Inhand Salary : IQR Capping
             - Num Bank Accounts : IQR Capping
             - Num Credi Cards : IQR Capping
             - Interest Rate : IQR Capping
             - Num of Loan : IQR Capping
             - Delay form due date : IQR Capping
             - Num of delayed payments : IQR Capping
             - Changed credit limit : IQR Capping
             - Num Credit Inquiries : IQR Capping
             - Outstanding debt : IQR Capping
             - credit utilization : IQR Capping
             - Total emi per month : IQR Capping
             - Amount invested monthly : IQR Capping
             - Monthly balance : IQR Capping        
    * Handling Skewed data
             - Annual_Income: yeo johnson tranformation 
             - Monthly_Inhand_Salary : Square root
             - Interest_Rate : yeo johnson tranformation 
             - Num_of_Loan : yeo johnson tranformation
             - Credit_Utilization_Ratio : square root tranformation
             - Total_EMI_per_month : square root tranformation
             - Amount_invested_monthly : square root tranformation
    * Handling categorical encoding
            - Occupation : onehot encoding
            - Payment_Behaviour : onehot encoding
            - Credit_Score :label encoding
           
## Flask and Api
>>
    * For backend we used [Flask](https://flask.palletsprojects.com/en/2.2.x/)
    
## Api Testing
>>
  * For Testing and documentaion we used [Postman](https://www.postman.com/)
  * For document [Click Here](https://github.com/SarkarPriyanshu/CreditScore/blob/main/Credit%20score%20classification%20APIs.postman_collection.json)

### [Sponsor By me]([https://github.com/SarkarPriyanshu])

## Technologies Used

- [Flask](https://flask.palletsprojects.com/en/2.2.x/), for backend
- [Jupyter Notebook](https://jupyter.org/), for Cleaning, Model traning & Evaluation
- [Postman](https://www.postman.com/), for Testing & Documentaions

## Chao

A passion project by [Priyanshu Sarkar] here is my [Github](https://github.com/SarkarPriyanshu) and  [CodeSandBox](https://codesandbox.io/u/SarkarPriyanshu)
