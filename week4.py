# 반복문
n=int(input())

for i in range(1,10):
    print(n,"*",i,"=",n*i)

num = int(input())

sum=0
for i in range(0,num+1):
    sum+=i

print(sum)

# 정수입력하기
t=int(input())

for i in range(t):
    a,b=input().split()
    a,b=int(a),int(b)
    print(a+b)

x = int(input())
n = int(input())

sum = 0
for i in range(n):
    a,b=map(int,input().split())
    num= a*b
    sum= sum + num
if(sum == x):
    print("Yes")
else:
    print("No")

n = int(input())

for i in range(n//4):
    print("long",end=" ")

print("int")

import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(a + b)

t= int(input())

for i in range(t):
    a,b= map(int,input().split())
    print("Case #"+str(i+1)+":",str(a+b))

for i in range(100):
    a,b= map(int,input().split())
    if(a==0 and b == 0):
        break
    print(a+b)

#기본 별찍기
n=int(input())
for i in range(n):
    print("*" * (i+1))

n=int(input())
for i in range(n):
    print(" " * (n-i-1),end="")
    print("*" * (i+1))

