
# ������: VMStat v 250211

���� ���������� � ��������, �������� �� ��������� � ����� ������� 
##    1. ���������

1. ���������, ��� � ��� ���������� Python 3.8.1 ��� ����.



## 2. ������ � ������� 

### 2.0 ����� ��������� 

PRODUCTIVE -  ��������� �������� ������ Chrome

ONLYONETESTPROGON - ������ ���� ������ ��� ����� ���������� � �������� 

help ��� ? - ��������� � �������� 



### 2.1 mains.py

#### ��������  
��������� ����� Web � �������� � �������� 

������ �� ������� ��������� � mzqlite.py, ���������� self.art
        
������ (���, vkstudio, spotify, yandex, sber,
                   youtube, vk, Tiktok,
                   Tlg, Instagram
                   ,,,minhears):

#### ��������� 

DONTWRITE2BASE - �� ���������� � ���� ������ 

NOYANDEX, NOSBER, NOVKSUB, NOYOUTUBE, NOTIKTOK, NOTLG

### 2.2 mainchk.py

#### ��������  

�������� ������ �� ��������� (�� ���� ������) � ��������� � ���������� ����  (������� maincompare)


#### ��������� 

FREQHOURS - �������� ��� � ����� ������ ��� ��������� ������


### 2.3 mainwwwgr.py

#### ��������  

����������� 

streamlit run C:/PyProjects/VkMusStat/mainwwwgr.py 




##    ����������.

### ���� ���� �� ������

#### Pycharm � ����� ������������ ���������� 

������� act.bat ��� venv\scripts\activate.bat


#### Pycharm � ����� ������������ ����������

���� �� ������ env (������� �� Program Files) � pycahrm � ��������������� ������, ������� ����� � pycahrm � ��������� ���� lib  

 
####  Pycharm � ������ zero(103) � ������ ��������� � ��������� python �� ������ �� �������� �������

���������� ���� � ����� venv/ pyenv.cfg 

 

#### ���� �� ������ env (������� �� Program Files) � pycahrm � ��������������� ������, ������� ����� � pycahrm � ��������� ���� lib  

### Pycharm. ����� ������  

��������� ������� pip � setuptools, ���� ���� ��������

py -m pip install --upgrade pip 

py -m pip install --upgrade pip setuptools  

py -m pip install --upgrade pip setuptools wheel 


### TinTst  

�� ������� ��������� pip install grpcio==1.56.2  protobuf==4.24.3 tinkoff-investments==0.2.0b56 

�� black �������  gprc � tinkoff-investments �� ������� ����������   

  

### mIndic  

wheel==0.37.1 setuptools==60.5.0 

�� black �������   lxml talib  gprc � tinkoff-investments matplotlib (������. res: python -m pip install -U matplotlib==3.2.0rc1) 

  

pip install deptry  

deptry .  

����� pip install.... 

  

���������� ������������� numpy pandas - ��������� ������ 

 
 

 

#### ���������� ����� ���� ����� VC++ NEEDED 

������� ����� https://www.lfd.uci.edu/~gohlke/pythonlibs/#ta-lib 

���������� �� ������ ������ pip install some-package.whl 

��������� ���������  

 


#### Selenium (VkMusStat) 

�� ����������� � ������ ������   �� ������ �������  

Solution: ��������� ����� ������ (������ 21 ������ selenium) pip install selenium==4.20.0 

� ����� (�� �� ����!) �������������  Java �� ����� ������ ������ ����� �� ������ https://www.java.com/releases/ � ������ � �����  

 


 

#### ���� ������  

 

������� �����:  

VACUUM main  

 

 

####  GIT _ HOWTO  

 

https://stackoverflow.com/questions/50538508/why-i-always-got-error-push-to-origin-master-was-rejected 

  

##### �� ������� - ���������  

������� ������ � const  

Commit (�������� ��� �� ������ ) � �������� ��� �� ������ ������  

** ���� ���� �� �������� �������  

git rm --cached .idea\*.* 

git rm --cached .devcontainer\*.* 

git rm --cached venv\*.* 

git rm --cached venv\* 

git rm --cached .oldbases\*.* 

git rm --cached .oldbases\* 

git rm --cached mreport.txt 

git rm --cached mlog.txt 

git rm --cached tb_keys.py 

[Ctrl + Shift + K] ����� Push �� ���� Git  

 

  

##### �� ����� - ���������   

[Ctrl T] Update Project �� ���� Git 

git pull origin master  

** ���� �� �������� �� �� ������� Commit   

** ���� �� �������� �� ������� Pull �� ���� Git  

** �� ����������� git pull ���������� ������ �� �������� �� ��� �������������� 

**  ���� �� ����� Remotes (https://github.com/mtvll/TinTst5.git = original) ��������� � PyCharm  

 

 
#### HEROKU  

 

##### ���� HEROKU ����� ��� ��������  

https://elements.heroku.com/buildpacks/numrut/heroku-buildpack-python-talib 

������ ��� �������  

~ $ heroku buildpacks:add --index 1 heroku/python 

~ $ heroku buildpacks:add --index 2 numrut/ta-lib 

 

���� ������ � numpy. �������� ������ � requirements  

 

 

##### ��������� ��������  

heroku run python3 ord_check.py 

 

##### ����������� � HEROKU  
 
����� ����� ��� Git Master 

Remote Branches -> Compare with current -> Files  

Get from Branch   

 

##### �������� ����� SHEDULER 

� cmd Windows  

heroku logs -a mtin --num=1000 >> pyth.txt 

 

#####  HEROKU  ������� 

������� ��� Windows  

- Git, heroku-x64  

  

� ��������� ������ PyCharm   (����� ������ �������� git init) 

 

pipreqs ./ --force --encoding=utf   

git status   

git add .  

git commit -m "5v"  

heroku login   

heroku git:remote -a mtin  

REM � ������ ��������� �������� (�� ������������ � bat) 

REM ���� ���������� ��������� "remote:        No matching distribution found for " 

REM �� ������ �� requirments � �� ������ ������ ������� pepreqs   

git push heroku master  

 

##### HEROKU ����������� 

����� ���������� �����������  

 �� ��������� ������ PyCharm  

heroku addons:create scheduler:standard 

 ������  

https://dashboard.heroku.com/apps/mtin/scheduler 

������� python3 namepgm.py  

 �����. 11 ���� = 8 UTC AM 

 

##### HEROKU PYCHARM  

����� ������ ������ ����� �� �������� �) ������������� � pycahrm plugins .ignore  

�) ������� ������ � �������� ��� � ����� ����������  

 

 

##### HEROKU � DJANGO  
https://devcenter.heroku.com/articles/django-app-configuration 
� procfile:  
web: gunicorn myproject.wsgi 
� settings 
import django_heroku 
import gunicorn 
� requirments 
gunicorn==20.0.4 

  

##### HEROKU. C������� REQUI ... 

pip3 install -r requirements.txt --user 

  

------------------------------------------------------------------------------------------------- 

 

##### PYTHONANYWHERE 

 ���� �� ������� ��������� ������������� � ������ --user  

pip --user  

 ��������� zip (������� ����� ���� ���������� git) �.�. ���� ����������� 100 ��  

Unzip � bash   

 

-------------------------------------------------------------------------------------------------- 

 

�������  

������ [] 

�������() 

������� {bierce = { 

... "day": "A period of twenty-four hours, mostly misspent", 

... "positive": "Mistaken at the top of one's voice", 

... "misfortune": "The kind of fortune that never misses", 

... }} 

���������{} 

 

���������  

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

 

 