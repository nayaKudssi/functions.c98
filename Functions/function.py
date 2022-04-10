def countwords():
    filename=input("Enter the file name: ")
    now=0
    file=open(filename,'r')
    for line in file:
        words=line.split()
        now=now+len(words)
    print("number of words are ")
    print(now)
countwords()