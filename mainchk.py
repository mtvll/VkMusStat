from mzqllite import *
# from mfile import *
# from mmail import *
from mzweb import *
from moss import *

import maincompare

MTITLE = "MUZCHEK"


def main():
    param1 = sys.argv[1] if (len(sys.argv) > 1) else False

    status_prod = True if param1 == TXTPRODUCTIVE else False

    try:
        write_file(MTITLE + " Start " + VER)

        kill_chrome(status_prod)

        db = cDb()

        web = cWebm()

        db.dbchk2table()
        # добавлеение строки в таблицу
        # Проверка раз в 6 часов
        # Таблица1. название - ссылка  - какчастопроверять  1-7 дней или 0.25 - раз в 76 часов
        # Таблица2. текст (для проверки) - поле (для проверки) нееоб
        # Таблица3. нужен ли прокси- последняя проверка дата - послдн значение

        # Типы проверки:
        # Тип 1. IsOnPage Наличие на странице ( плейлист bandlink, книги, фильмы)
        # a=web.findonpage("https://band.link/scanner?search=Rayvan","ничего не найдено")
        # a=web2.findonpage("https://flibusta.is/booksearch?ask=нагибин","ничего не найдено")
        # a=web2.findonpage("https://flibusta.is/booksearch?ask=оплетаев","не найдено")
        # Если изменения то почта  (с другм сообщением) навзание, ссылка, как было - как стало
        # Тип 2. IsOnPageAdd Обновление на странице в конкретном поле (плейлист vk)
        # Если изменения то почта  (с другм сообщением) навзание, ссылка, как было - как стало
        # Тип 3. NewPostOnPage Обновление на странице в виде нового поста (вк).
        # Если изменения без почты, а просто дейсвтие (клик) на определенный элемент

        # mdriver = chromeinitilize()

        mstr = ""

        for i in db.arr:
            try:
                if i.needproxy != str(int(True)):
                    res = web.findonpage(i.mlink, i.mstr, i.ishere, i.mstrfield)
                    if i.ishere in ('0','1'):
                        mres = str((int(res)))
                        mres2tst=mres
                    if i.ishere == '-1':
                        mres = res
                        t1=str(mres).splitlines(keepends=True)
                        t2=str(i.lastval).splitlines(keepends=True)
                        mres2tst = ''.join(difflib.context_diff(t1, t2))
                    if res==True and i.alwaysshow>0:
                        mstr = mstr + "GOOD STATUS " + i.mname + " Status:" + str(
                            mres2tst) + " Link:" + i.mlink + "\n"
                    if mres != i.lastval:
                        mstr = mstr+ "CHANGE STATUS " + i.mname + " NewStatus:" + str(mres2tst) + " Link:" + i.mlink +"\n"
                        i.lastval = res
                    db.update_dbchk_row(i)
            except Exception as e:
                printsend(" CHK " + i.mname + "  Message" + e.msg, MTITLE + ERRORSTR)
                continue

        printsend(mstr,MTITLE)

        db.closeconnection()
        write_file(MTITLE + " End")

        maincompare.main()

    except Exception as ex:
        printsend(ex.msg, MTITLE + ERRORSTR)


if __name__ == "__main__":
    main()
