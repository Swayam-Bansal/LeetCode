#Soultion 1: Brute Force
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        j = len(nums)

        for i in range(0, j):
            for j in range(len(nums) -1, i, -1):
                if nums[i] + nums[j] == target:
                    return [i, j]
                

# Soltuion 2: Using HashMaps ...
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if hash_set.get(difference) is not None:
                return [i, hash_set[difference]]
            
            hash_set[nums[i]] = i
        
        