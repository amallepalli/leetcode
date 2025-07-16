from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    thisdict = {}
    for i in range(len(nums)):
        thisdict[nums[i]] = i
    
    for i in range(len(nums)):
        leftover = target - nums[i]
        if (thisdict.get(leftover) != None and thisdict.get(leftover) != i):
            return [i, thisdict.get(leftover)]

nums = [1, 3, 4, 2]
target = 6
print(twoSum(nums, target))
