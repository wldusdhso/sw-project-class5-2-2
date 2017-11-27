class Guess:

    def __init__(self, word):
        #단어를 인자로 받아, 기록해둠
        self.secretWord = word
        #추측한 글자들의 집합 초기화
        self.guessedChars = []
        #실패한 추측의 회수 기록
        self.numTries = 0
        #지금까지 알아낸 글자
        self.currentStatus = []
        for i in range(len(word)):
            self.currentStatus.append('_')
        #그위치를 가리키는 데이터
        self.where = 0

    def display(self):
        print("Current: ", ''.join(self.currentStatus))
        print("Tries: ", self.numTries)


    def guess(self, character):
        #추측한 글자를 집합에 추가
        self.guessedChars.append(character)
        #추측 실패했을 때 실패횟수 늘리기
        if character not in self.secretWord:
            self.numTries+=1
        #currentstatus와 where 갱신
        else:
            self.where = 0
            while self.where<len(self.secretWord):
                if self.secretWord[self.where] == character:
                    self.currentStatus[self.where]= character
                self.where+=1
        #True와 False 반환
        if '_' not in self.currentStatus:
            return True
        else: return False
