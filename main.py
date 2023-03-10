# -*- coding: utf-8 -*-
# Для создлания .py из .ui: pyuic5 design.ui -o design.py
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import design  # Это наш конвертированный файл дизайна
from searcher import master_handler # импортируем нашу функцию поиска по папкам
import os


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowTitle("Чиловый проjект")
        self.setDirBtn.clicked.connect(self.set_dir_fnc)
        self.searchBtn.clicked.connect(self.search_fnc)
        self.filesWidget.itemSelectionChanged.connect(self.open_file_fnc)
        self.found_files = []
    
    def set_dir_fnc(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Укажите базовую директорию')
        self.dirLine.setText(folderpath)
        
    def search_fnc(self):
        self.filesWidget.clear() # Очищаем список файлов
        
        word = self.wordsLine.text()
        if not word.strip():
            QMessageBox.critical(self, "Ошибка ", "Укажите слова для поиска", QMessageBox.Ok)
            return 
        folder = self.dirLine.text()
        if not os.path.isdir(folder):
            QMessageBox.critical(self, "Ошибка ", "Укажите существующую базовую директорию", QMessageBox.Ok)
            return
        self.found_files = master_handler(word, folder)
        
        for path, wrd in self.found_files:
            self.filesWidget.addItem(f"File: {path}; WORD: {wrd}")
        pass
    
    def open_file_fnc(self):
        index = self.filesWidget.currentIndex().row()
        if index >= len(self.found_files):
            QMessageBox.critical(self, "Ошибка ", "Неизвестная ошибка. Перезапустите поиск", QMessageBox.Ok)
            return
        file_path = self.found_files[index][0]
        os.startfile(file_path)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
