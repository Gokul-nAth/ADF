import time
try:
    n=int(input('Enter the prime limit : '))
    if(n<2):
        raise ValueError
    a=[True]*n
    for i in range(2,n):
        if(a[i]==True and (i*i)<n):
            for j in range(i*i,n,i):
                a[j]=False
    for i in range(2,n):
        if(a[i]==True):
            print(i)
            time.sleep(5)
except ValueError:
    print('Invalid input\nEnter a valid number')