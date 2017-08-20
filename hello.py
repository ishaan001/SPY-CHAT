



locat="Delhi"
if __name__=='main':
    print "hello world"
    for i in range(10,20,2):
        print i
    fibo=[]
    a,b=0,1
    while(b<1000):
        fibo.append(a)
        a,b=b,a+b
    print fibo

