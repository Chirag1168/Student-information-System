def test():
    a=[]
    n=input("enter the size of list")
    for i in range(0,n):
        ele=input("enter element")
        a.append(ele)
    sele=input("enter element to be search")
    i=0
    while(i<=n-1):
        if(a[i]==sele):
            print"element found at position ",i+1
            i=i+1
            break
        if(i==n):
            print"element not found"
            
        
    
    
    
    
    
