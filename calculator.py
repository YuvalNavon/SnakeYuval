def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if (y!=0):
        return x / y


def main():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    while True:
        choice = input("Enter choice (1,2,3,4): ")
        if choice == "EXIT": break
        else:
            a = float(input("Enter first number"))
            b = float(input("Enter second number"))
            if (choice == "1"): print(add(a,b))
            if (choice == "2"): print(subtract(a,b))
            if (choice == "3"): print(multiply(a,b))
            if (choice == "4"): print(divide(a,b))


if __name__ == '__main__':
    main()
