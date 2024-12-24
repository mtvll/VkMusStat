from mzqllite import *
# from mfile import *
# from mmail import *
from mzweb import *
from moss import *

import maincompare

MTITLE = "MUZCHEK"


def main():
    """

    """
    param1 = sys.argv[1] if (len(sys.argv) > 1) else ""

    status_prod = True if TXTPRODUCTIVE in param1 else False

    myfreqhours= True  if "FREQHOURS" in param1 else False

    TestMode1Progon = True if "TESTMODE" in param1 else False

    try:
        write_file(MTITLE + " Start " + MVERSION)

        kill_chrome(status_prod)

        db = cDb()

        web = cWebm()

        # Ограничение по имени строки
        # db.dbchk2table("monVk")

        db.dbchk2table("",myfreqhours)


        # добавлеение строки в таблицу
        # Проверка раз в 6 часов
        # Таблица1. название - ссылка  - какчастопроверять  1-7 дней или 0.25 - раз в 76 часов
        # Таблица2. текст (для проверки) - поле (для проверки) нееоб
        # Таблица3. нужен ли прокси- последняя проверка дата - послдн значение

        mstr = ""

        # db.arr=db.arr[:3]

        for i in db.arr:
            try:
                if i.needproxy != str(int(True)):
                    # Простая проверка
                    if i.ishere in ('0','1'):
                        res = web.findonpage(i.mlink, i.mstr, i.ishere, i.mstrfield)
                        mres = str((int(res)))
                        mres2tst=mres
                    # Проверка лайков и лайки
                    if i.ishere == '-2':
                        res = web.findonpageandclick(i.mlink, i.mstr, i.ishere, i.mstrfield,i.lastval)
                        if isinstance(res, list) and len(res)>=1:
                            res=res[0].text
                            print("ПРОверка последнего поста дала list. Выделено значение:" + encodeifUnicodeErr(res))
                        mres = res
                        mres2tst = res
                        i.lastval = res
                    # Проверка конкретных полей в данных
                    if i.ishere == '-1':
                        res = web.findonpage(i.mlink, i.mstr, i.ishere, i.mstrfield)
                        mres = res
                        t1=str(mres).splitlines(keepends=True)
                        t2=str(i.lastval).splitlines(keepends=True)
                        if "band.link" in i.mlink:
                            mres2tst=str(mres)
                        else:
                            mres2tst = ''.join(difflib.context_diff(t1, t2))
                    if res==True:
                        res=mres='1'
                    if res==False:
                        res=mres='0'
                    # Монитоерить всегда для важных плейлистов (а не только переходы да-нет_
                    if res=='1' and i.alwaysshow>0:
                        mstr = mstr + "GOOD STATUS " + i.mname + " Status:" + str(
                            mres2tst) + " Link:" + i.mlink + "\n"
                    # Изменения для неважных (убрал лайки =-2)
                    if (mres != i.lastval) and i.ishere != '-2':
                        mstr = mstr+ "CHANGE STATUS " + i.mname + " NewStatus:" + str(mres2tst) + " Link:" + i.mlink +"\n"
                        i.lastval = res
                    db.update_dbchk_row(i)
                if TestMode1Progon:
                    print("Тестовый прогон (1 итерация) окончен")
                    break
            except Exception as e:
                printsend(" CHK " + i.mname + "  Message" + e.msg, MTITLE + ERRORSTR)
                continue

        printsend(mstr,MTITLE)

        db.closeconnection()
        write_file(MTITLE + " End")

        if not myfreqhours:
            maincompare.main()

    except Exception as ex:
        printsend(ex.msg, MTITLE + ERRORSTR)


if __name__ == "__main__":
    main()
