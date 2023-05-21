def counter(fname):

    num_charc=0
    num_spaces=0
    num_words=0

    #fname contient le chemin vers le fichier
    with open(fname, 'r') as f:
        for _ in f.read():
            num_charc+=1
            if _ == " ":
                num_spaces+=1
    with open(fname, 'r') as f:
        lineList=f.readlines()   
        print(lineList) 
        num_lines=len(lineList)

        for i in lineList:
            if  i.startswith("\n"):
                print("pass")
            else:

            #print(len(i.strip().split(' ')))
                num_words+=len(i.strip().split(' '))
    return [num_words,num_lines, num_charc, num_spaces]

print(counter("./counter.txt"))
