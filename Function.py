def countwords():
    file=input("Which file name?")
    numwords=0
    f=open(file,"r")
    for line in f:
        words=line.split()
        numwords+=len(words)

    print(numwords)
countwords()    