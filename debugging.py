def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0: 
           divisors.append(i)
    #divisors = [x for x in range(1, num+1) if num % x == 1]
    return divisors


def main():
    while True:
        try:
            num = int(input("Enter a valid number: "))
            if num < 0:
                raise ValueError("Negative Number is not valid")
            print(divisors(num))
            print("Ok programa")
            break
        except ValueError:
            print("String is no valid")
        except Exception:
            print("Negative Number is not valid")


if __name__ == '__main__':
    main()