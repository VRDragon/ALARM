import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
fromaddr = "rezotechnology@gmail.com"
toaddr = "+421902313910@sms.t-mobile.sk"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "UPOZORNENIE"
body = "OBJEKT BOL NARUSENY"
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "password")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
