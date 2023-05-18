
# choice referance

#PAPER
#SCISSORS
#ROCK
#LIZARD
#SPOCK

PLAYER_INFO_FILE = 'players_infos.csv'
ROUND_0_FILE = 'round_0.csv'
MATCHES_FILE = 'matches.csv'


# player prompts

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



round_Number=0


while  (round_Number<3):
    print(f"round numer is : {round_Number}")
    player1=input("enter player 1 :")
    player2=input("enter player 2 :")
    if player1 in allowed_choices:

        # game logic 
        match player1:
            case "PAPER":
                
                if  player2 in allowed_choices_P2:
                    
                    if player2 in PAPERWinCombo:
                        print("player 1 wins ")
                    elif player2 in PAPERLoseCombo:
                        print("player2 wins")
                        #player1=input("enter player 1 :")
                    else:
                        print("Draw")
                        #player1=input("enter player 1 :")
                        #sort player alphabatecaly  and choose first on the list 

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    round_Number-=1
                    
                    
            case "SCISSORS":

                if  player2 in allowed_choices_P2:
                    
                    if player2 in SCISSORSWinCombo:
                        print("player 1 wins ")
                    elif player2 in SCISSORSLoseCombo:
                        print("player2 wins")
                    else:
                        print("Draw")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    round_Number-=1


            case "ROCK":

                if  player2 in allowed_choices_P2:
                    
                    if player2 in ROCKWinCombo:
                        print("player 1 wins ")
                    elif player2 in ROCKLoseCombo:
                        print("player2 wins")
                    else:
                        print("Draw")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    round_Number-=1
            case "LIZARD":

                if  player2 in allowed_choices_P2:
                    
                    if player2 in LIZARDWinCombo:
                        print("player 1 wins ")
                    elif player2 in LIZARDLoseCombo:
                        print("player2 wins")
                    else:
                        print("Draw")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    round_Number-=1

            case "SPOCK":

                if  player2 in allowed_choices_P2:
                    
                    if player2 in SPOCKdWinCombo:
                        print("player 1 wins ")
                    elif player2 in SPOCKdLoseCombo:
                        print("player2 wins")
                    else:
                        print("Draw")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    round_Number-=1


        round_Number+=1
        
    else:
        break
