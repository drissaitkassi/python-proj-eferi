import csv

# with open("round_0.csv",newline="") as rounds:
#     csv_reader=csv.DictReader(rounds,delimiter=",")
#     for row in csv_reader:
#         #print(row)
#         print(f"{row['Player 1']} vs {row['Player 2']}")


# with open("players_infos.csv",newline="") as players:
#     csv_reader=csv.DictReader(players,delimiter=",")
#     next(csv_reader)
#     for row in csv_reader:
#         #print(row)
#         # print(f' player name : {row[0]} round: {row[1]} sign played {row[2]} ')
#         if row['Name']=="Jack" and row['Round']=='0':
#             print(row['Sign'])

# def getMaxRound(filename):
#     roundList=[]
#     with open(filename,newline="") as players:
#         csv_reader=csv.DictReader(players,delimiter=",")
#         next(csv_reader)
#         for row in csv_reader:
#             roundList.append(row['Round'])
#             #print(row['Round'])
#     return max(roundList)
# print(getMaxRound("./test1/players_infos.csv"))



#print(max(testList))

myDict={'Round':'rozezeznds',
        'Winner':'winnezezer',
        'Player 1 name':'pezeze1',
        'Player 1 sign':'my ass' ,
        'Player 2 name':'punk',
        'Player 2 sign':'your punck ass'}
head=['Round','Winner','Player 1 name','Player 1 sign','Player 2 name','Player 2 sign']

# class HandleFiles:
    
#     def __init__(self) -> None:
#         pass
       
#     def createMatchFile(header):
#         with open(header,"a",newline='') as matche:
#             writer=csv.DictWriter(matches,fieldnames=head)
#             writer.writeheader()

#     def recordmatched(matchDict):
#         with open(matchDict,"a",newline='') as matche:
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

# print(zip(('Henry', 'Jack'),('Paul', 'John')))
 
# testTupleList=[]
# winnerLIST=['ab','cd','ef','gh']

# for i in range(len(testTupleList)):
#     print(i+1)
# index=0
# for index in range(len(winnerLIST)-1):
#     testTupleList.append((winnerLIST[index],winnerLIST[index+1]))
#     index=index+1
# print(testTupleList)

# it=iter(winnerLIST)
# print([*zip(it, it)])


'''======== test converting winner list into list of tuples for every 2 elemnts 
& initializing it to empty list ======================'''

# print("======= winner list full=======")
# print(winnerList)
# it=iter(winnerList)
# print("======= winner list converted to list of tuples=======")
# winnerTupleList=[*zip(it, it)]
# print(winnerTupleList)
# winnerList=[]
# print("======= winner list initilized =======")
# print(winnerList)


# if roundNumber == 0:
#     ''' get names from file '''
#     pass
# else :
#     ''' get names from winner list'''
#     ''' we should check if winner list is > 1'''
#     if len(winnerList) >1 :
#         '''convert winner list to name tuples '''
#         ''' run dual and initialize winner list to []'''
#         pass 
#     else :
#         pass
#     pass
def createMatchFile(fileName,headers):
    with open(fileName,"a",newline='') as matche:
        writer=csv.DictWriter(matche,fieldnames=headers)
        writer.writeheader()

#createMatchFile('match.csv')

def recordmatched(fileName,matchDict,headers):
    with open(fileName,"a",newline='') as matche:
        writer=csv.DictWriter(matche,fieldnames=headers)
        writer.writerow(matchDict)
recordmatched('match.csv',myDict,head)