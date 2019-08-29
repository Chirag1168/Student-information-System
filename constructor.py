class person():
    ag=0
    nm=None

    def __init__(self):
        self.ag=input("enter age")
        self.nm=raw_input("enter name")
    def putdata(self):
        print"age=",self.ag
        print"name=",self.nm
class student(person):
    tf=0
    lf=0
    ttf=0
    def __init__(self):
        person.__init__(self)
        self.tf=input("enter tution fees")
        self.lf=input("enter libary fees ")
    def compute(self):
        self.ttf=self.tf+self.lf
    def showdata(self):
        print"tution fees=",self.tf
        print"libary fees=",self.lf
        print"total fees=",self.ttf
def test():
    stu=student()
    stu.compute()
    stu.putdata()
    stu.showdata()
        
