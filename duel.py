# PAPER combination
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



def dual(round,pl1Name,pl1Sign,pl2Name,pl2Sign):
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
                        print("player 1 wins ")
                    elif pl2Sign in ROCKLoseCombo:
                        print("pl2Sign wins")
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
                        print("player 1 wins ")
                    elif pl2Sign in LIZARDLoseCombo:
                        print("pl2Sign wins")
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
                        print("player 1 wins ")
                    elif pl2Sign in SPOCKdLoseCombo:
                        print("pl2Sign wins")
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
    
    print(matchDict)
    return matchDict


dual('1','John','PAPER','Paul','PAPER')