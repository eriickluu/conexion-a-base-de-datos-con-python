import peewee 
import datetime

HOST = 'localhost'
USER = 'root'
PASSWORD = 'toor'
DATABASE = 'minicurso_python'

database = peewee.MySQLDatabase(DATABASE, host=HOST, port=3306, user=USER, passwd=PASSWORD)

class User(peewee.Model):
    username = peewee.CharField(unique=True, max_length=50, index=True)
    password = peewee.CharField(max_length=50, null=True)
    email = peewee.CharField(max_length=50)
    active = peewee.BooleanField(default=True)
    created_date = peewee.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = database
        db_table = 'users'

    def __str__(self):
        return self.username

if __name__ == '__main__':
    
    # count = User.select().count()
    # count = User.select().where(User.id > 2).count()
    # print(count)

    # users = User.select().where(User.id > 1).limit(2)
    # users = User.select().where(User.id > 1).order_by(User.id.asc())
    # users = User.select().where(User.id > 1).order_by(User.id.desc())
    # users = User.select().where(User.id > 1).order_by(+User.id)
    # users = User.select().where(User.id > 1).order_by(-User.id)
    # for user in users:
    #     print(user)
    last = User.select().order_by(User.id.desc()).limit(1).get()
    print(last)

    
