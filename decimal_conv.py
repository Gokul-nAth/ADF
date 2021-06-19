def dec_to_Bin(temp):
    ans=''
    while (temp != 0):
        if (temp % 2 == 0):
            ans='0'+ans
        else:
            ans='1'+ans
        temp = int(temp / 2)
    return ans

def dec_to_Oct(temp):
    oct=''
    while(temp!=0):
        oct=str(temp%8)+oct
        temp=int(temp/8)
    return oct;

def dec_to_Hex(temp):
    hex=''
    while(temp!=0):
        if(temp%16<10):
            hex=str(temp%16)+hex
        else:
            hex=chr((temp%16)+55)+hex
        temp=int(temp/16)
    return hex
try:
    num=int(input('Enter the decimal number : '))
    if(num<1):
        raise ValueError
    print('Decimal -> Binary : '+dec_to_Bin(num))

    print('Decimal -> Octal : '+dec_to_Oct(num))

    print('Decimal -> Hexa decimal : '+dec_to_Hex(num))
except ValueError:
    print('Enter a valid input')


