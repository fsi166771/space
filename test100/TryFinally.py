try:
    f=open('d:/djangoworkspace/test100/test.txt','r')
    print f.read()

finally:
    if f:
        f.close()