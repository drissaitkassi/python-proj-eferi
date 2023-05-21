def prix_moyen_du_gaz(fichier):
    listPrixGazUs=[]
    listPrixGazBelgique=[]

    with open(fichier,"r") as f:
        #print(f.readlines()[1::])
        for i in f.readlines()[1::]:
            listPrixGazBelgique.append(float(i.split("\t")[0]))
            listPrixGazUs.append(float(i.split("\t")[1]))
    avgUs=sum(listPrixGazUs)/len(listPrixGazUs)
    avgBel=sum(listPrixGazBelgique)/len(listPrixGazBelgique)
    #print(listPrixGazBelgique)
    return {'belgium': avgBel, 'usa': avgUs}

print(prix_moyen_du_gaz("./moyenne.txt"))