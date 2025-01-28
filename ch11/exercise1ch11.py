# define a function as parameter give num,*args pass list in in *args and return a list which give the elements, formed by *args power num and if empty print a msg
# ex- nums=[1,2,3] to_power=(3,*nums) o/p--> [1,8,27]  1 cube =1 2 cube=8 3 cube=27
# using list comprehension
def to_power(num,*args):
   if args:
      return [i**num for i in args]
   else:
      return "You didn't passed any argument"
      

n=int(input("enter size of list"))

l=[]
for i in range(n):
   s=int(input(f"enter element in list at position {i+1}: "))
   l.append(s)

num=int(input("enter a number for power: "))

print(to_power(num,*l))