'''x = lambda a:a+10
print(x(5))'''
#any number of argument
'''def myfun(n):
    return lambda a:a+n

mytripler=myfun(3)
print(mytripler(11))'''

'''x=lambda a,b,c:a+b+c
print(x(2,4,6))'''

'''def myfun(n):
    return lambda a:a*n
v=myfun(3)
print(v(4))'''

'''x = lambda a:a**2
print(x(5))'''

'''x = lambda a:a**3
print(x(5))'''

'''x = lambda a:a+10
print(x(5))'''

'''x= lambda a:(a * 9/5) + 32
print(x(5))'''

#program to filter out the even item from list 
'''my_list=[1,5,4,6,8,11,3,12]
new_list=list(filter(lambda x:(x%2==0),my_list))
print(new_list)'''

'''languages=['java','Python','Java Script']
version=[14,3,6]
result=zip(languages, version)
print(list(result))'''

'''number_list=[1,2,3]
str_list=['one','two','three']
result=zip()
print(result)

result_list=list(result)
print(result_list)

result=zip(number_list,str_list)

result_set=set(result)
print(result_set)'''

'''list1=[10,20,30,40,50]
def add(n):
    return n+5
a=map(add,list1)
list(a)'''

# import functools
# a=functools.reduce(lambda x,y:x+y,list1)
# a

