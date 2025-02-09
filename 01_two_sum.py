"""
Time complexity: Beat 32%
Memory complexity: Beat 91%
The loookup efficienct between list and dict
2025/02/06
"""

def twoSum(nums, target):
    for x in range(len(nums)):
        remain = target - nums[x]
        nums[x] = 'ph'
        if remain in nums:
            return [x, nums.index(remain)]
        else:
            nums[x] = (target - remain)
print(twoSum([3,3],6))