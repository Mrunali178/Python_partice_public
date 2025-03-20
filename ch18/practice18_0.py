#read method ---> reads file data
#open method --> open file using path
#close method ---> closes file 
#tell method --> tell position of cursor

f = open('D:\\Mrunali\\Python_pratice\\ch18\\file.txt')
print(f"cursor position - {f.tell()}")  #o/p--> cursor position - 0
print(f.read())
print(f"cursor position - {f.tell()}")   #o/p--> cursor position - 178
print(f.read())                          
print(f"cursor position - {f.tell()}")   #o/p--> cursor position - 178
f.close()

#the object f can also be iterated using for loop
print("for loop")
f = open('D:\\Mrunali\\Python_pratice\\ch18\\file.txt')
for line in f:
    print(line,end='')
f.close()

#o/p-->Raising errors prevents unexpected behavior
        # Helps in debugging by showing where things go wrong
        # Enforces correct input and program flow
        # Allows us to handle exceptions properlyend of this starting next method


print("end of this starting next method")
#o/p--> Raising errors prevents unexpected behavior
        # Helps in debugging by showing where things go wrong
        # Enforces correct input and program flow
        # Allows us to handle exceptions properly

#this is the o/p as the cursor moved and last and when we again called read method the cursor started from the position it left from and there was nothing

#seek method is used to chng position of the cursor
f = open('D:\\Mrunali\\Python_pratice\\ch18\\file.txt')
print(f"cursor position - {f.tell()}")  #o/p--> cursor position - 0
print(f.read())
print(f"cursor position before seek method - {f.tell()}")   #o/p--> cursor position - 178
f.seek(0)
print(f"cursor position after seek method - {f.tell()}")
print(f.read())                          
print(f"cursor position - {f.tell()}")   #o/p--> cursor position - 178
f.close()


#o/p--> 
        # cursor position - 0
        # Raising errors prevents unexpected behavior
        # Helps in debugging by showing where things go wrong
        # Enforces correct input and program flow
        # Allows us to handle exceptions properly
        # cursor position before seek method - 178

        # cursor position after seek method - 0
        # Raising errors prevents unexpected behavior
        # Helps in debugging by showing where things go wrong
        # Enforces correct input and program flow
        # Allows us to handle exceptions properly
        # cursor position - 178

#readline method  --> reads one line at a time
print()
print("readline method")

f = open('D:\\Mrunali\\Python_pratice\\ch18\\file.txt')
print(f"cursor position - {f.tell()}")  #o/p--> cursor position - 0
print(f.readline())   #o/p--> Raising errors prevents unexpected behavior

print(f"cursor position - {f.tell()}")   #o/p--> cursor position - 45
print(f.readline())                      #o/p--> Helps in debugging by showing where things go wrong 
f.close()


#readlines method  --> read lines in form of list can also be iterated using for loop
print()
print("readlines method")

f = open('D:\\Mrunali\\Python_pratice\\ch18\\file.txt')
lines=f.readlines()
print(lines)   #o/p--> ['Raising errors prevents unexpected behavior\n', 'Helps in debugging by showing where things go wrong\n', 'Enforces correct input and program flow\n', 'Allows us to handle exceptions properly']
print(len(lines))   #o/p--> 4
for line in lines: 
    print(line, end='')  #using end as for loop automatically chngs line and same print so 1 line will be left extra
f.close() 

#o/p of for loop -->
                # Raising errors prevents unexpected behavior
                # Helps in debugging by showing where things go wrong
                # Enforces correct input and program flow
                # Allows us to handle exceptions properly


#to display name of file we use data descriptor name(its not method we don't need to use parenthesis) and to see our file is closed or not we use close
print()
print(f.name)  #o/p-->D:\Mrunali\Python_pratice\ch18\file.txt
print(f.closed)  #o/p--> True

#slicing can also be performed
print("slicing can also be done")
f = open('D:\\Mrunali\\Python_pratice\\ch18\\file.txt')
for line in f.readlines()[:2]:
    print(line,end='')
f.close()

#o/p-->Raising errors prevents unexpected behavior
        # Helps in debugging by showing where things go wrong


# with block

# The with statement is used to handle resources (like files, network connections, or database connections) efficiently. It ensures that the resource is properly closed after its use, even if an error occurs
# Benefits of with block:
# No need to manually close the file.
# Even if an error occurs inside the block, Python ensures the file is closed properly.
# Code is cleaner and more readable.
with open(r'D:\Mrunali\Python_pratice\ch18\file.txt') as f:
    data=f.read()
    print(data)
print(f.closed)  #o/p--> True