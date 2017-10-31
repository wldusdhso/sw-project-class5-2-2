import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()
        
        
    def initUI(self):
        self.strDb = ""
        #label
        nameL = QLabel('Name:')
        ageL = QLabel('Age:')
        scoreL = QLabel('Score:')
        amountL = QLabel('Amount:')
        keyL = QLabel('Key:')
        resultL = QLabel('Result:')

        #edit
        self.nameE = QLineEdit(self)
        self.ageE = QLineEdit(self)
        self.scoreE = QLineEdit(self)
        self.amountE = QLineEdit(self)

        #button
        addButton = QPushButton("Add")
        delButton = QPushButton("Del")
        findButton = QPushButton("Find")
        incButton = QPushButton("Inc")
        showButton = QPushButton("show")

        #combobox
        self.keyCombo = QComboBox(self)
        self.keyCombo.addItem("Name")
        self.keyCombo.addItem("Age")
        self.keyCombo.addItem("Score")

        #textedit
        self.resultText = QTextEdit(self)

        #hbox1
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(nameL)
        hbox_1.addWidget(self.nameE)
        hbox_1.addWidget(ageL)
        hbox_1.addWidget(self.ageE)
        hbox_1.addWidget(scoreL)
        hbox_1.addWidget(self.scoreE)

        #hbox2
        hbox_2 = QHBoxLayout()
        hbox_2.addStretch(1)
        hbox_2.addWidget(amountL)
        hbox_2.addWidget(self.amountE)
        hbox_2.addWidget(keyL)
        hbox_2.addWidget(self.keyCombo)

        #hbox3
        hbox_3 = QHBoxLayout()
        hbox_3.addStretch(1)
        hbox_3.addWidget(addButton)
        hbox_3.addWidget(delButton)
        hbox_3.addWidget(findButton)
        hbox_3.addWidget(incButton)
        hbox_3.addWidget(showButton)

        #vbox
        vbox = QVBoxLayout()
        vbox.addLayout(hbox_1)
        vbox.addLayout(hbox_2)
        vbox.addLayout(hbox_3)
        vbox.addWidget(resultL)
        vbox.addWidget(self.resultText)
        

        #do
        findButton.clicked.connect(self.findDB)
        addButton.clicked.connect(self.addDB)
        delButton.clicked.connect(self.delDB)
        incButton.clicked.connect(self.incDB)
        showButton.clicked.connect(self.showDB)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()
    #show the data into person db
    def showScoreDB(self):
        for p in self.scoredb:
            for attr in p:
                self.strDb += attr +" "+ str(p[attr])+"\t"
            self.strDb += "\n"
        self.resultText.setText(self.strDb)
        self.strDb = ""
    #findButton function
    def findDB(self):
        findstr = ""
        for p in self.scoredb:
            findName = self.nameE.text()
            if p['Name']== findName:
                for attr in p:
                    findstr += attr + " " + str(p[attr]) + "\t"
                findstr += "\n"
        self.resultText.setText(findstr)
    #addButton function
    def addDB(self):
        addName = self.nameE.text()
        addAge = int(self.ageE.text())
        addScore = int(self.scoreE.text())
        record = {'Name':addName,'Age':addAge,'Score':addScore}
        self.scoredb += [record]
        self.showScoreDB()
    #deleteButton function
    def delDB(self):
        delList = []
        for p in self.scoredb:
            delName = self.nameE.text()
            if p['Name']==delName:
                delList += [p]
        for p in delList:
            self.scoredb.remove(p)
        self.showScoreDB()
    #increaseButton function
    def incDB(self):
        incName = self.nameE.text()
        incScore = self.amountE.text()
        for p in self.scoredb:
            if p['Name']==incName:
                p['Score'] = int(p['Score'])+ int(incScore)
        self.showScoreDB()
    #showButton function
    def showDB(self):
        currentbox = self.keyCombo.currentText()
        for p in sorted(self.scoredb, key=lambda person: person[currentbox]):
            for attr in sorted(p):
                self.strDb += attr + " " + str(p[attr]) + "\t"
            self.strDb += "\n"
        self.resultText.setText(self.strDb)
        self.strDb = ""





        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





