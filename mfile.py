import datetime
# from mconst import *
from mmail import *


def printsend(mstr, title, write2file=True) :
    if (mstr!=""):
        try:            #20240414 ���� ���������� � ������� ��������
            print(mstr)
        except:
            print (title + 'TRACK: Coding problems. Only emailed')
            pass
        if write2file:
            write_file(title + mstr)
        send_mail(title, mstr)


def getctime():
    mdate = datetime.datetime.now()
    return mdate.strftime("%H:%M:%S")


def getcdate(delta=0):
    mdate = datetime.datetime.now() - datetime.timedelta(days=delta)
    # return mdate.strftime("%d-%b-%Y") + ": "
    return mdate.strftime("%d-%b-%Y")


def write_file(new_line):
    f = open('mreport.txt', 'a',encoding="utf-8")

    mdate = datetime.datetime.now()

    mcurdate = getcdate() + ": "
    mcurtime = getctime() + " "
    mwday = mdate.strftime("%A")

    f.write(mcurdate + mcurtime + "(" + mwday + ") " + new_line + '\n')

    f.close()
