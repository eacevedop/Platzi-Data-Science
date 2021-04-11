def main():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Edwin", "Lastname": "Acevedo"}

    super_list = [
        {"firstname": "Edwin", "Lastname": "Acevedo"},
        {"firstname": "Miguel", "Lastname": "Acevedo"},
        {"firstname": "Pepe", "Lastname": "Acevedo"},
        {"firstname": "José", "Lastname": "Acevedo"},
        {"firstname": "Edwin", "Lastname": "Acevedo"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 5.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    main()