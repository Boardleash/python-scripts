#!/usr/bin/env python3

###################################
# TITLE: weightlifting-stats.py
# AUTHOR: Boardleash (Derek)
# DATE: Thursday, December 4th 2025
###################################

# Python script to pull weightlifting stats from weightlifting database

import mariadb
import pandas as pd
import readline
import sqlalchemy as db

#------------------------------
# DB Connector Using SQLAlchemy 
#------------------------------
engine = db.create_engine('mariadb+mariadbconnector://testuser:test@localhost:3306/fitness')
connection = engine.connect()

#------ GENERAL DATABASE QUERY ---------
query = "select * from weightlifting;"
df = pd.read_sql_query(query,connection)
connection.close()
#---------------------------------------

def avgStats():
  avg_all = round(df['weight_lbs'].mean(),1)
  avg_legs = round(df[df['muscle_group'].str.contains('Legs')]['weight_lbs'].mean(),1)
  avg_back = round(df[df['muscle_group'].str.contains('Back')]['weight_lbs'].mean(),1)
  avg_chest = round(df[df['muscle_group'].str.contains('Chest')]['weight_lbs'].mean(),1)
  avg_shoulders = round(df[df['muscle_group'].str.contains('Shoulders')]['weight_lbs'].mean(),1)
  avg_arms = round(df[df['muscle_group'].str.contains('Arms')]['weight_lbs'].mean(),1)

  print(f"The average amount of weight lifted for ALL LIFTS is {avg_all} pounds.\n"
        f"The average amount of weight lifted for LEGS is {avg_legs} pounds.\n"
        f"The average amount of weight lifted for BACK is {avg_back} pounds.\n"
        f"The average amount of weight lifted for CHEST is {avg_chest} pounds.\n"
        f"The average amount of weight lifted for SHOULDERS is {avg_shoulders} pounds.\n"
        f"The average amount of weight lifted for ARMS is {avg_arms} pounds.")

def sumStats():
  sum_all = round(df['weight_lbs'].sum(),1)
  sum_legs = round(df[df['muscle_group'].str.contains('Legs')]['weight_lbs'].sum(),1)
  sum_back = round(df[df['muscle_group'].str.contains('Back')]['weight_lbs'].sum(),1)
  sum_chest = round(df[df['muscle_group'].str.contains('Chest')]['weight_lbs'].sum(),1)
  sum_shoulders = round(df[df['muscle_group'].str.contains('Shoulders')]['weight_lbs'].sum(),1)
  sum_arms = round(df[df['muscle_group'].str.contains('Arms')]['weight_lbs'].sum(),1)

  print(f"The sum of ALL weight lifted is {sum_all} pounds.\n"
        f"The sum of weight lifted for LEGS is {sum_legs} pounds.\n"
        f"The sum of weight lifted for BACK is {sum_back} pounds.\n"
        f"The sum of weight lifted for CHEST is {sum_chest} pounds.\n"
        f"The sum of weight lifted for SHOULDERS is {sum_shoulders} pounds.\n"
        f"The sum of weight lifted for ARMS is {sum_arms} pounds.")

#---- SCRIPT EXECUTION ----
question = input("What data would you like to see (AVERAGE or TOTAL)?: ")
if question.lower()  == "average":
  avgStats()
elif question.lower() == "total":
  sumStats()
else:
  print("That is not a valid response.")
  exit

# EOF
