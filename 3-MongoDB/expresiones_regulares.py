from pymongo import MongoClient
import re

client = MongoClient() #localhost 27017

db = client['minicurso_python']

if __name__ == '__main__':
    # regex = re.compile('codigo')   # LIKE %codigo%
    # users = db.users.find_one({'username' : regex })
    # for user in users:
    #     print(user)

    # regex = re.compile('^codigo')  # LIKE %codigo
    # users = db.users.find_one({'username' : regex })
    # for user in users:
    #     print(user)

    regex = re.compile('codigo$')    # LIKE codigo%
    users = db.users.find_one({'username' : regex })
    for user in users:
        print(user)