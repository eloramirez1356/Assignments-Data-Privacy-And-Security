# -*- coding: utf-8 -*-
"""
Eloy Ramirez Hernanz

CS-528

Homework 1 Problem 2. Laplacian Mechanism
"""

   
   
#Libraries Needed for the implementation of the program
import pandas
import numpy

dataDf = pandas.read_csv('D:\\Universidad\\IIT\\CS-528 Data Privacy And Security\\Assignments\\Assignment 1\\dataAssignment1.csv',
                          delimiter=';')

#First, obtain all the different values from the 4 QI we are going to use.
dataQiP2Df = dataDf[['Age','Education','Marital-Status','Race']]

##Create new dataset with the values for obtaining the mean, from 25 to 90
dfProblem2 = dataQiP2Df[dataQiP2Df.Age > 24]

#Here I create the three groups requested in question 1

generated1000dfOriginal = dfProblem2.head(1000)
generated1000dfWithout90 = dfProblem2.head(1000)
idx = generated1000dfWithout90.index[generated1000dfWithout90['Age']==90][0]
generated1000dfWithout90.drop(idx, axis=0, inplace=True)
generated1000dfWithout26 = dfProblem2.head(1000)
idx = generated1000dfWithout26.index[generated1000dfWithout26['Age']==26][0]
generated1000dfWithout26.drop(idx, axis=0, inplace=True)
generated1000dfWithout25 = dfProblem2.head(1000)
idx = generated1000dfWithout25.index[generated1000dfWithout25['Age']==25][0]
generated1000dfWithout25.drop(idx, axis=0, inplace=True)


##Here I calculate the means for calculating the sensitivity
#Mean of 1000 of the first group of 1000 (First group requested in question 1)
meanOriginal1000 = generated1000dfOriginal.mean()

##Mean removing one row of one person of 90 years (Second group requested in question 1)
meanNeighbour90 = generated1000dfWithout90.mean()

##Mean removing one row of one person of 26 years (Third group requested in question 1)
meanNeighbour26 = generated1000dfWithout26.mean()

##Mean removing one row of one person of 25 years (Fourth group requested in question 1)
meanNeighbour25 = generated1000dfWithout25.mean()

#Sensitivity calculated with the 4 means obtained before
sensitivity = max(meanOriginal1000.values - meanNeighbour90.values, meanOriginal1000.values - meanNeighbour26.values, meanOriginal1000.values - meanNeighbour25.values)

#Calculating noise with 0.5 epsilon and the sensitivity calculated before
noise05=numpy.random.laplace(0, (sensitivity/0.5))

#Adding noise with epsilon 0.5 to the queries (To the result of the averages)
meanOriginal1000Noisy05 = meanOriginal1000 + noise05
meanNeighbour90Noisy05 = meanNeighbour90 + noise05
meanNeighbour26Noisy05 = meanNeighbour26 + noise05
meanNeighbour25Noisy05 = meanNeighbour25 + noise05

#Results calculated before rounded to 2 digits as mentioned
meanOriginal1000Noisy05Rounded = round(meanOriginal1000Noisy05, 2)
meanOriginal90Noisy05Rounded = round(meanNeighbour90Noisy05, 2)
meanOriginal26Noisy05Rounded = round(meanNeighbour26Noisy05, 2)
meanOriginal25Noisy05Rounded = round(meanNeighbour25Noisy05, 2)

#Measures applied to determine if the results are 0.5 indistinguisable
measureSetWithout90Ep05 = numpy.log(meanOriginal1000Noisy05Rounded.values/meanOriginal90Noisy05Rounded.values)
measureSetWithout26Ep05 = numpy.log(meanOriginal1000Noisy05Rounded.values/meanOriginal26Noisy05Rounded.values)
measureSetWithout25Ep05 = numpy.log(meanOriginal1000Noisy05Rounded.values/meanOriginal25Noisy05Rounded.values)


#Calculating noise with epsilon 1 and the sensitivity calculated before
noise1=numpy.random.laplace(0, (sensitivity/1))


#Adding noise with epsilon 1 to the queries (To the result of the averages)
meanOriginal1000Noisy1 = meanOriginal1000 + noise1
meanNeighbour90Noisy1 = meanNeighbour90 + noise1
meanNeighbour26Noisy1 = meanNeighbour26 + noise1
meanNeighbour25Noisy1 = meanNeighbour25 + noise1

#Results calculated before rounded to 2 digits as mentioned
meanOriginal1000Noisy1Rounded = round(meanOriginal1000Noisy1, 2)
meanOriginal90Noisy1Rounded = round(meanNeighbour90Noisy1, 2)
meanOriginal26Noisy1Rounded = round(meanNeighbour26Noisy1, 2)
meanOriginal25Noisy1Rounded = round(meanNeighbour25Noisy1, 2)

#Measures applied to determine if the results are 1 indistinguisable
measureSetWithout90Ep1 = numpy.log(meanOriginal1000Noisy1Rounded.values/meanOriginal90Noisy1Rounded.values)
measureSetWithout26Ep1 = numpy.log(meanOriginal1000Noisy1Rounded.values/meanOriginal26Noisy1Rounded.values)
measureSetWithout25Ep1 = numpy.log(meanOriginal1000Noisy1Rounded.values/meanOriginal25Noisy1Rounded.values)


#Another measure would be comparing all the elements of the sets and count the ones that are equals
newMeasure = numpy.log10(999/1000)







