import csv
# PAPER combination

PLAYER_INFO_FILE = 'players_infos.csv'
ROUND_0_FILE = 'round_0.csv'
MATCHES_FILE = 'matches.csv'

PAPERWinCombo=["ROCK","SPOCK"]
PAPERDraw="PAPER"
PAPERLoseCombo=["SCISSORS","LIZARD"]

# SCISSORS combination
SCISSORSWinCombo=["PAPER","LIZARD"]
SCISSORSDraw="SCISSORS"
SCISSORSLoseCombo=["SPOCK","ROCK"]

# ROCK combination
ROCKWinCombo=["SCISSORS","LIZARD"]
ROCKDraw="ROCK"
ROCKLoseCombo=["SPOCK","PAPER"]

# LIZARD combination
LIZARDWinCombo=["SPOCK","PAPER"]
LIZARDDraw="LIZARD"
LIZARDLoseCombo=["SCISSORS","ROCK"]

# SPOCK combination
SPOCKdWinCombo=["SCISSORS","ROCK"]
SPOCKdDraw="SPOCK"
SPOCKdLoseCombo=["PAPER","LIZARD"]

# check invalid prompts for P1
allowed_choices=[
"PAPER",
"SCISSORS",
"ROCK",
"LIZARD",
"SPOCK"
]

# check invalid prompts for P2
allowed_choices_P2=[
"PAPER",
"SCISSORS",
"ROCK",
"LIZARD",
"SPOCK"
]

''' should be converted to str before passing it '''
roundNumber=1

''' winner list must be converted to tuples of oppenants using *zip and iter()'''
winnerList=[]

'''============ contains the actual logic of the dual
this function:
1) writes to match.csv 
2) append winners to winner list ========='''

def dual(round,dualInfos):
    pl1Name=dualInfos[0][0]
    pl1Sign=dualInfos[0][1]
    pl2Name=dualInfos[1][0]
    pl2Sign=dualInfos[1][1]
    winner=''
    if pl1Sign in allowed_choices:

    # game logic 
        match pl1Sign:
            case "PAPER":
                
                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in PAPERWinCombo:
                        winner=pl1Name
                        print(f" {pl1Name} wins ")
                    elif pl2Sign in PAPERLoseCombo:
                        winner=pl2Name
                        print(f" {pl2Name} wins ")
                        #pl1Sign=input("enter player 1 :")
                    else:
                        print("Draw")
                        #pl1Sign=input("enter player 1 :")
                        #sort player alphabatecaly  and choose first on the list 
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        print(f" {sortedListOfPlayer[0]} wins ")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    
                    
            case "SCISSORS":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in SCISSORSWinCombo:
                        winner=pl1Name
                        print(f" player 1 wins ")
                    elif pl2Sign in SCISSORSLoseCombo:
                        winner=pl2Name
                        print(f" player 2 wins ")
                    else:
                        print("Draw")
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        print(f" {sortedListOfPlayer[0]} wins ")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 


            case "ROCK":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in ROCKWinCombo:
                        winner=pl1Name
                        print(f" {pl1Name} wins ")
                    elif pl2Sign in ROCKLoseCombo:
                        winner=pl2Name
                        print(f" {pl2Name} wins ")
                    else:
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        print(f" {sortedListOfPlayer[0]} wins ")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
            case "LIZARD":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in LIZARDWinCombo:
                        winner=pl1Name
                        print(f" {pl1Name} wins ")
                    elif pl2Sign in LIZARDLoseCombo:
                        winner=pl2Name
                        print(f" {pl2Name} wins ")
                    else:
                        print('draw')
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        print(f" {sortedListOfPlayer[0]} wins ")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 

            case "SPOCK":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in SPOCKdWinCombo:
                        winner=pl1Name
                        print(f" {pl1Name} wins ")
                    elif pl2Sign in SPOCKdLoseCombo:
                        winner=pl2Name
                        print(f" {pl2Name} wins ")
                    else:
                        print("Draw")
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        print(f" {sortedListOfPlayer[0]} wins ")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
 
    matchDict={'Round':round,'Winner':winner,
               'Player 1 name':pl1Name,
               'Player 1 sign':pl1Sign,
               'Player 2 name':pl2Name,
               'Player 2 sign':pl2Sign
                 }
    
    #record matchs in matches.csv
    print(matchDict)
    return matchDict


'''=============== return a list of tuples each tuple contains the names for single dual ==============='''

def round_0():
    playersInDuals=[]
    with open("round_0.csv",newline="") as rounds:
        csv_reader=csv.DictReader(rounds,delimiter=",")
        for row in csv_reader:
            #print(row)
            playersInDuals.append((row['Player 1'],row['Player 2']))
            #dual('0',row['Player 1'],'SCISSORS',row['Player 2'],'SPOCK')
    return playersInDuals


def afterRound():
    pass

list_of_players=[('Henry', 'Jack'), ('Paul', 'John')]


'''========== return a list of 2 tuples   containing  [(p1Name,p1Sign),(p2Name,p2Sign)]
which represent a "dual" =========='''

def playersSign(playerNameTuple,roundNumn):
    playerSing=[]
    for name in playerNameTuple:
        with open("players_infos.csv",newline="") as players:
            csv_reader=csv.DictReader(players,delimiter=",")
            next(csv_reader)
            for row in csv_reader:
                if row['Name']==name and row['Round']==roundNumn:
                    #print(row['Sign'])
                    playerSing.append((row['Name'],row['Sign']))

    return playerSing

''' =========== create list of duals by appending each dualinfo to the list ========
we need a dual list to know how many time we should run the dual function as well as to gather 
all duals in one place ========== '''


playersSignList=[]
for nameTuple in list_of_players:
    playersSignList.append(playersSign(nameTuple,str(roundNumber)))
#print(playersSignList) 


'''========test dual function with a list of duals ======='''

# listOfDuals=[[('Henry', 'SPOCK'), ('Jack', 'PAPER')], [('Paul', 'ROCK'), ('John', 'LIZARD')]]
# for mydual in listOfDuals:
#     dual(str(roundNumber),mydual)





