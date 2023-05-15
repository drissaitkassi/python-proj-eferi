
# choice referance

#feuille
#sizeaux
#pierre
#lezard
#spock


# player prompts



# feuille combination
feuilleWinCombo=["pierre","spock"]
feuilleDraw="feuille"
feuilleLoseCombo=["sizeaux","lezard"]

# sizeaux combination
sizeauxWinCombo=["feuille","lezard"]
sizeauxDraw="sizeaux"
sizeauxLoseCombo=["spock","pierre"]

# pierre combination
pierreWinCombo=["sizeaux","lezard"]
pierreDraw="pierre"
pierreLoseCombo=["spock","feuille"]

# lezard combination
lezardWinCombo=["spock","feuille"]
lezardDraw="lezard"
lezardLoseCombo=["sizeaux","pierre"]

# spock combination
spockdWinCombo=["sizeaux","pierre"]
spockdDraw="spock"
spockdLoseCombo=["feuille","lezard"]

# check invalid prompts for P1
allowed_choices=["F","S","P","L","Sp"]

# check invalid prompts for P2
allowed_choices_P2=[
"feuille",
"sizeaux",
"pierre",
"lezard",
"spock"
]


round_Number=0


while  (round_Number<3):
    print(f"round numer is : {round_Number}")
    player1=input("enter player 1 :")
    player2=input("enter player 2 :")
    if player1 in allowed_choices:

        # game logic 
        match player1:
            case "F":
                
                if  player2 in allowed_choices_P2:
                    
                    if player2 in feuilleWinCombo:
                        print("player 1 wins ")
                    elif player2 in feuilleLoseCombo:
                        print("player2 wins")
                        #player1=input("enter player 1 :")
                    else:
                        print("Draw")
                        #player1=input("enter player 1 :")

                else:
                    print("player 2 entered an unvalid choice")
                    #round number will increment so i need to decrement it since the player
                    #entered an invalid input 
                    round_Number-=1
        #player1=input("enter player 1 :")
                    
                    
        #     case "S":
        #         if player2 in sizeauxWinCombo:
        #             print("player 1 wins ")
        #         elif player2 in sizeauxLoseCombo:
        #             print("player2 wins")
        #         else:
        #             print("Draw")
        #     case "P":
        #         if player2 in pierreWinCombo:
        #             print("player 1 wins ")
        #         elif player2 in pierreLoseCombo:
        #             print("player2 wins")
        #         else:
        #             print("Draw")
        #     case "L":
        #         if player2 in lezardWinCombo:
        #             print("player 1 wins ")
        #         elif player2 in lezardLoseCombo:
        #             print("player2 wins")
        #         else:
        #             print("Draw")
        #     case "Sp":
        #         if player2 in spockdWinCombo:
        #             print("player 1 wins ")
        #         elif player2 in spockdLoseCombo:
        #             print("player2 wins")
        #         else:
        #             print("Draw")
        round_Number+=1
        
    else:
        break
    