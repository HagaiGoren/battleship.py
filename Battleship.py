# Omer Dan  ID- 316478882
# Hagai Goren ID- 208957555

import json

# globals
historyfile = "json.json"
data = {}


# TODO: add defaults in order to start json- we did
# TODO: save game - player names with scores-we did
# TODO: update inside data base, high scores, etc
# TODO: function shows last 2 players that played


def print_menu():
    print("-------- Welcome to battleship ---------")
    print("press H for game high scores")
    print("press N for player history")
    print("press P to start play")
    print("press Q to quit the game")


def set_gamedata_from_historyfile():
     global data
     with open(historyfile, 'r') as jsonfile:
         data = json.load(jsonfile)


def update_historyfile_from_gamedata():
    global data
    with open(historyfile, 'w') as jsonfile:
            json.dump(data, jsonfile)


def get_player_games(name):
    f = open("json.json", "r").read()
    data1 = json.load(f)
    print(data1.players)



def high_scores():
    firstMax = 0
    secMax = 0
    thirdMax = 0

    for currObject in data:
        currMax = max(currObject[0],firstMax)
        if (currMax > firstMax):
            thirdMax = secMax
            secMax = firstMax
            firstMax = currMax
            continue
        currMax = max(currObject[0], secMax)
        if (currMax > secMax):
            thirdMax = secMax
            secMax = currMax
            continue
        currMax = max(currObject[0], thirdMax)
        if (currMax > thirdMax):
            thirdMax = currMax

    return firstMax, secMax, thirdMax

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            current_pos = board[i][j]
            if current_pos == "0" or current_pos == "1":
                print("?", end=" ")
            else:
                print(current_pos, end=" ")
        print("")


def play():
    numberOfships =
    player1, player2 = get_name()
    #player1 = get_name("1")
    #player2 = get_name("2")
    level = input("Please choose board size: 1 - 6X6 | 2 - 8X8 | 3 - 10X10")
    board1 = random_board(level)
    board2 = random_board(level)
    player1Counter = 0
    player2Counter = 0
    current_player = 1
    while not player1Counter < numberOfships and not player2Counter < numberOfships:
        opponent_board = board2 if current_player == 1 else board1
        print_board(opponent_board)
        (row, column) = get_guess()
        current_pos = opponent_board[int(row)][int(column)]
        if current_pos == "0":
            opponent_board[int(row)][int(column)] = "M"
            print("HAHA you missed")
        elif current_pos == "1":
            opponent_board[int(row)][int(column)] = "H"
            if (current_player == 1):
                player1Counter += 1
            else:
                player2Counter += 1
            print("GOOD JOB")
        else:
            print("Invalid guess")

        current_player = 1 if current_player == 2 else 2

    winner = player1 if current_player == 2 else player2
    print("The winner is: " + winner)
    # Save in history

def get_player_index(players, name):
    for index, item in enumerate(players):
        if item['name'] == name:
            return index
    return -1

def get_name():
    player1 = input("Please enter player's 1 name: ")
    players = data['players']
    index1 = get_player_index(players,player1)
    if (index1 > -1):
        print("your scoreboard", players[index1]["games"])
    else:
        set_new_player(player1)
        print("welcome new player!")
    player2 = player1
    while player2 == player1:
        player2 = input("Please enter player's 2 name: ")
        if player2 == player1:
            print("please choose different name")

    index2 = get_player_index(players, player2)
    if (index2 > -1):
        print("your scoreboard", players[index2]["games"])
    else:
        set_new_player(player2)
        print("welcome new player!")

    return player1, player2


def set_new_player(playerName):
    player_item={"name": playerName, "games": [], "highest_score":0 }
    data['players'].append(player_item)
    update_historyfile_from_gamedata()


def get_guess():
    row = input("Please enter your guess row: ")
    if row not in "levelX2+4":
        print("That row is wrong! it should be number in your level range")

    column = input("Please enter your guess column: ")
    if column not in "levelX2+4":
        print("That column is wrong! please chose number in your level range")

    return int(row)-1, int(column)-1

# TODO: We need to create many boards and return board for specific level
def random_board(level):
    # 0 - Water
    # 1 - Ship
    # H - Hit
    # S - Sunk
    # M - Miss

    board6X6 = [
        ["0", "0", "0", "1", "0", "0"],
        ["1", "1", "0", "1", "0", "1"],
        ["0", "0", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "0", "1"]
    ]
    board6X6 = [
        ["1", "1", "0", "1", "0", "0"],
        ["1", "1", "0", "1", "0", "1"],
        ["0", "0", "0", "1", "0", "1"],
        ["1", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "0", "0", "1"]
    ]
    board8X8 = [
        ["0", "0", "0", "1", "0", "1", "0", "1"],
        ["1", "1", "0", "1", "0", "1", "0", "1"],
        ["0", "0", "0", "1", "0", "1", "0", "1"],
        ["1", "1", "1", "0", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "0", "0"],
        ["1", "1", "1", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "1", "1"]
    ]
    board8X8 = [
        ["0", "0", "0", "1", "0", "1", "0", "1"],
        ["1", "0", "0", "1", "0", "1", "0", "1"],
        ["1", "0", "0", "1", "0", "1", "0", "1"],
        ["0", "1", "1", "0", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0"],
        ["1", "1", "1", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0", "1", "1", "1"]
    ]
    board10X10 = [
        ["1", "1", "0", "1", "0", "1", "0", "0", "1", "1"],
        ["1", "1", "0", "1", "0", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["0", "0", "0", "0", "0", "1", "1", "0", "0", "1"],
        ["1", "1", "1", "1", "0", "0", "1", "0", "0", "1"],
        ["0", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "1", "0", "0"],
    ]
    board10X10 = [
        ["1", "1", "0", "1", "0", "1", "0", "0", "1", "1"],
        ["1", "0", "0", "1", "0", "1", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
        ["1", "1", "0", "0", "1", "1", "1", "0", "0", "1"],
        ["1", "1", "0", "0", "0", "0", "1", "0", "0", "1"],
        ["0", "0", "0", "0", "0", "0", "1", "0", "0", "0"],
        ["0", "0", "0", "1", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "1", "1", "0", "0", "1", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0", "1", "0", "0"],
    ]
    return


while True:
    set_gamedata_from_historyfile()
    print_menu()
    selection = input().upper()
    if selection == "H":
        high_scores()
    #elif selection == "N":
        #history()
    elif selection == "P":
        play()
    elif selection == "Q":
        break
    else:
        print("please press again")
1
quit()