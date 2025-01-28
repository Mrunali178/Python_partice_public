# *args or * operator --> used to make functions more flexible means no need to pass number of arguments it takes it itself

#normal function
def total(a,b):  # two parameters passed hence only two arguments can be passed and not more than that
    return a+b
print(total(1,2))  #o/p-->  3

# but with * opertaor can pass any number of arguments it take arguments in the form of tuple

def all_total(*args):
    # print(args)  #o/p--> (1, 2, 3, 4)
    # print(type(args)) #o/p--> <class 'tuple'>
    # print(args) #o/p--> () whan no argument passed it will not give error but a empty tuple
    #for total sum
    total=0
    for i in args:
        total+=i
    return total

# all_total(1,2,3,4)
print(all_total(1,2))  #o/p--> 3
print(all_total(1,2,3,4))  #o/p--> 10
print(all_total())  #o/p--> 0


# *args with normal parameter
def mul_para(num,*args):
    print(args) 
    multiply=1 
    for i in args:
        multiply*=i
    return multiply
print(mul_para(1,2)) # now since the num parameter is compulsary 1st argument is must as if no argument is passed it will give an error-->missing 1 required positional argument: 'num'
# print(mul_para())  # and will leave 1st and take other in the tuple also normal parameter after * parameter iws not allowed


#*args as argument
def mul_num(*args):
    mul=1
    print(args)  #1st o/p-->  ([2, 3, 4],) # 2nd o/p--> (2, 3, 4) after unpacking values
    for i in args:
        mul*=i
    return mul
nums=[2,3,4]
print(mul_num(nums)) # o/p-->  [2, 3, 4]
#it will directly pass the list hence it will be like([2,3,4]) and hence no multiplication will be performed so to solve this we use * as argument
print(mul_num(*nums)) # #o/p--> 24
# it will unpack the values of the list hence multiplication will be performed 