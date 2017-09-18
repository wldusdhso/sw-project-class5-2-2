import pickle

dbfilename = 'assignment3.dat'


def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while (True):
        inputstr = (input("Score DB > "))
        if inputstr == " ": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                parse[1] = int(parse[1])
            except:
                record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                scdb += [record]
            else:
                print("'Name' is not number")

        elif parse[0] == 'find':
            findl = []
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        findl += [p]
                        sortKey = 'Name'
                        showScoreDB(findl, sortKey)
                    except:
                        continue
                            
        elif parse[0] == 'del':
            deldb = []
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        deldb += [p]
                    except:
                        continue
            for p in deldb:
                try:
                    scdb.remove(p)
                except:
                    continue

        elif parse[0] == 'inc':
            for p in scdb:
                if p['Name'] == parse[1]:
                    try:
                        p['Score'] = str(int(p['Score']) + int(parse[3]))
                    except:
                        continue

        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])




def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
