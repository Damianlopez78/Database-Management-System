import pymysql

#this scipt will connect to MySQL work bech database
#replace password with your password
#db=yourDBnamehere with the name of the Database
#then you can call setDB anywhere in this project where we have to use the DB
def setDB():
    connection = pymysql.connect(host='localhost',user='root',password='alejandra96',db='cs631_db',autocommit=True)
    cursor = connection.cursor()
    return cursor