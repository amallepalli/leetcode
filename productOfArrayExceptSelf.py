from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    prefixProd = [0] * (len(nums) + 1)
    prefixProd[0] = 1
    prefixProd[1] = nums[0]
    
    for i in range(2, len(nums) + 1):
        prefixProd[i] = prefixProd[i - 1] * nums[i-1]
    
    postfixProd = [0] * (len(nums) + 1)
    postfixProd[-1] = 1
    postfixProd[len(nums) - 1] = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        postfixProd[i] = postfixProd[i + 1] * nums[i]
    
    finalProd = [0] * len(nums)
    for i in range(len(nums)):
        finalProd[i] = prefixProd[i] * postfixProd[i + 1]
    return finalProd
nums = [1, 2, 4, 6]
print(productExceptSelf(nums))