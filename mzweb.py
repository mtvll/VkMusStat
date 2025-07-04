import socket
import time
import urllib.request
import traceback

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from mfile import *

from mconst  import *

# import mzqllite

MPAUSE = 3


class cWebm(object):
    def __init__(self):
        # create chromeoptions instance
        options = webdriver.ChromeOptions()
        self.cmd_param = ""

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

        # options.add_argument('--headless')
        options.add_argument("--disable-extensions")
        options.add_experimental_option('extensionLoadTimeout', 60000)
        # options.add_argument('--remote-debugging-pipe')

        # from selenium.webdriver.chrome.service import Service
        # from selenium import webdriver
        #
        # service = Service(executable_path='./chromedriver.exe')
        # driver = webdriver.Chrome(service=service, options=options)



        # options.add_argument('--remote-debugging-pipe')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        #
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

    # def checkisnumber(self, instr):
    #     instr = instr.replace(' ', '')
    #     try:
    #         c = int(instr)
    #         return c
    #     except Exception as ex:
    #         return MYNOTNUMBER


    # def checkisnumber(instr, mfrom=""):
    #     instr = instr.replace(' ', '')
    #     try:
    #         if (mfrom == "youtube") and (instr[-1] == "M"):
    #             instr = float(instr[:-1]) * 1000000
    #         if (mfrom == "youtube") and (instr[-1] == "K"):
    #             instr = float(instr[:-1]) * 1000
    #         c = int(instr)
    #         return c
    #     except Exception as ex:
    #         return -999

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

        yhearsmonth_txt = self.driver.find_elements(By.XPATH, "//span[contains(text(), 'в месяц')]")[0].text
        yhearsmonth = re.search(r'\d+', yhearsmonth_txt).group()
        ylikesmonth = "-1"
        ylikesall = "-1"

        # 250401 Закомментил
        # yhearsmonth = self.driver.find_elements(By.CLASS_NAME, "artist-trends__total-count")[0].text
        # ylikesmonth = self.driver.find_elements(By.CLASS_NAME, "artist-trends__total-count")[1].text
        # ylikesall = self.driver.find_elements(By.CLASS_NAME, "d-button__label")[1].text

        print (yhearsmonth)
        return checkisnumberr(yhearsmonth), checkisnumberr(ylikesmonth), checkisnumberr(ylikesall)

    def getyoutubeday(self, link):
        # document.getElementsByClassName("description-item style-scope ytd-about-channel-renderer")[
        #     3].getElementsByClassName("style-scope ytd-about-channel-renderer")[2]
        # Странно что вместо
        # v0 = self.driver.find_elements(By.CLASS_NAME,
        #                                "description-item,style-scope,ytd-about-channel-renderer")[3].find_elements(By.CLASS_NAME,"style-scope,ytd-about-channel-renderer")[2]
        # сработало
        # v0 = self.driver.find_elements(By.CLASS_NAME,
        #                                 "description-item,style-scope,ytd-about-channel-renderer")[4]

        self.golinkpause(link + "/about")
        time.sleep(MPAUSE)
        v1 = self.driver.find_elements(By.CLASS_NAME,
                                       "description-item,style-scope,ytd-about-channel-renderer")[4]
        # v2 = v1.find_elements(By.CLASS_NAME,"style-scope,ytd-about-channel-renderer")[2].text
        # Заменил 240807 на
        # v3 = v1.find_elements(By.CLASS_NAME, "style-scope,ytd-about-channel-renderer")[3].text
        maxx = len(v1.find_elements(By.CLASS_NAME, "style-scope,ytd-about-channel-renderer"))
        v3 = v1.find_elements(By.CLASS_NAME, "style-scope,ytd-about-channel-renderer")[maxx - 1].text
        # print("v2  " + v2)
        # print("v3  " + v3)

        # v0="RAYVAN\n@rayvan\n\n\ 929 subsribesrs"
        v = v3.split()[0]

        return checkisnumberr(v, "youtube")

    def getspotifyday(self, link):
        # document.getElementsByClassName("meta-item style-scope ytd-c4-tabbed-header-renderer")[3] < span class
        # =​"meta-item style-scope ytd-c4-tabbed-header-renderer" > ​flex < yt-formatted-string
        # id=​"subscriber-count" class =​"style-scope ytd-c4-tabbed-header-renderer" aria-label=​"929 subscribers" >
        # ​929 subscribers​ < / yt-formatted-string > ​ < span aria-hidden=​"true" class =​"delimiter style-scope
        # ytd-c4-tabbed-header-renderer" > ​‧​ < / span > ​ < / span > ​
        self.golinkpause(link)
        v0 = self.driver.find_elements(By.CLASS_NAME, "Ydwa1P5GkCggtLlSvphs")
        # v0="RAYVAN\n@rayvan\n\n\ 929 subsribesrs"
        v = v0[0].text.split()[0]
        return checkisnumberr(v)

    def gettlgday(self, link):
        # document.getElementsByClassName("tgme_page_extra")[0]
        # <div class=​"css-mgke3u-DivNumber e1457k4r1">​…​</div>​flex
        self.golinkpause(link)
        vs0 = self.driver.find_elements(By.CLASS_NAME, "tgme_page_extra")[0]
        vs = vs0.text.replace(" subscribers", "").replace(" ", "")
        return checkisnumberr(vs)

    def gettiktokday(self, link):
        # document.getElementsByClassName("css-mgke3u-DivNumber e1457k4r1")[1]
        # <div class=​"css-mgke3u-DivNumber e1457k4r1">​…​</div>​flex
        self.golinkpause(link)

        # 241244 Раздел ниже vs0 раскомментил, тк старый глючил
        vs0 = self.driver.find_elements(By.CLASS_NAME, "css-mgke3u-DivNumber,e1457k4r1")[1]
        vs = vs0.text.split()[0]

        vl0 = self.driver.find_elements(By.CLASS_NAME, "css-1ou6a1c-DivNumber,e1457k4r1")[0]
        vl = vl0.text.split()[0]

        # 241244 Раздел закоментил одновременно с верхним
        # s=self.driver.find_element(By.XPATH,"//meta[@name='description']").get_attribute("content")
        #
        # vl=s[s.index("TikTok |") + len("TikTok |"):s.index("Likes.")]
        # vs = s[s.index("Likes.") + len("Likes."):s.index("Followers")]

        # 240914 Раздел закомментил
        # vs0 = self.driver.find_elements(By.CLASS_NAME, "css-mgke3u-DivNumber,e1457k4r1")[1]
        # vs = vs0.text.split()[0]
        # # document.getElementsByClassName("css-ntsum2-DivNumber e1457k4r1")[0] < div # class =​"css-ntsum2-DivNumber
        # # e1457k4r1" > ​flex < strong title=​"Likes" data-e2e=​"likes-count" > ​8982​ < / strong > ​ < span
        # # data-e2e=​"likes" class =​"css-1pchix1-SpanUnit e1457k4r2" > ​Likes​ < / span > ​ < / div > ​
        #
        # # Заменил  240807 на ниже
        # # vl0 = self.driver.find_elements(By.CLASS_NAME, "css-ntsum2-DivNumber,e1457k4r1")[0]
        # # vl0 = self.driver.find_elements(By.CLASS_NAME, "css-mgke3u-DivNumber,e1457k4r1")[2]
        # # Заменил  2408018 на ниже
        # vl0 = self.driver.find_elements(By.CLASS_NAME, "css-1ou6a1c-DivNumber,e1457k4r1")[0]
        # vl = vl0.text.split()[0]
        return checkisnumberr(vs), checkisnumberr(vl)

    def getvkday(self, link):
        self.golinkpause(link)
        v = self.driver.find_elements(By.CLASS_NAME, "header_count,fl_l")[0].text
        return checkisnumberr(v)

    def getsberday(self, link):

        self.golinkpause(link)

        # 240901
        # v = self.driver.find_elements(By.CLASS_NAME,
        #                               "Text__text---dbe71,Text__align-Left---18ad4,Text__variant-H4---d5b75,"
        #                               "Text__gutter-None---012f4,Text__color-Primary---d90db,"
        #                               "styles_counterCount__LatF7")[
        #     6].text
        # ss = self.driver.find_elements(By.CLASS_NAME,
        #                           "Text_text__7_imM,Text_alignLeft__I9hpQ,Text_variantBodyS__2eN0i,Text_gutterNone__q_Sqi Text_colorWhite50__0U80B,Text_medium__TmC_D")
        # for i in range(len(ss)):
        #     print (str(i)+ss[i].text)
        v = self.driver.find_elements(By.CLASS_NAME,
                                      "Text_text__7_imM,Text_alignLeft__I9hpQ,Text_variantBodyS__2eN0i,Text_gutterNone__q_Sqi Text_colorWhite50__0U80B,Text_medium__TmC_D")[
            14].text

        v=v[:v.find(" ")]

        return checkisnumberr(v)

    # def getvkstudio(self, link):
    #     self.golinkpause(link)
    #     time.sleep(MPAUSE * 3)
    #     # Клик на список где выводятся интервалы
    #     # el_periods_list=self.driver.find_elements(By.CLASS_NAME,
    #     #                           "vkuiLink,Link-module__link--V7bkY,Select-module__link--ah62s,vkuiTappable,"
    #     #                           "vkuiInternalTappable,vkuiTappable--hasActive,vkui-focus-visible")
    #
    #     el_periods_list=self.driver.find_elements(By.CLASS_NAME,
    #                               "vkitLink__link--WXYoI,Select__link--UQ7MF,vkitLink__withIconInChildren--MOP1u,vkuiInternalTappable,vkuiLink__host,vkuiLink__withUnderline,vkuiTappable__host vkuiTappable__hasPointerNone,"
    #                               "vkuiClickable__host,vkuiClickable__realClickable,vkuistyles__-focus-visible,vkuiRootComponent__host")
    #     if len(el_periods_list)==0:
    #         printsend("ERROR in VK proc. el_periods_list.  Second iteration ", "VkWeb")
    #     el_periods_list[0].click()
    #     time.sleep(MPAUSE*2)
    #
    #     # Клик на пункт Сутки document.getElementsByClassName("vkuiLink Link-module__link--V7bkY
    #     # Select-module__link--ah62s vkuiTappable vkuiInternalTappable vkuiTappable--hasActive vkui-focus-visible")[
    #     # 0].click()
    #     # el_periods_24=self.driver.find_elements(By.CLASS_NAME,
    #     #                           "vkuiActionSheetItem,vkuiActionSheetItem--sizeY-compact,vkuiActionSheetItem--menu,"
    #     #                           "vkuiTappable,vkuiInternalTappable,vkuiTappable--hasHover,vkuiTappable--hasActive,"
    #     #                           "vkui-focus-visible")
    #     el_periods_24=self.driver.find_elements(By.CLASS_NAME,"vkuiActionSheetItem__children,vkuiText__host,"
    #                                                           "vkuiText__sizeYCompact,vkuiTypography__host,vkuiTypography__normalize,vkuiRootComponent__host")
    #
    #     if len(el_periods_24) == 0:
    #         printsend("ERROR in VK proc. el_periods_24.  Second iteration ", "VkWeb")
    #     el_periods_24[0].click()
    #     time.sleep(MPAUSE*2)
    #
    #     # Клик дважды на сортировку по названию
    #     # document.getElementsByClassName("TracksTable-module__headerCellInnerSorting--WW4Tz")[0].click()
    #     # заменил 241010 self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__headerCellInnerSorting--WW4Tz")[0].click()
    #     # заменил 241011 self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__headerCellInnerSorting--S6PJq")[0].click()
    #     el_hearsnumbers=self.driver.find_elements(By.CLASS_NAME, "TracksTable__headerCellInnerSorting--GOKyi")
    #     if len(el_hearsnumbers)==0:
    #         printsend("ERROR in VK proc. el_hearsnumbers.  Second iteration ", "VkWeb")
    #     el_hearsnumbers[0].click()
    #
    #
    #     time.sleep(MPAUSE*2)
    #     el_hearsnumbers[0].click()
    #     time.sleep(MPAUSE*2)
    #
    #     # document.getElementsByClassName("TracksTable-module__row--nFfI0")
    #     # заменил 241010 mtab = self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__row--nFfI0")
    #     # заменил 241110 mtab = self.driver.find_elements(By.CLASS_NAME, "TracksTable-module__row--e3vmp")
    #     mtab = self.driver.find_elements(By.CLASS_NAME, "TracksTable__row--KhG2m,TracksTable__rowAlbum--kasmQ")
    #     if len(mtab) == 0:
    #         printsend("ERROR in VK proc. mtab.  Second iteration ", "VkWeb")
    #
    #     time.sleep(MPAUSE)
    #
    #     return mtab
    def getvkstudio(self, link):
        self.golinkpause(link)
        time.sleep(MPAUSE * 3)

        # Поиск и клик по списку интервалов
        # el_periods_list = self.driver.find_elements(By.CLASS_NAME, "vkitLink__link--WXYoI")
        # el_periods_list = self.driver.find_elements(By.CLASS_NAME, "Select__root--oZRjh")

        # 1. Клик на выпадающий список периодов (исправленный селектор)
        el_periods_list = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div[class*='Select__link']"  # Более надежный селектор
        )

        if not el_periods_list:
            printsend("ERROR: Period dropdown not found. Trying fallback selector...", "VkWeb")
            # Попытка альтернативного селектора
            el_periods_list = self.driver.find_elements(
                By.CSS_SELECTOR,
                "div.vkuiLink.vkuiLink--withUnderline"
            )
            if not el_periods_list:
                printsend("ERROR: Fallback selector also failed", "VkWeb")
                return []

        el_periods_list[0].click()
        time.sleep(MPAUSE * 2)

        # 2. Клик на пункт "7 дней" (улучшенный селектор)
        el_periods_7days = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.vkuiActionSheetItem > div.vkuiActionSheetItem__children"
        )

        if not el_periods_7days:
            printsend("ERROR: 7 days option not found", "VkWeb")
            return []

        el_periods_7days[0].click()
        time.sleep(MPAUSE * 2)

        # 3. Сортировка по прослушиваниям (надежный селектор)
        el_listeners_sort = self.driver.find_elements(
            By.CSS_SELECTOR,
            "div.TracksTable__headerCellSorting--PUF58"
        )

        if not el_listeners_sort:
            printsend("ERROR: Sort header not found", "VkWeb")
            return []

        el_listeners_sort[0].click()
        time.sleep(MPAUSE * 2)
        el_listeners_sort[0].click()
        time.sleep(MPAUSE * 2)

        # 4. Получение списка треков (универсальный селектор)
        mtab = self.driver.find_elements(
            By.CSS_SELECTOR,
            "a[class*='TracksTable__row']"
        )

        if not mtab:
            printsend("ERROR: No tracks found", "VkWeb")
            return []

        time.sleep(MPAUSE)


        el_periods_list = self.driver.find_elements(
            By.CLASS_NAME,
            "vkitLink__link--WXYoI,Select__link--UQ7MF,vkitLink__withIconInChildren--MOP1u,"
            "vkuiInternalTappable,vkuiLink__host,vkuiLink__withUnderline,vkuiTappable__host,"
            "vkuiTappable__hasPointerNone,vkuiClickable__host,vkuiClickable__realClickable,"
            "vkuistyles__-focus-visible,vkuiRootComponent__host"
        )

        if len(el_periods_list) == 0:
            printsend("ERROR in VK proc. el_periods_list. Second iteration", "VkWeb")
            return None
        el_periods_list[0].click()
        time.sleep(MPAUSE * 2)

        # Поиск и клик по пункту 'Сутки'
        el_periods_24 = self.driver.find_elements(By.CLASS_NAME, "vkuiActionSheetItem__children")
        if len(el_periods_24) == 0:
            printsend("ERROR in VK proc. el_periods_24. Second iteration", "VkWeb")
            return None
        el_periods_24[0].click()
        time.sleep(MPAUSE * 2)

        # Двойной клик по сортировке по названию
        el_hearsnumbers = self.driver.find_elements(By.CLASS_NAME, "TracksTable__headerCellInnerSorting--GOKyi")
        if len(el_hearsnumbers) == 0:
            printsend("ERROR in VK proc. el_hearsnumbers. Second iteration", "VkWeb")
            return None
        el_hearsnumbers[0].click()
        time.sleep(MPAUSE * 2)
        el_hearsnumbers[0].click()
        time.sleep(MPAUSE * 2)

        # Поиск строк таблицы
        mtab = self.driver.find_elements(By.CLASS_NAME, "TracksTable__row--KhG2m")
        if len(mtab) == 0:
            printsend("ERROR in VK proc. mtab. Second iteration", "VkWeb")
            return None

        time.sleep(MPAUSE)
        return mtab

    def findonpage(self, link, mstr, ishere, iclass=""):
        # document.getElementsByClassName("meta-item style-scope ytd-c4-tabbed-header-renderer")[3] < span class
        # =​"meta-item style-scope ytd-c4-tabbed-header-renderer" > ​flex < yt-formatted-string
        # id=​"subscriber-count" class =​"style-scope ytd-c4-tabbed-header-renderer" aria-label=​"929 subscribers" >
        # ​929 subscribers​ < / yt-formatted-string > ​ < span aria-hidden=​"true" class =​"delimiter style-scope
        # ytd-c4-tabbed-header-renderer" > ​‧​ < / span > ​ < / span > ​

        # self.golinkpause("https://pushkinmuseum.art/education/museyon/clubs/admission/index.php?lang=ru#start_with")
        # msource = self.driver.page_source
        # mtab = self.driver.find_elements(By.CLASS_NAME, "columns-2-section__inner__left")

        if ishere == "":
            ishere = False

        self.golinkpause(link)

        if ishere in ('0', '1'):

            ishere = True if ishere == "1" else False

            msource = self.driver.page_source

            if ((mstr in msource) and (ishere is True)) or ((mstr not in msource) and (ishere is False)):
                res = True
            else:
                res = False

        elif ishere == '-1':
            try:
                res = self.driver.find_elements(By.CLASS_NAME, iclass)[0].text
                if ("band.link" in link):
                    res=False
            except Exception as e:
                if ("band.link" in link):
                    res=True
                else:
                    printsend(" ERR. Проверить контейнер " + iclass + "  в строке " + link, ERRORSTR)
                    res = ""

        elif ishere == '-2':
            try:
                res = self.driver.find_elements(By.CLASS_NAME, iclass)
                for i in range(len(res)):
                    if res[i].text != "" and "запись закреплена" not in res[i].text:
                        mstr = self.driver.find_elements(By.CLASS_NAME, "wall_posts,own,mark_top")[i].text.split("\n")[
                               :4]
                        cc = self.driver.find_elements(By.CLASS_NAME, iclass)
                        cc[0].find_elements(By.CLASS_NAME,
                                                  "PostBottomAction,PostBottomAction--withBg,PostButtonReactions,"
                                                  "PostButtonReactions--post")
                        # document.getElementsByClassName( "_post post page_block all own post--withPostBottomAction
                        # post_with_ads_button post--with-likes deep_active Post--redesign")[
                        # 0].getElementsByClassName( "PostBottomAction PostBottomAction--withBg PostButtonReactions
                        # PostButtonReactions--post") [0].click()

                        res = ' '.join(mstr)
                        break
            except Exception as e:
                printsend(" ERR. Проверить контейнер " + iclass + "  в строке " + link, ERRORSTR)
                res = ""

        return res

    def findonpageandclick(self, link, mstr, ishere, iclass, ilast):

        if ishere == "":
            ishere = False

        self.golinkpause(link)

        try:
            res = self.driver.find_elements(By.CLASS_NAME, iclass)
            for i in range(len(res)):
                if res[i].text != "" and "запись закреплена" not in res[i].text:
                    # mstr = self.driver.find_elements(By.CLASS_NAME, "wall_posts,own,mark_top")[i].text.split("\n")[2]
                    # res = ' '.join(mstr)
                    res = self.driver.find_elements(By.CLASS_NAME, "wall_post_text")[i].text
                    res = res.replace('\n', '_')

                    if res != ilast:
                        cc = self.driver.find_elements(By.CLASS_NAME, iclass)
                        cc[i].find_elements(By.CLASS_NAME,
                                                  "PostBottomAction,PostBottomAction--withBg,PostButtonReactions,"
                                                  "PostButtonReactions--post")[
                            0].click()
                        print("!!! INF: New post in {l} contain {s}".format(l=link,s=res))
                    print2file("LOG: New post in {l} contain {s} and old contains {s2}".format(l=link,s=res,s2=ilast))
                    break
        except Exception as e:
            # printsend(" ERR. Проверить контейнер " + iclass + "  в строке " + link, ERRORSTR)
            res = ""

        return res

    def getcitywalls(self, link):
        self.golinkpause(link)

        march = self.driver.find_elements(By.CLASS_NAME, "value")[0].text
        myear = self.driver.find_elements(By.CLASS_NAME, "value")[1].text
        mstyle = self.driver.find_elements(By.CLASS_NAME, "value")[2].text
        return march, myear, mstyle

    def getcitywalls2getstreet(self, link):

        try:
            self.golinkpause(link)

            # если звухзначное число то в строке присутствует ...
            mnpages=self.driver.find_elements(By.CLASS_NAME, "cssPager")
            if len(mnpages)>0:
                npages = self.driver.find_elements(By.CLASS_NAME, "cssPager")[0].text
                maxstr = npages[-3:-1] if "···" in npages else npages[-2:-1]
            else:
                maxstr='1'

            mname = self.driver.find_elements(By.CLASS_NAME, "title")[0].text
            mpages = maxstr

            mlist = []

            for i in range(int(maxstr)):

                if i > 0:
                    mlink = link.split(".html", 1)[0] + "-page" + str(i + 1) + ".html"
                    self.golinkpause(mlink)

                houselist = self.driver.find_elements(By.CLASS_NAME, "photo")

                # self.driver.find_elements(By.CLASS_NAME, "photo")[0].find_elements(By.TAG_NAME, "a")[0].get_attribute(
                # "href")

                for ii in range(len(houselist)):
                    thouse = houselist[ii].find_elements(By.TAG_NAME, "a")[0].get_attribute("href")

                    mhouse=(thouse[:thouse.find('html') + 4])

                    mlist.append(mhouse)

            print2file(mname + "  Pages: " + mpages + "  Houses: " + str(len(mlist)))



            return mlist

        except Exception:
            stack = traceback.extract_stack()
            printsend('ERROR IN FUNC {}'.format(stack[-1][2]) + " | PREV {}".format(stack[-2][2]), ERRORSTR)

    def getcitywalls2gethouse(self, link):

        try:

            self.golinkpause(link)

            md = {}

            md["name"] = self.driver.find_elements(By.XPATH, '//h1')[0].text

            marchit = self.driver.find_elements(By.CLASS_NAME, "value")[0].text.split("\n")
            md["arch1"] = marchit[0] if len(marchit) > 0 else ""
            md["arch2"] = marchit[1] if len(marchit) > 1 else ""
            md["arch3"] = marchit[2] if len(marchit) > 2 else ""
            md["arch4"] = marchit[3] if len(marchit) > 3 else ""

            md["year"] = self.driver.find_elements(By.CLASS_NAME, "value")[1].text
            md["style"] = self.driver.find_elements(By.CLASS_NAME, "value")[2].text

            maddr = self.driver.find_elements(By.CLASS_NAME, "address")[0].text.split("\n")
            if "," not in maddr[0]:
                md["city"] = maddr[0]
                istart = 1
            else:
                md["city"] = "Санкт - Петербург"
                istart = 0
            md["maddr1"] = maddr[istart] if len(maddr) > 0 else ""
            md["maddr2"] = maddr[istart + 1] if len(maddr) > istart + 1 else ""
            md["maddr3"] = maddr[istart + 2] if len(maddr) > istart + 2 else ""
            md["maddr4"] = maddr[istart + 3] if len(maddr) > istart + 3 else ""
            # addr1n # addr1h # addr1l

            if (len(self.driver.find_elements(By.CLASS_NAME, "mceContentBody")))>0:
                mstat = "/n".join(
                    self.driver.find_elements(By.CLASS_NAME, "mceContentBody")[0].text.split("\n")[:3]).lower()
            else:
                print("INFOOOOOO:::: Пустой контент")
                mstat=''
            if "пам" in mstat and "арх" in mstat in mstat:
                md["status"] = "пам архитектуры"
            if "пам" in mstat and "арх" in mstat and "регион" in mstat:
                md["status"] = "пам архитектуры (рег)"
            if "утрачен" in mstat:
                md["status"] = "утраченное"
            else:
                md["status"] = ""


            # 240714 закомментил так как был текст а лучше html
            # mnote = self.driver.find_elements(By.CLASS_NAME, "mceContentBody")
            # # mpage = "/n".join(mnote[:len(mnote)].text)
            # mpage = ""
            # for i in range(len(mnote)):
            #     mpage = mpage + mnote[i].text + "\n" + "-----------------------" + "\n"
            # md["note"] = mpage

            md["note"]=self.driver.find_elements(By.XPATH, "//div[@style='padding: 16px 0 5px 0']")[0].get_attribute('innerHTML')

            # print(md["note"])

            img = self.driver.find_elements(By.CLASS_NAME, "photo")[0].find_elements(By.TAG_NAME, "img")[
                0].get_attribute(
                "src")


            md["photo_small_link"]=img

            md["photo_small"]=sqlite3.Binary(img2blob(img))

            # img = self.driver.find_elements(By.CLASS_NAME, "photo")[0].find_elements(By.TAG_NAME, "img")[
            #     0].get_attribute(
            #     "src")
            #
            # mfilename = "getcitywalls2_tmp.jpg"
            # mfile = urllib.request.urlretrieve(img, mfilename)
            # blobdata = open(mfilename, 'rb').read()
            # md["mainphoto"] = sqlite3.Binary(blobdata)




        except Exception:
            stack = traceback.extract_stack()
            printsend('ERROR IN FUNC {}'.format(stack[-1][2]) + " | PREV {} |СITY".format(stack[-2][2]), ERRORSTR)

        try:

            self.driver.find_elements(By.CLASS_NAME, "photo")[0].click()
            # 241116 ПАУЗА ЕСЛИ ОШИБКА В ОБРАБОТКЕ ВНУТРЕННИХ ФОТО
            time.sleep(MPAUSE)

            mpointlink = self.driver.find_elements(By.CLASS_NAME, "staticmap")[0].find_elements(By.TAG_NAME, "img")[
                0].get_attribute("src")
            md["longitude"] = mpointlink.split("ll=", 1)[1].split(",", 1)[0]
            md["latitude"] = mpointlink.split("ll=", 1)[1].split(",", 1)[1].split("&", 1)[0]

            md["photo_link"]=""

            if "absent" not in  md["photo_small_link"]:
                img = self.driver.find_elements(By.CLASS_NAME, "photowrap")[0].find_elements(By.TAG_NAME, "img")[
                    0].get_attribute(
                    "src")
                md["photo_link"]=img
                md["photocomment"] =self.driver.find_elements(By.CLASS_NAME, "info")[1].find_elements(By.CLASS_NAME, "title")[0].text
            else:
                md["photo_link"] = md["photocomment"] = ""

            # 240730 Убрал загрузку больших фото
            md["photo"] = None
            # md["photo"]=sqlite3.Binary(img2blob(img))

            md["link"] = link

            return md

        except Exception:
            stack = traceback.extract_stack()
            # printsend('ERROR IN FUNC {}'.format(stack[-1][2]) + " | PREV {} |СITY".format(stack[-2][2]), ERRORSTR)
            printsend('\nERROR IN FUNC with LINK: ' +link+"\n", ERRORSTR)
            pass
