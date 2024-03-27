from multipledispatch import dispatch
class Claculator:
    @dispatch(int, int)
    def sum(self, x, y):
        print("Sum: ", x + y)

    @dispatch(int, int, int)
    def sum(self, x, y, z):
        print("Sum: ", x + y + z)

cal1 = Claculator()
cal1.sum(4, 5)
cal1.sum(3, 4, 5)
