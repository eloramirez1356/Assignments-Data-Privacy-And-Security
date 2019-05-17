# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 17:08:34 2019

@author: Eloy Ramirez Hernanz

CWID: A20433696
"""
from phe import paillier
import numpy as np
import socket
import pickle


#Generation of random matrix B, using numbers between 0 and 10.
B = np.random.randint(10, size=(8, 4))
print(B)

#Method for obtaining the encrypted numbers for obtaining the product AxB
def multMatrixEncripted(encryptedA, B):
    
    #Obtain the number of rows of A for iterating over it 
    rowsA = np.size(encryptedA,0)
    
    #Obtain the number of columns of B for iterating over it 
    columns = np.size(B,1)
    
    
    encryptedValuesOfAxB = []
    row = []
    componentOfRow = [];
    
    #For loop for looping in the rows
    for j in range(0,rowsA):
        #For loop for looping int the columns
        for l in range(0,columns):
            #For loop for iterating in all the elements of the rows of encryptedA and columns of B
            for k in range(0, 8):
                #Operation for obtaining the E(Ajk * Bkl) = E(Ajk)^Bkl
                componentOfRow.append(((encryptedA[j][k])**(int(B[k][l]))))
        row.append(componentOfRow)
        print(componentOfRow)
        componentOfRow = []
    #Creation of the matrix with the encrypted values of AxB
    encryptedValuesOfAxB.append(row)
    row = []
        
    #The returned product AxB of the method
    return encryptedValuesOfAxB


#Creation of a socket for receiving the encrypted matrix A from Alice
s = socket.socket() 
port = 1234
s.bind(('127.0.0.1', port))
s.listen(1) 
while True: 
  
   # Establish connection with Alice when she make a connection request. 
   c, addr = s.accept()      
   print('Got connection from', addr)
  
   print('Receiving matrix')
   
   #Procedure for obtaining the encoded matrix from Alice (using pickle because the matrix is too big, more than one packet of 4096)
   data = b""
   while True:
       packet = c.recv(4096)
       print('packet Received')
       print(packet)
       if not packet: 
           break
       data += packet
   print('Matrix received')
   #Encrypted matrix A received from Alice by Bob
   encryptedA = pickle.loads(data)
   #After receiving the encrypted matrix from Alice, Bob applies the method multMatrixEncripted for obtaining the encrypted values for calculating AxB
   solutionMatrix = multMatrixEncripted(encryptedA, B)
   
   
   break
#Closing the connection
c.close()

#Creation of the socket for the communication with Alice, for sending the encrypted values for calculating AxB
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket2.connect(('127.0.0.1', 4321)) 

#Sending the values to Alice with which she could calculate the product AxB
dataSolution = pickle.dumps(solutionMatrix)
print(dataSolution)
socket2.send(dataSolution)
#Closing the connection
socket2.close()

#Creation of socket for obtaining the final product AxB decrypted by Alice
while True: 
  
   # Establish connection with client. 
   c2, addr2 = s.accept()      
   print('Got connection from', addr2)

   print('Receiving matrix')
   #Receiving the final matrix AxB sent by Alice
   data = b""
   while True:
       packet = c2.recv(4096)
       print('packet Received')
       print(packet)
       if not packet: 
           break
       data += packet
   print('Matrix received')
   AxB = pickle.loads(data)
   
   
   break
#Close the communication
c2.close()
   

    
