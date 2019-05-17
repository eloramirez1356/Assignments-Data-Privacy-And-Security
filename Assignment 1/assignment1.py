# -*- coding: utf-8 -*-
"""
Eloy Ramirez Hernanz

CS-528

Homework 1 Problem 1

"""

#Libraries Needed for the implementation of the program
import pandas

#First, obtain all the different values from the 4 QI we are going to use.

dataDf = pandas.read_csv('D:\\Universidad\\IIT\\CS-528 Data Privacy And Security\\Assignments\\Assignment 1\\dataAssignment1.csv',
                          delimiter=';')

dataQiP1Df = dataDf[['Age','Education','Marital-Status','Race']]

#Defining variables for applying the hierarchies to the data
varAge = ''
varEducation = ''
varMaritalStatus = ''
varRace = ''

#Loop that iterates the dataset for applying the hierarchies to the data
for index, row in dataQiP1Df.iterrows():

    #Applying the hierarchy of Age
   if(row['Age']<35):
       varAge = 'Young'
   elif(row['Age']>=70):
       varAge = 'Old'
   elif(row['Age']<70 and row['Age']>=35):
       varAge = 'Adult'
   else:
       varAge = '*'
       
   dataQiP1Df.loc[index, 'Age'] = varAge
   
   #Applying the hierarchy of Education
   if(row['Education'].strip() == 'Bachelors' or row['Education'].strip() == 'Masters' or row['Education'].strip() == 'Doctorate' or row['Education'].strip() == 'Prof-school' or row['Education'].strip() == 'Some-college'):
       varEducation = 'Degree Level'
   elif(row['Education'].strip() == 'HS-grad' or row['Education'].strip() == 'Assoc-acdm' or row['Education'].strip() == 'Assoc-voc'):
       varEducation = 'High School Level'
   elif(row['Education'].strip() == '11th' or row['Education'].strip() == '9th' or row['Education'].strip() == '7th-8th' or row['Education'].strip() == '12th' or row['Education'].strip() == '1st-4th' or row['Education'].strip() == '10th' or row['Education'].strip() == '5th-6th' or row['Education'].strip() == 'Preschool'):
       varEducation = 'School Level or lower'
   else:
       varEducation = '*'
       
   dataQiP1Df.loc[index, 'Education'] = varEducation
   
   #Applying the hierarchy of Marital Status
   if(row['Marital-Status'].strip() == 'Divorced' or row['Marital-Status'].strip() == 'Widowed' or row['Marital-Status'].strip() == 'Never-married'):
       varMaritalStatus = 'Not Married'
   elif(row['Marital-Status'].strip() == 'Married-civ-spouse' or row['Marital-Status'].strip() == 'Separated' or row['Marital-Status'].strip() == 'Married-spouse-absent' or row['Marital-Status'].strip() == 'Married-AF-spouse'):
       varMaritalStatus = 'Married'
   else:
       varMaritalStatus = '*'
       
   dataQiP1Df.loc[index, 'Marital-Status'] = varMaritalStatus
   
   #Applying the hierarchy of Race
   if(row['Race'].strip() == 'Asian-Pac-Islander' or row['Race'].strip() == 'Amer-Indian-Eskimo'):
       varRace = 'American'
   elif(row['Race'].strip() == 'Other' or row['Race'].strip() == 'Black' or row['Race'].strip() == 'White'):
       varRace = 'General'
   else:
       varRace = '*'

   dataQiP1Df.loc[index, 'Race'] = varRace
   
   
#Obtaining the dataframe with the solution with the k-anonimity
dataQiP1Df.groupby(['Age','Education','Marital-Status','Race']).size().reset_index().rename(columns={0:'k'})

#Distorsion results
distorsion = ((1/2)+(1/2)+(1/2)+(1/2))/4

#Precision results
precision = 1-(((1/2)+(1/2)+(1/2)+(1/2)*32651)/32651*4)

   
