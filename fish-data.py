#!/usr/bin/env python3

#------------------------
# TITLE: fish-data.py
# AUTHOR: Boardleash (Derek)
# DATE: Tuesday, December 9th 2025
#----------------------------------

# Python script to pull some data from a MySQL database container regarding tinned fish
# Requires that a MySQL database is running with the appropriate data

import mysql.connector
import pandas as pd
import readline
import sqlalchemy as db

#------------------------------
# DB Connector using SQLAlchemy
#------------------------------

#engine = db.create_engine('mysql+mysqlconnector://testuser:test@localhost:48124/tins')
engine = db.create_engine('mysql+mysqlconnector://root@localhost:48124/tins')
connection = engine.connect()

#--------- DB CONNECTION FAIL BLOCK ------------
#try:
#  connection.close()
#  query = "select * from sardines limit 1;"
#  test_df = pd.read_sql_query(query,connection)
#  print(test_df)
#except:
#  print("Database connection is already closed.")

#-------- GENERAL DATABASE QUERIES -----------------------
anchovy_query = "select * from anchovies;"
mackerel_query = "select * from mackerel;"
sardines_query = "select * from sardines;"
anchovy_df = pd.read_sql_query(anchovy_query,connection)
mackerel_df = pd.read_sql_query(mackerel_query,connection)
sardines_df = pd.read_sql_query(sardines_query,connection)
connection.close()
#---------------------------------------------------------

def anchovyData():
  '''Function for pulling data related to the anchovies table of the database.'''
  question = input("What information are you looking for?\na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if question.lower() == "a" or question.lower() == "most expensive tins":
    filtered_df = anchovy_df[['brand', 'base', 'cost']]
    expensive = filtered_df[(filtered_df['cost'] > 7)].sort_values(by='cost', ascending=False)
    print(f"\nThe most expensive tins are as follows:\n\n{expensive}")

  elif question.lower() == "b" or question.lower() == "top consumed tins":
    filtered_df = anchovy_df[['brand', 'base', 'consumed']]
    consumed = filtered_df[(filtered_df['consumed'] > 0)].sort_values(by='consumed', ascending=False)
    print(f"\nThe top consumed tins are as follows:\n\n{consumed}")

  elif question.lower() == "c" or question.lower() == "other":
    new_question = input("Please select an option below as it pertains to the other information you are looking for?\na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Anchovy Brand Sources\nYour Response: ")

    if new_question.lower() == "a" or new_question.lower() == "brands":
      anchovy_brands = sorted(anchovy_df['brand'].unique())
      print("There are "+str(len(anchovy_brands))+" unique brands that are currently in the database.")
      print("The following unique brands are being tracked in the database: \n")
      for i in anchovy_brands:
        print(i)

    elif new_question.lower() == "b" or new_question.lower() == "bases":
      anchovy_bases = sorted(anchovy_df['base'].unique())
      print("There are a total of "+str(len(anchovy_bases))+" unique bases that are currently in the database.")
      print("The following bases are being tracked in the database: \n")
      for i in anchovy_bases:
        print(i)

    elif new_question.lower() == "c" or new_question.lower() == "boneless and skinless":
      boneless_skinless = anchovy_df[anchovy_df['boneless'].str.contains('y') | anchovy_df['skinless'].str.contains('y')]
      distinct_brands = sorted(boneless_skinless['brand'].unique())
      print("There are a total of "+str(len(boneless_skinless))+" unique boneless/skinless options that are in the database.")
      print("The following brands have a boneless/skinless option:\n")
      for i in distinct_brands:
        print(i)

    elif new_question.lower() == "d" or new_question.lower() == "sardine brand sources":
      anchovy_sources = sorted(anchovy_df['origin'].unique())
      print("The anchovies tracked in this database come from the following unique locations:\n")
      for i in anchovy_sources:
        print(i)

    else:
      print("That is an invalid response.")
      exit
  else:
    print("That is an invalid response.")
    exit

def mackerelData():
  '''Function for pulling data from the mackerel table in the database.'''
  question = input("What information are you looking for?\na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if question.lower() == "a" or question.lower() == "most expensive tins":
    filtered_df = mackerel_df[['brand', 'base', 'cost']]
    expensive = filtered_df[(filtered_df['cost'] > 7)].sort_values(by='cost', ascending=False)
    print(f"\nThe most expensive tins are as follows:\n\n{expensive}")

  elif question.lower() == "b" or question.lower() == "top consumed tins":
    filtered_df = mackerel_df[['brand', 'base', 'consumed']]
    consumed = filtered_df[(filtered_df['consumed'] > 0)].sort_values(by='consumed', ascending=False)
    print(f"\nThe top consumed tins are as follows:\n\n{consumed}")

  elif question.lower() == "c" or question.lower() == "other":
    new_question = input("Please select an option below as it pertains to the other information you are looking for?\na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Mackerel Brand Sources\nYour Response: ")

    if new_question.lower() == "a" or new_question.lower() == "brands":
      mackerel_brands = sorted(mackerel_df['brand'].unique())
      print("There are "+str(len(mackerel_brands))+" unique brands that are currently in the database.")
      print("The following unique brands are being tracked in the database: \n")
      for i in mackerel_brands:
        print(i)

    elif new_question.lower() == "b" or new_question.lower() == "bases":
      base_bank = df.values.tolist()
      print("There are a total of "+str(len(base_bank))+" unique bases that are currently in the database.")
      print("The following bases are being tracked in the database: \n")
      for i in base_bank:
        print(i[0])

    elif new_question.lower() == "c" or new_question.lower() == "boneless and skinless":
      boneless_count = df.values.tolist()
      boneless_brands = df_two.values.tolist()
      print("There are a total of "+str(len(boneless_count))+" unique boneless/skinless options that are in the database.")
      print("The following brands have a boneless/skinless option:\n")
      for i in boneless_brands:
        print(i[0])

    elif new_question.lower() == "d" or new_question.lower() == "mackerel brand sources":
      location_bank = df.values.tolist()
      print("The mackerel tracked in this database come from the following unique locations:\n")
      for i in location_bank:
        print(i[0])

    else:
      print("That is an invalid response.")
      exit
  else:
    print("That is an invalid response.")
    exit

def sardineData():
  '''Function for pulling data from the sardine table in the database.'''
  question = input("What information are you looking for?\na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if question.lower() == "a" or question.lower() == "most expensive tins":
    print(f"\nThe most expensive tins are as follows:\n\n{df}")
  elif question.lower() == "b" or question.lower() == "top consumed tins":
    print(f"\nThe top consumed tins are as follows:\n\n{df}")
  elif question.lower() == "c" or question.lower() == "other":
    new_question = input("Please select an option below as it pertains to the other information you are looking for?\na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Sardine Brand Sources\nYour Response: ")
    if new_question.lower() == "a" or new_question.lower() == "brands":
      sardine_bank = df.values.tolist()
      print("There are "+str(len(sardine_bank))+" unique brands that are currently in the database.")
      print("The following brands are being tracked in the database: \n")
      for i in sardine_bank:
        print(i[0])
    elif new_question.lower() == "b" or new_question.lower() == "bases":
      base_bank = df.values.tolist()
      print("There are a total of "+str(len(base_bank))+" unique bases that are currently in the database.")
      print("The following bases are being tracked in the database: \n")
      for i in base_bank:
        print(i[0])
    elif new_question.lower() == "c" or new_question.lower() == "boneless and skinless":
      boneless_count = df.values.tolist()
      boneless_brands = df_two.values.tolist()
      print("There are a total of "+str(len(boneless_count))+" unique boneless/skinless options that are in the database.")
      print("The following brands have a boneless/skinless option:\n")
      for i in boneless_brands:
        print(i[0])
    elif new_question.lower() == "d" or new_question.lower() == "sardine brand sources":
      location_bank = df.values.tolist()
      print("The sardines tracked in this database come from the following unique locations:\n")
      for i in location_bank:
        print(i[0])
    else:
      print("That is an invalid response.")
      exit

#--------------
# Main Function 
#--------------

def fishData():
  '''Main function for full script execution.'''
  question = input("Which type of fish are you looking for information on?\na. Anchovies\nb. Mackerel\nc. Sardines\nYour Response: ")
  if question.lower() == "a" or question.lower() == "anchovies":
    anchovyData()
  elif question.lower() == "b" or question.lower() == "mackerel":
    mackerelData()
  elif question.lower() == "c" or question.lower() == "sardines":
    sardineData()
  
fishData()

# EOF
