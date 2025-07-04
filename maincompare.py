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

        # r=cp.getartistparamByName("Rayvan", "minhears")


        mstr_main = "\n"
        mstr_sec = ""

        for i in cp.art:
            mname = i.name
            minhears = cp.getartistparamByName(mname, "minhears")
            res = cp.comp_services(mname,abs(minhears))
            if (minhears>0):
                mstr_main = mstr_main + res
            else:
                mstr_sec = mstr_sec + res

        # db.closeconnection()

        mstr_main = mstr_main + '\n' if mstr_main !="" else mstr_main
        mstr_sec =mstr_sec + '\n' if mstr_sec != "" else mstr_sec

        for i in cp.art:
            mname = i.name
            minhears = cp.getartistparamByName(mname, "minhears")
            res = cp.comp_tracks(mname,abs(minhears))
            if (minhears > 0):
                mstr_main = mstr_main + res
            else:
                mstr_sec = mstr_sec + res


        # 250506 Не выводить старые  прослушки
        mstr_sec=""


        mstr=""
        if len(mstr_main)>0 or len(mstr_main)>0:
            mstr=mstr_main+'\n'+'\n' + "--------------------------------------------" +'\n'+'\n'+mstr_sec


        # db.closeconnection()
        printsend(mstr, MTITLE, False)

        write_file(MTITLE + " End")

    except Exception as ex:
        printsend(ex.msg, MTITLE + ERRORSTR)


if __name__ == "__main__":
    main()
