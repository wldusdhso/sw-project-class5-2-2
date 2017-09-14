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
        try:#예외처리
            inputstr = (input("Score DB > "))
            if inputstr == "": continue
            parse = inputstr.split(" ")
            if parse[0] == 'add':
                parse[2] = int(parse[2])
                parse[3] = int(parse[3])
                try: parse[1] = int(parse[1])##예
                except:
                    record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                    scdb += [record]
                else : print("'Name' is not number")
            elif parse[0] == 'del':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        scdb-= p
            elif parse[0] == 'show':
                sortKey = 'Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
            elif parse[0] == 'find':
                for t in scdb:
                    if t['Name'] == parse[1] :
                        for attr in t : print(attr, "=", t[attr], end=' ')
                        print()
            elif parse[0] == 'inc' :
                for a in scdb :
                    if a['Name'] == parse[1]:
                        a['Score'] += int(parse[2])
            elif parse[0] == 'quit':
                break
        except: print("Invalid command: " + parse[0])


def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr, "=", p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
