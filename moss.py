import psutil
from mconst import *
from mfile import *
import mconst


def kill_chrome(instatus):

    if (instatus == True):
        is_close = False
        for proc in psutil.process_iter():
            if proc.name() == "chrome.exe":
                proc.kill()
                is_close = True
        if is_close:
            write_file("Close Chrome.exe")
