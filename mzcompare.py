import sqlite3
import datetime
from mfile import *

from mconst import *
from mzqllite import *


class cCompare(cDb):
    def __init__(self):
        c = cDb()

        # data = []
        # self.mpd =pd.DataFrame(data)
        self.mpd = c.get2days_4compare()
        self.art = c.art

    def comp_services_bestsongs(self, martist, df, cname, cnmb):
        v1 = df[cname].values[0]
        v2 = df[cname].values[1]
        v1n = df[cnmb].values[0]
        v2n = df[cnmb].values[1]

        if (v1 != v2) and (v1n != 0) and (v2n != 0):
            res = "CHKSERVICE: " + martist + " [" + cname + "] Old Value:" + v1 + "(" + str(v1n) + ")" + " New:" + str(
                v2) + "(" + str(v2n) + ")" + "\n"
        else:
            res = ""

        return res

    def comp_services(self, martist,minArtistHearsVk):

        ms = ""

        mlist = ["hears_vk", "adds_vk", "eff_vk", "hears_month_ynd", "likes_month_ynd",
                 "likes_all_ynd", "sub_sber", "sub_youtube", "hears_month_spot", "sub_vk", "sub_tiktok", "likes_tiktok"]
        df = self.mpd[(self.mpd['martist'] == martist) & (self.mpd['ServiceOrTrack'] == "service")]
        if len(df) != 2:
            return ms

        v1hears = df["hears_vk"].values[0]
        v2hears = df["hears_vk"].values[1]

        for i in mlist:
            v1 = df[i].values[0] if df[i].values[0] != "" else 0
            v2 = df[i].values[1] if df[i].values[1] != "" else 0
            ds = abs((v1 - v2) * 100 / max(v1, v2)) if (v1 > MIN_VAL_FOR_COMPARE) and (v2 > MIN_VAL_FOR_COMPARE) else 0
            if i in ["hears_vk", "adds_vk", "eff_vk"]:
                ds= ds if (v1hears > minArtistHearsVk) and (v2hears > minArtistHearsVk) else 0
            if ds > ALERT_PROC_IN_COMPARE:
                ms = ms + "CHKSERVICE: " + martist + " [" + i + "] Old Value:" + str(v1) + " New:" + str(v2) + "\n"

        ms = ms + self.comp_services_bestsongs(martist, df, "hears_best_song", "hears_best_n") if (v1hears > minArtistHearsVk) and (v2hears > minArtistHearsVk) else ms
        ms = ms  + self.comp_services_bestsongs(martist, df, "eff_best_song", "eff_best_n") if (v1hears > minArtistHearsVk) and (v2hears > minArtistHearsVk) else ms
        # if (df["hears_best_song"].values[0]!=df["hears_best_song"].values[0]):
        #     ms = ms + "CHKSERVICE: " + martist + " [" + "hears_best_song" + "] Old Value:" + str(v1) + " New:" + str(v2) + "\n"

        return ms


    def comp_tracks(self, martist, minArtistHearsVk):

        ms = ""

        mlist = [ "hears_vk", "adds_vk", "eff_vk"]

        df = self.mpd[(self.mpd['martist'] == martist) & (self.mpd['ServiceOrTrack'] == "track")]
        if len(df) == 0:
            return ms


        tracklist =[]
        for ii in df["mtrack"]:
            dfi=df[df["mtrack"]==ii]
            v1hears = dfi["hears_vk"].values[0]
            v2hears = dfi["hears_vk"].values[1] if len(dfi) > 1 else 0
            if (v1hears > minArtistHearsVk) and (v2hears > minArtistHearsVk):
                if len(dfi)==2 and ii not in tracklist:
                    for i in mlist:
                        v1 = dfi[i].values[0] if dfi[i].values[0] != "" else 0
                        v2 = dfi[i].values[1] if dfi[i].values[1] != "" else 0
                        ds = abs((v1 - v2) * 100 / max(v1, v2)) if (v1 > MIN_VAL_FOR_COMPARE) and (v2 > MIN_VAL_FOR_COMPARE) else 0
                        if ds > ALERT_PROC_IN_COMPARE:
                            ms = ms + "CHKSERVICE_TRACK: " + martist +"."+ii+ " [" + i + "] Old Value:" + str(v1) + " New:" + str(v2) + "\n"
                            tracklist.append(ii)
        return ms
