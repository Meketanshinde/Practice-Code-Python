#Python Lambda Functions are anonymous function means that the function 
# is without a name. As we already know that the def keyword is used to 
# define a normal function in Python. Similarly, the lambda keyword is used 
# to define an anonymous function in Python. 

#syntax:
#lambda arguments: expression

# Example:
li = [5, 8, 10, 20, 50, 100]
division = list(map(lambda y: y/2, li))
print (list(division))

