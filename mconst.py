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


HELPTXT="Use one or more param: PRODUCTIVE, DONTWRITE2BASE, NOYOUTUBE, NOTIKTOK, NOVK и др"

# проверка дублей в city "SELECT link, COUNT(*) FROM buildingdb GROUP BY link HAVING COUNT(*) > 1;"
# если ошибка что не находит файл в подпапке, надо его просто отредактировать в github
# при работа mainchk проверять заглавные или строчные буквы прямо на странице!!!
# при работа mainchk проверять яззык чтобы был нужный!!!

MVERSION="250706 Поправил переменные с помощью ИИ "
MVERSION="250211 Сделан readme и поправлены переменные "
MVERSION="241223 Поправлены отчеты, мин % для отчетов и др "
# MVERSION="241203 Поправлены graph "
# MVERSION="241014 Скорректи ошибки во вк что вылетала запись в бд"
# MVERSION="241116 Все улицы и пригороды"
# MVERSION="240930 Скорректи письма тк не отправлялись"
# MVERSION="240925 Добавил письма только на вторую итерацию"
# MVERSION="240912 Переформатнул ТИкТок через Meta"
# MVERSION="240902 Поправил Sber"
# MVERSION="240820 Поправил TikTok+ Yandex"
# MVERSION="240815 Поправил Вк перед переименованием таблиц"
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
TXTONLYONETESTPROGON = "ONLYONETESTPROGON"

TXTFREQHOURS="FREQHOURS"

TXTNOYANDEX= "NOYANDEX"
TXTNOSBER="NOSBER"
TXTNOVKSUB="NOVKSUB"
TXTNOYOUTUBE="NOYOUTUBE"
TXTNOTIKTOK="NOTIKTOK"
TXTNOTLG="NOTLG"

MIN_HEARS_FOR_EFFECTIVETY = 20
MIN_VAL_FOR_COMPARE = 10
ALERT_PROC_IN_COMPARE=20

MYNOTNUMBER=-1


DBNAME = "mus2024.db"
# DBNAME = "mus2024(4test).db"

TITLE_CHK="CHKSERVICE: "

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


# Для ASUS 250706
MDIR2 = r"--user-data-dir=C:\Users\Konstantin\AppData\Local\Google\Chrome\User Data"
MPROF2 = r"--profile-directory=Default"
# MDIR2 = r"--user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data"
# MPROF2 = r"--profile-directory=Profile 12"


# Полезные скрипты
#
# Корректировка значений когда чтото пошло не  так
# UPDATE MuzStat Set likes_month_ynd=-1 where likes_month_ynd=9999
# UPDATE MuzStat Set likes_all_ynd=-1 where likes_all_ynd=9999

class Artist:
    def __init__(self, name, vkstudio="", spot="", yandex="", sber="", youtube="", vk="", tiktok="", tlg="",
                 instagram="", l3="", l4="", l5="", minhears=20, run_after_error=False):
        self.name = name
        self.vkstudio = vkstudio
        self.spot = spot
        self.yandex = yandex
        self.sber = sber
        self.youtube = youtube
        self.vk = vk
        self.tiktok = tiktok
        self.tlg = tlg
        self.instagram = instagram
        self.l3 = l3
        self.l4 = l4
        self.l5 = l5
        self.minhears = minhears
        self.run_after_error = run_after_error