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

roundNumber=0

winnerList=[]

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

# playersSignList=[]
# for nameTuple in list_of_players:
#     playersSignList.append(playersSign(nameTuple,'1'))
#print(playersSignList)  
# print(playersSign([('Henry', 'Jack')],'1'))

listOfDuals=[[('Henry', 'SPOCK'), ('Jack', 'PAPER')], [('Paul', 'ROCK'), ('John', 'LIZARD')]]

# adual=[('Henry', 'SPOCK'), ('Jack', 'PAPER')]
# dual('1',adual)

for mydual in listOfDuals:
    dual(1,mydual)





# print(playersSignList)
# if roundNumber==0:
#     dualTuples=round_0()
#     playersSign()
# print(round_0())


# for i in range(len(round_0())):
#     dual()

