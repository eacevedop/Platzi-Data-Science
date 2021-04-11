def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0: 
           divisors.append(i)
    #divisors = [x for x in range(1, num+1) if num % x == 1]
    return divisors


def main():    
    while True:
        num = input("Enter a valid number: ")
        assert num.isnumeric(), "String is not valid"   
        print(divisors(int(num)))
        print("Ok programa")
        break
        
        


if __name__ == '__main__':
    main()