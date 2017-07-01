#coding=utf-8
f=open('D:/djangoworkspace/test100/test.txt','rb')
u = f.read().decode('gbk')
print u
f.close()


import codecs
with codecs.open('D:/djangoworkspace/test100/test.txt','r','utf-8') as ff:
    print ff.read()

