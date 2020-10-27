#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:10:10 2020

@author: mohammadansari
"""

import io
import pandas as pd
import requests as r
import numpy as np

#variables needed for ease of file access 

path = '/Users/mohammadansari/Downloads/'
file_1 = 'joined.csv'

file_out = 'cleaned_raw_data.csv'
file_out2 = 'healing_damage_position.csv'
file_out3 = 'total_data.csv'


#confirm the file downloaded has data needed 
df = pd.read_csv(path + file_1)


#cleaning Data from duplicates and null values
df = df.drop_duplicates()
print(df)

#create function to replace column nulls with median 
#based off a solution found on Pythonhealthcare.org  
def drop_null_with_medians (df):
    
    
    # Get list of DataFrame column names
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    
    cols = list(df.select_dtypes(include=numerics))
    # Looping  through numerical columns to get missing values 
    for column in cols:
        # Transfer column to independent series
        col_data = df[column]
        # Look to see if there is any missing numerical data
        missing_data = sum(col_data.isna())
        if missing_data > 0:
            # Get median and replace missing numerical data with median
            col_median = col_data.median()
            col_data.fillna(col_median, inplace=True)
            df[column] = col_data
    return df   



df=drop_null_with_medians (df)
print(df)

#calculate column averages and replace null values with column averages in Tableau

#calculate maximum values for COVID Death, tests, and cases for each country in Tableau
#File write output  
df.to_csv(path + file_out)

