# -*- coding: utf-8 -*-
"""
Created on Sun May 10 09:15:07 2026

@author: Atefe
"""

l = ['Iran' , 'Spain', 'Portugal' , 'Morocco']



class tarkib():
    
    def __init__(self, i , j):
        self.i = i
        self.j = j
       
    
    def tarkib(self , i , j ):
        self.i = i
        self.j = j
        
        
        from collections import defaultdict
        n = defaultdict(tuple)
        for i in l:
                for j in l:
                    z = input ("Enter the result {(i, j)} : ")           
                    tup = tuple(z.split())
                    if i is not j:
                        n[(i , j)] = (tup)
                    elif (j , i) == (i , j):
                        break
        
        print(dict (n)) 
        print (tup)
        
 

    
d = tarkib(l,l)
print(d.tarkib(l , l))


