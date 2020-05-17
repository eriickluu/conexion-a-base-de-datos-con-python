import pymysql as MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = 'toor'
DATABASE = 'minicurso_python'

if __name__ == '__main__':
    try:
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)

        cursor = connection.cursor()

        connection.close()
    
    except MySQLdb.Error as error:
        print(error)
