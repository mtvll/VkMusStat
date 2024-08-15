# 20240705 Добавил try для верного streamlit
try:
    from tb_keys import *
except ImportError as error:
    pass
import sqlite3

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import difflib

# проверка дублей в city "SELECT link, COUNT(*) FROM citytable GROUP BY link HAVING COUNT(*) > 1;"
# если ошибка что не находит файл в подпапке, надо его просто отредактировать в github
# при работа mainchk проверять заглавные или строчные буквы прямо на странице!!!
# при работа mainchk проверять яззык чтобы был нужный!!!

MVERSION="240815 Поправил Вк перед переименованием таблиц"
# MVERSION="240707 Скорректировал сервер и makbludo"
# MVERSION="240704 Добавлен streanlit в git и текст к эффективности2"
# MVERSION="2406252Streamlit (only RAYVAN and delete Eff)"
# MVERSION="240622 Добавлен like вконтакте"
# MVERSION="240621 Добавлены поля для инстаграм и тг2"
# MVERSION="240614 Новый мейл в отдельном файле"
# MVERSION = "240609 Проверка Rayvan и другие "
# MVERSION = "2.6 от 03.06 Добавлена возможность проверки больших полей (Эрмитаж, Русский музей)"


TXTPRODUCTIVE  = "PRODUCTIVE"

TXTDONTWRITE2BASE  = "DONTWRITE2BASE"

MIN_HEARS_FOR_EFFECTIVETY = 20
MIN_VAL_FOR_COMPARE = 10
ALERT_PROC_IN_COMPARE=30

MYNOTNUMBER=-1


DBNAME = "mus2024.db"
# DBNAME = "mus2024(4test).db"

TABLESTAT = "MuzStat"
TABLECHK = "MuzChk"

ERRORSTR=": ERR"

IsTRACK = 'track'
IsSERVICE = 'service'


COEFFEFFECT = 1000
CAPTIONEFF='VK.Эффект(добавлений на 1000 просл)'
CAPTIONHEAR='VK.Прослушивания'
CAPTIONADD='VK.Добавления'


MDIR1 = r"--user-data-dir=C:\Users\K\AppData\Local\Google\Chrome\User Data"
MPROF1 = r"--profile-directory=Profile 4"
MPC1 = "WIN-OR93J55JCVR"

MDIR2 = r"--user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data"
MPROF2 = r"--profile-directory=Profile 12"


# Полезные скрипты
#
# Корректировка значений когда чтото пошло не  так
# UPDATE MuzStat Set likes_month_ynd=-1 where likes_month_ynd=9999
# UPDATE MuzStat Set likes_all_ynd=-1 where likes_all_ynd=9999
