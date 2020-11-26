#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:26:04 2020

@author: Shreya Bhattad
"""
import json

data = {}


def read_records():
    global data
    with open("emp1.json",'r') as read_file :
        data = json.load(read_file)
    #print(data)

def correct_types():
    for x in data.values():
        x['age'] = int(x['age'])
  
def find_average_age() : 
    sum =0 
    for x in data.values() :
        sum += x['age']
    return sum / len(data)

def find_average_age_for_dept(dept):
    avg_age = 0
    count = 0
    for x in data.values() :
        if x['dept'] == dept :
                count += 1
                avg_age += x['age'] 
    return avg_age/count            
        
    
def main():
    read_records()
    correct_types()
    print("Average emp age is:", find_average_age())

    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))



if __name__ == "__main__":
    main()
   