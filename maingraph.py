from mzqllite import *
# from mfile import *
# from mmail import *
# from mzweb import *
from moss import *

MTITLE = "MUZGRAPH"


def main():
    try:

        write_file(MTITLE + " Start " + MVERSION)

        #    kill_chrome(STATUS_PRODUCTIVE)

        db = cDb()

        #    web = cWeb()

        db.graph_services("'RAYVAN'")
        db.graph_services("'Алексир'")
        db.graph_services("'Нонна'")
        db.graph_services("'Вячеслав Мясников'")
        db.graph_services("'Vigi'")




        # db.graph_tracks("'С другой'", "'Алексир'")
        # db.graph_tracks("'Верни'", "'Алексир'")

        db.graph_tracks("'С другой'", "'Алексир'")
        db.graph_tracks("'Верни'", "'Алексир'")


        # db.graph_services("'RAYVAN'")
        # db.graph_services("'Алексир'")
        # db.graph_services("'MILZ'")
        # db.graph_services("'Вячеслав Мясников'")
        # db.graph_services("'Vigi'")
        # db.graph_services("'Ирина Эмирова'")
        # db.graph_services("'София Мосейчук'")
        # db.graph_services("'Rustam Fahrtdinov'")
        # db.graph_services("'KALUGIN'")
        # db.graph_services("'Makaronnoe bludo'")
        # db.graph_services("'Хор Ирины Павленко'")
        # db.graph_services("'Нонна'")


        #
        #
        # db.graph_tracks("'Улетай'", "'RAYVAN'")
        # db.graph_tracks("'Такая простая'", "'RAYVAN'")

        #    db.graph_tracks("'Спиммм Dark Mix'", "'MILZ'")

        db.closeconnection()
        write_file(MTITLE + " End")

    except Exception as ex:
        printsend(ex.msg, MTITLE + ERRORSTR)


if __name__ == "__main__":
    main()
