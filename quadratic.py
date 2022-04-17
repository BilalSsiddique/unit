import math


def quadratic_func(a, b, c):
    if type(a) is int and type(b) is int and type(c) is int:
        disc = b * b - 4 * a * c
        if a > 0:
        
            if disc == 0:
                x1 = (-b + math.sqrt(disc)) / (2 * a)
                return (x1,)
            x1 = (-b + math.sqrt(disc)) / (2 * a)
            x2 = (-b - math.sqrt(disc)) / (2 * a)
            return x1, x2
        else:
            return -1
    else:
        return -1



# print(quadratic_func(2, 7, 5))
