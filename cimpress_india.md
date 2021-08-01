### Suppose all the server log files(/tmp/logs/*.log) should be synchronized to the backup server(192.168.1.100) in the same directory every Monday at 3 PM .How can you config it in crontab?

step 1: Create a script that syncronizes the log files
```
cat <<EOF >>  /tmp/sync_logfiles.sh
 #!/bin/bash
rsync -tuP /tmp/*.log ubuntu@192.168.1.100:"/tmp/"
EOF
```
step 2: run the below command to add an entry in cron
```
crontab -l| { cat; echo "0 15 * * *  /home/ubuntu/sync_logfiles.sh >> /var/log/sync/sync_logfiles.log" ; } | crontab  
  
```
Step 3: Make Sure that the entry is added into the cron.
```
crontab -l
```

### write a python script to automatically send the coupon information to each employee through each one’s email.

```
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

```

```
<p>Dear {{ NAME }},</p>
<p>We are glad to tell you have a {{ CVALUE }} yuan coupon. </p>
<p> The coupon code is {{ CCODE }} </p>
<p> Please have a nice tour on our main website: ysd.com. </p>

```

### Somebody accidentally dropped a table in MySQL at Thursday 6 PM. how to restore 



### NodeJS service need to be automatically build, deploy.

