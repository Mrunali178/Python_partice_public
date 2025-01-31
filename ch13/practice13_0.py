# enumerte function
# used with for loop to track position along with item
# normally we can do it as
names=['abc','abcde','abcdef']
pos=0
for i in names:
    print(f"{pos}--> {i}")
    pos+=1
#o/p---> 0--> abc
        # 1--> abcde
        # 2--> abcdef
# with enumerate

for position,i in enumerate (names):
        print(f"{position}--->{i}")
# o/p---> 0--->abc
        # 1--->abcde
        # 2--->abcdef

# define function with 2 arguments list and a string to find position and if present or not if not return -1
def strs(l,s):
    for pos,i in enumerate(l):
        if i==s:
            return pos,i
    return -1
l=['abc','123','mru']
s=input("enter string you want to know position of: ")
print(strs(l,s))
# o/p--> enter string you want to know position of: abcde
# -1
# enter string you want to know position of: 123
# (1, '123')