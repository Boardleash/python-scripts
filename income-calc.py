#!/usr/bin/env python3
#----------------------------
# TITLE: income-calc.py
# AUTHOR: Boardleash (Derek)
# DATE: Monday, July 7 2025
#----------------------------
#---------------------------- DESCRIPTION ------------------------------------
# Python script to provide income based answers based on your response
#-----------------------------------------------------------------------------
#import readline
#--- Hourly Function
def hourlyKnown():
  '''Work with known hourly earnings'''
  biweekly = round((hourly * 80),2)
  monthly = round((biweekly * 2),2)
  annual = round((monthly * 12),2)
  monthlyRent = round(((annual * 0.30) / 12),2)
  print(f"Based on your HOURLY income (excluding taxes):\n"
        f"${biweekly} is what you earn every two weeks.\n"
        f"${monthly} is what you bring home every month.\n"
        f"${annual} is what you make a year.\n"
        f"Using the 30% rule, you can afford ${monthlyRent} in rent a month.")
#--- Annual Function
def annualKnown():
  '''Work with known annual earnings'''
  monthly = round((annual / 12),2)
  biweekly = round((monthly / 2),2)
  hourly = round((biweekly / 80),2)
  monthlyRent = round(((annual * 0.30) / 12),2)
  print(f"Based on your ANNUAL income (excluding taxes):\n"
        f"${hourly} is what you make an hour.\n"
        f"${biweekly} is what you earn every two weeks.\n"
        f"${monthly} is what you bring home every month.\n"
        f"Using the 30% rule, you can afford ${monthlyRent} in rent a month.")

#--- Main Script
question = input("Which income amount are you able to provide?: \
  \na. Annual\nb. Hourly\nYour response: ")
if question.lower() == 'a' or question.lower() == 'annual':
  annual = input("Please enter your annual income amount: ")
  if annual.isalpha():
    print("Invalid input.")
  else:
    annual = float(annual.replace(",","").replace("$",""))
    annualKnown()
elif question.lower() == 'b' or question.lower() == 'hourly':
  hourly = input("Please enter what you make hourly: ")
  if hourly.isalpha():
    print("Invalid input.")
  else:
    hourly = float(hourly.replace(",","").replace("$",""))
    hourlyKnown()
else:
  print("Invalid response.")
  exit

# EOF