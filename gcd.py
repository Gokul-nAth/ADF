try:
    a=int(input('Enter the first numbers : '))
    b=int(input('Enter the second numbers : '))
    if(a>0 and b>0):
        smallest=a
        if(b<a):
            smallest=b
        for i in range(b,0,-1):
                if(a%i==0 and b%i==0):
                    print('GCD of given numbers : ',i)
                    break
    else:
        raise ValueError
except ValueError:
    print('Invalid input')
