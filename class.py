class room:
    l=0
    b=0
    a=0
    def getdata(self,l,b):
        self.l=l
        self.b=b
    def compute(self):
        self.a=self.l*self.b
        return self.a
def test():
    r=room()
    r.getdata(5,4)
    a=r.compute()
    print"area =",a
        
