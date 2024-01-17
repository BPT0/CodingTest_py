# """
#     헤시테이블 - 메모리를 사용해 시간 복잡도를 줄일 때 사용
#     key in {} 을 이용하여 O(1) 을 이용하여 
#     시간 복잡도를 줄일 수 있음
# """

# # 가장 긴 연속된 수열
# # 정렬 x, 정수형 배열 
# # nums 원소를 가지고 만들 수 있는 가장 연속되 수의 개수

# # Longest Consecutive Sequence
# # 1. Dictonary를 이용하여 구현
# def longestConsecutive(nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#     longest = 0
#     # nums 요소들을 Dictionary의 key에 삽입하가
#     numDict = {}
    
#     for num in nums:
#         numDict[num] = True
        
#     for num in numDict:
#         # if 
#         # - 최솟값을 찾는 조건 작성
#         # - 조회하는 값의 -1 보다 작은 요소 있는지 조회 O(1)
#         if num-1 not in numDict:
#             # 연속됨을 새기 위해 cnt 변수 선언
#             cnt = 1 
#             target = num + 1
#             # while - numDict 순차 탐색 반복하기, 
#             # -> target이 있을때까지
#             # Q. if 로 하면 어떤지? 사용 불가
#             # - numDict 를 순회하며 target이 있는지 판별하며 더여야함
#             # - 그래서 if문 으로 대체 불가
#             while target in numDict:
#                 # target 이 있으면 target +1
#                 target +=1
#                 # 연속된 숫자가 되는 것이브로 +1
#                 cnt +=1
#             # 최솟값 0 조건도 고려해야 하므로
#             # 두값 비교해 max 값 리턴
#             longest = max(longest, cnt)
#     return longest
            
# longestConsecutive([100,4,200,1,3,2])