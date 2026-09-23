import mysql.connector
def connect_database():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="joneilestrada2007",
        database="FITTRACK")
    return connection
    
    