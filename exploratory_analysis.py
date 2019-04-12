# Exploratory Analysis
# Table of Contents
# Introduction
# Gathering Data
# Assessing Data
# Cleaning Data
# Exploratory analysis

# Introduction

#The dataset has been chosen from the options provided by Udacity.The U.S. Department of Transportation's (DOT) Bureau of Transportation Statistics (BTS) tracks the on-time performance of domestic flights operated by large air carriers. Summary information on the number of on-time, delayed, canceled and diverted flights appears in DOT's monthly Air Travel Consumer Report, published about 30 days after the month's end, as well as in summary tables posted on this website. BTS began collecting  details on the causes of flight delays in June 2003. Summary statistics and raw data are made available to the public at the time the Air Travel Consumer Report is released.

# The datset used here reports flights in the United States, including carriers, arrival and departure delays,in 1987.

# Due to memory constraint here only one year flight data has been analysed.

# Importing relevant libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
​
%matplotlib inline

# Gathering data

# Reading the manually unzipped file into a pandas dataframe

df=pd.read_csv('1987.csv')
# Assessing data

# First few columns of the dataset

df.head(5)

# Info of the dataset

df.info()

# Descriptive statistics for the dataset

df.describe()

# Quality issues

# Numerous columns with null values viz. TaxiIn,TaxiOut,TailNum etc.
# Null values in columns of ArrTime.
# Null values in ArrDelay and DepDelay.
# An entire column for representing Year.
# Erroneous datatype of DayOfWeek,DayofMonth,Month,FlightNum columns.

# Tidiness issues

# Improper representation of time in ArrTime,CRSArrTime,DepTime,CRSDepTime columns.

# Cleaning data

# Creating a copy of dataset before cleaning

df_new=df.copy()

# Define:
# Dropping all columns with complete null values as no information can be conveyed from them and they only occupy memory.

# Code

df_new=df_new.drop(['AirTime','TaxiIn','TaxiOut','Diverted','CarrierDelay','CancellationCode','WeatherDelay',
             'NASDelay','SecurityDelay','LateAircraftDelay','TailNum'],axis=1)
# Test

df_new.describe()