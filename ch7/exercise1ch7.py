# define a function that takes a number(n) and return a dictionary containing cube of numbers from 1 to n
def cube_finder(n):
    cubes={}
    for i in range(1,n+1): #as range is started from 1 range is stoped at n+1
       cubes[i]=i**3 
    return cubes
num=int(input("enter a number: "))
print(cube_finder(num))


#word counter -> how many times letter repeated in a word
def word_count(s):
    counter={}
    for i in s:
        counter[i]=s.count(i)
    return counter
print(word_count('yasssh')) # o/p--> {'y': 1, 'a': 1, 's': 3, 'h': 1}