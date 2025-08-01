from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    myDict = {}
    for i in range(len(nums)):
        if myDict.get(nums[i]) != None:
            myDict[nums[i]] += 1
        else:
            myDict[nums[i]] = 1
    
    startSeq = []
    for num in nums:
        if myDict.get(num+1) != None and myDict.get(num-1) == None:
            startSeq.append(num)
    if (len(startSeq) == 0):
        return 1
    lcs = [1] * len(startSeq)
    for i in range(len(startSeq)):
        val = startSeq[i] + 1
        while (myDict.get(val)) != None:
            lcs[i] += 1
            val += 1
    return max(lcs)

nums = [2,20,4,10,3,4,5]
print(longestConsecutive(nums))
