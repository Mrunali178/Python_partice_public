# define a function that takes input of every type of data and covert num to string using list comprehension
l=['true','false',[1,2,3],1,1.0,3]
res=[str(i) for i in l if (type(i)==int or type(i)==float)]
print(res)  #o/p--> ['1', '1.0', '3']
