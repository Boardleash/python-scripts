#!/usr/bin/env python3
#----------------------------------
# TITLE: github-repo-lister.py
# AUTHOR: Boardleash (Derek)
# DATE: Sunday, February 23 2025
#----------------------------------
#----------------------------- DESCRIPTION -----------------------------------
# Credit to user 'kenorb' who posted an answer/response to a similar question 
# on Stack Overflow on October 15th, 2025 at 22:56.
# I wanted to build a script around their contribution to make it user 
# interactive, particularly to edit the user variable.
# Link to Stack Overflow question and answer:
# https://stackoverflow.com/questions/8713596/how-to-retrieve-the-list-of- \
# all-github-repositories-of-a-person
#-----------------------------------------------------------------------------
import re
import requests

class clrs:
    cyn = '\033[1;36m'
    noc = '\033[0m'

print(clrs.cyn+f"This script will retrieve a list of PUBLIC GitHub  \
repositories for a particular user.\nThis does NOT clone, checkout or pull \
files or repositories from the user's GitHub!\nThis ONLY provides a list of \
available PUBLIC repositories that the GitHub user created.\nIf you want to \
quit out of the script, type 'quit' or 'q' at the second question\n"+clrs.noc)

#--- Get the repos
def meatnpotatoes():
    '''Ask for GitHub username and get GitHub repos.'''
    GITUSER = input("What's the GitHub username for the repos you want: ")
    DATA = requests.get("https://api.github.com/users/"+GITUSER+"/repos?")

    # Set up a pattern to use for parsing the DATA variable.
    PATTERN = 'git@[^"]*'
    SEARCH = re.findall(PATTERN, DATA.text)
    ANSWER = input("Do you want to save this list? (Yes/No): ")
    if ANSWER.lower() == 'y' or ANSWER.lower() == 'yes':
        for x in SEARCH:
            print(x)
            FILE = open(GITUSER+"_GitHub_Repos", 'a+')
            FILE.write(x+"\n")
            FILE.close()
        print("\nGitHub repo list for "+GITUSER+" saved in current directory.")
    elif ANSWER.lower() == 'n' or ANSWER.lower() == 'no':
        for x in SEARCH:
            print(x)
    elif ANSWER.lower() == 'q' or ANSWER.lower() == 'quit':
        exit
    else:
        print("Invalid response.  Let's start over.")
        meatnpotatoes()

#--- Execute the main function/script.
meatnpotatoes()

# EOF