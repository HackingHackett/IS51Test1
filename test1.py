def option1(): 
    x = 100 * 10
    return x

def option2(): 
    x =  (2**0 + 2**1 + 2**2 + 2**3 + 2**4 + 2**5 + 2**6 + 2**7 + 2**8 + 2**9)
    return x

def main():

    if option1() == option2():
        print('Option 1  and Option 2 pays the same')

    elif option1() > option2(): 
        print('Option 1 is better')     

    elif option1() < option2() :
        print('Option 2 is better')

main()