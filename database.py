import sqlite3
import mysql.connector
import ibm_db
import ibmdbpy

def createTable():
    connection = sqlite3.connect('login.db')
    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL, PASSWORD TEXT, EMAIL TEXT, CONTACT INT(10))")
    connection.execute("INSERT INTO USERS VALUES(?,?,?,?)",("hardik","har123" ,"hardik@gmail.com", 9819191919))
    connection.commit()
    res = connection.execute("SELECT * FROM USERS")
    for i in res:
        print("user", i[0])
        print("pass", i[1])
        print("email", i[2])
        print("con", i[4])
        

    connection.close()

def cloudConnection():
        
    config = {  
        'user': 'admin',
        'password': 'RSBEAFVWPHCSDPXM',
        'host': 'aws-us-east-1-portal.23.dblayer.com',
        'port': 29624,
        'database': 'compose',

        # Create SSL connection with the se lf-signed certificate
        'ssl_verify_cert': True,
        'ssl_ca': 'cert.pem'
         }
    connect = mysql.connector.connect(**config)  
    cur = connect.cursor()  
    cur.execute("SHOW DATABASES")

    for row in cur:  
        print(row[0])

    connect.close()

        
def cloudConnectiontwo():
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

    query = "SELECT * from lokesh where username='lokesh';"
    stmt = ibm_db.exec_immediation(conn, query)
    st = ibm_db.fetch_both(stmt)
    
           

    
    

cloudConnectiontwo()        
