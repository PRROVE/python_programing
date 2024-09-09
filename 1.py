"""name = input("Enter your name: ")
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
-백준 곱셈문제 2588번

print(not True)
print(False or True)
print(False and (False or True))
"""

H,M=input().split()
H,M=int(H),int(M)

if(M < 45):
    if(H !=0):
        print(H-1,60-45+M)
    else:
        print(23-H,60-45+M)
elif(M >= 45):
    print(H,M-45)
