def test():
    d={}
    n=input("enter no of elements")
    for i in range(0,n):
        a=raw_input("enter name")
        b=raw_input("enter phno")
        d[a]=b
    nm=raw_input("enter name to be deleted")
    print "before deletion",d
    del d[nm]
    print "after deletion", d
