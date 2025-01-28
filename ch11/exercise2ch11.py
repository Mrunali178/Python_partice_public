# define a function which consist of list and return a list consisting reverse with 1st letter capital
def fun(l,**kwargs):
    if kwargs.get('reverse_str')==True:
        return[i[::-1].title() for i in l]
    else:
        return [i.title() for i in l] 
l=["harshit","yash"]
print(fun(l,reverse_str=True))