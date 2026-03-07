#!/usr/bin/env python3

#---------------------------------
# TITLE: lifting-graph.py
# AUTHOR: Boardleash (Derek)
# DATE: Saturday, March 7th 2026
#---------------------------------

#--------------------------------------- DESCRIPTION -------------------------------------------------------
# This script is dependent on a MariaDB database, that has necessary data 
# Make necessary changes to the database information and query to suit whatever you may have
# This is a Python script that pulls data from a database and presents that to a user as a graph
#-----------------------------------------------------------------------------------------------------------

import mariadb
import matplotlib.pyplot as plt
import numpy as np
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
queryOne = "select * from weightlifting;"
queryTwo = "select * from burned order by date desc limit 7;"
dfOne = pd.read_sql_query(queryOne,connection)
dfTwo = pd.read_sql_query(queryTwo,connection)
connection.close()

#---------------------------------------
# Functions for Graphs - Use for Testing
#---------------------------------------
def weightsTotals():
  sum_legs = round(dfOne[dfOne['muscle_group'].str.contains('Legs')]['weight_lbs'].sum(),1)
  sum_back = round(dfOne[dfOne['muscle_group'].str.contains('Back')]['weight_lbs'].sum(),1)
  sum_chest = round(dfOne[dfOne['muscle_group'].str.contains('Chest')]['weight_lbs'].sum(),1)
  sum_shoulders = round(dfOne[dfOne['muscle_group'].str.contains('Shoulders')]['weight_lbs'].sum(),1)
  sum_arms = round(dfOne[dfOne['muscle_group'].str.contains('Arms')]['weight_lbs'].sum(),1)
  weights = [sum_arms,sum_back,sum_chest,sum_legs,sum_shoulders]
  pie_labels = ['Arms','Back','Chest','Legs','Shoulders']
  pie_colors = plt.get_cmap('Reds')(np.linspace(0.2,1,num=5))
  plt.pie(weights,colors=pie_colors,labels=pie_labels)
  plt.title('WEIGHTLIFTING SUMS')
  plt.show()

def burnedCalories():
  burned = dfTwo['calories_burned'].tolist()
  date = pd.to_datetime(dfTwo['date']).dt.strftime('%Y-%m-%d').tolist()
  plt.bar(date,burned)
  plt.xlabel('DATE')
  plt.ylabel('CALORIES BURNED')
  plt.title('BURNED CALORIES METRICS')
  plt.show()

def weightGroups():
  sum_legs = round(dfOne[dfOne['muscle_group'].str.contains('Legs')]['weight_lbs'].sum(),1)
  sum_back = round(dfOne[dfOne['muscle_group'].str.contains('Back')]['weight_lbs'].sum(),1)
  sum_chest = round(dfOne[dfOne['muscle_group'].str.contains('Chest')]['weight_lbs'].sum(),1)
  sum_shoulders = round(dfOne[dfOne['muscle_group'].str.contains('Shoulders')]['weight_lbs'].sum(),1)
  sum_arms = round(dfOne[dfOne['muscle_group'].str.contains('Arms')]['weight_lbs'].sum(),1)
  weights = [sum_arms,sum_back,sum_chest,sum_legs,sum_shoulders]
  groups = ['Arms','Back','Chest','Legs','Shoulders']
  plt.barh(groups,weights)
  plt.xlabel('WEIGHT LIFTED (in lbs)')
  plt.ylabel('MUSCLE GROUP')
  plt.title('AMOUNT OF WEIGHT LIFTED (since tracking)')
  plt.show()

def repGroups():
  rep_legs = round(dfOne[dfOne['muscle_group'].str.contains('Legs')]['reps'].sum(),1)
  rep_back = round(dfOne[dfOne['muscle_group'].str.contains('Back')]['reps'].sum(),1)
  rep_chest = round(dfOne[dfOne['muscle_group'].str.contains('Chest')]['reps'].sum(),1)
  rep_shoulders = round(dfOne[dfOne['muscle_group'].str.contains('Shoulders')]['reps'].sum(),1)
  rep_arms = round(dfOne[dfOne['muscle_group'].str.contains('Arms')]['reps'].sum(),1)
  rep_groups = [rep_arms,rep_back,rep_chest,rep_legs,rep_shoulders]
  groups = ['Arms','Back','Chest','Legs','Shoulders']
  plt.bar(groups,rep_groups)
  plt.xlabel('MUSCLE GROUP')
  plt.ylabel('AMOUNT OF REPS')
  plt.title('MUSCLE GROUP REPS')
  plt.show()
  
def megaPlot():
  plt.rc('font',size='10')
  plt.rc('xtick',labelsize='8')
  plt.rc('ytick',labelsize='8')
  fig,axs = plt.subplots(2,2)
  #--- WEIGHTS TOTAL DATA
  sum_legs = round(dfOne[dfOne['muscle_group'].str.contains('Legs')]['weight_lbs'].sum(),1)
  sum_back = round(dfOne[dfOne['muscle_group'].str.contains('Back')]['weight_lbs'].sum(),1)
  sum_chest = round(dfOne[dfOne['muscle_group'].str.contains('Chest')]['weight_lbs'].sum(),1)
  sum_shoulders = round(dfOne[dfOne['muscle_group'].str.contains('Shoulders')]['weight_lbs'].sum(),1)
  sum_arms = round(dfOne[dfOne['muscle_group'].str.contains('Arms')]['weight_lbs'].sum(),1)
  weights = [sum_arms,sum_back,sum_chest,sum_legs,sum_shoulders]
  pie_labels = ['Arms','Back','Chest','Legs','Shoulders']
  pie_colors = plt.get_cmap('Reds')(np.linspace(0.2,1,num=5))
  axs[0,0].pie(weights,colors=pie_colors,labels=pie_labels)
  axs[0,0].set_title('WEIGHTLIFTING SUMS')
  #--- BURNED CALORIES DATA
  burned = dfTwo['calories_burned'].tolist()
  date = pd.to_datetime(dfTwo['date']).dt.strftime('%Y-%m-%d').tolist()
  axs[0,1].bar(date,burned)
  axs[0,1].set_title('BURNED CALORIES')
  axs[0,1].set_xlabel('DATE')
  axs[0,1].set_ylabel('CALORIES BURNED')
  #--- WEIGHT GROUPS DATA
  groups = ['Arms','Back','Chest','Legs','Shoulders']
  axs[1,0].barh(groups,weights)
  axs[1,0].set_title('WEIGHT LIFTED (since tracking)')
  axs[1,0].set_xlabel('WEIGHT LIFTED (in lbs)')
  axs[1,0].set_ylabel('MUSCLE GROUP')
  #--- REP GROUPS DATA
  rep_legs = round(dfOne[dfOne['muscle_group'].str.contains('Legs')]['reps'].sum(),1)
  rep_back = round(dfOne[dfOne['muscle_group'].str.contains('Back')]['reps'].sum(),1)
  rep_chest = round(dfOne[dfOne['muscle_group'].str.contains('Chest')]['reps'].sum(),1)
  rep_shoulders = round(dfOne[dfOne['muscle_group'].str.contains('Shoulders')]['reps'].sum(),1)
  rep_arms = round(dfOne[dfOne['muscle_group'].str.contains('Arms')]['reps'].sum(),1)
  rep_groups = [rep_arms,rep_back,rep_chest,rep_legs,rep_shoulders]
  axs[1,1].plot(groups,rep_groups)
  axs[1,1].set_title('MUSCLE GROUP REPS')
  axs[1,1].set_xlabel('MUSCLE GROUP')
  axs[1,1].set_ylabel('AMOUNT OF REPS')

  plt.tight_layout()
  plt.show()
#----------------------------
# Plot and Present the Graphs  
#----------------------------
if __name__ == '__main__':
  #burnedCalories()
  #repGroups()
  #weightGroups()
  #weightMetrics()
  megaPlot()

# EOF