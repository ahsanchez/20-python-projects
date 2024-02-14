import smtplib

to = "fakeemail@gmail.com"
content = "This an test email"


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("fakeemail@gmail.com", "1234")
    server.sendmail("fakeemail@gmail.com", to, content)
    server.close


sendEmail(to, content)
