# from your Gmail account  
import smtplib
import ibm_db
from userView import *
# list of email_id to send the mail 


class SendMail:
    conn = ''
    name = ''
    def logincould():
        dsn_driver = "IBM DB2 ODBC DRIVER"
        dsn_databases = "BLUDB"
        dsn_hostname = 'dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net'
        dsn_port = "50000"
        dsn_protocal = "TCPIP"
        dsn_uid = 'wkg83160'
        dsn_pwd = "8g2kgt18+2tljbrb"
        dsn = ("DRIVER={{IBM DB2 ODBC DRIVER}};"
               "DATABASE={0};"
               "HOSTNAME = {1};"
               "PORT = {2};"
               "PROTOCOL = TCPIP;"
               "UID={3};"
               "pwd ={4};").format(dsn_databases, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)
        global conn
        conn = ibm_db.connect(dsn, "", "")
        print("cloud connected")


    def fetchdetails():
        name = 'mohit'
        SendMail.logincould()
        try:
            name_obj = Ui_MainWindowBoard()
            name = name_obj.Namereturner()
            print("yeah", name)

        except:
            print("uisng default username",name)
        SendMail.name = name
        query1 = "SELECT REFPERSON1EMAIL, REFPERSON2EMAIL from WKG83160.USERS1 WHERE USERNAME='%s'" % (name)

        ans = ibm_db.exec_immediate(conn, query1)
        print(ans)
        person_emails = ibm_db.fetch_both(ans)
        print(person_emails['REFPERSON1EMAIL'],person_emails['REFPERSON2EMAIL'])
        return person_emails['REFPERSON1EMAIL'], person_emails['REFPERSON2EMAIL']


    def main(self):
        carry_mails = SendMail.fetchdetails()
        c1 = carry_mails[0].strip(' ')
        c2 = carry_mails[1].strip(' ')
        #li = ["lokeshpamani@gmail.com", "mahi941333@gmail.com", "dadhichhardik26@gmail.com"]
        li = []
        li.append(c1)
        li.append(c2)
        print(li)
        for i in range(len(li)):
            s = smtplib.SMTP('smtp.gmail.com', 587)
            # tls for security
            s.starttls()
            # sender email id pass!
            print('emaillllllll')
            s.login("lpamnani26@gmail.com", "8094905494")
            print('loginnnnnnn')
            message = "Hey this is python generated mail from your desktop app! Your relative name {} mood is {}".format(SendMail.name, 'Joy')
            s.sendmail("dadhichhardik26@gmail.com", li[i], message)
            print("sended!")
            s.quit()


if __name__ == '__main__':
    sent_m = SendMail()
    sent_m.main()
