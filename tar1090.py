import requests
import smtplib
from email.mime.text import MIMEText
import schedule
import time

t = time.time()

url = 'https://adsbapi.variflight.com/adsb/rank?lang=zh_CN&token=7b0cb9df1bcecc93fc918f9ac9a8f3e3&searchText='
res = requests.get(url)
data = res.json()
data = data['list']
def send_msg():
    for i in data:
        if i['truename'] == "Js**":
            num = i['row']-1
            average_num = str(i['anumAverage'])
            anumTotal = str(i['anumTotal'])
            dayTotal = str(i['dayTotal'])
            msgAverage = str(i['msgAverage'])
            msgTotal = str(i['msgTotal'])
            row = str(i['row'])
            print(average_num)
            subject = '今日日报'  # 标题
            sender = "wpj1999@163.com"  # 发送方
            content = "排名" + row + "\n均架数" + average_num + "\n总架数" + anumTotal + "\n在线天数" + dayTotal + "\n日均消息" + \
                      msgAverage + "\n总消息数" + msgTotal# 发送内容
            recver = "1241996582@qq.com"  # 接收方
            password = "QFYAWBNDMHYFADDO"
            message = MIMEText(content, 'plain', 'utf-8')

            message['Subject'] = subject
            message['To'] = recver
            message['From'] = sender

            smtp = smtplib.SMTP_SSL("smtp.163.com", 465)
            smtp.login(sender, password)
            smtp.sendmail(sender, [recver, ], message.as_string())  # as_string 对 message 的消息进行了封装
            smtp.quit()

send_msg()

schedule.every().day.at("10:40").do(send_msg)

while True:

    schedule.run_pending()
    time.sleep(100)

