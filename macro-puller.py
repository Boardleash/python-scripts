#!/usr/bin/env python3
#------------------------------
# TITLE: macro-puller.py
# AUTHOR: Boardleash (Derek)
# DATE: Monday, April 6th 2026
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

timeframe = input("Monthly or weekly data? ('M/m' OR 'W/w'): ")
month = input("What month? (January,february,mar...etc): ")

#  Convert month to needed format
if len(month.lower()) > 3:
  month_object = datetime.strptime(month, '%B')
  month = month_object.strftime('%m')
elif len(month.lower()) < 4:
  month_object = datetime.strptime(month, '%b')
  month = month_object.strftime('%m')

# If looking for monthly data, get number of days in the month to set end date
# Use the start date and end date to query DB for necessary data and store it
if timeframe.lower() == 'm':
  month_days = calendar.monthrange(year,int(month))
  start_date = f'{year}-{month}-01'
  end_date = f'{year}-{month}-{month_days[1]}'
  query = f"select date,sum(cal) as calories,sum(pro) as protein,sum(carb) as \
          carbs,sum(fat) as fat from meals where date between '{start_date}' \
          and '{end_date}';"
  df = pd.read_sql_query(query,connection)

# If looking for weekly data, use selected month and get Mondays for that
# month (Mondays start the week).  Provide user with options of weeks in
# that month that start with Monday.  Use their selection for DB query
elif timeframe.lower() == 'w':
  mondays = []
  for day in cal.itermonthdates(year,int(month)):
    if day.month == int(month) and day.weekday() == 0:
      mondays.append(str(day))
  letters = string.ascii_lowercase[:len(mondays)]
  dates = dict(zip(letters,mondays))
  week = input(f"Which week of that month (starting on a Monday)? \
         \na. {dates.get('a')}\nb. {dates.get('b')}\nc. {dates.get('c')} \
         \nd. {dates.get('d')}\ne. {dates.get('e')}\n")
  pref_week = dates.get(week)
  query = f"select date,sum(cal) as calories,sum(pro) as protein,sum(carb) as \
          carbs,sum(fat) as fat from meals where date between '{pref_week}' \
          and '{pref_week}' + interval 6 day group by date order by date;"
  df = pd.read_sql_query(query,connection)
else:
  print("Invalid input")
connection.close()
#------------------------------ GRAPH FUNCTION -------------------------------
def dataPlot():
  #--- SUBPLOT SETUP (for either option)
  plt.rc('font',size='10')
  plt.rc('xtick',labelsize='6')
  plt.rc('ytick',labelsize='6')
  pie_percentage = '%1.1f%%'

  #--- VARIABLES (for either option)
  d_one = df['protein'].tolist()
  d_two = df['carbs'].tolist()
  d_three = df['fat'].tolist()
  d_four= df['calories'].tolist()
  d_five = pd.to_datetime(df['date']).dt.strftime('%a-%b-%d').tolist()

  #--- MONTH GRAPH 
  if timeframe.lower() == 'm':
    fig,(ax1,ax2) = plt.subplots(1,2)
    month = month_object.strftime('%B')
    fig.suptitle(f"{month} Monthly Nutrient Metrics")

    macros = [d_one[0],d_two[0],d_three[0]]
    pie_labels = ['Protein','Carbohydrates','Fat']
    pie_colors = plt.get_cmap('Blues')(np.linspace(0.3,1,num=3))

    #--- PIE CHART
    ax1.pie(macros,colors=pie_colors,labels=pie_labels,autopct=pie_percentage \
           ,textprops={'fontsize':6})
    ax1.set_title('Macros')

    #--- BAR CHART
    ax2.bar(d_four,height=d_four,label='Calories',color='r')
    ax2.set_title('Calories')
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Consumed (in kcal)')

    plt.tight_layout()
    plt.show()

  #--- WEEK GRAPH
  elif timeframe.lower() == 'w':
    fig,ax = plt.subplots(2,2)
    fig.suptitle("Weekly Nutrient Metrics")

    #--- VARIABLES
    sum_pro = df['protein'].sum()
    sum_carb = df['carbs'].sum()
    sum_fat = df['fat'].sum()
    total_macros = [sum_pro,sum_carb,sum_fat]
    pieOne_labels = ['Protein','Carbohydrates','Fat']
    pieOne_colors = plt.get_cmap('Reds')(np.linspace(0.3,1,num=3))
    pieTwo_colors = plt.get_cmap('Purples')(np.linspace(0.3,1,num=7))
    w = 0.2
    x = np.arange(len(d_five))
    
    #--- PIE CHART SUBPLOT
    ax[0,0].pie(total_macros,colors=pieOne_colors,labels=pieOne_labels, \
               autopct=pie_percentage,textprops={'fontsize':6})
    ax[0,0].set_title("Total Week Macros")

    #--- BAR CHART SUBPLOT (DAILY MACROS FOR SELECTED WEEK)
    ax[0,1].bar(x,d_one,w,label='Protein',color='Red')
    ax[0,1].bar(x+w,d_two,w,label='Carbs',color='Green')
    ax[0,1].bar(x-w,d_three,w,label='Fat',color='Blue')
    ax[0,1].set_title('Macros')
    ax[0,1].set_xlabel('Date')
    ax[0,1].set_xticks(x,d_five)
    ax[0,1].set_ylabel("Consumed (in grams)")
    ax[0,1].legend(fontsize='6',loc='best')
    
    #--- BAR CHART SUBPLOT (DAILY CALORIES FOR SELECTED WEEK)
    ax[1,0].bar(x,d_four,w,label='Calories',color='Orange')
    ax[1,0].set_title('Calories')
    ax[1,0].set_xlabel('Date')
    ax[1,0].set_xticks(x,d_five)
    ax[1,0].set_ylabel("Consumed (in kcal)")

    #--- PIE CHART SUBPLOT (DAILY CALORIES FOR SELECTED WEEK)
    ax[1,1].pie(d_four,colors=pieTwo_colors,labels=d_five, \
               autopct=pie_percentage,textprops={'fontsize':6})
    ax[1,1].set_title("Daily Calorie Totals")

    plt.tight_layout()
    plt.show()
#---------------------------
# Plot and Present the Graph  
#---------------------------
if __name__ == '__main__':
  dataPlot()

# EOF