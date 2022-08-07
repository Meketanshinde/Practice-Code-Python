#Types of function

'''def type1(): #no para no return type
    print('Good morning')
type1()

def type2(a,b): # parameter no return type
    print('Addition',a+b)
type2(2,3)

def type3(): # no para return  type
    return print('This too shall pass')
type3()

def type4(c,d): #para with return type 
    return print('division',c/d)
type4(10,2)'''


'''def addition(a,b):
    print('addition of two number is ',a,b)

n=int(input('enter 1st value: '))
m=int(input('ENTER THE SECONF VALUE :'))
addition(12,47)#Static value
addition(n,m)#input var
addition(int(input('first')),int(input('second')))# input passes to function'''

#type3
'''def addition(a,b):
    return a+b
a=addition(int(input('first')),int(input('second')))
print(addition(34,67))
print('addition of two number is ',a)'''

'''def multiplication(a,b):
    multi=a*b
    print('after calling the function:',multi)

multiplication(20,10)
'''

'''def t(max=5):
    for val in range(max):
        print (val)
t()'''

# this program shows that even if the changed the sequence the answer will remain the same 
'''def volumn(r,h):

    print('radius is: ', r)
    print('height is: ',h)
    vol=3.14*r*h*r
    print('volumn of the cylinder is: ', vol)

volumn(r=10,h=5)
print('sequence changed')
volumn(h=5,r=10)'''

'''def addition(*x):
    print(x)#collection of values from function call are stored as tuple
    print(type(x))
    sum=0
    for i in x:
        sum+=i

    print('addition is ',sum)

addition(10,20)
print('passing three arguments ')
addition(10,20,30)
print('passing four arguments: ')
addition(20,10,30,40)'''

'''def addition(**x):

    print(x)
    print(type(x))
    sum=0
    for i in x:

        sum+=x[i]

    print('addition is :', sum)
addition(first=10, second=20)
print('passing three arguments :')
addition(first=10,second=20, third=30)
print('passing four arguments: ')
addition(first=10,second=20,third=30,fourth=40)'''

def SI(p,r,t):
    si=p*r*t/100
    print('Simple Interest is',si)
SI(10000,5,3)
