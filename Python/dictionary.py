
if __name__ == "__main__":
    my_car = {"Model": "Gold", "Year": 2013, "Color": "Red"}

    # Values and keys
    for value, key in zip(my_car.values(), my_car.keys()):
        print("{}: {}".format(key, value))

    # Get item
    print(f'My car is {my_car.get("Color")}')

    # Remove item
    my_car.pop("Color")
    print(my_car)

    # Merge dictionary
    owner = {"Owner_name": "Marcos", "Age": 26}

    print({**my_car, **owner})
