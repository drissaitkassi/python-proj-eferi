def count_words(fname):
    with open(fname,'r') as file:
        text = file.read()
        thisCount = text.count('this')
    theseCount = text.count('these')
    return thisCount+theseCount