class Guess:

    def __init__(self, word):
        self.secretWord = word #비밀로 선택된 단어를 인자로 받아 기록 #랜덤으로 받은 비밀단어
        self.guessedChars = [] #추측에 이용된 글자들의 집합을 빈 집합으로 초기화
        self.numTries = 0 #실패한 추측의 회수를 기록하기 위한 변수를 0으로 초기화
        self.currentStatus = "_" * len(self.secretWord) #실행시켰을때 단어가 표시될 곳을 "_"로 초기화



    def display(self):
        print("Current : " + self.currentStatus) #실행시켰을때 맞춘 단어 표시
        print("Tries : ", self.numTries) #실행시켰을때 실패한 횟수를 표시


    def guess(self, character):
        self.guessedChars.append(character) #입력한 단어를 guessedChars에 추가
        if self.secretWord.find(character) > -1: #입력한 단어를 secretWord에서 찾는다
            for i in range (len(self.secretWord)): #secretWord의 길이만큼 for문
                if self.secretWord[i] == character: #입력한 단어가 secretWord에 있으면
                    success = self.currentStatus[:i] + character + self.currentStatus[i:] #Current에 단어를 입력
                    self.currentStatus = success

                    if success == self.secretWord: #내가 입력한 단어와 secretWord가 일치하면 True, 아니면 False
                        return True
                    else:
                        return False

        else:
            self.numTries = self.numTries + 1 #만약 입력한 단어가 틀렸으면 numTries에 1을 추가
