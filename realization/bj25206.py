num = int(input())

# 공백으로 입력 구분하며
# num 개수 만큼 입력 제한하기
suList = list(map(int, input().split()))
find = int(input())
count = 0

# for문 돌면서
for i in range(0, num-1):
    if suList[i] == find:
        count+=1

print(count)

