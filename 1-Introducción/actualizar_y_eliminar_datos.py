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
UPDATE_USER = "UPDATE users SET username='{username}', password='{password}' WHERE id = {id}"
DELETE_USER = "DELETE FROM users WHERE id = {id}"

if __name__ == '__main__':
    try:
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)

        cursor = connection.cursor()
        
        cursor.execute(DROP_USER)
        cursor.execute(USER_TABLE)

        query = INSERT_USER.format(username='erick', password='password')
        
        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()

        query = UPDATE_USER.format(username='codigofacilito', password='123', id=1)

        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()

        query = SELECT_USER.format(id=1)
        print(query)

        cursor.execute(query)
        
        users = cursor.fetchall()

        print(users[0])

        query = DELETE_USER.format(id=1)

        try:
            cursor.execute(query)
            connection.commit()
        except:
            connection.rollback()

        connection.close()
    
    except MySQLdb.Error as error:
        print(error)