def longestConsecutive(nums):
    longest = 0
    numDict = {}

    for num in nums:
        numDict[num] = True
        
    for num in numDict:
        if num-1 not in numDict:
            cnt = 1 
            target = num + 1
            
            while target in numDict:
                target += 1
                cnt += 1
            
            longest = max(longest, cnt)
    
    return longest
            
longestConsecutive([100, 4, 200, 1, 3, 2])
