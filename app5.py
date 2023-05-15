# def stat_poeme(poeme):

#     ## poeme contient le path du fichier disponible dans Fichiers du navigateur
#     myDict={'ind' : "", 'long': "", 'txt':""}
    
#     with open(poeme,"r") as po:
#         listLigne= po.readlines()
#         lengthList=[]
#         #print("=========================================")
#         for l in listLigne:
#             ligneSansEspace=l.strip()
#             lengthList.append(len(ligneSansEspace))
#             # #index
#             # print(listLigne.index(l))
#             #long
#             #print(f"length of a line {len(ligneSansEspace)}")
#             # #contenu
#             # print(f"CONTENU DE LA LIGNE :{ligneSansEspace}")
#         maxLenght=max(lengthList)
#         for l in listLigne:
#             if len(l.strip()) == maxLenght :
#                 myDict["ind"]=listLigne.index(l)
#                 myDict["long"]=maxLenght
#                 myDict["txt"]=l.strip()
#                 #print(listLigne.index(l))
#                 #print(f"CONTENU DE LA LIGNE :{ligneSansEspace}")
#     print(myDict)
#     return myDict

# stat_poeme("./poeme.txt")
# #stat_poeme("C:/Users/HP/Desktop/python-eferi/python-proj-eferi/poeme.txt")

def stat_poeme(poeme):
    myDict={'ind' : "", 'long': "", 'txt':""}
    with open(poeme,"r") as po:
        listLigne= po.readlines()
        lengthList=[]
        for l in listLigne:
            ligneSansEspace=l.strip()
            lengthList.append(len(ligneSansEspace))
        maxLenght=max(lengthList)
        for l in listLigne:
            if len(l.strip()) == maxLenght :
                myDict["ind"]=listLigne.index(l)
                myDict["long"]=maxLenght
                myDict["txt"]=l.strip()
    return myDict

stat_poeme("./poeme.txt")
#stat_poeme("C:/Users/HP/Desktop/python-eferi/python-proj-eferi/poeme.txt")
