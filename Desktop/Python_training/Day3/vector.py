class Vector:

    """Vector class => supports add, sub and string disply
       Methods:
            __str__() - human-readable representation of  vector.
            __add__() - Add two vectors
            __sub__() - subtract two vectors
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

# main function
if __name__ == '__main__':

    # vector input
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)

    print("Vector 1:", v1)
    print("Vector 2:", v2)

    # add two vectors
    v3 = v1 + v2
    print("v1 + v2 =", v3)

    # subtract two vectors
    v4 = v1 - v2
    print("v1 - v2 =", v4)