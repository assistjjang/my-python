import sys
import os
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic
import urllib.request
import change_curr

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
form = resource_path('helloworld.ui')
# 출처: https://editor752.tistory.com/140 [CF::LF]


form_class = uic.loadUiType(form)[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    exchange_val = float(change_curr.get_eur())
    transfer_fee_val = 0
    
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        #self.transfer_fee.setValidator(QDoubleValidator(-999.0, 999.0, 2))
        self.transfer_fee.editingFinished.connect(self.fun_transfer_fee_editfinished)
        self.select_eur.clicked.connect(self.sel_rb_eur)
        self.select_gbp.clicked.connect(self.sel_rb_gbp)
        self.change_btn.clicked.connect(self.btnClick)
    
    def btnClick(self):
        test = str(self.exchange_val * self.transfer_fee_val / 100)
        self.dp_curr.setText(test + " 억원")
    
    def sel_rb_eur(self):
        self.exchange_val = float(change_curr.get_eur())
    
    def sel_rb_gbp(self):
        self.exchange_val = float(change_curr.get_gbp())

    def fun_transfer_fee_editfinished(self):
        self.transfer_fee_val = float(self.transfer_fee.text())

# 출처: https://jy-tblog.tistory.com/26 [jy.log:티스토리]

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()

