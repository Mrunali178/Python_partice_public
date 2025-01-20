# take input from user name , age,favmovie and fav tune and print it in dictionary form but not in single line 
user={}
name=input("enter name : ")
age=input("enter age : ")
fav_movie=input("enter fav_movies seperated by comma: ").split(",")
fav_tune=input("enter fav_tunes seperated by comma: ").split(",")
user["name"]=name
user["age"]=age
user["fav_movie"]=fav_movie
user["fav_tune"]=fav_tune
for i,j in user.items():
    print(f'{i} , {j}') #for diffrent line 
