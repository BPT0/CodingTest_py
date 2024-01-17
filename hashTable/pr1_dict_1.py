# 위 함수는 같은 원소를 2번 사용했으므로 코드 변경 필요
# 같아지는 조건을 검사하여 1번만 조회하게 수정  
def two_sum(nums, target):
    memo = {}
    
    # O(n)
    for v in nums:
        memo[v] = 1

    # O(n) - for문
    for v in nums:
        needed_number = target - v
        if target/2 == needed_number:
            return True
        
        # O(1) - dict에서 key값을 조회 - 중요!!
        # * 시간 복잡도가 O(1)인 이유는
        # * Dictionary는 Hashtable로 구성되어있고
        # * HashFunction 을 이용하여 
        # * 값이 유무 판별 가능하기 때문
        if needed_number in memo:
            return True
    return False

two_sum(nums= [4,1,9,7,8,2], target=14)
