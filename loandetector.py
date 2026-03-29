import pandas as pd#importing pandas library
from sklearn.linear_model import LogisticRegression # Importing Logistic Regression library 
input1 = {
    'IncomeL':[1, 1, 0, 0, 1, 0, 1, 0, 1, 0],#using mathematical way to denote High And Low As it does not understand English 
    'CreditH': [1, 1, 0, 0, 1, 0, 1, 0, 1, 0], # using mathematical way to denote Good Credit And Bad Credit As it does not understand English
    'LoanA':[1, 1, 0, 0, 1, 0, 1, 0, 1, 0]# using approved and rejected as 0 and 1
}# Data Given
de = pd.DataFrame(input1)#We now organize the following data in a proper organized way
a = de[['Income', 'Credit']]#It is an input we give to get the output which is stored in a which is independent variable
b = de['Approved']#It is dependent variable and is the output 
m = LogisticRegression()#Using Logical Regression
m.fit(a,b)#used to instruct the computer to form relation between input and output 
try:
    # User Data Input
    uincome = int(input("Enter Income[1 for Income>3 lakh per year(annum), 0 for <3 lakh per year(annum)]: "))#Getting Input from user for income
    ucredit = int(input("Enter Credit History as [1 for CIBIL Score>= 750, 0 for <= 600 and >= -1]: "))#Getting Input from user for credit
    user = [[uincome, ucredit]]#Stores income and credit in a matrix form

    prob = m.predict_proba(user)[0][1]#Calculates Probabilty
    pred=m.predict(user)#Used for predicting 
    print("Analysis for Person:")#Shows analysis for an person 
    print(f"Approval Chances: {prob * 100:.2f}%")#Showing Proabilty in form of percentage
    if pred[0]==1:
      print("Approved")#Shows its Approved
    else:
      print("Rejected")#Shows its Rejected 
except :
    print("Error: Please enter only numbers (0 or 1).")#Tells the user to enter 0 or 1 for getting to know about loan
