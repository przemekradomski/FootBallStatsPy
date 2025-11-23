from utils import player_analysis
from utils import team_analysis

def printTopRedCards():
    if player_analysis.red_cards is not None:
        print("Top czerwone kartki")
        print(player_analysis.red_cards.sort_values(ascending=False))
    else:
        print("Brak danych o czerwonych kartkach")
def printTopYellowCards():
    if player_analysis.yellow_cards is not None:
        print("Top żółte kartki")
        print(player_analysis.yellow_cards.sort_values(ascending=False))
    else:
        print("Brak danych o żółtych kartkach")
def printTopGoals():
    if player_analysis.goals is not None:
        print("Top Gole")
        print(player_analysis.goals.sort_values(ascending=False))
    else:
        print("Brak danych o golach")
def printTopAssists():
    if player_analysis.assists is not None:
        print("Top asysty")
        print(player_analysis.assists.sort_values(ascending=False))
    else:
        print("Brak danych o asystach")
def printTeamTopGoals():
    if team_analysis.teamTopGoals is not None:
        print("Top gole drużyny")
        print(team_analysis.teamTopGoals)
    else:
        print("Brak danych o golach")
def printTeamTopAssists():
    if team_analysis.teamTopAssists is not None:
        print("Top asysty drużyny")
        print(team_analysis.teamTopAssists)
    else:
        print("Brak danych o asystach")
def printTeamTopRedCards():
    if team_analysis.teamTopRedCards is not None:
        print("Top czerwone kartki drużyny")
        print(team_analysis.teamTopRedCards)
    else:
        print("Brak danych o czerwonych kartkach")
def printTeamTopYellowCards():
    if team_analysis.teamTopYellowCards is not None:
        print("Top żółte kartki drużyny")
        print(team_analysis.teamTopYellowCards)
    else:
        print("Brak danych o żółtych kartkach")
