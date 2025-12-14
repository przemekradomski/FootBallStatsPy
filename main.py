import pandas as pd
from utils import player_analysis
from utils import team_analysis
from scripts import print_datas
from termcolor import colored

def loadData(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(colored(f"Błąd: Nie znaleziono pliku {file_path}", "red"))
        return None
    except Exception as e:
        print(colored(f"Błąd podczas ładowania danych: {e}", "red"))
        return None

def getUserInput():
    print("Wybierz z czego chcesz zobaczyć ranking:")
    print("1. Top gole")
    print("2. Top asysty")
    print("3. Top żółte kartki")
    print("4. Top czerwone kartki")
    choice = input("Wybierz 1, 2, 3 lub 4: ")
    if choice == "1":
        player_analysis.topGoals(df)
        print_datas.printTopGoals()
        team_analysis.topTeamGoals(df)
        print_datas.printTeamTopGoals()
    elif choice == "2":
        player_analysis.topAssists(df)
        print_datas.printTopAssists()
        team_analysis.topTeamAssists(df)
        print_datas.printTeamTopAssists()
    elif choice == "3":
        player_analysis.topYellowCards(df)
        print_datas.printTopYellowCards()
        team_analysis.topTeamYellowCards(df)
        print_datas.printTeamTopYellowCards()
    elif choice == "4":
        player_analysis.topRedCards(df)
        print_datas.printTopRedCards()
        team_analysis.topTeamRedCards(df)
        print_datas.printTeamTopRedCards()    
    else:
        print(colored("Nieprawidłowa opcja", "red"))

if __name__ == "__main__":
    df = loadData("data/sports_data.csv")
    if df is not None:
        getUserInput()
