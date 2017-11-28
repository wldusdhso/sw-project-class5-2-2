class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.numTries = 0
        self.guessedChars = []
        self.currentStatus = '_'*len(self.secretWord)
        self.currentword = '_'*len(self.secretWord)
        self.indexnumL =[]

    def display(self):
        return 'Current: '+ self.currentStatus+'\n'+'Tries: '+ str(self.numTries)


    def guess(self, character):
        self.guessedChars += [character]
        character = character.lower()
        if self.secretWord == self.currentStatus:
            return True
        elif character in self.secretWord:
            indexnum = 0
            self.indexnumL = []
            while self.secretWord.find(character,indexnum)!=-1:
                indexnum = self.secretWord.find(character,indexnum)
                self.indexnumL += [indexnum]
                indexnum += 1
            for i in self.indexnumL:
                if i == len(self.currentword)-1:
                    self.currentword = self.currentword[:-1]+character
                else:
                    self.currentword = self.currentword[:i]+character+self.currentword[i+1:]
            self.currentStatus = self.currentword
            return False
        elif self.secretWord.find(character) ==-1:
            self.numTries += 1
            return False







