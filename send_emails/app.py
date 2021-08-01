import csv
from smtplib import SMTP 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import jinja2

templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = "template.html"


def send_mail(EMAIL,BODY):
    to_email = EMAIL
    from_email = "navaganeshr69@gmail.com"
    subject = 'YSD Coupon Code Send'
    message = MIMEMultipart()  
    message['Subject'] = subject
    message['From'] = from_email
    message['To'] = to_email
    message.attach(MIMEText(BODY, "html"))
    msgBody = message.as_string()
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('navaganeshr69@gmail.com', 'kgvmdvksdasdsdsa')
    server.sendmail(from_email, to_email, msgBody)
    server.quit()

def send_coupons():
    f = open('employees.csv')
    csv_file = csv.reader(f)
    for row in csv_file:
          template = templateEnv.get_template(TEMPLATE_FILE)
          bodyContent = template.render(NAME=row[0],CCODE=row[2],CVALUE=row[3])   
          send_mail(EMAIL=row[1],BODY=bodyContent)

if __name__ == "__main__":
    send_coupons()  
