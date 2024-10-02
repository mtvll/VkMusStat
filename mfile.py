import datetime
# from mconst import *
from mmail import *

import urllib.request


def checkisnumberr(instr, mfrom=""):
    instr = instr.replace(' ', '')
    try:
        # Убрал проверку на youtube
        # if (mfrom == "youtube") and (instr[-1] == "M"):
        if  (instr[-1] == "M"):
            instr = float(instr[:-1]) * 1000000
        # if (mfrom == "youtube") and (instr[-1] == "K"):
        if  (instr[-1] == "K"):
            instr = float(instr[:-1]) * 1000
        c = int(instr)
        return c
    except Exception as ex:
        return -1

def printsend(mstr, title, write2file=True) :
    if (mstr!=""):
        try:            #20240414 ���� ���������� � ������� ��������
            print(mstr)
        except:
            print (title + 'TRACK: Coding problems. Only emailed')
            pass
        if write2file:
            write_file(title + mstr)
        if "Second iteration" in mstr or TITLE_CHK[0:3] in mstr:
            send_mail(title, mstr)

def img2blob(img):
    mfilename = "getcitywalls2_tmp.jpg"
    mfile = urllib.request.urlretrieve(img, mfilename)
    blobdata = open(mfilename, 'rb').read()
    return blobdata

def print2file(mstr) :
    if (mstr!=""):
        try:            #20240414 ���� ���������� � ������� ��������
            print(mstr)
        except:
            print ('TRACK: Coding problems. Only emailed')
            pass
        write_file(mstr)


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
