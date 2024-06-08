import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys
import difflib

# при работа mainchk проверять заглавные или строчные буквы прямо на странице!!!


VER = "240609 Проверена Rayvan - проверка в шоты"
VER = "2.6 от 03.06 Добавлена возможность проверки больших полей (Эрмитаж, Русский музей)"


TXTPRODUCTIVE  = "PRODUCTIVE"

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
