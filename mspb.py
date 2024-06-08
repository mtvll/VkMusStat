import os
import sqlite3
import openpyxl
from mzweb import *

base_name = 'mus2024spb.db'

def export_to_sqlite():
    '''Экспорт данных из xlsx в sqlite'''

    # 1. Создание и подключение к базе

    # Получаем текущую папку проекта
    prj_dir = os.path.abspath(os.path.curdir)
    a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Имя базы

    # метод sqlite3.connect автоматически создаст базу, если ее нет
    connect = sqlite3.connect(prj_dir + '/' + base_name)
    # курсор - это специальный объект, который делает запросы и получает результаты запросов
    cursor = connect.cursor()

    # создание таблицы если ее не существует
    cursor.execute('CREATE TABLE IF NOT EXISTS spb91 (WKT text, mName text,googlelink text,description  text,style text,access text,citywallslink text,years text, architect text)')


    # 2. Работа c xlsx файлом

    # Читаем файл и лист1 книги excel
    file_to_read = openpyxl.load_workbook('spb91.xlsx', data_only=True)
    sheet = file_to_read['Стили_и_Entrances']

    # Цикл по строкам начиная со второй (в первой заголовки)

    for row in range(2, sheet.max_row + 1):
        # Объявление списка
        data = []
        # Цикл по столбцам от 1 до 4 ( 5 не включая)
        for col in range(1, 10):
            # value содержит значение ячейки с координатами row col
            value = sheet.cell(row, col).value
            # Список который мы потом будем добавлять
            data.append(value)

    # 3. Запись в базу и закрытие соединения

        # Вставка данных в поля таблицы
        cursor.execute("INSERT INTO spb91 VALUES (?, ?, ?, ?,?, ?, ?, ?,?);", (data[0], data[1], data[2], data[3],data[4], data[5], data[6], data[7],data[8]))

    # сохраняем изменения
    connect.commit()
    # закрытие соединения
    connect.close()


def clear_base():
    '''Очистка базы sqlite'''

    # Получаем текущую папку проекта
    prj_dir = os.path.abspath(os.path.curdir)

    # Имя базы
    base_name = 'auto.sqlite3'

    connect = sqlite3.connect(prj_dir + '/' + base_name)
    cursor = connect.cursor()

    # Запись в базу, сохранение и закрытие соединения
    cursor.execute("DELETE FROM spb91")
    connect.commit()
    connect.close()

def spbsql2table():

    class spbb:
        def __init__(self,d1,d2,d3,d4,d5,d6,d7,d8,d9 ):
            self.d1=d1
            self.d2=d2
            self.d3=d3
            self.d4=d4
            self.d5=d5
            self.d6=d6
            self.d7=d7
            self.d8=d8
            self.d9=d9

        #
    prj_dir = os.path.abspath(os.path.curdir)
    a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # метод sqlite3.connect автоматически создаст базу, если ее нет
    connection = sqlite3.connect(prj_dir + '/' + base_name)
    # курсор - это специальный объект, который делает запросы и получает результаты запросов
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM spb91')

    web = cWebm()


    ar = []

    for row in cursor.fetchall():
        ar.append(spbb(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

    import re
    mdesc = row[3]

    for ii in ar:
        ss=str(ii.d7)
        if ss.find("citywalls") < 0:
            mdesc = ii.d4

            match = re.search('https://www.citywalls.ru(.+?)html', mdesc)
            # if match:
            #     print(match.group(0))  #  "Keywords: key, key, key"
            #
            if match ==None:
                print(ii.d2 + " " + "CHECK DESC")
                continue

            mcity=match.group(0)


            march,myaears,mstyle =web.getcitywalls(mcity)

            cursor.execute(
                'UPDATE spb91 SET years = ?, style =?, architect =?,citywallslink=?'
                'WHERE mName= ?',
                (myaears, mstyle, march, mcity, ii.d2,))
            connection.commit()
            res = "DONE"
        else:
            res = "SKIP"
        print (ii.d2+" "+ res)

# Запуск функции
# export_to_sqlite()

spbsql2table()