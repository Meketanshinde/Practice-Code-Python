def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)
    
num = 5
if num<0:
    print('Enter positive Number')
elif num==0:
    print('Factorial is 0')
else:
    print('Factorial of number',num, 'is:' ,factorial(num))