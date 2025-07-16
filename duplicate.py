from typing import List


def hasDuplicate(nums: List[int]) -> bool:
    thisdict = {}
    for x in nums:
        if (thisdict.get(x) != None):
            return True
        thisdict[x] = 1
    return False

nums = [1, 2, 3, 4]
print(hasDuplicate(nums=nums))
