# from html file take out the links and copy it in new text file
with open ("D:\\Mrunali\\Python_pratice\\ch18\\exercise2html.html",'r') as rf:
    with open("D:\\Mrunali\\Python_pratice\\ch18\\file5.txt",'a') as wf:
    # with open("file5.txt",'a') as wf:
        for line in rf.readlines():
            if '<a href=' in line:
                pos=line.find('<a href=')
                first=line.find('\"',pos)
                second=line.find('\"',pos)
                url=line[first+1:second]
                wf.write(url)