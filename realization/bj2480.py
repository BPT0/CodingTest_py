"""
    1~6까지 3개의 주사위를 던짐
    상금 
    1. 같은 눈 3개 나오면 10000원 + 같은눈 *천원
    2. 같은 눈 2개 나오면 1000원 + 같은눈 * 100원
    3. 모두 다른 눈이 나오는 경우 그중 가장 큰눈 * 100원
"""
a, b, c = map(int, input().split())
nun = input().split()
prize = 0
if nun[0] == nun[1] and nun[1] == nun[2] and nun[0] == nun[2]:
    prize = 10000 + int(nun[0]) * 1000
elif nun[0] == nun[1] or nun[1] == nun[2] or nun[0] == nun[2]:
    if nun[1] == nun[2]:
        prize = 1000 + int(nun[1]) * 1000
    else:
        prize = 1000 + int(nun[1]) * 100
else:
    prize = max(int(nun[0]), int(nun[1]), int(nun[2])) * 100

print(prize)

# map 함수를 이용했으면 좋았겠다.