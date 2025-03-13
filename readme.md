
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




##    ПРИЛОЖЕНИЕ.

### ЕСЛИ ГЛЮК НА МАШИНЕ

#### Pycharm – чтобы пользоваться терминалом 

Сначала act.bat или venv\scripts\activate.bat


#### Pycharm – чтобы пользоваться терминалом

Если не верный env (берется из Program Files) в pycahrm – переименовываем старый, создаем новый в pycahrm и переносим туда lib  

 
####  Pycharm – ошибка zero(103) в списке библиотек и сообщение python не найден со странным адресом

Посмотреть путь в файле venv/ pyenv.cfg 

 

#### Если не верный env (берется из Program Files) в pycahrm – переименовываем старый, создаем новый в pycahrm и переносим туда lib  

### Pycharm. Новый проект  

проверить сначала pip и setuptools, если надо обновить

py -m pip install --upgrade pip 

py -m pip install --upgrade pip setuptools  

py -m pip install --upgrade pip setuptools wheel 


### TinTst  

На сервере сработало pip install grpcio==1.56.2  protobuf==4.24.3 tinkoff-investments==0.2.0b56 

На black перенес  gprc и tinkoff-investments из рабочих директорий   

  

### mIndic  

wheel==0.37.1 setuptools==60.5.0 

На black перенес   lxml talib  gprc и tinkoff-investments matplotlib (ошибка. res: python -m pip install -U matplotlib==3.2.0rc1) 

  

pip install deptry  

deptry .  

потом pip install.... 

  

постепенно устанавливаем numpy pandas - последние версии 

 
 

 

#### УСТАНОВИТЬ ПАКЕТ ЕСЛИ ПИШЕТ VC++ NEEDED 

Скачать пакет https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib 

Установить на пустой машине pip install some-package.whl 

Перенести билиотеку  

 


#### Selenium (VkMusStat) 

Не запускается и выдает ошибку   не найден драйвер  

Solution: установил более раннюю (вместо 21 версию selenium) pip install selenium==4.20.0 

а также (но не факт!) переустановил  Java на более раннюю версию узнав ее отсюда https://www.java.com/releases/ и скачав с инета  

 


 

#### БАЗА ДАННЫХ  

 

Очистка места:  

VACUUM main  

 

 

####  GIT _ HOWTO  

 

https://stackoverflow.com/questions/50538508/why-i-always-got-error-push-to-origin-master-was-rejected 

  

##### На сервере - исходнике  

Изменяю версию в const  

Commit (указываю имя из версии ) и проверяю нет ли лишних файлов  

** Если есть то выполняю команды  

git rm --cached .idea\*.* 

git rm --cached .devcontainer\*.* 

git rm --cached venv\*.* 

git rm --cached venv\* 

git rm --cached .oldbases\*.* 

git rm --cached .oldbases\* 

git rm --cached mreport.txt 

git rm --cached mlog.txt 

git rm --cached tb_keys.py 

[Ctrl + Shift + K] делаю Push из меню Git  

 

  

##### На компе - приемнике   

[Ctrl T] Update Project из меню Git 

git pull origin master  

** если не работает то мб сделать Commit   

** если не работает то сделать Pull из меню Git  

** на серебрянном git pull комнандная строка не работает тк нет аутентификации 

**  если не видны Remotes (https://github.com/mtvll/TinTst5.git = original) перезайти в PyCharm  

 

 
#### HEROKU  

 

##### ЕСЛИ HEROKU ПИШЕТ ПРО ПРОБЛЕМЫ  

https://elements.heroku.com/buildpacks/numrut/heroku-buildpack-python-talib 

Ввести две команды  

~ $ heroku buildpacks:add --index 1 heroku/python 

~ $ heroku buildpacks:add --index 2 numrut/ta-lib 

 

Была ошибка в numpy. Поправил версию в requirements  

 

 

##### ЗАПУСТИТЬ УДАЛЕННО  

heroku run python3 ord_check.py 

 

##### СИНХРОННИТЬ С HEROKU  
 
Внизу слева где Git Master 

Remote Branches -> Compare with current -> Files  

Get from Branch   

 

##### ПРОСМОТР ЛОГОВ SHEDULER 

В cmd Windows  

heroku logs -a mtin --num=1000 >> pyth.txt 

 

#####  HEROKU  скачать 

Скачать для Windows  

- Git, heroku-x64  

  

В командной строке PyCharm   (перед первым запуском git init) 

 

pipreqs ./ --force --encoding=utf   

git status   

git add .  

git commit -m "5v"  

heroku login   

heroku git:remote -a mtin  

REM А дальше отдельной командой (не подцепляется в bat) 

REM если возмникает сообщение "remote:        No matching distribution found for " 

REM то убрать из requirments и не делать первую комнаду pepreqs   

git push heroku master  

 

##### HEROKU ПЛАНИРОВЩИК 

Чтобы установить планировщик  

 Из командной строки PyCharm  

heroku addons:create scheduler:standard 

 Дальше  

https://dashboard.heroku.com/apps/mtin/scheduler 

Указать python3 namepgm.py  

 Время. 11 утра = 8 UTC AM 

 

##### HEROKU PYCHARM  

Чтобы убрать лишние файлы из загрузки а) устанавливаем в pycahrm plugins .ignore  

б) находим шаьлон и помещаем его в главн директорию  

 

 

##### HEROKU И DJANGO  
https://devcenter.heroku.com/articles/django-app-configuration 
в procfile:  
web: gunicorn myproject.wsgi 
в settings 
import django_heroku 
import gunicorn 
в requirments 
gunicorn==20.0.4 

  

##### HEROKU. CСОЗДАТЬ REQUI ... 

pip3 install -r requirements.txt --user 

  

------------------------------------------------------------------------------------------------- 

 

##### PYTHONANYWHERE 

 если не хватает библиотек устанавливать с ключом --user  

pip --user  

 Загрузить zip (удалить перед этим директорию git) т.к. есть ограничение 100 Мб  

Unzip в bash   

 

-------------------------------------------------------------------------------------------------- 

 

ОБЪЕКТЫ  

Списки [] 

Кортежи() 

Словари {bierce = { 

... "day": "A period of twenty-four hours, mostly misspent", 

... "positive": "Mistaken at the top of one's voice", 

... "misfortune": "The kind of fortune that never misses", 

... }} 

Множества{} 

 

ОПЕРАТОРЫ  

if disaster: 

print("Woe!") 

 

while count <= 5: 

... print(count) 

... count += 1 

 

>>> list(range(0, 3)) 

[0, 1, 2] 

 

>>> number_list = [] 

>>> for number in range(1, 6): 

... number_list.append(number) 

 

def print_more(required1, required2, *args): 

... print('Need this one:', required1) 

... print('Need this one too:', required2) 

... print('All the rest:', args) 

 

 