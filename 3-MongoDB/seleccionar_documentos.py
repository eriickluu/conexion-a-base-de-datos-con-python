from pymongo import MongoClient

client = MongoClient() #localhost 27017

db = client['minicurso_python']

if __name__ == '__main__':
    # users = db.users.find()
    # users = db.users.find({'age':23})
    # users = db.users.find({'age':23}).limit(2)
    # users = db.users.find({'age':23}).count()
    # print(users)
    # users = db.users.find( { "$or" : [ {"username:": "Erick"}, {"age" : 23} ] } )
    # users = db.users.find( { "$and" : [ {"username:": "Erick"}, {"age" : 23} ] } )

    # user = db.users.find_one()
    # print(user)
    user = db.users.find_one({'age' : 5})
    print(user)

    # for user in users:
    #     print(user)
