"""
    dict
    * 시간 복잡도를 줄일수 있는 좋은 알고리즘
    2.접근방법
    * 직관적으로 생가 - 완전탐색, 극한화, 단순화
    * 자료구조와 알고리즘 활용 - 문제 이해 토대로 구성 -> 자구, 알고리즘을 활용해 시간복잡도 줄이기
    3.메모리 사용
    * 시간복잡도를 줄이기 위해 메모리를 사용 ex)HashTable
    
"""
# 4.구현
def twoSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dict 정의, 요소 추가
        makeTargetnums = {}
        # 반환할 arr 추가
        answer = [0, 0]
        for key in nums:
            if key in makeTargetnums:
                makeTargetnums[key] = False
            else: 
                makeTargetnums[key] = True

        for idx, sub in enumerate(nums, 0):
            n = target - sub
            if n in makeTargetnums and n == nums[idx+1]:
                answer = [idx, idx+1]
                return answer
                

nums = [3,2,4]
twoSum(nums, target=6)