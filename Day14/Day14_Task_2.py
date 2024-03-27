class Mathematics:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __sub__(self, other):
        return self.x - other.x

    def __mul__(self, other):
        return self.x * other.x

    def __truediv__(self, other):
        if other.x != 0:
            return self.x / other.x
        else:
            print("Error: Can not divide a number with Zero")


mat1 = Mathematics(3)
mat2 = Mathematics(5)
print("Sum of Two numbers: ", mat1 + mat2)
print("Subtraction of Two numbers: ", mat1 - mat2)
print("Multiplication of Two numbers: ", mat1 * mat2)
print("Division of two numbers: ", mat1 / mat2)
