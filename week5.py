# 1차원 배열
n = int(input())
data = list(map(int, input().split()))
v = int(input())
count = 0
for i in range(len(data)):
    if v == data[i]:
        count += 1
print(count)

n,x =map(int,input().split())
data = list(map(int,input().split()))
for i in range(len(data)):
    if(x > data[i]):
        print(data[i],end=" ")

n= int(input())
data = list(map(int,input().split()))
print(min(data),max(data))

a = [int(input()) for _ in range(9)]
max_value = max(a)
index_max = a.index(max_value)+1
print(max_value)
print(index_max)

N, M = map(int, input().split())
baskets = [0] * (N + 1)

for _ in range(M):
    i, j, k = map(int, input().split())
    baskets[i:j + 1] = [k] * (j - i + 1)

print(*baskets[1:])

N, M = map(int, input().split())
baskets = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]

print(*baskets)

all_students = set(range(1, 31))

submitted_students = set()
for _ in range(28):
    submitted_students.add(int(input()))

missing_students = all_students - submitted_students

for student in sorted(missing_students):
    print(student)

remainders = set()

for _ in range(10):
    number = int(input())
    remainders.add(number % 42)

print(len(remainders))

import sys

N, M = map(int, sys.stdin.readline().split())

Basket = [i for i in range(1, N + 1)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())

    Temp = Basket[i - 1:j]
    Temp.reverse()
    Basket[i - 1:j] = Temp

print(*Basket)

N = int(input())

scores = list(map(int, input().split()))

max_score = max(scores)

new_scores = [(score / max_score) * 100 for score in scores]

average = sum(new_scores) / N

print(average)
