# from your Gmail account  
import smtplib

# list of email_id to send the mail 
li = ["lokeshpamani@gmail.com", "mahi941333@gmail.com"]

for i in range(len(li)):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    #tls for security
    s.starttls()
    #sender email id pass!
    s.login("dadhichhardik26@gmail.com", "")
    message = "Hey this is python generated mail from your desktop app"
    s.sendmail("dadhichhardik26@gmail.com", li[i], message)
    s.quit() 