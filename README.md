Response


JSON








{
  "message": {
    "content": "Problem Statement You are working as a data scientist in a global finance company. Over the years, the company has collected basic bank details and gathered a lot of credit-related information. The management wants to build an intelligent system to segregate the people into credit score brackets to reduce the manual efforts.",
    "header": "Credit score classification",
    "summary": "Given a person’s credit-related information, build a machine learning model that."
  },
  "resultStatus": "SUCCESS"
}




What it do?
This api get some of financial related data and returns the credit score
result : 1 means customer have a Good credit score.
result : 2 means customer have a Standard credit score.
result : 3 means customer have a Poor credit score.

Why this Api?
Well banking and financial bodies need to know about certain custumers credit score before taking some sort of action on that customer, it can be anything like, providing aid by giving loan or any sort of benefits, or taking legal action on customer based on his/her past behaviour and factors like credit score.
How to use?


Python








http://localhost:5000/predict


Expected input data


JSON








{
  "ID": "0x94d1",
  "Customer_ID": "CUS_0xbfe8",
  "Month": "April",
  "Name": "Ellen Freilichl",
  "Age": 15,
  "SSN": "29-08-5018",
  "Occupation": "Entrepreneur",
  "Annual_Income": 15007.61,
  "Monthly_Inhand_Salary": 1135.634167,
  "Num_Bank_Accounts": 6,
  "Num_Credit_Card": 6,
  "Interest_Rate": 27,
  "Num_of_Loan": -100,
  "Type_of_Loan": "Credit-Builder Loan, Mortgage Loan, Auto Loan",
  "Delay_from_due_date": 30,
  "Num_of_Delayed_Payment": 16,
  "Changed_Credit_Limit": 15.28,
  "Num_Credit_Inquiries": 13,
  "Credit_Mix": "Standard",
  "Outstanding_Debt": 2530.81,
  "Credit_Utilization_Ratio": 34.049925,
  "Credit_History_Age": "16 Years and 0 Months",
  "Payment_of_Min_Amount": "Yes",
  "Total_EMI_per_month": 49.658257,
  "Amount_invested_monthly": 100.15900461026104,
  "Payment_Behaviour": "Low_spent_Small_value_payments",
  "Monthly_Balance": 253.74615507352132,
  "Credit_Score": "Standard"
}


Resultant Prediction


JSON








{
    "result": "1"
}




