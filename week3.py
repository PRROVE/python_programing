# 비교연산자
a,b= input().split()
a,b= int(a),int(b)
if(a>b):
    print(">")
elif(a==b):
    print("==")
else:
    print("<")

# 조건문
a= input()
a=int(a)

if(a>=90):
    print("A")
elif(a>=80):
    print("B")
elif(a>=70):
    print("C")
elif(a>=60):
    print("D")
else:
    print("F")

a=input()
a=int(a)

if(a % 4 == 0 and a % 100 != 0):
    print("1")
elif(a % 400 ==0 ):
    print("1")
else:
    print("0")

#알람시계 문제
hour,min = input().split()
hour,min=int(hour),int(min)

if(min < 45):
    if(hour>0):
        print(hour-1,60-45+min)
    elif(hour==0):
        hour=23
        print(hour,60-45+min)
elif(min >= 45):
        print(hour,min-45)
else:
    print(hour,min-45)

#오븐시계
hour,min = map(int,input().split())
time = int(input())

if(min+ time >= 60):
    if(hour + ((min+time) // 60) >= 24):
        print(((hour+(min+time)//60)-24),(min+time)%60)
    else:
        print(hour+(min+time)//60,(min+time)%60)
else:
    print(hour,min+time)

#주사위 세개
a,b,c = map(int,input().split())

if(a == b == c):
    print(10000 + (a * 1000))
elif(a == b or a == c):
        print(1000 +(a*100))
elif(b == c):
        print(1000 +(b*100))
else:
    print(100*max(a,b,c))