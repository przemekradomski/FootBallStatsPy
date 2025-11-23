import pandas as pd

# Zmienne modułowe dostępne z innych plików
red_cards = None
yellow_cards = None
goals = None
assists = None

def topRedCards(df):
    global red_cards
    if 'Red_Cards' not in df.columns:
        print("Nie ma kolumny Red_Cards")
        return
    red_cards = df['Red_Cards']

def topYellowCards(df):
    global yellow_cards
    if 'Yellow_Cards' not in df.columns:
        print("Nie ma kolumny Yellow_Cards")
        return
    yellow_cards = df['Yellow_Cards']

def topGoals(df):
    global goals
    if 'Goals' not in df.columns:
        print("Nie ma kolumny Goals")
        return
    goals = df['Goals']

def topAssists(df):
    global assists
    if 'Assists' not in df.columns:
        print("Nie ma kolumny Assists")
        return
    assists = df['Assists']