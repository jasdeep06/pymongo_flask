from pymongo import MongoClient
from pprint import pprint

#mongo client
client=MongoClient("Your URI")

#exercise1 database
db=client['exercise1']

#movies collection
movies=db["movies"]

#documents
info=[{"title" : "Fight Club",
"writer" : "Chuck Palahniuk",
"year" : 1999,
"actors" : [
  "Brad Pitt",
  "Edward Norton"
]},
{"title" : "Pulp Fiction",
"writer" : "Quentin Tarantino",
"year" : 1994,
"actors" : [
  "John Travolta",
  "Uma Thurman"
]},

{"title" : "Inglorious Basterds",
"writer" : "Quentin Tarantino",
"year" : 2009,
"actors" : [
  "Brad Pitt",
  "Diane Kruger",
  "Eli Roth"
]},
{"title" : "The Hobbit: The Desolation of Smaug",
"writer" : "J.R.R. Tolkein",
"year" : 2013,
"franchise" : "The Hobbit"
},
{"title" : "The Hobbit: An Unexpected Journey",
"writer" : "J.R.R. Tolkein",
"year" : 2012,
"franchise" : "The Hobbit"
 },
{"title" : "The Hobbit: The Battle of the Five Armies",
"writer": "J.R.R. Tolkein",
"year" : 2012,
"franchise" : "The Hobbit",
"synopsis" : "Bilbo and Company are forced to engage in a war against an array of combatants and keep the Lonely Mountain from falling into the hands of a rising darkness."
},
{
"title" : "Pee Wee Herman's Big Adventure"
},
{
"title" : "Avatar"
}
]


#inserting documents
movies.insert_many(info)

#getting all documents
for movie in movies.find():
    pprint(movie)

#get all documents with writer set to "Quentin Tarantino"
for movie in movies.find({"writer":"Quentin Tarantino"}):
    pprint(movie)

#get all documents where actors include "Brad Pitt"
for movie in movies.find({"actor":"Brad Pitt"}):
    pprint(movie)

#get all documents with franchise set to "The Hobbit"
for movie in movies.find({"franchise":"The Hobbit"}):
    pprint(movie)

#get all movies released in the 90s
for movie in movies.find({"year":{"$lt":2000}}):
    pprint(movie)

#get all movies released before the year 2000 or after 2010
for movie in movies.find({"$or":[{"year":{"$lt":2000}},{"year":{"$gt":2010}}]}):
    pprint(movie)


#add a synopsis to "The Hobbit: An Unexpected Journey" : "A reluctant hobbit, Bilbo Baggins,
# sets out to the Lonely Mountain with a spirited group of dwarves to reclaim their mountain home -
# and the gold within it - from the dragon Smaug."
movies.update_one({"title":"The Hobbit: An Unexpected Journey"},{"$set":{"synopsis":"A reluctant hobbit, Bilbo Baggins,\
 sets out to the Lonely Mountain with a spirited group of \
dwarves to reclaim their mountain home - and the gold within it - from the dragon Smaug."}})

#add a synopsis to "The Hobbit: The Desolation of Smaug" : "The dwarves, along with Bilbo Baggins and
# Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug. Bilbo Baggins
#  is in possession of a mysterious and magical ring."
movies.update_one({"title":"The Hobbit: The Desolation of Smaug"},{"$set":{"synopsis":"The dwarves, along with\
 Bilbo Baggins and Gandalf the Grey, continue their quest to reclaim Erebor, their homeland, from Smaug.\
  Bilbo Baggins is in possession of a mysterious and magical ring."
}})

#add an actor named "Samuel L. Jackson" to the movie "Pulp Fiction"
movies.update_one({"title":"Pulp Fiction"},{"$addToSet":{"actors":"Samuel L. Jackson"}})

#find all movies that have a synopsis that contains the word "Bilbo"
movies.create_index([('synopsis','text')])
for movie in movies.find({"$text":{"$search":"Bilbo"}}):
    pprint(movie)

#find all movies that have a synopsis that contains the word "Gandalf"
for movie in movies.find({"$text":{"$search":"Gandalf"}}):
    pprint(movie)

#find all movies that have a synopsis that contains the phrase "Gandalf the Grey" exactly
#Wrap exact quotes around double quotes
for movie in movies.find({"$text":{"$search":"\"Gandalf The Grey\""}}):
    pprint(movie)

#find all movies that have a synopsis that contains the word "Bilbo" and not the word "Gandalf"
#precede word to be ommited by hyphen
for movie in movies.find({"$text":{"$search":"Bilbo -Gandalf"}}):
    pprint(movie)

#find all movies that have a synopsis that contains the word "dwarves" or "hobbit"
for movie in movies.find({"$text":{"$search":"dwarves hobbit"}}):
    pprint(movie)

#find all movies that have a synopsis that contains the word "gold" and "dragon"
for movie in movies.find({"$text":{"$search":"\"gold\" \"dragon\""}}):
    print(movie)


#delete the movie "Pee Wee Herman's Big Adventure"
movies.delete_one({"title":"Pee Wee Herman's Big Adventure"})

#delete the movie "Avatar"
movies.delete_one({"title":"Avatar"})

#create "users" collection
users=db["users"]

users_info=[{"username" : "GoodGuyGreg",
"first_name" : "Good Guy",
"last_name" : "Greg"},
            {
"username" : "ScumbagSteve",
"full_name" :
    {"first" : "Scumbag",
  "last" : "Steve"
     }}]

#insert user_info to "users"
users.insert_many(users_info)

post_info=[{"username" : "GoodGuyGreg",
"title" : "Passes out at party",
"body" : "Wakes up early and cleans house"},{"username" : "GoodGuyGreg",
"title" : "Steals your identity",
"body" : "Raises your credit score"
},{
"username" : "GoodGuyGreg",
"title" : "Reports a bug in your code",
"body" : "Sends you a Pull Request",
},{
"username" : "ScumbagSteve"
,"title": "Borrows something",
"body" : "Sells it",
},{
"username" : "ScumbagSteve",
"title" : "Borrows everything",
"body" : "The end"
},{
"username" : "ScumbagSteve",
"title" : "Forks your repo on github",
"body" : "Sets to private"
}

]

posts=db["posts"]

#inset post_info to posts
posts.insert_many(post_info)

comments=db["comments"]

comments_info=[{"username" : "GoodGuyGreg",
"comment" : "Hope you got a good deal!",
"post" : posts.find_one({"title":"Borrows something"})["_id"]},
               {"username" : "GoodGuyGreg",
"comment" : "What's mine is yours!",
"post" : posts.find_one({"title":"Borrows everything"})["_id"]},
               {"username" : "GoodGuyGreg",
"comment" : "Don't violate the licensing agreement!",
"post" : posts.find_one({"title":"Forks your repo on github"})["_id"]},
{"username" : "ScumbagSteve",
"comment" : "It still isn't clean",
"post" : posts.find_one({"title":"Passes out at party"})["_id"]},
{"username" : "ScumbagSteve",
"comment" : "Denied your PR cause I found a hack",
"post" : posts.find_one({"title":"Reports a bug in your code"})["_id"]}]

#insert comments_info to "comments"
comments.insert_many(comments_info)

#find all users
for user in users.find():
    print(user)

#find all posts
for post in posts.find():
    print(post)

#find all posts that was authored by "GoodGuyGreg"
for post in posts.find({"username":"GoodGuyGreg"}):
    print(post)

#find all posts that was authored by "ScumbagSteve"
for post in posts.find({"username":"ScumbagSteve"}):
    print(post)

#find all comments
for comment in comments.find():
    print(comment)

#find all comments that was authored by "GoodGuyGreg"
for comment in comments.find({"username":"GoodGuyGreg"}):
    print(comment)

#find all comments that was authored by "ScumbagSteve"
for comment in comments.find({"username":"ScumbagSteve"}):
    print(comment)

#find all comments belonging to the post "Reports a bug in your code"
for comment in comments.find({"post":posts.find_one({"title":"Reports a bug in your code"})["_id"]}):
    print(comment)