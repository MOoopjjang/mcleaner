#!python3
#-*- coding:utf-8 -*-



import sys
import json
import os , sys
from mcleaner import MCleaner
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

"""
Make By MOoop

Desc :
   지정된 경로에 garbage파일을 삭제하는 프로그램

History :
    2019.10.26 create
    2020.06.15 GUI 추가


version 1.0      
"""

form_class = uic.loadUiType('mclean.ui')[0]


class MCleanUI(QMainWindow , form_class):
	def __init__( self ):
		super().__init__()
		self.setupUi( self )
		self.setFixedSize(520,480)

		self._mcleaner , self._exts , self._path = self._load_()
		self.btn_clean.clicked.connect(self._clean_)

		self._display_()


	def _display_(self):
		if self._path is not None:self.line_path.setText(self._path)
		if self._exts is not None:self.line_target.setText(",".join(self._exts))

		self.line_count.setText("0")

		# self.btn_clean.setStyleSheet("background-color: blue")


	def _load_( self ):
		if os.path.exists('config.json'):
			with open('config.json' , 'r') as fr:
				jobj = json.load(fr)
				return ( MCleaner(jobj.get('path') , jobj.get('exts')) ,jobj.get('exts') ,jobj.get('path') )
		else:
			return ( MCleaner() , None , None )

	def _clean_( self ):
		self.line_count.clear()
		self.pte_processing.clear()

		if self.line_path.text() == '' or self.line_target.text() == '':
			QMessageBox.question(self ,'Warning','위치와 삭제할 대상의종류를 입력하세요!',QMessageBox.Yes)
			return

		self._mcleaner.setRootPath(self.line_path.text()).setExts(self.line_target.text().split(","))
		count = 0
		for index , path in self._mcleaner.run():
			self.pte_processing.appendPlainText(path)
			count = index

		self.line_count.setText(str(count))


def main():
	app = QApplication(sys.argv)
	myWindow = MCleanUI()
	myWindow.show()
	app.exec_()




if __name__ == '__main__':
	main()


