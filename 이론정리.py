# 정수형 소수형 문자열 사칙연산 기본
name = input("Enter your name: ")
print(int("1414"))
print(float("1.414"))
print(int("1492")+520)

print(int(float("1.414")))
print(float("14"))

age =int(float(input("Enter age: ")))
print(age)

a,b= input().split()
a,b = int(a), int(b)
print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)"""

"""a=int(input())
b=int(input())

sum=a*(b%10)
sum2=a*((b%100)//10)
sum3=a*int(b/100)

total= sum+(sum2*10)+(sum3*100)

print(sum)
print(sum2)
print(sum3)
print(total)

# 리스트와 배열 기본이론
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

# 반복문 기초
for i in range(7):#세로로 움직이는 반복문
    #print(i,end="")
    print("&" * (7 - i), end="")
    for j in range(1,i+2): #가로로 움직이는 반복문
        print(j,end="")
    print()


nrow = 3
ncol = 5
for i in range(nrow):
    for j in range(ncol):
        print("(",i,",",j,")",sep ="", end="")
    print()

# 인덱스의 기본
a = [[1,2],[3,4],5]
print(len(a))
print(a[0][0])
print(a[0:3]) #0인덱스 부터 3인덱스까지 슬라이싱 == range(0,3)
print(a[::2]) #2칸씩 뛰어서 출력  == range(0,len(a),2)
print(a[::-1]) #뒤로 한칸씩 움직여라

a=[1,2,3,4,5,6,7,8,5,4,1]
a.sort() #1부터 정렬, list 자체에 있는 값을 다 바꿔서 정렬
a.reverse() #뒤에서 부터 출력 , list 자체에 있는 값을 다 바꿔서 출력
print(a)


a=[1,2,3,4]
for i in range(len(a)):
    print(a[i]*2,sep="",end=" ")


a=[1,2,3]
for i in range(len(a)):
    a=[a[i]]

#ruturn 기본
def f1(a1,b2):
    a1 = 10
    a2 = 20
    a3 = a1+a2
    return a3

#return만 쓰면 함수의 반환은 NoneType / a3를 적으면 a3반환

#조건문 기본
def multplication(n):
    for i in range(1, 11):
        print(n, "*", i, "=", n * i)

multplication(2)
multplication(5)
multplication(10)


def grade_eval(a):
    if a>= 90:
        grade = "A"
    elif a >= 80:
        grade = "B"
    elif a >= 70:
        grade = "C"
    elif a >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
score = [80,60,75,81,65,24,88,90,86]
for s in score:
    grade = grade_eval(s)
    print(grade)