import math
import cmath


def quadratic_func(a, b, c):
    try:

        lst = [a, b, c]
        if all(isinstance(n, int) for n in lst) or all(isinstance(n, float) for n in lst):
            disc = b * b - 4 * a * c

            if a != 0:

                if disc == 0:
                    x1 = (-b + math.sqrt(disc)) / (2 * a)
                    return (x1,)
                elif disc > 0:
                    x1 = (-b + math.sqrt(disc)) / (2 * a)
                    x2 = (-b - math.sqrt(disc)) / (2 * a)
                    return x1, x2
                else:
                    x1 = (-b + cmath.sqrt(disc)) / (2 * a)
                    x2 = (-b - cmath.sqrt(disc)) / (2 * a)
                    return x1, x2

            else:
                return -1
        else:
            return -1
    except ValueError or TypeError:
        return lst


# print(quadratic_func(1,-4, 8))
