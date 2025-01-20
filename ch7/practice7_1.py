# in  keyword checks for the key
user_info={
    'name': 'yash',
    'age': 24,
    'fav_movie': ['coco','3 idiots'],
    'fav_tune':['MI Remix' , 'armor']
}
if 'name' in user_info: # checks if key exists in dictionary
    print('present')
else:
    print('not present')

if 'yash' in  user_info:
    print("yes") # this will give o/p no as in keyword only checks for the key and not value
else:
    print('no')

# to check values we can use value method
if 'yash' in user_info.values(): ##o/p-> true
    print("true")
else:
    print('false')

if ['coco'] in user_info.values(): ##o/p-> false puri list daalni padegi
    print("true")
else:
    print('false')

# loops  for loop
for i in user_info: # will print all the keys
    print(i) #o/p-> name
                    # age
                    # fav_movie
                    # fav_tune
# for values
for i in user_info.values(): # will print all the keys
    print(i) #o/p-> yash
                    # 24
                    # ['coco', '3 idiots']
                    # ['MI Remix', 'armor']

# this can be written as
for i in user_info:
    print(user_info[i]) # it's o/p will be same as above will print all the values 

# in for loop it is being printed like this as:-
# values method
user_info_qbc=user_info.values()
print (user_info_qbc) #o/p-|> dict_values(['yash', 24, ['coco', '3 idiots'], ['MI Remix', 'armor']])
print(type(user_info_qbc)) #o/p--> <class 'dict_values'>
# it is like list but we cann't chng it but can iterate thru it

# key method
user_info_keys=user_info.keys()
print (user_info_keys) #o/p-|> dict_keys(['name', 'age', 'fav_movie', 'fav_tune'])
print(type(user_info_keys)) #o/p--> <class 'dict_keys'>
# it ios like list but we cann't chng it but can iterate thru it

#items method
user_items=user_info.items() # this prints the dic in form of tuple and type dict_items
print(user_items) #o/p-> dict_items([('name', 'yash'), ('age', 24), ('fav_movie', ['coco', '3 idiots']), ('fav_tune', ['MI Remix', 'armor'])])
#so in for loop it can print both key and value
for i,j in user_info.items():
    print(f"key is {i} value is {j}") #o/p--> key is name value is yash
                                        # key is age value is 24
                                        # key is fav_movie value is ['coco', '3 idiots']
                                        # key is fav_tune value is ['MI Remix', 'armor']
for i in user_info.items():
    print(i) # will print in form of tuple

# add item in dict
user_info['fav songs'] = ['song1','song2']
print(user_info)

#pop method remove key value pair from dict but here we have to pass atleast 1 parameter
popped_item=user_info.pop('age')
print(user_info) #o/p-> {'name': 'yash', 'fav_movie': ['coco', '3 idiots'], 'fav_tune': ['MI Remix', 'armor'], 'fav songs': ['song1', 'song2']}     
print(popped_item) #24 #this method return popped element type jo bhi element delted h vo iska type hota h
print(type(popped_item)) # o/p-> <class 'int'>

#popitem method-> it will delete last key value pair and will return it in type tuple
poped=user_info.popitem()
print(user_info) # o/p-> {'name': 'yash', 'fav_movie': ['coco', '3 idiots'], 'fav_tune': ['MI Remix', 'armor']}
print(poped) # o/p-> ('fav songs', ['song1', 'song2'])
print(type(poped)) # o/p-> <class 'tuple'>


