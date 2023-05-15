def stat_poeme(poeme):
    ## poeme contient le path du fichier disponible dans Fichiers du navigateur

    myFile=open(poeme,"r")
    for i in myFile:
        print(i)
    myDict={}
    with open(poeme,"r") as po:
        listLigne= po.readlines()
        print("=========================================")
        for l in listLigne:
            ligneSansEspace=l.strip()
            print(ligneSansEspace)
            #index
            print(listLigne.index(l))
            #long
            print(f"length of a line {len(ligneSansEspace)}")
            #contenu
            print(f"CONTENU DE LA LIGNE :{ligneSansEspace}")


stat_poeme("./poeme.txt")
#stat_poeme("C:/Users/HP/Desktop/python-eferi/python-proj-eferi/poeme.txt")


