import math
from typing import Callable, Any

if __name__ == "__main__":
    # Return absolute value of a number (negative converted to positive)
    print(abs(-2.4))
    # Return bytes of something
    print((bytes(200)))
    # Enumerate
    for index, item in enumerate(["red", "blue", "grenn"]):
        print("Index: {}, item: {}".format(index, item))

    # Filter numbers in array
    def is_odd(number):
        return number % 2 != 0


    print(list(filter(is_odd, [1, 2, 3, 4, 5, 6])))

    # Hash value
    print(hash("Marcos"))

    # Return number rounded
    print(round(1.111, 2))

    # Iterate trough two or more arrays (zip)
    for item, price, release_year in zip(["Table", "Chair"], ["$223", "$192"], ["2022", "2021"]):
        print("Item: {}, Price: {}, Released year: {}".format(item, price, release_year))

    # lambda functions
    root_square: Callable[[Any], float] = lambda x: math.sqrt(x)
    print(root_square(64))
