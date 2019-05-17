# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 16:21:12 2019

@author: Eloy Ramirez Hernanz

CWID: A20433696
"""
from phe import paillier, encoding, util
import numpy as np
import socket
import pickle

#Generation of random matrix A, using numbers between 0 and 10.
A = np.random.randint(10, size=(5, 8))
print(A)

#Obtain the number of rows of A for iterating over it 
rowsA = np.size(A,0)
print(rowsA)

#Variable for changing the key size for the encryption and decryption
keyLength = 1024

#Generation of public key and private key
public_key, private_key = paillier.generate_paillier_keypair(n_length=keyLength)

#Variable for saving the encrypted matrix of A
encryptedA = []

#Iteration for encrypting all of the elements of A, and creating the encrypted matrix of A (encryptedA)
for i in range(0,rowsA):
    encryptedA.append([public_key.raw_encrypt(int(x)) for x in A[i,:]])
    
print(encryptedA)

#Creation of the socket for the communication with Bob, for sending the encripted matrix of A
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('127.0.0.1', 1234)) 

#Variable for sending the encrypted matrix of A (doing this way, with pickle, because it was too large for sending)
data=pickle.dumps(encryptedA)
print(data)
#Encrypted Matrix A sent to Bob
s.send(data)
#Closing the communication
s.close()

#Creation of socket for receiving the encrypted numbers for obtaining the product of the matrix, AxB, sent by Bob
socketSolution = socket.socket() 
port = 4321
socketSolution.bind(('127.0.0.1', port))
socketSolution.listen(1) 
while True: 
  
   # Establish connection with Bob. 
   c, addr = socketSolution.accept()      
   print('Got connection from', addr)
  
   #Receiving the encrypted values of AxB from Bob (using pickle because each packet received is higher than 4096 bits, so I receive multiple packages and then I join them)
   data = b""
   while True:
       packet = c.recv(4096)
       print('packet Received')
       print(packet)
       if not packet: 
           break
       data += packet
   print('Matrix received')
   #Received values for obtaining the AxB matrix from Bob
   solutionMatrixFromBob = pickle.loads(data)
   break
#Closing this communication after obtaining this data
c.close()

#Obtaining AxB with the data sent by Bob
AxB=[]
sumRow = 0
rowAxB = []
#Iteration of the matrix obtained from Bob, for sum all the numbers which compose the matrix AxB
#First loop for iterating each row of the matrix sent by Bob
for i in range(0, len(solutionMatrixFromBob[0])):
    #Second loop for iterating all the elements to sum in each row of the product matrix of AxB. 32 values to sum (8 values per column, in the 4 columns as AxB has dimension 5x4)
    for j in range(0, len(solutionMatrixFromBob[0][0])):
        #Adding of the values of each row obtained from the decryption of the encrypted values sent by Bob
        sumRow = sumRow + private_key.raw_decrypt(solutionMatrixFromBob[0][i][j])
        #If for adding each element into its column and row of AxB
        if(j==7 or j==15 or j==23 or j==31):
            rowAxB.append(sumRow)
            sumRow = 0
    AxB.append(rowAxB)
    rowAxB = []

#New socket for sending the matrix AxB to Bob
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 1234)) 

#Sending matrix AxB same procedure as before
data=pickle.dumps(AxB)
print(data)
s.send(data)
#Closing the communication after sending the result to Bob
s.close()           
    
