import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = ""
password = ""
toaddr = ""

# Instance of MIMEMultipart
message = MIMEMultipart()

# Storing the senders email
message["From"] = fromaddr

# Storing the recivers email
message["To"] = toaddr

# Storing the subject
message["subject"] = "Mail ödevi"

body = "Mail ödevi"

message.attach(MIMEText(body,"plain"))

s = smtplib.SMTP("smtp.gmail.com", 587)

s.starttls()

s.login(fromaddr, "")

text = message.as_string()

s.sendmail(fromaddr, toaddr, text)

s.quit()