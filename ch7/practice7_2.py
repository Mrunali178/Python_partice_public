# update dict (update method)
user_info={
    'name': 'yash',
    'age': 24,
    'fav_movie': ['coco','3 idiots'],
    'fav_tune':['MI Remix' , 'armor']
}
more_info = {'State': 'Indore','hobbies': ['art','reading']}
user_info.update(more_info) # this method will add elements to the original dict
# the error (unhashable type: 'dict') will occur if we write as ser_info.update({more_info})
print(user_info) #o/p-> {'name': 'yash', 'age': 24, 'fav_movie': ['coco', '3 idiots'], 
#'fav_tune': ['MI Remix', 'armor'], 'State': 'Indore', 'hobbies': ['art', 'reading']}

#now if we have same key in both dict so it will replace the old with new example-
more_info = {'State': 'MP','hobbies': ['art','reading']}
user_info.update(more_info)
print(user_info) #o/p-> {'name': 'yash', 'age': 24, 'fav_movie': ['coco', '3 idiots'], 
#'fav_tune': ['MI Remix', 'armor'], 'State': 'MP', 'hobbies': ['art', 'reading']} state is replaced by Mp[ pehel indore tha]

#if we wirte user_info.update({})
#print(user_info) this will not remove list but tells that no elemnt is added to the dict

#fromkeys method sare keys ko same value deni ho to use hota h
d=dict.fromkeys(['name','age','height'],'unknown')
print(d) #o/p-> {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

d=dict.fromkeys(('name','age','height'),'unknown') # can be a tuple
print(d) #o/p-> {'name': 'unknown', 'age': 'unknown', 'height': 'unknown'}

d=dict.fromkeys('abc','unknown') #string
print(d) #o/p-> {'a': 'unknown', 'b': 'unknown', 'c': 'unknown'}

d=dict.fromkeys(range(0,6),'unknown') #range
print(d) #o/p-> {0: 'unknown', 1: 'unknown', 2: 'unknown', 3: 'unknown', 4: 'unknown', 5: 'unknown'}

d=dict.fromkeys(['name','age','height'],['unknown','unknown'])
print(d) #o/p-> ['unknown', 'unknown'], 'age': ['unknown', 'unknown'], 'height': ['unknown', 'unknown']}

#get method
d={'name': 'Yash', 'age': 'unknown', 'height': 'unknown'}
print(d['name']) #o/p -> Yash
#print(d['names']) # will give error as no names key is present KeyError: 'names'
print(d.get('names')) # o/p-> none, it don't gives error

if 'name' in d: # checks if key exists in dictionary
    print('present')
else:
    print('not present')

# this (above) --> same can be done using get()
if d.get('names'):
    print('yes')
else:
    print("No")

print(d.get('names',"not found!!")) # none replaced with not found!!

# clear--> will make list empty
#d.clear()
#print(d)

#copy --> will make copy in other dict
# means ek alg dict bana degi aur uspe koi action perform hoga to vo original ko affecty nhi krega 
#pr agr d1=d kiya to isme same dict h ek ko chng kro dusra affect hoga
d1=d.copy()
print(d1.popitem())  #o/p--> ('height', 'unknown')
print(d) #o/p--> {'name': 'Yash', 'age': 'unknown', 'height': 'unknown'}
print(d1 is d) #o/p--> False (bcoz d1 and d are not at same memory place)

d1=d
print(d1.popitem())  #o/p--> ('height', 'unknown')
print(d) #o/p--> {'name': 'Yash', 'age': 'unknown'} 
print(d1 is d) #o/p--> True (bcoz d1 and d are  at same memory place)
