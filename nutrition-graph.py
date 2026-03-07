#!/usr/bin/env python3

###################################
# TITLE: nutrition-graph.py
# AUTHOR: Boardleash (Derek)
# DATE: Tuesday, February 17th 2026
###################################

#--------------------------------------- DESCRIPTION -------------------------------------------------------
# This script is dependent on a MariaDB database, that has necessary data 
# Make necessary changes to the database information and query to suit whatever you may have
# This is a Python script that pulls data from a database and presents that to a user as a graph
#-----------------------------------------------------------------------------------------------------------

import numpy as np
import mariadb
import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy as db

#------------------------------
# DB Connector using SQLAlchemy
#------------------------------
#engine = db.create_engine('mariadb+mariadbconnector://testuser:test@demersal:3306/fitness')
engine = db.create_engine('mariadb+mariadbconnector://testuser:test@demersal:48124/fitness')
connection = engine.connect()

#-----------------------------
# DB Queries for Relevant Data 
#-----------------------------
queryOne = "select date,weight_lbs from weighins;"
queryTwo = "select date as date,sum(pro) as protein,sum(carb) as carbs,sum(fat) as fat from meals group by date order by date desc limit 7;"
queryThree = "select date as date,sum(cal) as total_cal from meals group by date order by date desc limit 7;"
queryFour = "select * from meals;"
dfOne = pd.read_sql_query(queryOne,connection)
dfTwo = pd.read_sql_query(queryTwo,connection)
dfThree= pd.read_sql_query(queryThree,connection)
dfFour= pd.read_sql_query(queryFour,connection)
connection.close()

#---------------------------------------
# Functions for Graphs - Use for Testing
#---------------------------------------
def weighins():
  fig,ax = plt.subplots()
  weight = dfOne['weight_lbs'].tolist()
  dates = pd.to_datetime(dfOne['date']).dt.strftime('%Y-%m-%d').tolist()
  pos = range(len(dates))
  ax.plot(dates,weight)
  for i in range(len(weight)):
    ax.text(dates[i],weight[i],weight[i],size=10)
  plt.plot(weight, marker='X', linestyle='solid')
  plt.xlabel('DATE')
  plt.xticks(ticks=pos, labels=dates)
  plt.ylabel('WEIGHT (lbs)')
  plt.title('WEIGHT TRENDS')
  plt.grid(True)
  fig.patch.set_facecolor('#adf5eb')
  plt.show()

def macros():
  fig,ax = plt.subplots()
  sum_pro = round(dfTwo['protein'].sum(),1)
  sum_carb = round(dfTwo['carbs'].sum(),1)
  sum_fat = round(dfTwo['fat'].sum(),1)
  macros = [sum_carb,sum_fat,sum_pro]
  groups = ['Carbohydrates','Fats','Protein']
  plt.bar(groups,macros)
  plt.xlabel('MACROS')
  plt.ylabel('AMOUNT (grams)')
  plt.title('MACRO CHART')
  fig.patch.set_facecolor('#e0b4f0')
  plt.show()

def sevenDay():
  fig,ax = plt.subplots()
  calories = dfThree['total_cal'].tolist()
  calories.reverse()
  cal_dates = pd.to_datetime(dfThree['date']).dt.strftime('%Y-%m-%d').tolist()
  cal_dates.reverse()
  plt.barh(cal_dates,calories,color='orange')
  plt.title('7 DAY CALORIE CONSUMPTION')
  plt.xlabel('Calories Consumed')
  plt.ylabel('Date')
  fig.patch.set_facecolor('#e0b4f0')
  plt.show()

def overallMacro():
  sum_pro = round(dfFour['pro'].sum(),1)
  sum_carb = round(dfFour['carb'].sum(),1)
  sum_fat = round(dfFour['fat'].sum(),1)
  macros = [sum_carb,sum_fat,sum_pro]
  pie_labels = ['Carbohydrates','Fat','Protein']
  pie_colors = plt.get_cmap('Blues')(np.linspace(0.3,1,num=3))
  plt.pie(macros,colors=pie_colors,labels=pie_labels)#,radius=3,center=(4,4),wedgeprops={"linewidth":1,"edgecolor":"white"},frame=True)
  #plt.set(xlim=(0,8),xticks=np.arange(1,8),ylim=(0,8),yticks=np.arange(1,8))
  plt.title('OVERALL MACRONUTRIENT (since tracking)')
  plt.show()

#----------------------------------
# Primary Graph Function - Use This
#----------------------------------
def megaPlot():
  #--- SUBPLOT SETUP
  plt.rc('font',size='10')
  plt.rc('xtick',labelsize='6')
  plt.rc('ytick',labelsize='6')
  fig,ax = plt.subplots(2,2)

  #--- WEIGHT METRICS GRAPH DATA
  weight = dfOne['weight_lbs'].tolist()
  dates = pd.to_datetime(dfOne['date']).dt.strftime('%Y-%m-%d').tolist()
  limited_weight = weight[-5:]
  limited_dates = dates[-5:]
  pos = range(len(limited_dates))
  ax[0,0].plot(limited_dates,limited_weight,marker=6,linestyle='dotted',color='salmon')
  for i in range(len(limited_weight)):
    ax[0,0].text(limited_dates[i],limited_weight[i],limited_weight[i],size='6')
  ax[0,0].set_title('WEIGHT METRICS')
  ax[0,0].set_xlabel('Weighin Date')
  ax[0,0].set_ylabel('Weight (lbs)')
  ax[0,0].grid(True)
  ax[0,0].set_facecolor('#adf5eb')

  #--- MACRONUTRIENTS METRICS GRAPH DATA
  data_one = dfTwo['protein'].tolist()
  data_two = dfTwo['carbs'].tolist()
  data_three = dfTwo['fat'].tolist()
  data_four = pd.to_datetime(dfTwo['date']).dt.strftime('%Y-%m-%d').tolist()
  w = 0.2
  x = np.arange(len(data_four))
  ax[0,1].bar(x,data_one,w,color='r',label='Protein')
  ax[0,1].bar(x+w,data_two,w,color='g',label='Carbs')
  ax[0,1].bar(x-w,data_three,w,color='b',label='Fat')
  ax[0,1].set_title('MACRONUTRIENT METRICS')
  ax[0,1].set_xticks(x,data_four)
  ax[0,1].set_xlabel('Date')
  ax[0,1].set_ylabel('Macros Consumed (in grams)')
  ax[0,1].legend(fontsize='6',loc='best')
  ax[0,1].set_facecolor('#f5aded')

  #--- 7 DAY CALORIE CONSUMPTION DATA
  calories = dfThree['total_cal'].tolist()
  calories.reverse()
  cal_dates = pd.to_datetime(dfThree['date']).dt.strftime('%Y-%m-%d').tolist()
  cal_dates.reverse()
  ax[1,0].barh(cal_dates,calories,color='purple')
  ax[1,0].set_title('7 DAY CALORIE CONSUMPTION')
  ax[1,0].set_xlabel('Calories Consumed')
  ax[1,0].set_ylabel('Date')
  ax[1,0].set_facecolor('#e0b4f0')
  
  #--- OVERALL MACRONUTRIENT DATA
  sum_pro = round(dfFour['pro'].sum(),1)
  sum_carb = round(dfFour['carb'].sum(),1)
  sum_fat = round(dfFour['fat'].sum(),1)
  macros = [sum_carb,sum_fat,sum_pro]
  pie_labels = ['Carbohydrates','Fat','Protein']
  pie_colors = plt.get_cmap('Blues')(np.linspace(0.3,1,num=3))
  ax[1,1].pie(macros,colors=pie_colors,labels=pie_labels)#,radius=3,center=(4,4),wedgeprops={"linewidth":1,"edgecolor":"white"},frame=True)
  #ax[1,1].set(xlim=(0,8),xticks=np.arange(1,8),ylim=(0,8),yticks=np.arange(1,8))
  ax[1,1].set_title('OVERALL MACRONUTRIENT (since tracking)')

  plt.tight_layout()
  plt.show()
#---------------------------
# Plot and Present the Graph  
#---------------------------
if __name__ == '__main__':
  #weighins()
  #macros()
  #sevenDay()
  #overallMacro()
  megaPlot()

# EOF