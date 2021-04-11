import math

def main():
    #my_dict = {}
    #for i in range(1,101):
    #    if i % 3 != 0:
    #       my_dict[i]= i**3
    #print(my_dict)        

    my_dict = {i: i**3 for i in range(1,101) if i % 3 !=  0}

    dict_reto = {i: math.sqrt(i) for i in range(1,1001)}
    
    print(dict_reto)

if __name__ == '__main__':
    main()