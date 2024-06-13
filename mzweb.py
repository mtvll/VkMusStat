from mconst import *
from mfile  import *

# import mzqllite

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import socket

MPAUSE = 3


class cWebm(object):
    def __init__(self):
        # create chromeoptions instance
        options = webdriver.ChromeOptions()

        # provide location where chrome stores profiles
        if (socket.gethostname()) == MPC1:
            mdir = MDIR1
            mprof = MPROF1
        else:
            mdir = MDIR2
            mprof = MPROF2

        # options.add_argument(r"--user-data-dir=C:\\Users\\K\\AppData\\Local\\Google\\Chrome\\User Data")
        # options.add_argument(r"--profile-directory=Profile 4")

        options.add_argument(mdir)
        options.add_argument(mprof)

        # options.add_argument('--remote-debugging-pipe')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        self.driver = driver

    def init2(self):
        # create chromeoptions instance
        options = webdriver.ChromeOptions()

        # provide location where chrome stores profiles
        if (socket.gethostname()) == MPC1:
            mdir = MDIR1
            mprof = MPROF1
        else:
            mdir = MDIR2
            mprof = MPROF2

        options.add_argument(mdir)
        options.add_argument(mprof)
        options.add_extension('./veevpn.crx')
        # options.add_argument('--remote-debugging-pipe')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)

        self.driver = driver

    def golinkpause(self, link):
        self.driver.get(link)
        time.sleep(MPAUSE)

    def checkisnumber(self, instr, mfrom =""):
        instr = instr.replace(' ', '')
        try:
            if (mfrom=="youtube") and (instr[-1]=="M"):
                instr=float(instr[:-1])*1000000
            if (mfrom=="youtube") and (instr[-1]=="K"):
                instr=float(instr[:-1])*1000
            c = int(instr)
            return c
        except Exception as ex:
            return MYNOTNUMBER

    # def findonpage(self, link, str):
    #     self.golinkpause(link)
    #     v0 = self.driver.find_elements(By.CLASS_NAME, "meta-item,style-scope,ytd-c4-tabbed-header-renderer")
    #     if str in self.driver.page_source:
    #         res = True
    #     else:
    #         res = False
    #     return res

    def getyandexday(self, link):
        self.golinkpause(link)

        # Yandex
        # Слушателей в месяц
        # document.getElementsByClassName("artist-trends__total-count")[0]
        # <span class=​"artist-trends__total-count">​173​</span>​
        #
        # Лайков за февраль
        # document.getElementsByClassName("artist-trends__total-count")[1]
        # <span class=​"artist-trends__total-count">​4​</span>​
        #
        # Всего лайков
        # document.getElementsByClassName("d-button__label")[1]
        # <span class="d-button__label">88</span>

        yhearsmonth = self.driver.find_elements(By.CLASS_NAME, "artist-trends__total-count")[0].text
        ylikesmonth = self.driver.find_elements(By.CLASS_NAME, "artist-trends__total-count")[1].text
        ylikesall = self.driver.find_elements(By.CLASS_NAME, "d-button__label")[0].text

        return self.checkisnumber(yhearsmonth), self.checkisnumber(ylikesmonth), self.checkisnumber(ylikesall)

    def getyoutubeday(self, link):

        # ВАРИАНТ ИЗ ГЛАВНОЙ СТРАНИЦЫ
        # document.getElementsByClassName("meta-item style-scope ytd-c4-tabbed-header-renderer")[
        #     3].getElementsByClassName("style-scope ytd-c4-tabbed-header-renderer")[0].text


        self.golinkpause(link)

        v00 = self.driver.find_elements(By.CLASS_NAME, "meta-item,style-scope,ytd-c4-tabbed-header-renderer")[4]

        v = v00.text.split()[0]

        # ВАРИАНТ2 ИЗ  СТРАНИЦЫ ABOUT
        # document.getElementsByClassName("description-item style-scope ytd-about-channel-renderer")[
        #     3].getElementsByClassName("style-scope ytd-about-channel-renderer")[2]

        # self.golinkpause(link+"/about")
        #
        #
        # v1 = self.driver.find_elements(By.CLASS_NAME,
        #                                 "description-item,style-scope,ytd-about-channel-renderer")[4]
        # v2 = v1.find_elements(By.CLASS_NAME,"style-scope,ytd-about-channel-renderer")[2]
        #
        #                                # v0="RAYVAN\n@rayvan\n\n\ 929 subsribesrs"
        # v = v1.text.split()[0]

        return self.checkisnumber(v,"youtube")


    def getspotifyday(self, link):
        # document.getElementsByClassName("meta-item style-scope ytd-c4-tabbed-header-renderer")[3]
        # < span class =​"meta-item style-scope ytd-c4-tabbed-header-renderer" > ​flex < yt-formatted-string id=​"subscriber-count" class =​"style-scope ytd-c4-tabbed-header-renderer" aria-label=​"929 subscribers" > ​929 subscribers​ < / yt-formatted-string > ​ < span aria-hidden=​"true" class =​"delimiter style-scope ytd-c4-tabbed-header-renderer" > ​‧​ < / span > ​ < / span > ​
        self.golinkpause(link)
        v0 = self.driver.find_elements(By.CLASS_NAME, "Ydwa1P5GkCggtLlSvphs")
        # v0="RAYVAN\n@rayvan\n\n\ 929 subsribesrs"
        v = v0[0].text.split()[0]
        return self.checkisnumber(v)

    def gettiktokday(self, link):
        # document.getElementsByClassName("css-mgke3u-DivNumber e1457k4r1")[1]
        # <div class=​"css-mgke3u-DivNumber e1457k4r1">​…​</div>​flex
        self.golinkpause(link)
        vs0 = self.driver.find_elements(By.CLASS_NAME, "css-mgke3u-DivNumber,e1457k4r1")[1]
        vs = vs0.text.split()[0]
        # document.getElementsByClassName("css-ntsum2-DivNumber e1457k4r1")[0]
        # < div # class =​"css-ntsum2-DivNumber e1457k4r1" > ​flex < strong title=​"Likes" data-e2e=​"likes-count" > ​8982​ < / strong > ​ < span data-e2e=​"likes" class =​"css-1pchix1-SpanUnit e1457k4r2" > ​Likes​ < / span > ​ < / div > ​
        vl0 = self.driver.find_elements(By.CLASS_NAME, "css-ntsum2-DivNumber,e1457k4r1")[0]
        vl = vl0.text.split()[0]
        return self.checkisnumber(vs), self.checkisnumber(vl)

    def gettlgday(self, link):
        # document.getElementsByClassName("tgme_page_extra")[0]
        # <div class=​"css-mgke3u-DivNumber e1457k4r1">​…​</div>​flex
        self.golinkpause(link)
        vs0 = self.driver.find_elements(By.CLASS_NAME, "tgme_page_extra")[0]
        vs = vs0.text.replace(" subscribers", "").replace(" ", "")
        return self.checkisnumber(vs)

    def getvkday(self, link):
        self.golinkpause(link)
        v = self.driver.find_elements(By.CLASS_NAME, "header_count,fl_l")[0].text
        return self.checkisnumber(v)

    def getsberday(self, link):
        self.golinkpause(link)
        v = self.driver.find_elements(By.CLASS_NAME,
                                      "Text__text---dbe71,Text__align-Left---18ad4,Text__variant-H4---d5b75,"
                                      "Text__gutter-None---012f4,Text__color-Primary---d90db,"
                                      "styles_counterCount__LatF7")[
            6].text
        return self.checkisnumber(v)

    def getvkstudio(self, link):
        self.golinkpause(link)
        # Клик на список где выводятся интервалы
        self.driver.find_elements(By.CLASS_NAME,
                                  "vkuiLink,Link-module__link--V7bkY,Select-module__link--ah62s,vkuiTappable,"
                                  "vkuiInternalTappable,vkuiTappable--hasActive,vkui-focus-visible")[
            0].click()
        time.sleep(MPAUSE)

        # Клик на пункт Сутки
        # document.getElementsByClassName("vkuiLink Link-module__link--V7bkY Select-module__link--ah62s vkuiTappable vkuiInternalTappable vkuiTappable--hasActive vkui-focus-visible")[0].click()
        self.driver.find_elements(By.CLASS_NAME,
                                  "vkuiActionSheetItem,vkuiActionSheetItem--sizeY-compact,vkuiActionSheetItem--menu,"
                                  "vkuiTappable,vkuiInternalTappable,vkuiTappable--hasHover,vkuiTappable--hasActive,"
                                  "vkui-focus-visible")[
            0].click()
        time.sleep(MPAUSE)

        # Клик дважды на сортировку по названию
        # document.getElementsByClassName("TracksTable-module__headerCellInnerSorting--WW4Tz")[0].click()
        self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__headerCellInnerSorting--WW4Tz")[0].click()
        time.sleep(MPAUSE)
        self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__headerCellInnerSorting--WW4Tz")[0].click()
        time.sleep(MPAUSE)

        # document.getElementsByClassName("TracksTable-module__row--nFfI0")
        mtab = self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__row--nFfI0")
        time.sleep(MPAUSE)

        return mtab

    def findonpage(self, link, str, ishere, iclass=""):
        # document.getElementsByClassName("meta-item style-scope ytd-c4-tabbed-header-renderer")[3]
        # < span class =​"meta-item style-scope ytd-c4-tabbed-header-renderer" > ​flex < yt-formatted-string id=​"subscriber-count" class =​"style-scope ytd-c4-tabbed-header-renderer" aria-label=​"929 subscribers" > ​929 subscribers​ < / yt-formatted-string > ​ < span aria-hidden=​"true" class =​"delimiter style-scope ytd-c4-tabbed-header-renderer" > ​‧​ < / span > ​ < / span > ​

        # self.golinkpause("https://pushkinmuseum.art/education/museyon/clubs/admission/index.php?lang=ru#start_with")
        # msource = self.driver.page_source
        # mtab = self.driver.find_elements(By.CLASS_NAME, "columns-2-section__inner__left")

        if ishere == "":
            ishere = False

        self.golinkpause(link)

        if ishere in ('0','1'):

            ishere = True if ishere == "1" else False

            msource = self.driver.page_source

            if ((str in msource) and (ishere == True)) or ((str not in msource) and (ishere == False)):
                res = True
            else:
                res = False

        elif ishere == '-1':
            try:
                res  = self.driver.find_elements(By.CLASS_NAME, iclass)[0].text
            except Exception as e:
                printsend(" ERR. Проверить контейнер " +iclass + "  в строке " + link, ERRORSTR)
                res = ""
        return res


    def getcitywalls(self, link):
        self.golinkpause(link)
        march=self.driver.find_elements(By.CLASS_NAME,"value")[0].text
        myear = self.driver.find_elements(By.CLASS_NAME, "value")[1].text
        mstyle=self.driver.find_elements(By.CLASS_NAME, "value")[2].text
        return march, myear, mstyle
