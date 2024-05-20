"""Automated Email Sending Script"""

from os import name, getenv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd
import dotenv
dotenv.load_dotenv()

FROM_ADDR='ENTER_SENDERS_MAILID'

data=pd.read_csv("abc.csv")         # Enter path of CSV files containing EMAILs
TO_ADDR=data['EMAIL'].tolist()      # Change'EMAIL' to column name containg EMAILids
dataname = data['name'].tolist()

length=len(name)

for i in range (length):
    msg=MIMEMultipart()
    msg['From']=FROM_ADDR
    msg['To']=TO_ADDR[i]
    msg['subject']='Just to Check'
    body=name[i]+'Enter your content here'
    msg.attach(MIMEText(body,'plain'))

    EMAIL= getenv('EMAIL')
    PASSWORD = getenv('PASSWORD')

    mail=smtplib.SMTP('smtp.gmail.com',587)
    mail.ehlo()
    mail.starttls()
    mail.login(EMAIL,PASSWORD)
    text=msg.as_string()
    mail.sendmail(FROM_ADDR,TO_ADDR[i],text)
    mail.quit()
