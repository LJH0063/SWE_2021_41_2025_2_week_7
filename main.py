from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    result = [-1, -1]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[j] == target):
                result = [i, j]
                break
    
    return result

nums = [3, 3]
target = 6
print(twoSum(nums, target))

