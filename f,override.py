class A:
    def putdata(self):
        print"this is class A"
class B(A):
    def putdata(self):
        A.putdata(self)
        print"this is class B"
def test():
    obj=B()
    obj.putdata()
