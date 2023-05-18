import csv

# with open("round_0.csv",newline="") as rounds:
#     csv_reader=csv.reader(rounds,delimiter=",")
#     next(csv_reader)
#     for row in csv_reader:
#         print(f'{row[0]} vs {row[1]}')


# with open("players_infos.csv",newline="") as players:
#     csv_reader=csv.DictReader(players,delimiter=",")
#     next(csv_reader)
#     for row in csv_reader:
#         #print(row)
#         # print(f' player name : {row[0]} round: {row[1]} sign played {row[2]} ')
#         if row['Name']=="Jack" and row['Round']=='2':
#             print(row['Sign'])

# myDict={'Round':'rozezeznds','Winner':'winnezezer','Player 1 name':'pezeze1','Player 1 sign':'p1Sign','Player 2 name':'p2','Player 2 sign':'p2Sign' }
# head=['round','winner','player 1 name','player 1 sign','player 2 name','player 2 sign']

# class HandleFiles:
    
#     def __init__(self) -> None:
#         pass
       
#     def createMatchFile(header):
#         with open(header,"a",newline='') as matches:
#             writer=csv.DictWriter(matches,fieldnames=head)
#             writer.writeheader()

#     def recordmatched(matchDict):
#         with open(matchDict,"a",newline='') as matches:
#             writer=csv.DictWriter(matches,fieldnames=head)
#             writer.writerow(myDict)
            
#     def readPlayers(playersFile):
#         with open(playersFile,newline="") as players:
#             csv_reader=csv.reader(players,delimiter=",")
#             next(csv_reader)
#             for row in csv_reader:
#                 print(f' player name : {row[0]} round: {row[1]} sign played {row[2]} ')
#     def readRounds(roundFile):
#         with open(roundFile,newline="") as rounds:
#             csv_reader=csv.reader(rounds,delimiter=",")
#             next(csv_reader)
#             for row in csv_reader:
#                 print(f'{row[0]} vs {row[1]}')         


# createMatchFile(header=head)
# recordmatched(myDict)


print(sorted(['paul','john','aze']))