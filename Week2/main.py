#초급
a=int(input("숫자를 입력하세요: "))

if a%2==0:
    print("입력하신 수는 짝수 입니다.")
else:
    print("입력하신 수는 홀수입니다.")



#중상급
b=int(input("숫자를 입력하세요: "))
divisor=[]
for i in range(1, b+1):
    if b%i==0:
        divisor.append(i)

print(divisor)



#최상급
import random

def create():
    temp = [random.randint(0,99) for i in range(100)]
    return temp

if __name__ == "__main__" :
    num_list = create()


d=[] # 중복 없는 리스트
e=[] # 최대 중복 수 리스트
c=[0]*100 # 중복 개수 리스트
count=1 # 중복 개수 세는 변수. 최소 한 번 있기 때문에 1임.

num_list.sort() # 오름차순으로 정렬

d.append(num_list[0]) # 첫 번째 요소는 반드시 중복 없는 리스트에 들어가기 때문
for i in range(1, 100):
    if num_list[i-1] == num_list[i]:
        count+=1 # 다음 것과 비교해서 동일하면 count

    elif num_list[i-1] < num_list[i]:
        d.append(num_list[i]) # 다음 것과 다르면 다음 것을 d에 넣어줌.
        c[num_list[i-1]]=count # num_list[i-1]에 해당하는 c 칸에 중복된 count를 넣어줌.
        count=1 # count 초기화

max_overlap=0
for k in range(100, -1, -1): # 100 -> 0 으로 역순으로 하여 가장 중복된 수가 큰 거 찾기
    for l in range(100):
        if (c[l] == k) and (max_overlap<=k):
            max_overlap=k
            e.append(l) # 가장 큰 중복 수 가진 c칸이 곧 num_list에 해당하는 숫자임. 그것을 e에 넣어줌.

max_third=d[-3] # 세번 째로 큰 수는 중복 없는 d리스트에서 뒤에서 세번 째에 있음.

print("최고 중복 수는", e, "입니다. 중복횟수는", max_overlap, "입니다.")
print("세번째 최고 수는", max_third, "입니다.")
print(d)