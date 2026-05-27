# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:15:07 2026

@author: Atefe
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict





l = ['Iran' , 'Spain', 'Portugal' , 'Morocco']



class Tarkib():
    
    def __init__(self, i , j):
        self.i = i
        self.j = j
       
    
    def tarkib(self, i , j  ):
        self.i = i
        self.j = j
        n = defaultdict(tuple)
        #Winner=defaultdict(list)
        Count=defaultdict(list)
        Loses = defaultdict(list)
        
        for i in l:
                for j in l:
                   
                       if i == j:
                           continue
                       if  (j , i) in  n.keys():
                           continue
                       if (i , j) is not n.keys():
                           z = input (f"Enter the result {i}, {j} : ") 
                           tup = tuple(z.split())
                           n[(i , j)] = (tup)

        
        print(dict (n)) 
    
        #def Winner(self, i , j ):
            #self.i = i
            #self.j = j
            
        for (i , j) , (a, b) in n.items():
           # Winner[i].append(a) 
           # Winner[j].append(b) 
            
           if a>b:
               Count[i].append(a)
               Loses[j].append(b)
               
           else:
               Count[j].append(b)
               Loses[i].append(a)
               
        
        for key , value in Count.items():   
         for key2, value2 in Loses.items(): 
            #for key3, value3 in Points.items():
                 
             if key ==key2 :
                 value3 = 3 * len(value)
                 print(f"{key} , Wins: {len(value)} , Loses: {len(value2)}, Points: {value3}") 
                 
                 
        Matrics=[]                 
        with open( "data_file3.csv","w" , newline='') as File:
            
            for key , value in Count.items():
                File.write(f"{key} ,{len(value)} ,\n") 
            
        File = open("data_file3.csv")
        csv_file=csv.reader(File)
        
        for row in csv_file:
            Matrics.append([row[0] , row[1]])
        Matrics = np.array(Matrics)
        
        plt.bar(Matrics[: , 0],Matrics[: ,1].astype(int), width= 0.8)
        plt.ylim(0 , 4)
        plt.xlabel('x-axis')
        plt.ylabel('y - axis')
        plt.show()
        
        
    
d = Tarkib(l,l)

print(d.tarkib(l , l))


