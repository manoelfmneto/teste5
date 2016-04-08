'''
Created on 6 de abr de 2016

@author: manoe
'''
import math

class Plotter(object):

    def __init__(self, expoentes = [], coeficientes = []):
        '''
        Constructor
        '''
        self.expoentes = expoentes
        self.coeficientes = coeficientes
    
    def valor(self, x):
        temp = []
        for i in self.expoentes:
            temp.append(math.pow(x, i))
            
        resp = 0
        j = 0
        for k in self.coeficientes:
            resp += temp[j]*k 
            j += 1
        
        return resp 
                


           
        
        
        
        
        
        
        
        
        
        