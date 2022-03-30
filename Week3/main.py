'''
#1번
### a를 print하게 되면 맨 처음 입력받은 수가 나오게 된다.
### func(a)를 한다고 해서 그 a값이 변하는 것이 아님.
### func() 안에 있는 a는 지역변수이기 때문.
### 따라서 print(a)를 하게 되면 print() 안에 있는 a는 전역변수로
### input에 들어간 수가 됨.
### 따라서 다음과 같이 고쳐야 함.
a=int(input("숫자를 입력하세요: "))

def func(a):

    a = a*10
    return a

b = func(a)
print(b)
'''
#2번
a = int(input("숫자를 입력하세요: "))

def Pbo(a):
    if (a==1)|(a==2):
        return 1

    else :
        return Pbo(a-2) + (a-2)

print(Pbo(a))