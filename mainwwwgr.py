import pandas as pd
import time
import numpy as np
import streamlit as st
import plotly.express as px

import streamlit_authenticator as stauth
from streamlit_authenticator import Authenticate

from mzqllite import *


db = cDb()

conn = st.connection('mus2024', type='sql')

import yaml
from yaml.loader import SafeLoader
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)



name, authentication_status, username = authenticator.login('main', fields = {'Form name': 'Hi! Please enter user name and psw'})

if (username==None):
    username = ""

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.write(f'Welcome *{name}*')
    # 240705 Закоментил, занимает лишнее место
    # st.title('Some content')
elif authentication_status == False:
    st.error('Username/password is incorrect!')
elif authentication_status == None:
    st.warning('Please enter your username and password')


if username=="":
    exit(0)

if username.upper()  in ["TEST","K","YULIA"]:
    mstr = "%"
else:
    mstr = username.upper()

if username.upper()  in ["YARIK"]:
    mstr = "Кипиш Нот"

# print("user: "+username.upper())


# if username.upper() == 'RAYVAN':
#      mstr = username.upper()
#
# if username.upper() == 'Алексир':
#      mstr = username.upper()

st.sidebar.title("About")


sql = "SELECT  martist, mcurdate, hears_vk, adds_vk, eff_vk, hears_month_ynd, likes_month_ynd, likes_all_ynd, sub_sber, sub_youtube,  sub_vk,sub_tiktok,sub_tlg  FROM MuzStat WHERE martist LIKE "+ "'"+mstr +"'"+ "and ServiceOrTrack ='service'"
# 240710 Delete spotify
# sql = "SELECT  martist, mcurdate, hears_vk, adds_vk, eff_vk, hears_month_ynd, likes_month_ynd, likes_all_ynd, sub_sber, sub_youtube, hears_month_spot, sub_vk,sub_tiktok,sub_tlg  FROM MuzStat WHERE martist LIKE "+ mstr +" and ServiceOrTrack ='service'"

df0services = conn.query(sql)

# sql = "SELECT mcurdate, hears_vk, adds_vk, eff_vk  FROM MuzStat"
# df0tracks = pd.read_sql(sql, con=db.connection)

martist = st.sidebar.selectbox("Select Artist", df0services["martist"].unique().tolist())

df=df0services.loc[df0services['martist'] == martist]

mval =[]

mval.append ([CAPTIONADD,df['adds_vk'],"lines"])
mval.append ([CAPTIONHEAR,df['hears_vk'],"lines"])
mval.append ([CAPTIONEFF,(df['adds_vk']) * COEFFEFFECT / df['hears_vk'],"lines+markers"])
mval.append (["Yand.ПрослушиванияМесяц",df['hears_month_ynd'],"lines"])
mval.append (["Yand.ЛайкиМесяц",df['likes_month_ynd'],"lines"])
mval.append (["Yand.ЛайкиВсе",df['likes_all_ynd'],"lines+markers"])
mval.append (["Sber.Подписчики",df['sub_sber'],"lines"])
mval.append (["Youtube.Подписчики",df['sub_youtube'],"lines"])
# mval.append (["Spot.ПрослушиванияМесяц",df['hears_month_spot'],"lines+markers"])
mval.append (["VK.Подписчики",df['sub_vk'],"lines"])
mval.append (["TikTok.Подписчики",df['sub_tiktok'],"lines"])
mval.append (["Tlg.Подписчики",df['sub_tlg'],"lines"])

chk = []

for i in range(len(mval)):
    chk.append(st.sidebar.checkbox(mval[i][0]))

created_time = df['mcurdate']

fig = go.Figure()

for i in range(len(mval)):
    if chk[i]==True:
        fig.add_trace(go.Scatter(x=created_time, y=mval[i][1], mode=mval[i][2], name=mval[i][0]))

# fig.add_trace(go.Scatter(x=created_time, y=mval[0][1], mode='lines', name=mval[0][0]))
# fig.add_trace(go.Scatter(x=created_time, y=mval[1][1], mode='lines', name='VK.Прослушивания'))
# fig.add_trace(go.Scatter(x=created_time, y=mval[2][1], mode='lines+markers', name='VK.Эффективность'))
#
# fig.add_trace(go.Scatter(x=created_time, y=mval[3][1], mode='lines', name='hears_month_ynd'))
# fig.add_trace(go.Scatter(x=created_time, y=mval[4][1], mode='lines', name='likes_month_ynd'))
# fig.add_trace(go.Scatter(x=created_time, y=mval[5][1], mode='lines+markers', name='likes_all_ynd'))
#
# fig.add_trace(go.Scatter(x=created_time, y=mval[6][1], mode='lines', name='sub_sber'))
# fig.add_trace(go.Scatter(x=created_time, y=mval[7][1], mode='lines', name='sub_youtube'))
# fig.add_trace(go.Scatter(x=created_time, y=mval[8][1], mode='lines+markers', name='hears_month_spot'))
#
# fig.add_trace(go.Scatter(x=created_time, y=mval[9][1], mode='lines+markers', name='VK.Подписчики'))
# fig.add_trace(go.Scatter(x=created_time, y=mval[10][1], mode='lines+markers', name='TikTok.Подписчики'))
fig.update_layout(title_text="Статистика музыканта: " + martist)

# l1 = df['adds_vk']
# l2 = df['hears_vk']
# l3 = (df['adds_vk']) * 1000 / df['hears_vk']
# l4 = df['hears_month_ynd']
# l5 = df['likes_month_ynd']
# l6 = df['likes_all_ynd']
# l7 = df['sub_sber']
# l8 = df['sub_youtube']
# l9 = df['hears_month_spot']
# l10 = df['sub_vk']
# l11 = df['sub_tiktok']
# created_time = df['mcurdate']
#
# fig = go.Figure()
# fig.add_trace(go.Scatter(x=created_time, y=l1, mode='lines', name='VK.Добавления'))
# fig.add_trace(go.Scatter(x=created_time, y=l2, mode='lines', name='VK.Прослушивания'))
# fig.add_trace(go.Scatter(x=created_time, y=l3, mode='lines+markers', name='VK.Эффективность'))
#
# fig.add_trace(go.Scatter(x=created_time, y=l4, mode='lines', name='hears_month_ynd'))
# fig.add_trace(go.Scatter(x=created_time, y=l5, mode='lines', name='likes_month_ynd'))
# fig.add_trace(go.Scatter(x=created_time, y=l6, mode='lines+markers', name='likes_all_ynd'))
#
# fig.add_trace(go.Scatter(x=created_time, y=l7, mode='lines', name='sub_sber'))
# fig.add_trace(go.Scatter(x=created_time, y=l8, mode='lines', name='sub_youtube'))
# fig.add_trace(go.Scatter(x=created_time, y=l9, mode='lines+markers', name='hears_month_spot'))
#
# fig.add_trace(go.Scatter(x=created_time, y=l10, mode='lines+markers', name='VK.Подписчики'))
# fig.add_trace(go.Scatter(x=created_time, y=l11, mode='lines+markers', name='TikTok.Подписчики'))
# fig.update_layout(title_text="Статистика музыканта: " + martist)

# fig.show()

#
# 240705 Закоментил, занимает лишнее место
# st.title('MUZSTAT Сбор статистики для музыкантов')

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })
# st.write(df)
#
# chart_data = pd.DataFrame(
#      np.random.randn(20, 3),
#      columns=['a', 'b', 'c'])
#
# selected_sex = st.selectbox("Select Sex", chart_data.columns)
# st.write(f"Selected Option: {selected_sex!r}")

# st.line_chart(df)

st.plotly_chart(fig)

sql = "SELECT mcurdate, mtrack, hears_vk, adds_vk, eff_vk  FROM MuzStat WHERE martist='" + martist + "'"

# df0tracks_old = pd.read_sql(sql, con=db.connection)

df0tracks = conn.query(sql)



mtrack = st.sidebar.selectbox("Select Tracks", df0tracks["mtrack"].unique().tolist())

df=df0tracks.loc[df0tracks['mtrack'] == mtrack]




x_CrestFactor = df['adds_vk']
y_CrestFactor = df['hears_vk']
z_CrestFactor = round(COEFFEFFECT / df['eff_vk'])
created_time = df['mcurdate']

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=created_time, y=x_CrestFactor, mode='lines', name=CAPTIONADD))
fig2.add_trace(go.Scatter(x=created_time, y=y_CrestFactor, mode='lines', name=CAPTIONHEAR))
fig2.add_trace(go.Scatter(x=created_time, y=z_CrestFactor, mode='lines+markers', name=CAPTIONEFF))

fig2.update_layout(title_text="Статистика трека: " + martist + ":" + mtrack)

st.plotly_chart(fig2)
