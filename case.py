from PyQt5 import QtCore, QtGui, uic,QtWidgets
from case_ui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
import sys
import os
import time
'''
qtCreatorFile = "ui\case.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
'''

class translation(QMainWindow, Ui_human_translation):

    def __init__(self, parent=None):
        super(translation, self).__init__(parent)
        self.setupUi(self) 
        self.translation.clicked.connect(self.transla)
        self.dictionary1.clicked.connect(self.diction1)
        self.dictionary2.clicked.connect(self.diction2)
        self.human_translation_2.clicked.connect(self.baidu_translation)
        self.dictionary2.setStyleSheet("color:red;")
        self.translation.setStyleSheet("background-color:rgb(242,58,58);color:white;")
        self.dictionary1.setStyleSheet("QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.human_translation_2.setStyleSheet("background-color:white;")
        self.textEdit.setStyleSheet("background-color:#f0f0f0;border-width:0;border-style:outset")
        self.textBrowser.setStyleSheet("border-width:0;border-style:outset;background-color:#f0f0f0;")
        self.bgcolor.setStyleSheet("background-color:white;")
        self.bgcolor1.setStyleSheet("background-color:#ffeff2;")
        self.label_3.setStyleSheet("QLabel:hover{color:rgb(255,0,0);}")
        self.label_4.setStyleSheet("QLabel:hover{color:rgb(255,0,0);}")
        jpg = QtGui.QPixmap('..\img\logo1.jpg')
        self.logo.setPixmap(jpg)
        jpg1=QtGui.QPixmap('..\img\A.png')
        self.logo1.setPixmap(jpg1)
        jpg2 = QtGui.QPixmap('..\img\B.png')
        self.logo2.setPixmap(jpg2)
        jpg3 = QtGui.QPixmap('..\img\c.png')
        self.logo3.setPixmap(jpg3)
        jpg4 = QtGui.QPixmap('..\img\d.png')
        self.logo4.setPixmap(jpg4)
        jpg5 = QtGui.QPixmap('..\img\photo.png')
        self.logo5.setPixmap(jpg5)
        self.textEdit.setPlaceholderText("请输入你要翻译的内容")
        self.index = 1

    def diction1(self):
        self.textEdit.setGeometry(QtCore.QRect(280, 154, 750, 150))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.textBrowser.setObjectName("textEdit")
        self.bgcolor1.setGeometry(QtCore.QRect(0, 175, 250, 60))
        self.dictionary2.setStyleSheet("color:black;")
        self.label_3.setStyleSheet("color:black;")
        self.label_4.setStyleSheet("color:black;")
        self.translation.setGeometry(QtCore.QRect(890, 330, 100, 40))
        self.human_translation_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.dictionary1.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;")
        self.label_3.setStyleSheet("QLabel:hover{color:rgb(255,0,0);}")
        self.label_4.setStyleSheet("QLabel:hover{color:rgb(255,0,0);}")
        self.translation.setText("查 询")
        self.dictionary2.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.textEdit.setPlaceholderText("请输入要查询的单词...")

    def diction2(self):
        self.textEdit.setGeometry(QtCore.QRect(280, 50, 750, 330))
        self.textEdit.setObjectName("textEdit")
        self.textBrowser.setGeometry(QtCore.QRect(280, 415, 750, 330))
        self.textBrowser.setObjectName("textEdit")
        self.bgcolor1.setGeometry(QtCore.QRect(0, 245, 250, 60))
        self.dictionary1.setStyleSheet("color:black;")
        self.label_3.setStyleSheet("color:black;")
        self.label_4.setStyleSheet("color:black;")
        self.translation.setGeometry(QtCore.QRect(790, 315, 100, 40))
        self.human_translation_2.setGeometry(QtCore.QRect(910, 315, 100, 40))
        self.dictionary1.setStyleSheet("border-style:outset;border-width:0;")
        self.dictionary2.setStyleSheet("border-style:outset;border-width:0;color:red;")
        self.label_3.setStyleSheet("QLabel:hover{color:rgb(255,0,0);}")
        self.label_4.setStyleSheet("QLabel:hover{color:rgb(255,0,0);}")
        self.translation.setText("翻 译")
        self.dictionary1.setStyleSheet(
            "QPushButton:hover{color:rgb(255,0,0)}""QPushButton{border-style:outset;border-width:0;}")
        self.textEdit.setPlaceholderText("请输入要翻译的文字或内容")
        
        
    def transla(self):
        #test1 = int(self.textEdit.toPlainText())
        #test2 = test1 * 10
        content = self.textEdit.toPlainText()
        input_path = '输入的路径'
        with open(input_path,'w') as f:
            f.write(content)
        output_path = '输出的路径'
        cmd = 'nmt推断命令'
        p=os.popen(cmd)
        p.read()
        with open(output_path,"rb") as f:    #设置文件对象
            text = f.read()
        #file = open(output_path, encoding='gbk')
        #print(file)
        self.textBrowser.setText(text.decode(encoding='utf-8'))
        self.index += 1

    def baidu_translation(self):
        appid = '你的百度翻译api id'
        secretKey = '你的百度翻译api key'
        httpClient = None
        myurl = '/api/trans/vip/translate'
        content = self.textEdit.toPlainText()
        q = content
        fromLang = 'zh'  # 源语言
        toLang = 'en'  # 翻译后的语言
        salt = random.randint(32768, 65536)
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
            q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
            salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            jsonResponse = response.read().decode("utf-8")  # 获得返回的结果，结果为json格式
            js = json.loads(jsonResponse)  # 将json格式的结果转换字典结构
            dst = str(js["trans_result"][0]["dst"])  # 取得翻译后的文本结果
            self.textBrowser.setText(dst) # 打印结果
        except Exception as e:
            self.textBrowser.setText("请求错误")
        finally:
            if httpClient:
                httpClient.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window =translation()
    window.show()
    sys.exit(app.exec_())