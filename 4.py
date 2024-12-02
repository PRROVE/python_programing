def f1(a1,b2):
    a1 = 10
    a2 = 20
    a3 = a1+a2
    return a3

#return만 쓰면 함수의 반환은 NoneType / a3를 적으면 a3반환

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

