a= [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]

a.append([11])
print(a)
a.extend([12,13])
print(a)
append = 괄호안에 list를 벗겨주지 않고 list에 포함시켜줌
extend = 괄호안에 list를 벗기고 list에 포함시켜줌


for i in range(100):
    a,b= map(int,input().split())
    if(a==0 and b == 0):
        break
    print(a+b)