#!/usr/bin/env python3
#------------------------
# TITLE: fish-data.py
# AUTHOR: Boardleash (Derek)
# DATE: Tuesday, December 9th 2025
#----------------------------------
#------------------------------ DESCRIPTION ----------------------------------
# Python script to pull data from database regarding tinned fish
# Requires MySQL database to be online with appropriate data
#-----------------------------------------------------------------------------
import mysql.connector
import pandas as pd
import sqlalchemy as db

#--- DB Connection and Queries
engine = db.create_engine('mysql+mysqlconnector://testuser:test@demersal: \
  48123/tins')
#engine = db.create_engine('mysql+mysqlconnector://testuser:test@altdem: \
# 48123/tins')
#engine = db.create_engine('mysql+mysqlconnector://testuser:test@atlantis: \
# 48123/tins')
connection = engine.connect()
a_query = "select * from anchovies;"
m_query = "select * from mackerel;"
s_query = "select * from sardines;"
a_df = pd.read_sql_query(a_query,connection)
m_df = pd.read_sql_query(m_query,connection)
s_df = pd.read_sql_query(s_query,connection)
connection.close()

#--- Anchovy Data Function
def anchovyData():
  '''Manipulate anchovy data from database.'''
  q_one = input("What information are you looking for? \
    \na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if q_one.lower() == "a" or q_one.lower() == "most expensive tins":
    filter_df = a_df[['brand', 'base', 'cost']]
    expensive = filter_df[(filter_df['cost'] > 7)].sort_values(by='cost', \
      ascending=False).to_string(index=False)
    print(f"\nThe most expensive anchovy tins are as follows:\n\n{expensive}")

  elif q_one.lower() == "b" or q_one.lower() == "top consumed tins":
    filter_df = a_df[['brand', 'base', 'consumed']]
    consumed = filter_df[(filter_df['consumed'] > 0)].sort_values \
      (by='consumed', ascending=False).to_string(index=False)
    print(f"\nThe top consumed anchovy tins are as follows:\n\n{consumed}")

  elif q_one.lower() == "c" or q_one.lower() == "other":
    q_two = input("Select an option below:\
    \na. Brands\nb. Bases\nc. Boneless and Skinless\nd. Anchovy Brand Sources\
    \nYour Response: ")

    if q_two.lower() == "a" or q_two.lower() == "brands":
      brands = sorted(a_df['brand'].unique())
      print(f"\nThere are "+str(len(brands))+" brands of anchovies tracked.\n"
      f"They are as follows:\n")
      for brand in brands:
        print(brand)

    elif q_two.lower() == "b" or q_two.lower() == "bases":
      bases = sorted(a_df['base'].unique())
      print(f"\nThere are "+str(len(bases))+" bases of anchovies tracked.\n"
      f"They are as follows:\n") 
      for base in bases:
        print(base)

    elif q_two.lower() == "c" or q_two.lower() == "boneless and skinless":
      boneless = a_df[a_df['boneless'].str.contains('y') | \
        a_df['skinless'].str.contains('y')]
      bnlesbrands = sorted(boneless['brand'].unique())
      print(f"\nThere are "+str(len(bnlesbrands))+" boneless/skinless \
options tracked.\nThey are as follows:\n")
      for nobones in bnlesbrands:
        print(nobones)

    elif q_two.lower() == "d" or q_two.lower() == "sardine brand sources":
      a_sources = sorted(a_df['origin'].unique())
      print(f"\nThe anchovies tracked come from the following locations:\n")
      for source in a_sources:
        print(source)

    else:
      print("That is an invalid response.")
      exit
  else:
    print("That is an invalid response.")
    exit
#--- Mackerel Function
def mackerelData():
  '''Manipulate mackerel data from database.'''
  q_one = input("What information are you looking for? \
    \na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if q_one.lower() == "a" or q_one.lower() == "most expensive tins":
    filter_df = m_df[['brand', 'base', 'cost']]
    expensive = filter_df[(filter_df['cost'] > 10)].sort_values \
      (by='cost', ascending=False).to_string(index=False)
    print(f"\nThe most expensive mackerel tins are as follows:\n\n{expensive}")

  elif q_one.lower() == "b" or q_one.lower() == "top consumed tins":
    filter_df = m_df[['brand', 'base', 'consumed']]
    consumed = filter_df[(filter_df['consumed'] > 0)].sort_values \
      (by='consumed', ascending=False).to_string(index=False)
    print(f"\nThe top consumed mackerel tins are as follows:\n\n{consumed}")

  elif q_one.lower() == "c" or q_one.lower() == "other":
    q_two = input("Please select an option below:\na. Brands\nb. Bases \
      \nc. Boneless and Skinless\nd. Mackerel Brand Sources\nYour Response: ")

    if q_two.lower() == "a" or q_two.lower() == "brands":
      brands = sorted(m_df['brand'].unique())
      print(f"\nThere are "+str(len(brands))+" mackerel brands tracked.\n"
        f"They are as follows:\n")
      for brand in brands:
        print(brand)

    elif q_two.lower() == "b" or q_two.lower() == "bases":
      bases = sorted(m_df['base'].unique())
      print(f"\nThere are "+str(len(bases))+" mackerel bases tracked.\n"
        f"They are as follows:\n")
      for base in bases:
        print(base)

    elif q_two.lower() == "c" or q_two.lower() == "boneless and skinless":
      boneless = m_df[m_df['boneless'].str.contains('y') | \
        m_df['skinless'].str.contains('y')]
      bnlesbrands = sorted(boneless['brand'].unique())
      print(f"\nThere are "+str(len(bnlesbrands))+" boneless/skinless \
options tracked.\nThey are as follows:\n")
      for nobones in bnlesbrands:
        print(nobones)

    elif q_two.lower() == "d" or q_two.lower() == "mackerel brand sources":
      sources= sorted(m_df['origin'].unique())
      print(f"\nThe mackerel tracked come from the following locations:\n")
      for source in sources:
        print(source)

    else:
      print("That is an invalid response.")
      exit
  else:
    print("That is an invalid response.")
    exit
#--- Sardine Function
def sardineData():
  '''Manipulate sardine data from database.'''
  q_one = input("What information are you looking for?\
    \na. Most Expensive Tins\nb. Top Consumed Tins\nc. Other\nYour Response: ")
  if q_one.lower() == "a" or q_one.lower() == "most expensive tins":
    filter_df = s_df[['brand', 'base', 'cost']]
    expensive = filter_df[(filter_df['cost'] > 11)].sort_values \
      (by='cost', ascending=False).to_string(index=False)
    print(f"\nThe most expensive sardine tins are as follows:\n\n{expensive}")

  elif q_one.lower() == "b" or q_one.lower() == "top consumed tins":
    filter_df = s_df[['brand', 'base', 'consumed']]
    consumed = filter_df[(filter_df['consumed'] > 7)].sort_values \
      (by='consumed', ascending=False).to_string(index=False)
    print(f"\nThe top consumed sardine tins are as follows:\n\n{consumed}")

  elif q_one.lower() == "c" or q_one.lower() == "other":
    q_two = input("Select an option below: \
      \na. Brands\nb. Bases\nc. Boneless and Skinless \
      \nd. Sardine Brand Sources\nYour Response: ")

    if q_two.lower() == "a" or q_two.lower() == "brands":
      brands = sorted(s_df['brand'].unique())
      print(f"\nThere are "+str(len(brands))+" sardine brands tracked.\n"
        f"They are as follows:\n")
      for brand in brands:
        print(brand)

    elif q_two.lower() == "b" or q_two.lower() == "bases":
      bases = sorted(s_df['base'].unique())
      print(f"\nThere are "+str(len(bases))+" sardine bases tracked.\n"
        f"They are as follows:\n")
      for base in bases:
        print(base)

    elif q_two.lower() == "c" or q_two.lower() == "boneless and skinless":
      boneless = s_df[s_df['boneless'].str.contains('y') | \
        s_df['skinless'].str.contains('y')]
      bnlesbrands = sorted(boneless['brand'].unique())
      print(f"\nThere are "+str(len(bnlesbrands))+" boneless/skinless \
options tracked.\nThey are as follows:\n")
      for nobones in bnlesbrands:
        print(nobones)

    elif q_two.lower() == "d" or q_two.lower() == "sardine brand sources":
      sources = sorted(s_df['origin'].unique())
      print(f"\nThe sardines tracked come from the following locations:\n")
      for source in sources:
        print(source)

    else:
      print("That is an invalid response.")
      exit
  else:
    print("That is an invalid response.")
    exit

#--- Main Function 
def fishData():
  '''Main function for full script execution.'''
  q_one = input("Which type of fish are you looking for information on? \
    \na. Anchovies\nb. Mackerel\nc. Sardines\nYour Response: ")
  if q_one.lower() == "a" or q_one.lower() == "anchovies":
    anchovyData()
  elif q_one.lower() == "b" or q_one.lower() == "mackerel":
    mackerelData()
  elif q_one.lower() == "c" or q_one.lower() == "sardines":
    sardineData()
  else:
    print("That is not a valid response.")
    exit
  
fishData()

# EOF