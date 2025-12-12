import pandas as pd
from termcolor import colored

teamTopGoals = None
teamTopRedCards = None
teamTopYellowCards = None
teamTopAssists = None

def topTeamGoals(df):
    global teamTopGoals
    if 'Goals' not in df.columns or 'Team' not in df.columns:
        print(termcolor.colored("Nie ma kolumny Goals lub Team", "red"))
        return
    teamTopGoals = df.groupby('Team')['Goals'].sum().sort_values(ascending=False)

def topTeamRedCards(df):
    global teamTopRedCards
    if 'Red_Cards' not in df.columns or 'Team' not in df.columns:
        print(termcolor.colored("Nie ma kolumny Red_Cards lub Team", "red"))
        return
    teamTopRedCards = df.groupby('Team')['Red_Cards'].sum().sort_values(ascending=False)

def topTeamYellowCards(df):
    global teamTopYellowCards
    if 'Yellow_Cards' not in df.columns or 'Team' not in df.columns:
        print(termcolor.colored("Nie ma kolumny Yellow_Cards lub Team", "red"))
        return
    teamTopYellowCards = df.groupby('Team')['Yellow_Cards'].sum().sort_values(ascending=False)

def topTeamAssists(df):
    global teamTopAssists
    if 'Assists' not in df.columns or 'Team' not in df.columns:
        print(termcolor.colored("Nie ma kolumny Assists lub Team", "red"))
        return
    teamTopAssists = df.groupby('Team')['Assists'].sum().sort_values(ascending=False)
