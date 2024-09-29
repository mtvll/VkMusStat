import mconst
from mzqllite import *
# from mfile import *
# from mmail import *
from mzweb import *
from moss import *
from mconst import *

MTITLE = "MUZSTAT"


def main():

    param1=""

    if (len(sys.argv) > 1):
        param1 = sys.argv[1]

    status_prod= True  if TXTPRODUCTIVE in param1 else False

    dontwrite2base = True if TXTDONTWRITE2BASE in param1  else False

    try:

        write_file(MTITLE + " Start " + MVERSION)

        kill_chrome(status_prod)

        db = cDb()

        # db.dbchk2table()

        # db.initstring()

        # mcol_names, mconnection=dbinitialize()

        # mSt=StatString(mcol_names)
        web = cWebm()

        web.cmd_param=param1

        # Отдельная программа - в будущем. Пока отладка в mains.py добавлеение строки в таблицу поиск на странице
        # название - ссылка  - какчастопроверять  1-7 - текст - нуженли прокси - последняя проверка дата - поле1 (
        # необ) Если false  то почта (с другм сообщением) навзание, ссылка лог на странице ... название - ссылка  - -
        # какчастопроверять  1-7 - текст = 0 - нуженли прокси - последняя проверка дата - поле1 об - значение 1,
        # 10 Если изменения то почта  (с другм сообщением) навзание, ссылка, как было - как стало

        # a=web.findonpage("https://band.link/scanner?search=%D0%9C%D1%8F%D1%81%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2","ничего не найдено")
        # a=web.findonpage("https://band.link/scanner?search=Rayvan","ничего не найдено")

        # a=web2.findonpage("https://flibusta.is/booksearch?ask=нагибин","ничего не найдено")
        # a=web2.findonpage("https://flibusta.is/booksearch?ask=оплетаев","не найдено")
        # a=web2.findonpage("https://flibusta.site/booksearch?ask=%D0%BE%D0%BF%D0%BB%D0%B5%D1%82%D0%B0%D0%B5%D0%B2","не найдено")

        # mdriver = chromeinitilize()

        for i in db.art:
            try:
                if (i.vkstudio != "" and not ("NOVKSTUDIO"  in web.cmd_param)):
                    mlink = "https://vk.com/studio#/artist/" + i.vkstudio + "/music/tracks"
                    tracks = web.getvkstudio(mlink)
                    db.vktracks2db(tracks, i.name)
                else:
                    db._dayhearsvk = db._dayaddsvk = db._dayeffvk = db._hears_best_n = db._eff_best_n =0
                    db._eff_best_song = db._hears_best_song = ""
            except Exception as ex:
                if (i.run_after_error==False):
                    db.art.append(Artist(i.name, i.vkstudio, "", "", "",
                       "","","",
                       "", "",minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":VKSTUDIO : {iteration}".format(iteration="Second iteration " if i.run_after_error else "") + i.vkstudio + "___" + str(ex), MTITLE + ERRORSTR)
                pass

            db.initstring(i.name)

            # Spotify требует ввода из России
            # try:
            #     if i.spot != "":
            #         mlink = "https://open.spotify.com/artist/" + i.spot
            #         db.columns["hears_month_spot"] = web.getspotifyday(mlink)
            # except:
            #     printsend(ERRORSTR +"  " + i.name + ":SPOTIFY : " +i.yandex)
            #     pass

            try:
                if i.yandex != "" and not ("NOYANDEX"  in web.cmd_param):
                    mlink = "https://music.yandex.ru/artist/" + i.yandex + "/info"
                    db.columns["hears_month_ynd"], db.columns["likes_month_ynd"], db.columns[
                        "likes_all_ynd"] = web.getyandexday(mlink)
            except Exception as ex:
                if (i.run_after_error == False):
                    db.art.append(Artist(i.name, "", "", i.yandex, "",
                                         "", "", "",
                                         "", "", minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":YANDExMuz : {iteration}".format(
                    iteration="Second iteration " if i.run_after_error else "") + i.yandex + "___" + str(ex),
                          MTITLE + ERRORSTR)
                # printsend("  " + i.name + ":YANDEX : " + i.yandex+ "___"+ str(ex), MTITLE + ERRORSTR)
                pass

            try:
                if i.sber != "" and not ("NOSBER"  in web.cmd_param):
                    mlink = "https://zvuk.com/artist/" + i.sber
                    db.columns["sub_sber"] = web.getsberday(mlink)
            except Exception as ex:
                if (i.run_after_error == False):
                    db.art.append(Artist(i.name, "", "", "", i.sber,
                                         "", "", "",
                                         "", "", minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":Sber : {iteration}".format(
                    iteration="Second iteration " if i.run_after_error else "") + i.sber + "___" + str(ex),
                          MTITLE + ERRORSTR)
                # printsend("  " + i.name + ":SBER : " + i.sber+ "___"+ str(ex), MTITLE + ERRORSTR)
                pass

            try:
                if i.vk != ""and not ("NOVKSUB"  in web.cmd_param):
                    mlink = "https://vk.com/" + i.vk
                    db.columns["sub_vk"] = web.getvkday(mlink)
            except Exception as ex:
                if (i.run_after_error == False):
                    db.art.append(Artist(i.name, "", "", "", "",
                                         "", i.vk, "",
                                         "", "", minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":VkSub : {iteration}".format(
                    iteration="Second iteration " if i.run_after_error else "") + i.vk + "___" + str(ex),
                          MTITLE + ERRORSTR)
                # printsend("  " + i.name + ":VK : " + i.vk+ "___"+ str(ex), MTITLE + ERRORSTR)
                pass

            try:
                if i.youtube != "" and not ("NOYOUTUBE"  in web.cmd_param):
                    mlink = "https://www.youtube.com/channel/" + i.youtube
                    db.columns["sub_youtube"] = web.getyoutubeday(mlink)
            except Exception as ex:
                if (i.run_after_error == False):
                    db.art.append(Artist(i.name, "", "", "", "",
                                         i.youtube, "", "",
                                         "", "", minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":Youtube : {iteration}".format(
                    iteration="Second iteration " if i.run_after_error else "") + i.youtube + "___" + str(ex),
                          MTITLE + ERRORSTR)
                # printsend("  " + i.name + ":YOUTUBE : " + i.youtube+ "___"+ str(ex), MTITLE + ERRORSTR)
                pass

            try:
                if i.tiktok != ""and not ("NOTIKTOK"  in web.cmd_param):
                    mlink = "https://www.tiktok.com/" + i.tiktok
                    db.columns["sub_tiktok"], db.columns["likes_tiktok"] = web.gettiktokday(mlink)
            except Exception as ex:
                if (i.run_after_error == False):
                    db.art.append(Artist(i.name, "", "", "", "",
                                         "", "", i.tiktok,
                                         "", "", minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":TikTok  : {iteration}".format(
                    iteration="Second iteration " if i.run_after_error else "") + i.tiktok + "___" + str(ex),
                          MTITLE + ERRORSTR)
                # printsend("  " + i.name + ":TIKTOK : " + i.tiktok+ "___"+ str(ex), MTITLE + ERRORSTR)
                pass

            try:
                if i.tlg != "" and not ("NOTLG"  in web.cmd_param):
                    mlink = "https://t.me/" + i.tlg
                    db.columns["sub_tlg"] = web.gettlgday(mlink)
            except Exception as ex:
                if (i.run_after_error == False):
                    db.art.append(Artist(i.name, "", "", "", "",
                                         "", "", "",
                                         i.tlg, "", minhears=i.minhears, run_after_error=True))
                printsend("  " + i.name + ":Teleg : {iteration}".format(
                    iteration="Second iteration " if i.run_after_error else "") + i.tlg + "___" + str(ex),
                          MTITLE + ERRORSTR)
                # printsend("  " + i.name + ":TIKTOK : " + i.tiktok+ "___"+ str(ex), MTITLE + ERRORSTR)
                pass


            # # mlink = "https://open.spotify.com/artist/" + i.spot
            # # SpotifyGetDaylyStatArtist(mdriver, mconnection, mlink, i.name)

            if dontwrite2base == False:
                db.day2db()

            write_file(MTITLE + " " + i.name + "  DONE")

        db.closeconnection()
        write_file(MTITLE + " End")

    except Exception as ex:
        # e = json.loads(ex.text)
        # response.status = e['payload']['message']
        printsend(ex.msg, MTITLE + ERRORSTR)
        # write_file("MUZZTAT: ERR " + ex.msg)
        # send_mail("MUZZTAT: ERR", ex.msg)


if __name__ == "__main__":
    main()
