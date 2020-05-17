from pymongo import MongoClient

client = MongoClient() #localhost 27017

db = client['minicurso_python']

if __name__ == '__main__':
    # db.users.update({'age': 23}, {'$set' : { 'age' : 24} } )
    # db.users.update_many({'age': 5}, {'$inc' : { 'age' : 1} } )

    # db.users.delete_one({'age': 24})
    db.users.delete_many({'age': 6})