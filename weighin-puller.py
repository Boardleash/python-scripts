#!/usr/bin/env python3
#------------------------------
# TITLE: weighin-puller.py
# AUTHOR: Boardleash (Derek)
# DATE: Monday, April 13th 2026
#------------------------------
#-------------------------------- DESCRIPTION ---------------------------------
# Python script to read data from a file using Pandas and present relevant
# information graphically
#------------------------------------------------------------------------------
import calendar
from datetime import datetime
import numpy as np
import mariadb
import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy as db
import string
#------------------------------- DATA COLLECTION ------------------------------
# Establish connection to database
engine = db.create_engine('mariadb+mariadbconnector://testuser:test@demersal: \
         48124/fitness')
#engine = db.create_engine('mariadb+mariadbconnector://testuser:test@altdem: \
#          48124/fitness')
#engine = db.create_engine('mariadb+mariadbconnector://testuser:test@atlantis: \
#         48124/fitness')
connection = engine.connect()

year = datetime.now().year
cal = calendar.Calendar()

month = input("What month? (January,february,mar...etc): ")

#  Convert month to needed format
if len(month.lower()) > 3:
  month_object = datetime.strptime(month, '%B')
  month = month_object.strftime('%m')
elif len(month.lower()) < 4:
  month_object = datetime.strptime(month, '%b')
  month = month_object.strftime('%m')

month_days = calendar.monthrange(year,int(month))
start_date = f'{year}-{month}-01'
end_date = f'{year}-{month}-{month_days[1]}'
query = f"select date,weight_lbs from weighins where date \
        between '{start_date}' and '{end_date}';"
df = pd.read_sql_query(query,connection)

connection.close()
#------------------------------ GRAPH FUNCTION -------------------------------
def dataPlot():
  #--- SUBPLOT SETUP (for either option)
  plt.rc('font',size='10')
  plt.rc('xtick',labelsize='6')
  plt.rc('ytick',labelsize='6')

  #--- VARIABLES (for either option)
  d_one = df['weight_lbs'].tolist()
  d_two= pd.to_datetime(df['date']).dt.strftime('%a-%b-%d').tolist()

  #--- MONTH GRAPH 
  fig,ax = plt.subplots()
  month = month_object.strftime('%B')

  plt.plot(d_two,d_one)
  plt.title(f'{month} Weighins')
  plt.xlabel('Weighin Date')
  plt.ylabel('Weight (in lbs)')

  plt.tight_layout()
  plt.show()
#---------------------------
# Plot and Present the Graph  
#---------------------------
if __name__ == '__main__':
  dataPlot()

# EOF