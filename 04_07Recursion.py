def sumofnum(n):
    if n==1:
        return n
    else:
        return n+sumofnum(n-1)

input_num=10
output=sumofnum(input_num)
print('sum of first {} natural number is {}'.format(input_num,output))
input_num=20
output=sumofnum(input_num)
print('sum of first {} natural number is {} '.format(input_num,output))

