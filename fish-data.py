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
anchovyQuery = "select * from anchovies;"
mackerelQuery = "select * from mackerel;"
sardineQuery = "select * from sardines;"
anchovyDf = pd.read_sql_query(anchovyQuery,connection)
mackerelDf = pd.read_sql_query(mackerelQuery,connection)
sardineDf = pd.read_sql_query(sardineQuery,connection)
connection.close()
#---------------------------------------------------------

def anchovyData():
  '''Function for pulling data related to the anchovies table of the database.'''
  question = input("What information are you looking for?\na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if question.lower() == "a" or question.lower() == "most expensive tins":
    filteredDf = anchovyDf[['brand', 'base', 'cost']]
    expensive = filteredDf[(filteredDf['cost'] > 7)].sort_values(by='cost', ascending=False).to_string(index=False)
    print(f"\nThe most expensive anchovy tins are as follows:\n\n{expensive}")

  elif question.lower() == "b" or question.lower() == "top consumed tins":
    filteredDf = anchovyDf[['brand', 'base', 'consumed']]
    consumed = filteredDf[(filteredDf['consumed'] > 0)].sort_values(by='consumed', ascending=False).to_string(index=False)
    print(f"\nThe top consumed anchovy tins are as follows:\n\n{consumed}")

  elif question.lower() == "c" or question.lower() == "other":
    newQuestion = input("Please select an option below as it pertains to the other information you are looking for?\na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Anchovy Brand Sources\nYour Response: ")

    if newQuestion.lower() == "a" or newQuestion.lower() == "brands":
      anchovyBrands = sorted(anchovyDf['brand'].unique())
      print(f"\nThere are "+str(len(anchovyBrands))+" unique brands of anchovies that are currently in the database.\n"
            f"The following unique brands of anchovies are being tracked in the database:\n")
      for brand in anchovyBrands:
        print(brand)

    elif newQuestion.lower() == "b" or newQuestion.lower() == "bases":
      anchovyBases = sorted(anchovyDf['base'].unique())
      print(f"\nThere are a total of "+str(len(anchovyBases))+" unique bases for anchovies that are currently in the database.\n"
            f"The following bases for anchovies are being tracked in the database:\n")
      for base in anchovyBases:
        print(base)

    elif newQuestion.lower() == "c" or newQuestion.lower() == "boneless and skinless":
      bonelessSkinless = anchovyDf[anchovyDf['boneless'].str.contains('y') | anchovyDf['skinless'].str.contains('y')]
      bonelessBrands = sorted(bonelessSkinless['brand'].unique())
      print(f"\nThere are a total of "+str(len(bonelessBrands))+" unique boneless/skinless anchovy options that are in the database.\n"
            f"The following brands have a boneless/skinless option for anchovies:\n")
      for nobones in bonelessBrands:
        print(nobones)

    elif newQuestion.lower() == "d" or newQuestion.lower() == "sardine brand sources":
      anchovySources = sorted(anchovyDf['origin'].unique())
      print(f"\nThe anchovies tracked in this database come from the following unique locations:\n")
      for source in anchovySources:
        print(source)

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
    filteredDf = mackerelDf[['brand', 'base', 'cost']]
    expensive = filteredDf[(filteredDf['cost'] > 7)].sort_values(by='cost', ascending=False).to_string(index=False)
    print(f"\nThe most expensive mackerel tins are as follows:\n\n{expensive}")

  elif question.lower() == "b" or question.lower() == "top consumed tins":
    filteredDf = mackerelDf[['brand', 'base', 'consumed']]
    consumed = filteredDf[(filteredDf['consumed'] > 0)].sort_values(by='consumed', ascending=False).to_string(index=False)
    print(f"\nThe top consumed mackerel tins are as follows:\n\n{consumed}")

  elif question.lower() == "c" or question.lower() == "other":
    newQuestion = input("Please select an option below as it pertains to the other information you are looking for?\na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Mackerel Brand Sources\nYour Response: ")

    if newQuestion.lower() == "a" or newQuestion.lower() == "brands":
      mackerelBrands= sorted(mackerelDf['brand'].unique())
      print(f"\nThere are "+str(len(mackerelBrands))+" unique brands of mackerel that are currently in the database.\n"
            f"The following unique brands of mackerel are being tracked in the database:\n")
      for brand in mackerelBrands:
        print(brand)

    elif newQuestion.lower() == "b" or newQuestion.lower() == "bases":
      mackerelBases = sorted(mackerelDf['base'].unique())
      print(f"\nThere are a total of "+str(len(mackerelBases))+" unique bases for mackerel that are currently in the database.\n"
            f"The following bases for mackerel are being tracked in the database:\n")
      for base in mackerelBases:
        print(base)

    elif newQuestion.lower() == "c" or newQuestion.lower() == "boneless and skinless":
      bonelessSkinless = mackerelDf[mackerelDf['boneless'].str.contains('y') | mackerelDf['skinless'].str.contains('y')]
      bonelessBrands = sorted(bonelessSkinless['brand'].unique())
      print(f"\nThere are a total of "+str(len(bonelessBrands))+" unique boneless/skinless options for mackerel that are in the database.\n"
            f"The following brands have a boneless/skinless option for mackerel:\n")
      for nobones in bonelessBrands:
        print(nobones)

    elif newQuestion.lower() == "d" or newQuestion.lower() == "mackerel brand sources":
      mackerelSources= sorted(mackerelDf['origin'].unique())
      print(f"\nThe mackerel tracked in this database come from the following unique locations:\n")
      for source in mackerelSources:
        print(source)

    else:
      print("That is an invalid response.")
      exit

def sardineData():
  '''Function for pulling data from the sardine table in the database.'''
  question = input("What information are you looking for?\na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if question.lower() == "a" or question.lower() == "most expensive tins":
    filteredDf = sardineDf[['brand', 'base', 'cost']]
    expensive = filteredDf[(filteredDf['cost'] > 10)].sort_values(by='cost', ascending=False).to_string(index=False)
    print(f"\nThe most expensive sardine tins are as follows:\n\n{expensive}")

  elif question.lower() == "b" or question.lower() == "top consumed tins":
    filteredDf = sardineDf[['brand', 'base', 'consumed']]
    consumed = filteredDf[(filteredDf['consumed'] > 7)].sort_values(by='consumed', ascending=False).to_string(index=False)
    print(f"\nThe top consumed sardine tins are as follows:\n\n{consumed}")

  elif question.lower() == "c" or question.lower() == "other":
    newQuestion = input("Please select an option below as it pertains to the other information you are looking for?\na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Sardine Brand Sources\nYour Response: ")

    if newQuestion.lower() == "a" or newQuestion.lower() == "brands":
      sardineBrands = sorted(sardineDf['brand'].unique())
      print(f"\nThere are "+str(len(sardineBrands))+" unique sardine brands that are currently in the database.\n"
            f"The following unique sardine brands are being tracked in the database:\n")
      for brand in sardineBrands:
        print(brand)

    elif newQuestion.lower() == "b" or newQuestion.lower() == "bases":
      sardineBases = sorted(sardineDf['base'].unique())
      print(f"\nThere are a total of "+str(len(sardineBases))+" unique sardine bases that are currently in the database.\n"
            f"The following sardine bases are being tracked in the database:\n")
      for base in sardineBases:
        print(base)

    elif newQuestion.lower() == "c" or newQuestion.lower() == "boneless and skinless":
      bonelessSkinless = sardineDf[sardineDf['boneless'].str.contains('y') | sardineDf['skinless'].str.contains('y')]
      bonelessBrands = sorted(bonelessSkinless['brand'].unique())
      print(f"\nThere are a total of "+str(len(bonelessBrands))+" unique boneless/skinless options for sardines that are in the database.\n"
            f"The following brands have a boneless/skinless option for sardines:\n")
      for nobones in bonelessBrands:
        print(nobones)

    elif newQuestion.lower() == "d" or newQuestion.lower() == "sardine brand sources":
      sardineSources = sorted(sardineDf['origin'].unique())
      print(f"\nThe sardines tracked in this database come from the following unique locations:\n")
      for source in sardineSources:
        print(source)

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
  else:
    print("That is not a valid response.")
    exit
  
fishData()

# EOF
