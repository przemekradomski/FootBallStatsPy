import pandas as pd

# Zmienne modułowe dostępne z innych plików
teamTopGoals = None
teamTopRedCards = None
teamTopYellowCards = None
teamTopAssists = None

def topTeamGoals(df):
    global teamTopGoals
    if 'Goals' not in df.columns or 'Team' not in df.columns:
        print("Nie ma kolumny Goals lub Team")
        return
    teamTopGoals = df.groupby('Team')['Goals'].sum().sort_values(ascending=False)

def topTeamRedCards(df):
    global teamTopRedCards
    if 'Red_Cards' not in df.columns or 'Team' not in df.columns:
        print("Nie ma kolumny Red_Cards lub Team")
        return
    teamTopRedCards = df.groupby('Team')['Red_Cards'].sum().sort_values(ascending=False)

def topTeamYellowCards(df):
    global teamTopYellowCards
    if 'Yellow_Cards' not in df.columns or 'Team' not in df.columns:
        print("Nie ma kolumny Yellow_Cards lub Team")
        return
    teamTopYellowCards = df.groupby('Team')['Yellow_Cards'].sum().sort_values(ascending=False)

def topTeamAssists(df):
    global teamTopAssists
    if 'Assists' not in df.columns or 'Team' not in df.columns:
        print("Nie ma kolumny Assists lub Team")
        return
    teamTopAssists = df.groupby('Team')['Assists'].sum().sort_values(ascending=False)