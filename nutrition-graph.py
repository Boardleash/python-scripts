#!/usr/bin/env python3
#-----------------------------------
# TITLE: nutrition-graph.py
# AUTHOR: Boardleash (Derek)
# DATE: Tuesday, February 17th 2026
#-----------------------------------
#----------------------------- DESCRIPTION -----------------------------------
# Python script to pull data from database and present it graphically
# Uses MariaDB and SQLAlchemy for database connection
#-----------------------------------------------------------------------------
import numpy as np
import mariadb
import matplotlib.pyplot as plt
import pandas as pd
import sqlalchemy as db

#--- DB Connector using SQLAlchemy
engine = db.create_engine('mariadb+mariadbconnector://testuser:test@demersal: \
  48124/fitness')
#engine = db.create_engine('mariadb+mariadbconnector://testuser:test@altdem: \
# 48124/fitness')
connection = engine.connect()

#--- DB Queries for Relevant Data 
queryOne = "select date,weight_lbs from weighins;"
queryTwo = "select date as date,sum(pro) as protein,sum(carb) as carbs,sum(fat) as fat from meals group by date order by date desc limit 7;"
queryThree = "select date as date,sum(cal) as total_cal from meals group by date order by date desc limit 7;"
queryFour = "select * from meals;"
dfOne = pd.read_sql_query(queryOne,connection)
dfTwo = pd.read_sql_query(queryTwo,connection)
dfThree= pd.read_sql_query(queryThree,connection)
dfFour= pd.read_sql_query(queryFour,connection)
connection.close()

#--- Primary Graph Function - Use This
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
  ax[0,0].plot(limited_dates,limited_weight,marker=6,linestyle='dotted', \
              color='salmon')
  for i in range(len(limited_weight)):
    ax[0,0].text(limited_dates[i],limited_weight[i],limited_weight[i], \
                size='6')
  ax[0,0].set_title('WEIGHT METRICS')
  ax[0,0].set_xlabel('Weighin Date')
  ax[0,0].set_ylabel('Weight (lbs)')
  ax[0,0].grid(True)
  ax[0,0].set_facecolor('#adf5eb')

  #--- MACRONUTRIENTS METRICS GRAPH DATA
  data_one = dfTwo['protein'].tolist()
  data_two = dfTwo['carbs'].tolist()
  data_three = dfTwo['fat'].tolist()
  data_four = pd.to_datetime(dfTwo['date']).dt.strftime('%Y-%b-%d').tolist()
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
  cal_dates = pd.to_datetime(dfThree['date']).dt.strftime('%Y-%b-%d').tolist()
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
  ax[1,1].pie(macros,colors=pie_colors,labels=pie_labels)#,radius=3, \
             #center=(4,4),wedgeprops={"linewidth":1,"edgecolor": \
             #"white"},frame=True)
  #ax[1,1].set(xlim=(0,8),xticks=np.arange(1,8),ylim=(0,8), \
  #           yticks=np.arange(1,8))
  ax[1,1].set_title('OVERALL MACRONUTRIENT (since tracking)')

  plt.tight_layout()
  plt.show()

#--- Plot and Present the Graph  
if __name__ == '__main__':
  megaPlot()

# EOF