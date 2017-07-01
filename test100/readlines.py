f=open('D:/djangoworkspace/test100/test.txt','r')
for line in f.readlines():
    print (line.strip())
    f.close()