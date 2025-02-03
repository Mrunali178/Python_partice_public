# define a generator which take one argument and print all even nums bettween it
def is_even(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
even_nums=is_even(6)
for i in even_nums:
    print(i)
for i in even_nums:
    print(i)
#this will  only loop once as we have generated sequence first in even_nums but if we directly use is_even with for loop it can be used many times
for i in is_even(4):
    print(i)
for i in is_even(4):
    print(i)