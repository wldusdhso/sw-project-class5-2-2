class Guess:

    def __init__(self, word):

        self.numTries = 0

        self.secretlist = list(word)
        self.answerlist = []
        self.guessedChars = []
        self.secretWord = ""
        self.currentStatus = ""

        for i in range(len(self.secretlist)):
            self.answerlist.append("_")

    def display(self):

        print("Used:", " ".join(self.guessedChars))
        print("Current:", "".join(self.answerlist))
        print("Tries:",self.numTries)

    def guess(self, character):

        self.guessedChars.append(character)
        for i in range(len(self.secretlist)):
            if self.secretlist[i] == character:

                self.answerlist[i] = self.secretlist[i]
        if not character in self.secretlist:
            self.numTries += 1
        self.currentStatus = "".join(self.answerlist)
        self.secretWord = "".join(self.secretlist)
        if "".join(self.answerlist) == "".join(self.secretlist):
            return True
        else:
            return False