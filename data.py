import ibm_db
import ibmdbpy

def cloudConnectiontwo():
    print("called")
    dsn_driver = "IBM DB2 ODBC DRIVER"
    dsn_databases = "BLUDB"
    dsn_hostname = "dashdb-txn-sbox-yp-lon02-01.services.eu-gb.bluemix.net"
    dsn_port = "50000"
    dsn_protocal = "TCPIP"
    dsn_uid = "zcv09671"
    dsn_pwd = "w74qq3sd56z^kr75"
    dsn =("DRIVER={{IBM DB2 ODBC DRIVER}};"
           "DATABASE={0};"
           "HOSTNAME = {1};"
           "PORT = {2};"
           "PROTOCOL = TCPIP;"
           "UID={3};"
           "pwd ={4};").format(dsn_databases, dsn_hostname, dsn_port, dsn_uid, dsn_pwd)

    conn = ibm_db.connect(dsn, "", "")
    
    #q = "CREATE TABLE USERS(ID int PRIMARY KEY AUTO_INCREMENT, USERNAME CHAR(40) NOT NULL, PASSWORD CHAR(30), EMAIL CHAR(40), CONTACT INT(10))"
    #stt =  ibm_db.exec_immediate(conn, q)

    print("cloud connected")
    
    
    

#cloudConnectiontwo()
