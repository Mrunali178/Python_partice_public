# w --> write mode --> this will overide your file and if not exists will create it
with open ('D:\\Mrunali\\Python_pratice\\ch18\\file1.txt','w') as f:
    f.write("Welcome")

# a--> append mode --> this will append the item at the end (same as list vala append) and if file not present will create it
with open ('D:\\Mrunali\\Python_pratice\\ch18\\file1.txt','a') as f:
    f.write(" User")

# r+ --> this mode can read and write to a file if exists and if not it will give error. This will overwrite the part needed by it and other will be remained same
with open ('D:\\Mrunali\\Python_pratice\\ch18\\file1.txt','r+') as f:
    f.write(" Hi ")  #welcome wel is preplaced by hi 


# to avoid this replacement we can use 
with open ('D:\\Mrunali\\Python_pratice\\ch18\\file1.txt','r+') as f:
    f.seek(len(f.read()))  #this works here as r+ can read and and write both hence seek method will take cursor to the end and then write
    f.write(" Welcome ") 

#if you want to write the text from a file from one to another we can do like:
with open ("D:\\Mrunali\\Python_pratice\\ch18\\file.txt",'r') as rf:
    with open("D:\\Mrunali\\Python_pratice\\ch18\\file2.txt",'w') as wf:
        wf.write(rf.read())