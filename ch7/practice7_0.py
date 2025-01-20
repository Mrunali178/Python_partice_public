#dictionaries
#key:value
user={'name': 'Mrunali', 'age':20}
print(user)  #o/p--> {'name': 'Mrunali', 'age': 20}
print(type(user)) #o/p--> <class 'dict'>

#also can be created as
user1=dict(name='yash',age=24)
print(user1)  #o/p--> {'name': 'yash', 'age': 24}
print(type(user1))#o/p--> <class 'dict'>

# there is no indexing in dictionaries due to unordered collection of data so to print values of dict we use key
print(user['name']) #o/p--> Mrunali

# anything can be stored in dict
#list in dict
user_info={
    'name': 'yash',
    'age': 24,
    'fav_movie': ['coco','3 idiots'],
    'fav_tune':['MI Remix' , 'armor']
} #this type of syntax is used for better readability
print(user_info) #o/p--> {'name': 'yash', 'age': 24, 'fav_movie': ['coco', '3 idiots'], 'fav_tune': ['MI Remix', 'armor']}
print(user_info['fav_movie']) #o/p--> ['coco', '3 idiots']

# dict in dict this will be studied later abhi erroe aara h
info={
    'user_info1' : {
    'name': 'yash',
    'age': 24,
    'fav_movie': ['coco','3 idiots'],
    'fav_tune':['MI Remix' , 'armor']
    },
    'user_info2':
    {
    'name': 'mru',
    'age': 20,
    'fav_movie': ['coco','3 idiots'],
    'fav_tune': ['MI Remix' ,'armor']
    }

}
print(info['user_info1'])  #o/p--> {'name': 'yash', 'age': 24, 'fav_movie': ['coco', '3 idiots'], 'fav_tune': ['MI Remix', 'armor']}
print(info['user_info1']['name']) #o/p--> yash
print(info['user_info1']['fav_tune'][0]) #o/p-> MI Remix

# add data to empty dict
users={}
users['name']='Ram'
print(users) #o/p--> {'name': 'Ram'}
users['age']=18
print(users) #o/p--> {'name': 'Ram', 'age': 18}