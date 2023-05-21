import csv
# PAPER combination
#todo change the file path by removing the ./test/

PLAYER_INFO_FILE = './test8/players_infos.csv'
ROUND_0_FILE = './test8/round_0.csv'
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
roundNumber=0

''' winner list must be converted to tuples of oppenants using *zip and iter()'''
winnerList=[]

''' Headers for match file'''
head=['Round','Winner','Player 1 name','Player 1 sign','Player 2 name','Player 2 sign']


def createMatchFile(fileName,headers):
    with open(fileName,"a",newline='') as matche:
        writer=csv.DictWriter(matche,fieldnames=headers)
        writer.writeheader()

def recordmatched(fileName,matchDict,headers):
    with open(fileName,"a",newline='') as matche:
        writer=csv.DictWriter(matche,fieldnames=headers)
        writer.writerow(matchDict)

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
                        winnerList.append(winner)
                    elif pl2Sign in PAPERLoseCombo:
                        winner=pl2Name
                        winnerList.append(winner)
                    else:
                        #sort player alphabatecaly  and choose first on the list 
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        winnerList.append(winner)

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    
                    
            case "SCISSORS":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in SCISSORSWinCombo:
                        winner=pl1Name
                        winnerList.append(winner)
                        
                    elif pl2Sign in SCISSORSLoseCombo:
                        winner=pl2Name
                        winnerList.append(winner)

                   
                    else:
                       
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        winnerList.append(winner)

                else:
                    print("player 2 entered an unvalid choice")


            case "ROCK":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in ROCKWinCombo:
                        winner=pl1Name
                        winnerList.append(winner)

                    elif pl2Sign in ROCKLoseCombo:
                        winner=pl2Name
                        winnerList.append(winner)
                    else:
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        winnerList.append(winner)

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
            case "LIZARD":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in LIZARDWinCombo:
                        winner=pl1Name
                        winnerList.append(winner)
                    elif pl2Sign in LIZARDLoseCombo:
                        winner=pl2Name
                        winnerList.append(winner)
                    else:
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        winnerList.append(winner)
                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 

            case "SPOCK":

                if  pl2Sign in allowed_choices_P2:
                    
                    if pl2Sign in SPOCKdWinCombo:
                        winner=pl1Name
                        winnerList.append(winner)

                    elif pl2Sign in SPOCKdLoseCombo:
                        winner=pl2Name
                        winnerList.append(winner)

                    else:
                        sortedListOfPlayer=sorted([pl1Name,pl2Name])
                        winner=sortedListOfPlayer[0]
                        winnerList.append(winner)


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
    
    #todo record matchs in matches.csv
    recordmatched(MATCHES_FILE,matchDict,head)
    return matchDict


'''=============== return a list of tuples each tuple contains the "names"
for a single dual on round zero ==============='''

def round_0():
    playersInDuals=[]
    with open(ROUND_0_FILE,newline="") as rounds:
        csv_reader=csv.DictReader(rounds,delimiter=",")
        for row in csv_reader:
            playersInDuals.append((row['Player 1'],row['Player 2']))
    return playersInDuals

def getMaxRound(filename):
    roundList=[]
    with open(filename,newline="") as players:
        csv_reader=csv.DictReader(players,delimiter=",")
        next(csv_reader)
        for row in csv_reader:
            roundList.append(row['Round'])
    return max(roundList)


'''========== return a list of 2 tuples   containing  [(p1Name,p1Sign),(p2Name,p2Sign)]
which represent a "dual" =========='''

def playersSign(playerNameTuple,roundNumn):
    playerSing=[]
    for name in playerNameTuple:
        with open(PLAYER_INFO_FILE,newline="") as players:
            csv_reader=csv.DictReader(players,delimiter=",")
            for row in csv_reader:
                if row['Name']==name and row['Round']==roundNumn:
                    playerSing.append((row['Name'],row['Sign']))

    return playerSing

''' =========== create list of duals by appending each dualinfo to the list ========
we need a dual list to know how many time we should run the dual function as well as to gather 
all duals in one place ========== '''




MAX_ROUNDS=getMaxRound("./test1/players_infos.csv")
createMatchFile(MATCHES_FILE,head)
while(roundNumber != MAX_ROUNDS):
        

    if roundNumber == 0:
        ''' get names from file '''
        listOfDuals=[]
        for nameTuple in round_0(): #from file 
            listOfDuals.append(playersSign(nameTuple,str(roundNumber)))
        for mydual in listOfDuals:
            dual(str(roundNumber),mydual)
        roundNumber+=1
    else :

        if len(winnerList) > 1:
            listOfDuals=[]
            it=iter(winnerList)
            winnerTupleList=[*zip(it, it)]
            for nameTuple in winnerTupleList: #from winner list
                listOfDuals.append(playersSign(nameTuple,str(roundNumber)))
            winnerList=[]
            for mydual in listOfDuals:
                dual(str(roundNumber),mydual)
            listOfDuals=[]
            roundNumber+=1

        else :
  
            print(f'TOURNAMENT WINNER : {winnerList[0]}')
            break

        