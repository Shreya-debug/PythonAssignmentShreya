#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:15:25 2020

@author: Shreya Bhattad
"""

import csv
import json
#import pandas as pd

#df=pd.read_csv("emp.csv")
#df.to_json("emp.json")


data ={ }

with open("emp.csv") as csvfile:
    csvReader = csv.DictReader(csvfile)
    for rows in csvReader:
        key = rows['name']
        data[key] = rows
    
with open("emp1.json", 'w') as jsonfile :
    jsonfile.write(json.dumps(data, indent = 4))
    