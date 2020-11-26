#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 11:26:04 2020

@author: Shreya Bhattad
"""


import csv

emps = []


def read_records():
    global emps
    with open("emp.csv") as f:
        rows = csv.DictReader(f)
        emps = [x for x in rows]


def correct_types():
    for e in emps:
        #print(type(e['age']))
        e['age'] = int(e['age'])


# average employee age
def find_average_age():
    avg_age = sum([x['age'] for x in emps]) / len(emps)
    return avg_age


# TODO:: implement this
def find_average_age_for_dept(dept):
    avg_age = 0
    count =0
    for e in emps :
        if e['dept'] == dept:
            count += 1
            avg_age = avg_age + e['age']
        
    return avg_age/count


def main():
    read_records()
    correct_types()
    print("Average emp age is:", find_average_age())

    print("Average emp age for dept d1:", find_average_age_for_dept("d1"))
    print("Average emp age for dept d2:", find_average_age_for_dept("d2"))

    # TODO: Do same thing with json file instead of csv file


if __name__ == "__main__":
    main()
