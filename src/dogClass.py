# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 08:45:41 2018

@author: 
"""

class dogClass():
    def _init_(self, name, weight, breed):
        self.name = name
        self.weight = weight
        self.breed = breed
        
    def bark(self):
        print('woof, woof, woof')
		print('how, how, how')
    def getDogInfo(self):
        return self.name + ' : '
        
