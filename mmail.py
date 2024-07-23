from mconst import *

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(subject, new_line):
    smtp_server = smtplib.SMTP_SSL(ML_SERVER, 465)
    # smtp_server.starttls()
    smtp_server.login(ML_LOG, ML_P)

    msg = MIMEMultipart()

    # Настройка параметров сообщения
    msg["From"] = ML_LOG
    msg["To"] = "kossrs@mail.ru"
    msg["Subject"] = subject

    # Добавление текста в сообщение
    msg.attach(MIMEText(new_line, "plain"))

    # Отправка письма
    smtp_server.sendmail(ML_LOG, msg["To"], msg.as_string())

    # Закрытие соединения
    smtp_server.quit()
