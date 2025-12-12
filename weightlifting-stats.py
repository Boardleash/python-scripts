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
  avgAll = round(df['weight_lbs'].mean(),1)
  avgLegs = round(df[df['muscle_group'].str.contains('Legs')]['weight_lbs'].mean(),1)
  avgBack = round(df[df['muscle_group'].str.contains('Back')]['weight_lbs'].mean(),1)
  avgChest = round(df[df['muscle_group'].str.contains('Chest')]['weight_lbs'].mean(),1)
  avgShoulders = round(df[df['muscle_group'].str.contains('Shoulders')]['weight_lbs'].mean(),1)
  avgArms = round(df[df['muscle_group'].str.contains('Arms')]['weight_lbs'].mean(),1)

  print(f"The average amount of weight lifted for ALL LIFTS is {avgAll} pounds.\n"
        f"The average amount of weight lifted for LEGS is {avgLegs} pounds.\n"
        f"The average amount of weight lifted for BACK is {avgBack} pounds.\n"
        f"The average amount of weight lifted for CHEST is {avgChest} pounds.\n"
        f"The average amount of weight lifted for SHOULDERS is {avgShoulders} pounds.\n"
        f"The average amount of weight lifted for ARMS is {avgArms} pounds.")

def sumStats():
  sumAll = round(df['weight_lbs'].sum(),1)
  sumLegs = round(df[df['muscle_group'].str.contains('Legs')]['weight_lbs'].sum(),1)
  sumBack = round(df[df['muscle_group'].str.contains('Back')]['weight_lbs'].sum(),1)
  sumChest = round(df[df['muscle_group'].str.contains('Chest')]['weight_lbs'].sum(),1)
  sumShoulders = round(df[df['muscle_group'].str.contains('Shoulders')]['weight_lbs'].sum(),1)
  sumArms = round(df[df['muscle_group'].str.contains('Arms')]['weight_lbs'].sum(),1)

  print(f"The sum of ALL weight lifted is {sumAll} pounds.\n"
        f"The sum of weight lifted for LEGS is {sumLegs} pounds.\n"
        f"The sum of weight lifted for BACK is {sumBack} pounds.\n"
        f"The sum of weight lifted for CHEST is {sumChest} pounds.\n"
        f"The sum of weight lifted for SHOULDERS is {sumShoulders} pounds.\n"
        f"The sum of weight lifted for ARMS is {sumArms} pounds.")

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
