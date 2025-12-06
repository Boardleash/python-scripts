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
import sys

#----------------------------------------------------------
# Standard DB Connector Configuration using MariaDB library
#----------------------------------------------------------

#db_config = { 
#        'host': 'localhost',
#        'port': '3306',
#        'user': 'testuser',
#        'password': 'test',
#        'database': 'fitness'}

#------------------------------
# DB Connector using SQLAlchemy
#------------------------------

engine = db.create_engine('mariadb+mariadbconnector://testuser:test@localhost:3306/fitness')
connection = engine.connect()

user_request = input("What data would you like to see (AVERAGE or TOTAL)?: ")

#------------------------
# USING MARIADB CONNECTOR
#------------------------

# Query, error handling and connection closing using "normal" MariaDB connection
#try:
#  connection =  mariadb.connect(**db_config)
#  cursor = connection.cursor()
#  cursor.execute("select * from weightlifting where muscle_group='legs'")
#  for row in cursor:
#    print(row)
#except mariadb.Error as e:
#  print(f"Error connecting to MariaDB: {e}")
#  sys.exit(1)
#finally:
#  if 'cursor' in locals() and cursor:
#    cursor.close()
#  if 'conn' in locals() and conn:
#    conn.close()
#    print("Connection closed.")

#-----------------
# USING SQLALCHEMY
#-----------------

if user_request.lower()  == "average":
  query_six = "select avg(weight_lbs) from weightlifting"
  df_six = pd.read_sql_query(query_six,connection).to_string(index=False,header=None)
  print(f"The average amount of weight lifted for ALL LIFTS is {df_six} pounds.")

  query = "select avg(weight_lbs) from weightlifting where muscle_group='legs'"
  df = pd.read_sql_query(query,connection).to_string(index=False,header=None)
  print(f"The average amount of weight lifted for LEGS is {df} pounds.")

  query_two = "select avg(weight_lbs) from weightlifting where muscle_group='back'"
  df_two = pd.read_sql_query(query_two,connection).to_string(index=False,header=None)
  print(f"The average amount of weight lifted for BACK is {df_two} pounds.")

  query_three = "select avg(weight_lbs) from weightlifting where muscle_group='chest'"
  df_three = pd.read_sql_query(query_three,connection).to_string(index=False,header=None)
  print(f"The average amount of weight lifted for CHEST is {df_three} pounds.")

  query_four = "select avg(weight_lbs) from weightlifting where muscle_group='shoulders'"
  df_four = pd.read_sql_query(query_four,connection).to_string(index=False,header=None)
  print(f"The average amount of weight lifted for SHOULDERS is {df_four} pounds.")

  query_five = "select avg(weight_lbs) from weightlifting where muscle_group='arms'"
  df_five = pd.read_sql_query(query_five,connection).to_string(index=False,header=None)
  print(f"The average amount of weight lifted for ARMS is {df_five} pounds.")
elif user_request.lower() == "total":
  query = "select sum(weight_lbs) from weightlifting"
  df = pd.read_sql_query(query,connection).to_string(index=False,header=None)
  print(f"The sum of ALL weight lifted is {df} pounds.")

  query_two = "select sum(weight_lbs) from weightlifting where muscle_group='legs'"
  df_two = pd.read_sql_query(query_two,connection).to_string(index=False,header=None)
  print(f"The sum of weight lifted for LEGS is {df_two} pounds.")

  query_three = "select sum(weight_lbs) from weightlifting where muscle_group='back'"
  df_three= pd.read_sql_query(query_three,connection).to_string(index=False,header=None)
  print(f"The sum of weight lifted for BACK is {df_three} pounds.")

  query_four = "select sum(weight_lbs) from weightlifting where muscle_group='chest'"
  df_four = pd.read_sql_query(query_four,connection).to_string(index=False,header=None)
  print(f"The sum of weight lifted for CHEST is {df_four} pounds.")

  query_five = "select sum(weight_lbs) from weightlifting where muscle_group='shoulders'"
  df_five = pd.read_sql_query(query_five,connection).to_string(index=False,header=None)
  print(f"The sum of weight lifted for SHOULDERS is {df_five} pounds.")

  query_six= "select sum(weight_lbs) from weightlifting where muscle_group='arms'"
  df_six = pd.read_sql_query(query_six,connection).to_string(index=False,header=None)
  print(f"The sum of weight lifted for ARMS is {df_six} pounds.")
else:
  print("That is not a valid entry.")

# Close connection to database
connection.close()
print("Database connection has been closed.")

# EOF
