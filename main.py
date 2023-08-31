####################################################################################################
################简易动物识别系统 By阮炜霖 2020101603#################################################
####################################################################################################
import sys
from PyQt5.QtCore import QStringListModel
from PyQt5 import QtCore, QtGui, QtWidgets
'''
import mysqldb
# 打开数据库连接
db = MySQLdb.connect("localhost", "testuser", "test123", "TESTDB", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# SQL 查询语句
sql = "SELECT * FROM know \
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      P = row[0]
      Q = row[1]
      # 打印结果
      print "P=%s,Q=%s" % \
             (P, Q )
except:
   print "Error: unable to fetch data"

# 关闭数据库连接
db.close()
'''

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("动物识别系统 By RWLinno 2020101603")
        Form.resize(660, 800)
        QtCore.QMetaObject.connectSlotsByName(Form)

### 标签部分
        self.label_choose = QtWidgets.QLabel(Form)
        self.label_choose.move(20,20)
        self.label_choose.setText("选择动物特征")
        self.label_choose.setStyleSheet("font: 14pt \"宋体\";")

        self.label_chosen = QtWidgets.QLabel(Form)
        self.label_chosen.move(300,20)
        self.label_chosen.setText("已选动物特征")
        self.label_chosen.setStyleSheet("font: 14pt \"宋体\";")

        self.label_procedure = QtWidgets.QLabel(Form)
        self.label_procedure.move(20,400)
        self.label_procedure.setText("推理过程")
        self.label_procedure.setStyleSheet("font: 14pt \"宋体\";")

        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.move(300,400)
        self.label_result.setText("识别结果")
        self.label_result.setStyleSheet("font: 14pt \"宋体\";")

### 按钮部分
        self.insertBtn = QtWidgets.QPushButton(Form)
        self.insertBtn.setText("添加规则")
        self.insertBtn.move(560,20)
        self.insertBtn.installEventFilter(self)
        self.insertBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.insertBtn.setObjectName("insertBtn")

        self.updateBtn = QtWidgets.QPushButton(Form)
        self.updateBtn.setText("修改规则")
        self.updateBtn.move(560,60)
        self.updateBtn.setObjectName("updateBtn")
        self.updateBtn.setStyleSheet("font: 14pt \"宋体\";")

        self.clearBtn = QtWidgets.QPushButton(Form)
        self.clearBtn.setText("清空选项")
        self.clearBtn.move(560,100)
        self.clearBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.clearBtn.setObjectName("cleartBtn")
        self.clearBtn.clicked.connect(Form.clear)

        self.startBtn = QtWidgets.QPushButton(Form)
        self.startBtn.setText("开始推理")
        self.startBtn.move(560,140)
        self.startBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.startBtn.setObjectName("startBtn")
        self.startBtn.clicked.connect(Form.start)

        self.flashBtn = QtWidgets.QPushButton(Form)
        self.flashBtn.setText("刷新页面")
        self.flashBtn.move(560,180)
        self.flashBtn.setStyleSheet("font: 14pt \"宋体\";")
        self.flashBtn.setObjectName("flashBtn")
        self.flashBtn.clicked.connect(Form.reflash)

### 显示栏
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.listView.setStyleSheet("font: 10pt \"宋体\";")
        self.listView.move(20,52)
        self.listView.setObjectName("listView")

        self.fact = QtWidgets.QTextEdit(Form)
        self.fact.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.fact.setStyleSheet("font: 12pt \"宋体\";")
        self.fact.move(300,52)
        self.fact.setObjectName("fact")

        self.procedure = QtWidgets.QTextEdit(Form)
        self.procedure.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.procedure.move(20,432)
        self.procedure.setStyleSheet("font: 12pt \"宋体\";")
        self.procedure.setObjectName("procedure")

        self.result = QtWidgets.QLabel(Form)
        self.result.setGeometry(QtCore.QRect(0, 0, 120,40))
        self.result.setStyleSheet("font: 12pt \"宋体\";")
        self.result.move(400,400)
        self.result.setText("")
        self.result.setObjectName("result")

        self.label_pic = QtWidgets.QLabel(Form)
        self.label_pic.setGeometry(QtCore.QRect(0, 0, 240, 320))
        self.label_pic.move(300,432)
        self.label_pic.setStyleSheet("image: url(:/pic/01.JPG);")
        self.label_pic.setText("图片显示")
        self.label_pic.setObjectName("pic")

##########################################
# 添加规则窗口
##########################################
class Ui_Dialog_add(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("添加规则")
        Dialog.setWindowTitle("添加规则")
        Dialog.resize(480, 240)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
### 按钮部分
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(360, 20, 80, 240))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
### 标签部分
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 251, 61))
        self.label.setStyleSheet("font: 16pt \"宋体\";")
        self.label.setObjectName("label")
        self.label.setText("键入想要添加的规则")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(20, 50, 351, 21))
        self.label2.setStyleSheet("font: 9pt \"宋体\";\n""color: rgb(85, 85, 85);")
        self.label2.setObjectName("label2")
        self.label2.setText('请以"前提1+前提2+前提3+...+前提n=结论"的格式输入(n>=1)')

        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(20, 90, 400, 120))
        self.textEdit.setObjectName("textEdit")

##########################################
# 规则库
##########################################
class Ui_Dialog_update(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("dialog")
        Dialog.resize(640, 480)
        Dialog.setWindowTitle("规则库")
        QtCore.QMetaObject.connectSlotsByName(Dialog)
### 按钮部分
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(500, 420, 72, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        self.pushButton = QtWidgets.QPushButton(Dialog)
        #self.pushButton.setGeometry(QtCore.QRect(500, 400, 81, 80))
        self.pushButton.move(500,390)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.delete)
        self.pushButton.setText("删除")

### 标签部分
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 10, 251, 61))
        self.label.setStyleSheet("font: 16pt \"宋体\";")
        self.label.setObjectName("label")

        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(20, 20, 31, 21))
        self.label2.setStyleSheet("font: 9pt \"宋体\";\n""color: rgb(85, 85, 85);")
        self.label2.setObjectName("label2")
        self.label2.setText("P")

        self.PList = QtWidgets.QListView(Dialog)
        self.PList.setGeometry(QtCore.QRect(20, 40, 256, 331))
        self.PList.setObjectName("PList")

        self.listView_2 = QtWidgets.QListView(Dialog)
        self.listView_2.setGeometry(QtCore.QRect(320, 40, 256, 331))
        self.listView_2.setObjectName("listView_2")

        self.label3 = QtWidgets.QLabel(Dialog)
        self.label3.setGeometry(QtCore.QRect(320, 20, 31, 21))
        self.label3.setStyleSheet("font: 9pt \"宋体\";\n""color: rgb(85, 85, 85);")
        self.label3.setObjectName("label_3")
        self.label3.setText("Q")

##########################################
# 主窗口UI
##########################################
class MainGUI(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        print("MainGUI")
        super(MainGUI, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        print(self.__P__)
        print(self.__Q__)
        self.__s__ = set()
        for plist in self.__P__:
            for p in plist:
                self.__s__.add(p)
        self.__s__ = list(self.__s__)
        self.slm = QStringListModel(self.__s__)
        print("__s__",self.__s__)
        self.listView.setModel(self.slm)
        self.listView.clicked.connect(self.select)

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r+', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines.split('+'))
        with open("Q.txt", 'r+', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)

    def clear(self):
        self.fact.clear()

    def reflash(self):
        print("listView flash")
        self.__read_file__()
        print(self.__P__)
        print(self.__Q__)
        self.__s__ = set()
        for plist in self.__P__:
            for p in plist:
                self.__s__.add(p)
        self.__s__ = list(self.__s__)
        slm = QStringListModel(self.__s__)
        print("__s__",self.__s__)
        self.listView.setModel(slm)
        self.listView.clicked.connect(self.select)
        self.listView.update()

    def start(self):
        str = self.fact.toPlainText().split('\n')
        self.__DB__ = str
        self.__read_file__()
        self.procedure.setText("----开始识别----")
        self.procedure.append('采用正向推理的方法')
        self.inference()
        self.procedure.append('----识别完成----')
        self.result.setText(self.__result__)

    def is_include_in_DB(self, p):
        for i in p:
            if i not in self.__DB__:
                return False
        return True

    def inference(self):
        self.__result__ = '无法识别'
        flag = False
        for i, p in enumerate(self.__P__):
            if self.is_include_in_DB(p):
                self.__DB__.append(self.__Q__[i])
                self.__result__ = self.__Q__[i]
                self.procedure.append('%s -> %s' % (p, self.__Q__[i]))
                flag = True
        if flag:
            pix = QtGui.QPixmap("pic/"+self.__result__+".jpg")
            print(self.__result__+".jpg")
            self.label_pic.setPixmap(pix)

    def add(self):
        pass

    def select(self, qModelIndex):
        self.fact.append(self.__s__[qModelIndex.row()])

##########################################
# 添加规则
##########################################
class AddGUI(QtWidgets.QDialog, Ui_Dialog_add):
    def __init__(self):
        super(AddGUI, self).__init__()
        self.setupUi(self)

    def accept(self):
        DB = self.textEdit.toPlainText().split('\n')
        P = []
        Q = []
        for d in DB:
            d = d.split('=')
            P.append(d[0])
            Q.append(d[1])
        self.write(P,Q)
        self.close()

    def write(self, P, Q):
        with open("Q.txt", 'a+', encoding='utf-8') as f:
            for q in Q:
                f.write("\n"+q)
        with open("P.txt", 'a+', encoding='utf-8') as f:
            for p in P:
                f.write("\n"+p)


##########################################
# 更新规则
##########################################
class UpdateGui(QtWidgets.QDialog, Ui_Dialog_update):
    def __init__(self):
        super(UpdateGui, self).__init__()
        self.setupUi(self)
        self.__read_file__()
        self.slm1 = QStringListModel()
        self.slm1.setStringList(self.__P__)
        self.PList.setModel(self.slm1)
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.__Q__)
        self.listView_2.setModel(self.slm2)

    def accept(self):
        self.__P__ = self.slm1.stringList()
        self.__Q__ = self.slm2.stringList()
        self.write(self.__P__, self.__Q__)
        mainGUI = MainGUI()
        self.close()

    def delete(self):
        select = self.PList.currentIndex().row()
        print(select)
        self.__P__.pop(select)
        self.__Q__.pop(select)
        print("P",self.__P__)
        print("Q",self.__Q__)
        self.slm1 = QStringListModel()
        self.slm1.setStringList(self.__P__)
        self.PList.setModel(self.slm1)
        self.slm2 = QStringListModel()
        self.slm2.setStringList(self.__Q__)
        self.listView_2.setModel(self.slm2)

    def write(self, P, Q):
        with open("Q.txt", 'w', encoding='utf-8') as f:
            flag = 0
            for q in Q:
                if flag :
                    f.write("\n")
                else :
                    flag=1
                f.write(q)

        with open("P.txt", 'w', encoding='utf-8') as f:
            flag = 0
            for p in P:
                if flag :
                    f.write("\n")
                else :
                    flag=1
                f.write(p)

    def __read_file__(self):
        self.__P__ = []
        self.__Q__ = []
        with open("P.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__P__.append(lines)
        with open("Q.txt", 'r', encoding='utf-8') as f:
            while True:
                lines = f.readline().split('\n')[0]
                if not lines:
                    break
                self.__Q__.append(lines)

##########################################
# main函数
##########################################
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainGUI = MainGUI()
    child1 = AddGUI()
    btn = mainGUI.insertBtn
    btn.clicked.connect(child1.show)
    child2 = UpdateGui()
    btn2 = mainGUI.updateBtn
    btn2.clicked.connect(child2.show)
    mainGUI.show()
    sys.exit(app.exec())