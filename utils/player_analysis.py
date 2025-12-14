import pandas as pd
from termcolor import colored

red_cards = None
yellow_cards = None
goals = None
assists = None

def topRedCards(df):
    global red_cards
    if 'Red_Cards' not in df.columns:
        print(colored("Nie ma kolumny Red_Cards", "red"))
        return
    red_cards = df['Red_Cards']

def topYellowCards(df):
    global yellow_cards
    if 'Yellow_Cards' not in df.columns:
        print(colored("Nie ma kolumny Yellow_Cards", "red"))
        return
    yellow_cards = df['Yellow_Cards']

def topGoals(df):
    global goals
    if 'Goals' not in df.columns:
        print(colored("Nie ma kolumny Goals", "red"))
        return
    goals = df['Goals']

def topAssists(df):
    global assists
    if 'Assists' not in df.columns:
        print(colored("Nie ma kolumny Assists", "red"))
        return
    assists = df['Assists']
