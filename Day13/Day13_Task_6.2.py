class Class1:
    def method1(self):
        print("method1 of Class1")

    def method2(self):
        print("methon2 of Class1")

class Class2(Class1):
    def method2(self):
        print("method2 of Class2")
    def method3(self):
        print("method3 of Class2")

c1 = Class1()
c1.method1()
c1.method2()

c2 = Class2()
c2.method1()
c2.method2()
c2.method3()