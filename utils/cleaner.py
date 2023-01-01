import re
import pandas as pd
import numpy as np

# This function cleans up the given data 
#  Handle missing and noisy data
class Cleaner:
    def __init__(self):
        self.LoanType = []

        # Handles the special character present in Age feature
    def handleAge(self,value):
        bad_chars=[';', ':', '!', "*",'_','-',"%",'#','$']  
        if type(value) == float :    
            pass
        else:
            if True if type(value)==int or type(value) == float else True if value.isnumeric() else False:
                return int(value)
            else:
                return int(''.join((filter(lambda i: i not in bad_chars,
                                      value)))) 
    
    # Handles the special character present in AnnualIncome feature
    def handleAnnualIncome(self,value):
        bad_chars=[';', ':','-','!', "*",'_',"%",'#','$']
        if True if type(value)==int or type(value) == float else True if value.isnumeric() else False:
            return float(value)
        else:
            return float(''.join((filter(lambda i: i not in bad_chars,
                                  value))))
    
    # Handles the special character present in AnnualIncome feature
    def handleNum_of_Delayed_Payment(self,value):
        bad_chars=[';', ':','-','!', "*",'_',"%",'#','$']
        if type(value) == float:
            return value
        # This condition check if the recieved value is int type or string type based on that it apply certain operations
        elif True if type(value)==int or type(value) == float else True if value.isnumeric() else False:
                return int(value)
        else:
            return int(''.join((filter(lambda i: i not in bad_chars,
                                          value))))
    
    def isFloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False
    # Handles the special character present in Changed_Credit_Limit feature
    def handleChanged_Credit_Limit(self,value):
        bad_chars=[';', ':', '!','-',"*",'_',"%",'#','$']
        if self.isFloat(value):
            return float(value)
        elif value == '_':
            return np.nan
        else:
            return int(''.join((filter(lambda i: i not in bad_chars,
                                                  value))))
    # Handles the special character present in Changed_Credit_Limit feature
    def handleCredit_History_Age(self,value):
        if type(value) == float:
            return value 
        else:
            return ' '.join([item for item in value.split(' ') if item.isnumeric()])
        
    # Handles the special character present in Amount_invested_monthly feature    
    def handleAmount_invested_monthly(self,value):
        bad_chars=[';', ':','-','!', "*",'_',"%",'#','$']
        if type(value) == float:
            return value
        # This condition check if the recieved value is int type or string type based on that it apply certain operations
        elif True if type(value)==int or type(value) == float else True if value.isnumeric() else False:
            return float(value)
        else:
            return float(''.join((filter(lambda i: i not in bad_chars,
                                                  value))))     
    
    # return unique values from type of loan   
    def typesOfLoans(self,df):
        for value in df['Type_of_Loan'].unique():
            if type(value) != float: 
                for item in value.split(','):
                    if 'and' in item:
                        if item.split('and')[1].strip() not in self.LoanType:
                            self.LoanType.append(item.split('and')[1].strip())
                    else:
                        if item.strip() not in self.LoanType:
                            self.LoanType.append(item.strip())     
            else:
                pass  

        return self.LoanType

    # Check for na valus
    def checkNa(self,index,data):
        if type(data[index])==float or data[index] == '_':
            data[f'{index}_Na'] = 1
        else:
            data[f'{index}_Na'] = 0
        return data 

    # Check for particular loan assign 1 to related index    
    def checkTypeOfLoan(self,loan,data):
        if type(loan) == str:
            for value in self.LoanType:
                if value in loan:
                    data[f'Type_of_Loan_{value}'] = 1
            else:
                data['Type_of_Loan_Na'] = 0.0 
        else:
            data['Type_of_Loan_Na'] = 1.0
        
        return data 

    # Handle Credit_History_Age_ value split the data into two feature
    def handleSplitCredit_History_Age(self,value,data):
        if type(value) == str:
            data['Credit_History_Age_years'] = int(value.split()[0])
            data['Credit_History_Age_months'] = int(value.split()[1])
        else:
            data['Credit_History_Age_years'] = value
            data['Credit_History_Age_months'] = value
        return data

    # get data from user clean,preprocess it and then return it as numpy array 
    def handleRandom(self,df):
        arrayOfData = []
        randomRow = np.random.randint(0, df.shape[0])
        extraRandomRow = np.random.randint(0, df.shape[0])
        for index in [randomRow,extraRandomRow]:
            arrayOfData.append(self.handleclean(randomRow,df))
        return arrayOfData

    # get data from user clean the data and return that data to user.
    def handleclean(self,randomRow=None,df=None,userData=None):
        data = None
        if isinstance(userData, pd.Series):
            data = userData
            data = data.iloc[2:]
        else:
            data = df.loc[randomRow,]
            data = data.iloc[2:]         
        
        
        #Cleaning data         
        data['Age'] = self.handleAge(data['Age'])
        data['Annual_Income'] = self.handleAnnualIncome(data['Annual_Income'])
        data['Num_of_Loan'] = self.handleAge(data['Num_of_Loan'])
        data['Num_of_Delayed_Payment'] = self.handleNum_of_Delayed_Payment(data['Num_of_Delayed_Payment'])
        data['Changed_Credit_Limit'] = self.handleChanged_Credit_Limit(data['Changed_Credit_Limit'])
        data['Outstanding_Debt'] = self.handleAnnualIncome(data['Outstanding_Debt'])
        data['Credit_History_Age'] = self.handleCredit_History_Age(data['Credit_History_Age'])
        data = self.handleSplitCredit_History_Age(data['Credit_History_Age'],data)
        data['Amount_invested_monthly'] = self.handleAmount_invested_monthly(data['Amount_invested_monthly'])
        data['Monthly_Balance'] = self.handleAmount_invested_monthly(data['Monthly_Balance'])
        
        for feature in [f'Type_of_Loan_{loan}' for loan in self.typesOfLoans(df)]:
            data[feature] = 0
        
        if bool(re.match('^[_______]*$',data['Occupation'])) == True:
            data['Occupation_Na'] = 1
        else:
            data['Occupation_Na'] = 0
            
        if type(data['Monthly_Inhand_Salary']) == float:
            data['Monthly_Inhand_Salary_Na'] = 1
        else:
            data['Monthly_Inhand_Salary_Na'] = 0


        data = self.checkTypeOfLoan(data['Type_of_Loan'],data)
        data = self.checkNa('Credit_Mix',data)
        data = self.checkNa('Credit_History_Age',data)
        data = self.checkNa('Payment_Behaviour',data)
        del data['Name']
        del data['SSN']
        del data['Type_of_Loan']
        del data['Credit_History_Age']    
        if data['Credit_Score']:
            del data['Credit_Score']    
        return data
        
        
