from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    
    for i in range(0, len(nums)):
        result = []
        next = target - nums[i]
        
        if (next in nums):
            if (nums.index(next) != i):
                result.append(i)
                result.append(nums.index(next))
                return result;
        
