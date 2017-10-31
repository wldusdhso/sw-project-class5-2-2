import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QLabel,
                             QComboBox, QTextEdit, QLineEdit, QGridLayout)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.keyname = 'Name'
        self.name = ""
        self.score = ""
        self.age = ""
        self.amount = ""
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        # 첫번째 줄 UI 작성 후 첫번째 레이아웃으로 등록
        name = QLabel("Name:", self)
        self.nameLineBox = QLineEdit()
        age = QLabel("Age:", self)
        self.ageLineBox = QLineEdit()
        score = QLabel("Score:", self)
        self.scoreLineBox = QLineEdit()

        pBox1 = QHBoxLayout()
        pBox1.addWidget(name)
        pBox1.addWidget(self.nameLineBox)
        pBox1.addWidget(age)
        pBox1.addWidget(self.ageLineBox)
        pBox1.addWidget(score)
        pBox1.addWidget(self.scoreLineBox)

        # 두번째 줄 UI 작성 후 두번째 레이아웃으로 등록
        space1 = QLabel("               ", self)
        amount = QLabel("Amount: ", self)
        self.amountLineBox = QLineEdit()
        key = QLabel("key:")
        self.keyComboBox = QComboBox()
        self.keyComboBox.addItem("Name")
        self.keyComboBox.addItem("Score")
        self.keyComboBox.addItem("Age")

        pBox2 = QHBoxLayout()
        pBox2.addWidget(space1)
        pBox2.addWidget(amount)
        pBox2.addWidget(self.amountLineBox)
        pBox2.addWidget(key)
        pBox2.addWidget(self.keyComboBox)

        # 세번째 줄 UI 작성 후 세번째 레이아웃으로 등록
        space2 = QLabel('                  ', self)
        addButton = QPushButton("Add", self)
        delButton = QPushButton("Del", self)
        findButton = QPushButton("Find", self)
        incButton = QPushButton("Inc", self)
        showButton = QPushButton("Show", self)

        addButton.clicked.connect(self.AddBtnClicked)
        delButton.clicked.connect(self.DelBtnClicked)
        findButton.clicked.connect(self.FindBtnClicked)
        incButton.clicked.connect(self.IncBtnClicked)
        showButton.clicked.connect(self.ShowBtnClicked)

        pBox3 = QHBoxLayout()
        pBox3.addWidget(space2)
        pBox3.addWidget(addButton)
        pBox3.addWidget(delButton)
        pBox3.addWidget(findButton)
        pBox3.addWidget(incButton)
        pBox3.addWidget(showButton)

        # 네번째 줄 UI 작성 후 네번째 레이아웃으로 등록
        result = QLabel("Result: ")

        pBox4 = QHBoxLayout()
        pBox4.addWidget(result)

        # 다섯번째 줄 UI 작성 후 다섯번째 레이아웃으로 등록
        self.textBox = QTextEdit(self)

        pBox5 = QHBoxLayout()
        pBox5.addWidget(self.textBox)

        # 수평 정렬 레이아웃을 수직으로 순서대로 배치
        qBox = QVBoxLayout()
        qBox.addLayout(pBox1)
        qBox.addLayout(pBox2)
        qBox.addLayout(pBox3)
        qBox.addLayout(pBox4)
        qBox.addLayout(pBox5)
        self.setLayout(qBox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('DataBaseManager')



    def closeEvent(self, event):
        self.writeScoreDB()

    def keydetector(self, text):
        self.keyname = text

    def setAge(self, text):
        self.age = text

    def setName(self, text):
        self.name = text

    def setScore(self, text):
        self.score = text

    def setAmount(self, text):
        self.amount = text

    def operateAdd(self):
        name = self.name
        age = self.age
        score = self.score
        record = {'Name': name, 'Age': age, 'Score': score}
        self.scoredb += [record]
        self.showScoreDB()

    def operateDele(self):
        idx = 0
        name = self.name
        while idx < len(self.scoredb):
            if self.scoredb[idx]['Name'] == name:
                self.scoredb.remove(self.scoredb[idx])
            else:
                idx += 1
        self.showScoreDB()

    def operateFind(self):
        string = ''
        name = self.name
        for d in self.scoredb:
            if d['Name'] == name:
                string += 'Name :  ' + d['Name'] + ",  " + "Age :  " + str(d["Age"]) + ',  ' + "Score :  " + str(
                    d["Score"])
                string += '\n'
        self.resultEdit.setText(string)

    def operateInc(self):
        name = self.name
        amount = self.amount
        idx = 0
        while idx < len(self.scoredb):
            if self.scoredb[idx]['Name'] == name:
                self.scoredb[idx]['Score'] += int(amount)
                idx += 1
            else:
                idx += 1
        self.showScoreDB()





    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            print("New DB: ", self.dbfilename)
            return []

        self.scdb = []
        try:
            self.scdb = pickle.load(fH)
        except:
            print("Empty DB: ", self.dbfilename)
        else:
            print("Open DB: ", self.dbfilename)
        fH.close()
        return scdb

    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scdb, fH)
        fH.close()

    def showScoreDB(self, keyname="Score"):
        temp = ""
        for p in sorted(self.scoredb, key=lambda person: person[keyname]):
            for attr in sorted(p):
                temp += attr + "=" + str(p[attr]) + " "

            temp += "\n"
        self.textBox.setText(temp)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())
