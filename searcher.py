# -*- coding: utf-8 -*-
import os, glob


def handle_folder(path, word, words, is_demo=False): #Начала функции , в которую передаётся path
    global dirs
    glob_path = os.path.join(path, '*')
    for filename in glob.glob(glob_path): #Цикл, который переберает все каталоги
        if os.path.isdir(filename): #Если находится католог
            handle_folder(filename, word, words) # запуская функцию ещё раз до последнего каталога
        else: #Если не находит
            try: #Пробует
                with open(filename, 'r') as f: #октрыть файл как файл для чтения
                    text = f.read() #Передаёт значение в переменную text
                if word.lower() in text.lower(): #Если предложение есть в тексте
                    if is_demo:
                        print(f"FILE: {filename} WORD: {word} ") #Выводит значение filename и предложение
                    dirs.add((filename, word))
                for i in words: #цикл , который переберает все слова
                    if i in text.lower(): #если слово есть в тексте
                        if is_demo:
                            print(f"FILE: {filename} WORD: {i} ") #Выводит значение Filename и слово
                        dirs.add((filename, word))
            except Exception: #Если не получилось
                pass#Пропускает


def master_handler(word, folder_path, is_demo=False):
    global dirs
    words = word.lower().split() #Переводит слова в нижний регистр и разбивает предложение по одному слову
    dirs = set()
    handle_folder(folder_path, word, words, is_demo=is_demo) #Запускает функция передавая тут значение folder_path - путь до каталога
    return list(dirs)
    

def main():
    word = input("Введите слова ")
    folder_path = input("Введите каталог ")
    master_handler(word, folder_path, is_demo=True) 
    print("DONE")


if __name__ == "__main__":
    main()