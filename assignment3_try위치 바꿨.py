import pickle

dbfilename = 'test3_4.dat'


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
                try: parse[1] = int(parse[1])##예
                except:
                    record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                    scdb += [record]
                else : print("'Name' is not number")
            except:
                continue

        elif parse[0] == 'find':
            findl = []
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        findl += [p]
                        sortKey = 'Name'
                        showScoreDB(findl, sortKey)
            except: continue

        elif parse[0] == 'del':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
            except:
                continue

        elif parse[0] == 'inc':
            try:
                for p in scdb:
                    if p['Name'] == parse[1]:
                        p['Score'] = str(int(p['Score']) + int(parse[3]))
            except: continue

        elif parse[0] == 'show':
            try:
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            except: continue

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