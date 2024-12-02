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
