# from mzqllite import *
from mzcompare import *
# from mfile import *
# from mmail import *
# from mzweb import *
from moss import *

# min_val = 30
#
# alert_proc=30
#
# - чтение таблицы
# текущая дата и артист (если не, то предыдущая дата и артист)
#
# - проверка
#
# - отчет
#
# - проверка внутри песен (где больше 30 прослушиваний)
# изменение эффективности, прослушек и добавлений на alert_proc
#
# - проверка внутри статистики (где значение больше 30)
# изменение всех параметров на на alert_proc
# изменение лучшей песни по двум значениям


MTITLE = "MUZCOMPARE"


def main():
    try:


        write_file(MTITLE + " Start " + MVERSION)

        cp = cCompare()

        r=cp.getartistparamByName("Rayvan", "minhears")


        mstr = ""
        for i in cp.art:
            mname = i.name
            minhears = cp.getartistparamByName(mname, "minhears")
            res = cp.comp_services(mname,minhears)
            mstr = mstr + res

        # db.closeconnection()

        mstr = mstr + '\n' if mstr !="" else mstr
        for i in cp.art:
            mname = i.name
            minhears = cp.getartistparamByName(mname, "minhears")
            res = cp.comp_tracks(mname,minhears)
            mstr = mstr + res

        # db.closeconnection()
        printsend(mstr, MTITLE, False)

        write_file(MTITLE + " End")

    except Exception as ex:
        printsend(ex.msg, MTITLE + ERRORSTR)


if __name__ == "__main__":
    main()
