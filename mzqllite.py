import datetime
from mfile import *

from mconst import *

import sqlite3


class cDb(object):
    def __init__(self):
        self.connection = sqlite3.connect(DBNAME)
        self.cursor = self.connection.cursor()
        self._dayhearsvk = 0
        self._dayaddsvk = 0
        self._dayeffvk = 0
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS ''' + TABLESTAT + '''  
        (mcurdate TEXT NOT NULL, mcurtime TEXT NOT NULL, martist TEXT NOT NULL,
        mtrack TEXT NOT NULL, hears_vk INTEGER, adds_vk INTEGER,
        eff_vk INTEGER, hears_vk_c TEXT, adds_vk_c TEXT, eff_vk_c TEXT, 
        ServiceOrTrack   TEXT, 
        hears_month_ynd  INTEGER, likes_month_ynd  INTEGER, likes_all_ynd    INTEGER,
        sub_sber         INTEGER, sub_youtube      INTEGER, hears_month_spot INTEGER,
        sub_vk           INTEGER, sub_tiktok       INTEGER, likes_tiktok     INTEGER
        )
        ''')
        self.cursor.execute('''
         CREATE TABLE IF NOT EXISTS ''' + TABLECHK + '''  
         (mname TEXT NOT NULL, mlink TEXT NOT NULL, freq FLOAT,
         mstr TEXT, mstrfield INTEGER, ishere BOOL, 
         lastdate TEXT, lasttime TEXT, lastval TEXT, needproxy BOOL)
         ''')

        self.connection.commit()

        #
        # class Artist:
        #     def __init__(self, name, vkstudio="", spot="", yandex="", sber="", youtube="", vk="", tiktok="",tlg="",instagram="",l3="",l4="",l5="",minhears=20):
        #         self.name = name
        #         self.vkstudio = vkstudio
        #         self.spot = spot
        #         self.yandex = yandex
        #         self.sber = sber
        #         self.youtube = youtube
        #         self.vk = vk
        #         self.tiktok = tiktok
        #         self.tlg = tlg
        #         self.instagram = instagram
        #         self.l3 = l3
        #         self.l4 = l4
        #         self.l5 = l5
        #         self.minhears = minhears


        # Артист (Имя, vkstudio, spotify, yandex, sber,
        #           youtube, vk, Tiktok,
        #           Tlg, Instagram
        #           ,,,minhears):

        self.art = [
            Artist('RAYVAN', "679765629422687778", "6MUpnjFA4zQu3s0t2Nzlfk", "8141812", "210105583",
                   "UCvtme_nmuo4NdcYniouDh2Q","rayvan.official","@rayvan.official",
                   "rayvanmusic", "rayvan.official"),
            Artist('Кипиш Нот', "8847225405052948823", "4QlySbg8i1tMfj0QPe2BUB", "22628661", "211979258",
                   "", "kipish_not", "",
                   "kipish_not", "makaronnoe_bludo"),
            Artist('Interpol86', "", "", "", "",
                   "","interpol86ru", "",
                   "",""),
            Artist('MILZ', "3968096882825495134", "181Jnv1B77SIvC7JW5cmop", "19171403", "212513613",
                   "UC27Z5ZvYSt95UtjFeGJ0wGA", "milz.singer"),
            Artist('Алексир', "3377722344143542502", "7aPj4tatJiiVIImj1uYdpV", "18574196", "212326111",
                   "UC5CM0orwcf0e81U8818LNVg", "aleksirme", "",
                   "aleksir_me","aleksir.me"),
            Artist('София Мосейчук', "", "4QiguGhNyTgHtELFp9KJDp", "15710563", "211630315", "",
                   "moseichuksofiia", "@krasotka.sofi","",
                   "krasotka_sofi", "krasotka_sofi",minhears=50),
            # Artist('Rustam Fahrtdinov', "6775914816193346218", "7g63TUNYZqiS3GbIEIbDdG", "3192939", "31876918",
            #        "UCyw22JexbXGNh3_wqaOkq2g", "rustamfahrtdinov", "@rustamfahrtdinov",
            #        "","rustam_fahrtdinov"),
            Artist('Rustam Fahrtdinov', "6775914816193346218", "7g63TUNYZqiS3GbIEIbDdG", "3192939", "31876918",
                   "UCyw22JexbXGNh3_wqaOkq2g", "rustamfahrtdinov", "",
                   "", "rustam_fahrtdinov"),
            Artist('KALUGIN', "1263271834263162561", "6CKpzSn0XsUadRH95LzdJp", "16539792", "211923181",
                   "UCxovuUXDDlOAIo1fY98vtyw", "kalugin_sergey_music", "@_kalugin___",
                   "kaluginsergei", "kalugin_s",minhears=50),
            Artist('Vigi', "160757614473898073", "", "17288582", "212086549", "", "vigisinger",minhears=30),
            Artist('Вячеслав Мясников', "2373197429746032417", "6rSChDc4zteS5rIH728wxA", "3118319", "1479802",
                   "UCKxaCaipSkU6MgQwv2y-lkw", "slava_myasnikov", "@miasnikov.s",
                   "","miasnikov.s",minhears=500),
            Artist('Ирина Эмирова', "5595344415242300490", "0XRzVBeXMuAoyLiKt611n2", "3987540", "167840734", "",
                   "irina_emirova","","",
                   "irina_emirova","",
                   "","",minhears=50),
            Artist('Хор Ирины Павленко', "2495875715565516380", "0sFrPGC1ewZMBmGrt8UmcM", "21014484", "212760210",
                   "","","",
                   "","irina_pavlenkovokaltomsk"),
            Artist('Нонна', "730034513534917869", "6beQNGwlwrvrT01TDwMBcl", "8590484", "209798494",
                   "", "singer_nonna","",
                   "", "nonna_official_",minhears=50),
            Artist('RemoteRussia', "", "", "", "", "", "", "", "remote_russia"),
            Artist('Анастасия Ларцева', "8539475736460412680", "", "", "", "", "", "")
        ]


    def initstring(self, artist):
        self.cursor.execute('PRAGMA table_info("MuzStat")')
        column_names = [i[1] for i in self.cursor.fetchall()]
        # print(column_names)
        userlist = []
        for values in column_names:
            userlist.append(values)
        self.columns = {key: "" for key in userlist}

        mdate = datetime.datetime.now()
        self.columns["mcurdate"] = getcdate()
        self.columns["mcurtime"] = getctime()
        self.columns["martist"] = artist

    def closeconnection(self):
        self.connection.close()

    def vktracks2db(self, ss, name):

        self._dayaddsvk = 0
        self._dayhearsvk = 0

        self._hears_best_song = ""
        self._hears_best_n = 0

        self._eff_best_song = 0
        self._eff_best_n = 0

        for s in ss:

            hears_vk_c = adds_vk_c = eff_vk_c = ""

            istr = s.text.split('\n')
            # print(istr)
            #
            if istr[3].find("%") > 0:
                hears_vk_c = istr[3]
                istr.pop(3)

            if istr[4].find("%") > 0:
                adds_vk_c = istr[4]
                istr.pop(4)

            mtrack = istr[1]
            hears_vk = int(checkisnumberr(istr[3]))
            adds_vk = int(checkisnumberr(istr[4]))
            martist = name

            eff_vk = 0 if adds_vk == 0 else round(hears_vk / adds_vk, 1)
            eff_vk = 0 if hears_vk < MIN_HEARS_FOR_EFFECTIVETY  else eff_vk

            self._dayhearsvk = self._dayhearsvk + hears_vk
            self._dayaddsvk = self._dayaddsvk + adds_vk
            self._dayeffvk = 0 if self._dayaddsvk == 0 else round(self._dayhearsvk / self._dayaddsvk, 1)

            if hears_vk > self._hears_best_n:
                self._hears_best_n = hears_vk
                self._hears_best_song = mtrack

            if (eff_vk < self._eff_best_n) and (eff_vk > 0):
                self._eff_best_n = eff_vk
                self._eff_best_song = mtrack

            mcurdate = getcdate()
            mcurtime = getctime()

            self.cursor.execute(
                'INSERT INTO MuzStat (mcurdate,mcurtime,martist,mtrack,hears_vk,adds_vk,eff_vk,hears_vk_c,adds_vk_c,eff_vk_c,ServiceOrTrack)'
                ' VALUES (?, ?, ?,?, ?,?, ?, ?,?, ?,?)',
                (mcurdate, mcurtime, martist, mtrack, hears_vk, adds_vk, eff_vk, hears_vk_c, adds_vk_c, eff_vk_c,
                 IsTRACK,))

        self.connection.commit()

    def day2db(self):

        self.cursor.execute(
            'INSERT INTO MuzStat (mcurdate,mcurtime,martist,mtrack,hears_vk,adds_vk,eff_vk,hears_vk_c,adds_vk_c,eff_vk_c,ServiceOrTrack,hears_month_ynd,likes_month_ynd,likes_all_ynd, sub_sber, sub_youtube, hears_month_spot, sub_vk, sub_tiktok, likes_tiktok, sub_tlg, hears_best_song, hears_best_n, eff_best_song, eff_best_n)'
            ' VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?,?,?,?,?)',
            (self.columns["mcurdate"], self.columns["mcurtime"], self.columns["martist"], "", self._dayhearsvk,
             self._dayaddsvk, self._dayeffvk, "", "", "",
             IsSERVICE, self.columns["hears_month_ynd"], self.columns["likes_month_ynd"], self.columns["likes_all_ynd"],
             self.columns["sub_sber"], self.columns["sub_youtube"], self.columns["hears_month_spot"],
             self.columns["sub_vk"], self.columns["sub_tiktok"], self.columns["likes_tiktok"], self.columns["sub_tlg"],
             self._hears_best_song, self._hears_best_n,self._eff_best_song,self._eff_best_n))

        self.connection.commit()

    arr=[]


    def dbchk2table(self, mselect="",myfreqhours=False):

        class ArtistChk:
            def __init__(self, mname, mlink, freq, mstr, mstrfield, ishere,  needproxy, lastdate="", lasttime="", lastval="", alwaysshow=""):
                self.mname = mname
                self.mlink = mlink
                self.freq = freq
                self.mstr = mstr
                self.mstrfield = mstrfield
                self.ishere = ishere
                self.needproxy = needproxy
                self.lastdate = lastdate
                self.lasttime = lasttime
                self.lastval = lastval
                self.alwaysshow = alwaysshow
        #
        # arr=[]

        msql='SELECT * FROM MuzChk' if mselect=="" else 'SELECT * FROM MuzChk Where mname Like "'+ mselect +'%"'

        self.cursor.execute(msql)
        # self.cursor.execute("SELECT * FROM MuzChk WHERE mname LIKE '%chkVK%'")


        for row in self.cursor.fetchall():
            # arr.append(row)
            if (myfreqhours and row[2]<24) or ( not myfreqhours):
                self.arr.append(ArtistChk(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))

            # print(row)


    def update_dbchk_row(self,arr):
        self.cursor.execute(
            'UPDATE MuzChk SET lastdate = ?, lasttime=?, lastval =?'
            'WHERE mname= ?',
            (getcdate(), getctime(), arr.lastval, arr.mname))
        self.connection.commit()

    # import matplotlib
    # import matplotlib.pyplot as plt
    # import matplotlib.dates as mdates
    # from matplotlib import style
    # from dateutil import parser




    def graph_tracks(self, song, artist):

        sql = "SELECT mcurdate, hears_vk, adds_vk, eff_vk  FROM MuzStat WHERE mtrack=" + song \
              + " AND martist=" + artist + " AND ServiceOrTrack ='track'"

        df = pd.read_sql(sql, con=self.connection)

        x_CrestFactor = df['adds_vk']
        y_CrestFactor = df['hears_vk']
        z_CrestFactor = round(COEFFEFFECT/df['eff_vk'])
        created_time = df['mcurdate']

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=created_time, y=x_CrestFactor, mode='lines', name=CAPTIONADD))
        fig.add_trace(go.Scatter(x=created_time, y=y_CrestFactor, mode='lines', name=CAPTIONHEAR))
        fig.add_trace(go.Scatter(x=created_time, y=z_CrestFactor, mode='lines+markers', name=CAPTIONEFF))

        fig.update_layout(title_text="Статистика трека: "+ artist + ":" + song)

        fig.show()


    def graph_services(self, artist):

        sql = "SELECT mcurdate, hears_vk, adds_vk, eff_vk, hears_month_ynd, likes_month_ynd, likes_all_ynd, sub_sber, sub_youtube, hears_month_spot, sub_vk,sub_tiktok  FROM MuzStat WHERE martist=" + artist\
              + " AND ServiceOrTrack ='service'"
        df = pd.read_sql(sql, con=self.connection)

        l1 = df['adds_vk']
        l2 = df['hears_vk']
        l3 = round(df['adds_vk']*COEFFEFFECT/df['hears_vk'])
        l4 = df['hears_month_ynd']
        l5 = df['likes_month_ynd']
        l6 = df['likes_all_ynd']
        l7 = df['sub_sber']
        l8 = df['sub_youtube']
        l9 = df['hears_month_spot']
        l10 = df['sub_vk']
        l11 = df['sub_tiktok']
        created_time = df['mcurdate']

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=created_time, y=l1, mode='lines', name=CAPTIONADD))
        fig.add_trace(go.Scatter(x=created_time, y=l2, mode='lines', name=CAPTIONHEAR))
        fig.add_trace(go.Scatter(x=created_time, y=l3, mode='lines+markers', name= CAPTIONEFF))

        fig.add_trace(go.Scatter(x=created_time, y=l4, mode='lines', name='hears_month_ynd'))
        fig.add_trace(go.Scatter(x=created_time, y=l5, mode='lines', name='likes_month_ynd'))
        fig.add_trace(go.Scatter(x=created_time, y=l6, mode='lines+markers', name='likes_all_ynd'))

        fig.add_trace(go.Scatter(x=created_time, y=l7, mode='lines', name='sub_sber'))
        fig.add_trace(go.Scatter(x=created_time, y=l8, mode='lines', name='sub_youtube'))
        fig.add_trace(go.Scatter(x=created_time, y=l9, mode='lines+markers', name='hears_month_spot'))

        fig.add_trace(go.Scatter(x=created_time, y=l10, mode='lines+markers', name='VK.Подписчики'))
        fig.add_trace(go.Scatter(x=created_time, y=l11, mode='lines+markers', name='TikTok.Подписчики'))
        fig.update_layout(title_text="Статистика музыканта: "+ artist)

        fig.show()


    def get2days_4compare(self):

        sql = "SELECT * FROM MuzStat WHERE mcurdate='" + getcdate() +"'"
        df = pd.read_sql(sql, con=self.connection)
        startday=1 if df.empty else 0

        sql = "SELECT * FROM MuzStat WHERE mcurdate='" + getcdate(startday) +"'" + " OR mcurdate='" + getcdate(startday+1) +"'"
        df = pd.read_sql(sql, con=self.connection)


        return df


    def getartistparamByName(self,mname,mparm):

        res= MIN_VAL_FOR_COMPARE
        for i in self.art:
            if i.name.lower()==mname.lower():
                return i.__dict__[mparm]
        return res


        sql = "SELECT * FROM MuzStat WHERE mcurdate='" + getcdate() +"'"
        df = pd.read_sql(sql, con=self.connection)
        startday=1 if df.empty else 0

        sql = "SELECT * FROM MuzStat WHERE mcurdate='" + getcdate(startday) +"'" + " OR mcurdate='" + getcdate(startday+1) +"'"
        df = pd.read_sql(sql, con=self.connection)


        return df
