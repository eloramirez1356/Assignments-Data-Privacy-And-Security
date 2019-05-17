# -*- coding: utf-8 -*-
"""
Eloy Ramirez Hernanz

CS-528

Homework 1 Problem 2. Exponential Mechanism
"""

#Libraries Needed
import pandas
import numpy

#First, obtain all the different values from the 4 QI we are going to use.

dataDf = pandas.read_csv('D:\\Universidad\\IIT\\CS-528 Data Privacy And Security\\Assignments\\Assignment 1\\dataAssignment1.csv',
                          delimiter=';')

##Dataframe with the columns we want
dataQiP2Df = dataDf[['Age','Education','Marital-Status','Race']]

dataQiP2Df['Education'].value_counts()

generated1000df = dataQiP2Df.head(1000)
generated1000dfWithoutMostFrequent = dataQiP2Df.head(1000)
idx = generated1000dfWithoutMostFrequent.index[generated1000dfWithoutMostFrequent['Education']==' HS-grad'][0]
generated1000dfWithoutMostFrequent.drop(idx, axis=0, inplace=True)
generated1000dfWithoutSecondMostFreq = dataQiP2Df.head(1000)
idx = generated1000dfWithoutSecondMostFreq.index[generated1000dfWithoutSecondMostFreq['Education']==' Some-college'][0]
generated1000dfWithoutSecondMostFreq.drop(idx, axis=0, inplace=True)
generated1000dfWithoutLeastFreq = dataQiP2Df.head(1000)
idx = generated1000dfWithoutLeastFreq.index[generated1000dfWithoutLeastFreq['Education']==' Preschool'][0]
generated1000dfWithoutLeastFreq.drop(idx, axis=0, inplace=True)

print('Generated 1000')
maxOfgenerated1000df = generated1000df['Education'].value_counts().max()
allValuesGenerated1000df = generated1000df['Education'].value_counts()

print('Without the most freq')
maxOfgenerated1000dfWithoutMostFrequent = generated1000dfWithoutMostFrequent['Education'].value_counts().max()
allValuesGenerated1000dfWithoutMostFrequent = generated1000dfWithoutMostFrequent['Education'].value_counts()

print('Without second most freq')
maxOfgenerated1000dfWithoutSecondMostFreq = generated1000dfWithoutSecondMostFreq['Education'].value_counts().max()
allValuesGenerated1000dfWithoutSecondMostFreq = generated1000dfWithoutSecondMostFreq['Education'].value_counts()
print('Without least freq')
maxOfgenerated1000dfWithoutLeastFreq = generated1000dfWithoutLeastFreq['Education'].value_counts().max()
allValuesGenerated1000dfWithoutLeastFreq = generated1000dfWithoutLeastFreq['Education'].value_counts()

sensitivity = max(maxOfgenerated1000df - maxOfgenerated1000dfWithoutMostFrequent, maxOfgenerated1000df - maxOfgenerated1000dfWithoutSecondMostFreq, maxOfgenerated1000df - maxOfgenerated1000dfWithoutLeastFreq)

#Calculate the probability function
epsilon05 = 0.5
epsilon1 = 1

denominatorOfProbOfGenerated1000df = 0
for i in allValuesGenerated1000df:
    denominatorOfProbOfGenerated1000df = denominatorOfProbOfGenerated1000df + numpy.exp(epsilon05*i/2*sensitivity)

probOfGenerated1000dfEp05 = (numpy.exp(epsilon05*maxOfgenerated1000df/2*sensitivity))/denominatorOfProbOfGenerated1000df

denominatorOfProbOfGenerated1000dfWithoutMostFrequent = 0
for i in allValuesGenerated1000dfWithoutMostFrequent:
    denominatorOfProbOfGenerated1000dfWithoutMostFrequent = denominatorOfProbOfGenerated1000dfWithoutMostFrequent + numpy.exp(epsilon05*i/2*sensitivity)

probOfGenerated1000dfWithoutMostFrequentEp05 = (numpy.exp(epsilon05*maxOfgenerated1000dfWithoutMostFrequent/2*sensitivity))/denominatorOfProbOfGenerated1000dfWithoutMostFrequent

denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent = 0
for i in allValuesGenerated1000dfWithoutSecondMostFreq:
    denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent = denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent + numpy.exp(epsilon05*i/2*sensitivity)

probOfGenerated1000dfWithoutSecondMostFrequentEp05 = (numpy.exp(epsilon05*maxOfgenerated1000dfWithoutSecondMostFreq/2*sensitivity))/denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent

denominatorOfProbOfGenerated1000dfWithoutLeastFrequent = 0
for i in allValuesGenerated1000dfWithoutLeastFreq:
    denominatorOfProbOfGenerated1000dfWithoutLeastFrequent = denominatorOfProbOfGenerated1000dfWithoutLeastFrequent + numpy.exp(epsilon05*i/2*sensitivity)

probOfGenerated1000dfWithoutLeastFrequentEp05 = (numpy.exp(epsilon05*maxOfgenerated1000dfWithoutLeastFreq/2*sensitivity))/denominatorOfProbOfGenerated1000dfWithoutLeastFrequent

#Measures for the epsilon
#Measure for the 1000 with the one without most
epsilonOriginalAndWithoutMostEp05 = probOfGenerated1000dfEp05/probOfGenerated1000dfWithoutMostFrequentEp05
#Measure for the 1000 with the one without second most
epsilonOriginalAndWithoutSecondMostEp05 = probOfGenerated1000dfEp05/probOfGenerated1000dfWithoutSecondMostFrequentEp05
#Measure for the 1000 with the one without least
epsilonOriginalAndWithoutLeastEp05 = probOfGenerated1000dfEp05/probOfGenerated1000dfWithoutLeastFrequentEp05

####Epsilon 1

denominatorOfProbOfGenerated1000df = 0
for i in allValuesGenerated1000df:
    denominatorOfProbOfGenerated1000df = denominatorOfProbOfGenerated1000df + numpy.exp(epsilon1*i/2*sensitivity)

probOfGenerated1000dfEp1 = (numpy.exp(epsilon1*maxOfgenerated1000df/2*sensitivity))/denominatorOfProbOfGenerated1000df

denominatorOfProbOfGenerated1000dfWithoutMostFrequent = 0
for i in allValuesGenerated1000dfWithoutMostFrequent:
    denominatorOfProbOfGenerated1000dfWithoutMostFrequent = denominatorOfProbOfGenerated1000dfWithoutMostFrequent + numpy.exp(epsilon1*i/2*sensitivity)

probOfGenerated1000dfWithoutMostFrequentEp1 = (numpy.exp(epsilon1*maxOfgenerated1000dfWithoutMostFrequent/2*sensitivity))/denominatorOfProbOfGenerated1000dfWithoutMostFrequent

denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent = 0
for i in allValuesGenerated1000dfWithoutSecondMostFreq:
    denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent = denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent + numpy.exp(epsilon1*i/2*sensitivity)

probOfGenerated1000dfWithoutSecondMostFrequentEp1 = (numpy.exp(epsilon1*maxOfgenerated1000dfWithoutSecondMostFreq/2*sensitivity))/denominatorOfProbOfGenerated1000dfWithoutSecondMostFrequent

denominatorOfProbOfGenerated1000dfWithoutLeastFrequent = 0
for i in allValuesGenerated1000dfWithoutLeastFreq:
    denominatorOfProbOfGenerated1000dfWithoutLeastFrequent = denominatorOfProbOfGenerated1000dfWithoutLeastFrequent + numpy.exp(epsilon1*i/2*sensitivity)

probOfGenerated1000dfWithoutLeastFrequentEp1 = (numpy.exp(epsilon1*maxOfgenerated1000dfWithoutLeastFreq/2*sensitivity))/denominatorOfProbOfGenerated1000dfWithoutLeastFrequent

#Measures for the epsilon
#Measure for the 1000 with the one without most
epsilonOriginalAndWithoutMostEp1 = probOfGenerated1000dfEp1/probOfGenerated1000dfWithoutMostFrequentEp1
#Measure for the 1000 with the one without second most
epsilonOriginalAndWithoutSecondMostEp1 = probOfGenerated1000dfEp1/probOfGenerated1000dfWithoutSecondMostFrequentEp1
#Measure for the 1000 with the one without least
epsilonOriginalAndWithoutLeastEp1 = probOfGenerated1000dfEp1/probOfGenerated1000dfWithoutLeastFrequentEp1

##New measure:

#Measure for the 1000 with the one without most
epsilonOriginalAndWithoutMostEp05 = numpy.log(probOfGenerated1000dfEp05/probOfGenerated1000dfWithoutMostFrequentEp05)
#Measure for the 1000 with the one without second most
epsilonOriginalAndWithoutSecondMostEp05 = numpy.log(probOfGenerated1000dfEp05/probOfGenerated1000dfWithoutSecondMostFrequentEp05)
#Measure for the 1000 with the one without least
epsilonOriginalAndWithoutLeastEp05 = numpy.log(probOfGenerated1000dfEp05/probOfGenerated1000dfWithoutLeastFrequentEp05)


#Measures for the epsilon
#Measure for the 1000 with the one without most
epsilonOriginalAndWithoutMostEp1 = numpy.log(probOfGenerated1000dfEp1/probOfGenerated1000dfWithoutMostFrequentEp1)
#Measure for the 1000 with the one without second most
epsilonOriginalAndWithoutSecondMostEp1 = numpy.log(probOfGenerated1000dfEp1/probOfGenerated1000dfWithoutSecondMostFrequentEp1)
#Measure for the 1000 with the one without least
epsilonOriginalAndWithoutLeastEp1 = numpy.log(probOfGenerated1000dfEp1/probOfGenerated1000dfWithoutLeastFrequentEp1)