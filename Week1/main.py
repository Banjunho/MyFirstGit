# 1번 문제
'''
 a에 형변환 없이 input을 사용할 경우 str로 저장이 된다.
 따라서 int형변환을 사용하자.
'''
a = int(input("숫자를 입력하세요: "))
b = a * 10
print(b)


# 2번 문제
price = int(input("금액을 입력하세요: "))
aa = str(price // 10000)
bb = str((price % 10000) // 1000)
cc = str((price % 1000) // 100)
dd = str((price % 100) // 10)
ee = str((price % 10))

print(aa+"만", bb+"천", cc+"백", dd+"십", ee+"원")


# 3번 문제
a = int(input("숫자를 입력하세요: "))
print(("*" * a + "\n") * a)