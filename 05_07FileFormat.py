
'''f=open('test1.txt','w')
f.write('')
f.close()
f=open('test.txt','w')
f.write('This too shall pass')
f.write('Good morning')
f.close()

f=open('test.txt',mode='r',encoding='utf-8')
f.read()
f.close()'''

'''f=open('test.txt',mode='r',encoding='utf-8')
print(f.readline())
f.close()'''

'''f=open('test.txt',mode='r',encoding='utf-8')
for line in f:
    print(line, end='')
f.close()'''


'''f=open('test.txt',mode='r',encoding='utf-8')
print(f.readline())
print(f.readline())
#print(f.read(1))
f.close()'''


f=open('test.txt',mode='r',encoding='utf-8')
print(f.readline())
f.tell()
print(f.readline())
f.seek(0)
print(f.readline())
f.tell()

#OAF java after data analytics 