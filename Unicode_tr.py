# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 22:04:09 2017

@author: karja
"""

import os
import unicodedata as unic
from pathlib import Path
import pandas as pd

# Translate a Unicode to Character
def tra_cr(kata):
        return kata.encode('raw_unicode_escape').decode('raw_unicode_escape')
 
# Initial attributes for creating library of databas
class Uni_at:
    
    # Attributes that contain database
    def __init__(self):
        self.alchr = [] 
        self.chrmod = []
        self.nchr = {}
        self.k_nc = []
    
    # Create self.alchr database that exctract from 'UnCo.txt'
    def get_chr():
        h_path = str(Path.home())
        os.chdir('%s\\Documents' %h_path)
        
        # Check the existence of "UnCo.txt"
        try:
            opt = open('UnCo.txt','r')
        except:
            print('You need to have "Unco.txt" file copy to your',
                  '%s\\Documents' %h_path)
        else:
            Uni_at.alchr = []
            for i in opt:
                Uni_at.alchr.append(i)

    # Create self.chrmod for clearing '\n' in the lists       
    def set_chr():
        Uni_at.chrmod = []
        for i in Uni_at.alchr:
            if len(i) == 7:
                Uni_at.chrmod.append(i[:6])
            elif len(i)==8:
                Uni_at.chrmod.append(i[:7])
            elif len(i)==9:
                Uni_at.chrmod.append(i[:8])
                
    # Create self.nchr (for the dict database from both names
    # and unicodeChar) and self.k_nc (keys to dict db of self.nchr)
    def cr_db():
        Uni_at.nchr = {}
        for i in Uni_at.chrmod:
            try:
                Uni_at.nchr[unic.name(tra_cr(i))] = tra_cr(i)
            except:
                continue
            
        Uni_at.k_nc = list(Uni_at.nchr.keys())

# Create database attributes       
def create_db():
    Uni_at.get_chr()
    Uni_at.set_chr()
    Uni_at.cr_db()

# Automatically create database when this file is imported
create_db()

# Making Data Frame    
pd_unc = pd.Series(Uni_at.nchr)

# Unicodes range are listed
def unc(num1,num2):
    try:
        int(num1)
        int(num2)
    except:
        print("You need to input numbers only!!!")
    else:
        if num2 > num1:
            if num2 <= 16473 and num1 >= -16473:  
                return list(pd_unc[num1:num2])
            else:
                print("Out of range!!!")
        elif num1 > num2:
            if num1 <= 16473 and num2 >= -16473:
                return list(pd_unc[num2:num1])
            else:
                print("Out of range!!!")
        elif num1 == num2 == 0:
            return list(pd_unc[:])
        else:
            if -16473 <= num1 == num2 < 16473:
                return pd_unc[num1]
            else:
                print("No record")

# Unicodes are coded and compile as dictionary
def dict_unc(num1, num2):
    try:
        int(num1)
        int(num2)
    except:
        print("You need to input numbers only!!!")
    else:
        if num2 > num1:
            if num2 <= 16473 and num1 >= -16473:  
                return {a:pd_unc[a] for a in range(num1,num2)}
            else:
                print("Out of range!!!")
        elif num1 > num2:
            if num1 <= 16473 and num2 >= -16473:
                return {a:pd_unc[a] for a in range(num2,num1)}
            else:
                print("Out of range!!!")
        elif num1 == num2 == 0:
            return {a:pd_unc[a] for a in range(0,len(pd_unc))}
        else:
            if -16473 <= num1 == num2 < 16473:
                return pd_unc[num1]
            else:
                print("No record")

# Label and unicode compile as dictionary
def lab_unc(num1, num2):
    try:
        int(num1)
        int(num2)
    except:
        print("You need to input numbers only!!!")
    else:
        if num2 > num1:
            if num2 <= 16473 and num1 >= -16473:  
                return dict(pd_unc[num1:num2])
            else:
                print("Out of range!!!")
        elif num1 > num2:
            if num1 <= 16473 and num2 >= -16473:
                return dict(pd_unc[num2:num1])
            else:
                print("Out of range!!!")
        elif num1 == num2 == 0:
            return dict(pd_unc[:])
        else:
            if -16473 <= num1 == num2 < 16473:
                return pd_unc[num1]
            else:
                print("No record")

'''
# Unblock this code to create docx for unicode database.
# Note:
# [YOU MAY NEED TO INSTALL PYTHON-DOCX USING PIP
# SOME UNICODE CHAR MAY NOT APPEAR CORRECTLY, PLEASE HELP TO GIVE SUGGESTION
# THANK YOU ☺]
'''
# =============================================================================
# from docx import Document
# doc1 = Document()
#  
# for i, g in Uni_at.nchr.items():
#     try:
#         doc1.add_paragraph('{:>2} {:>12}'.format(g,i), style='ListNumber')
#     except:
#         continue
# 
# doc1.save('Unicode_tr.docx')
# =============================================================================
