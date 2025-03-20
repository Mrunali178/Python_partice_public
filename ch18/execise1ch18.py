#text in file3 write it the string fromat in file4
with open('D:\\Mrunali\\Python_pratice\\ch18\\file3.txt','r') as rf:
    with open('D:\\Mrunali\\Python_pratice\\ch18\\file4.txt','w') as wf:
    # with open('file4.txt','w') as wf:
        for line in rf.readlines():
            name, salary = line.split(",") 
            wf.write(f"{name}'s salary is {salary}")