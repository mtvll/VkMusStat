
# Проект: VMStat v 250211

Сбор статистики и сервисов, проверка на плейлисты и вывод графики 
##    1. Установка

1. Убедитесь, что у вас установлен Python 3.8.1 или выше.



## 2. Модули и функции 

### 2.0 Общие параметры 

PRODUCTIVE -  закрывает открытые модули Chrome

ONLYONETESTPROGON - только один прогон при сборе статистики и проверки 

help или ? - сообщение о функциях 



### 2.1 mains.py

#### Описание  
Обращение через Web к соцсетям и сервисам 

Ссылки на соцсети находятся в mzqlite.py, переменная self.art
        
Артист (Имя, vkstudio, spotify, yandex, sber,
                   youtube, vk, Tiktok,
                   Tlg, Instagram
                   ,,,minhears):

#### Параметры 

DONTWRITE2BASE - не записывать в базу данных 

NOYANDEX, NOSBER, NOVKSUB, NOYOUTUBE, NOTIKTOK, NOTLG

### 2.2 mainchk.py

#### Описание  

Проверка ссылок на плейлисты (из базы данных) и сравнение с предыдщуим днем  (вызовом maincompare)


#### Параметры 

FREQHOURS - проверка раз в часов только для проставки лайков


### 2.3 mainwwwgr.py

#### Описание  

Запускается 

streamlit run C:/PyProjects/VkMusStat/mainwwwgr.py 
