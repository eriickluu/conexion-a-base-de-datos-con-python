import pymysql as MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = 'toor'
DATABASE = 'minicurso_python'

USER_TABLE = """CREATE TABLE users(
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL
                )"""

DROP_USER = "DROP TABLE IF EXISTS `users`"
SHOW_TABLES = "SHOW TABLES"
INSERT_USER = "INSERT INTO users (username, password) VALUES ('{username}', '{password}')"
SELECT_USER = "SELECT * FROM users WHERE id = {id}"

if __name__ == '__main__':
    try:
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)

        cursor = connection.cursor()
        
        cursor.execute(DROP_USER)
        cursor.execute(USER_TABLE)

        username = input("Ingrese el username:")
        password = input("Ingrese el password:")

        query = INSERT_USER.format(username=username, password=password)
        print(query)
        
        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()

        query = SELECT_USER.format(id=1)
        print(query)

        cursor.execute(query)
        
        users = cursor.fetchall()
        
        # for user in users:
        #     print(user)

        print(users[0])

        connection.close()
    
    except MySQLdb.Error as error:
        print(error)
