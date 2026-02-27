
def outer_function(x: int):
    def inner_function(y: int):
        return x + y
    return inner_function



add_10 = outer_function(10)
print(add_10(10))

def square_of(x: int):
    def number(y: int):
        return y ** x
    return number


square_of_2 = square_of(2)
print(square_of_2(6))