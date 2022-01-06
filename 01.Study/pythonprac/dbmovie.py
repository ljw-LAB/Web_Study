from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.o4ut0.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# movie = db.movies.find_one({'title':'가버나움'})
# print(movie['star'])

star_data = db.movies.find_one({'title':'가버나움'})

# all_movie = list(db.movies.find({'star' : '9.59'},{'_id':False}))
# print(all_movie)

# all_movie = list(db.movies.find({'star':star_data['star']},{'_id':False}))
# for m in all_movie :
#     print(m['title'])

db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})
