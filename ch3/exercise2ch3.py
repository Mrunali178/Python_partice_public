## and or in if else
# ask user name and age if name starts from a or A and age is above 10 he can watch coco movie else can't

name,age=input("Enter your name and age separated by comma: ").split(",")
age=int(age)
if ((name[0]=="a"or name[0]=="A") and age>=10):
   print("you can watch coco movie")
else:
    print('sorry, you cannot watch coco movie')