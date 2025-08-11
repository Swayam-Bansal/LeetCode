# Solution 1: Brute Force approach 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # we can sort the array first, and this will group up all the duplicate numbers together
        nums.sort()

        # now we can simply iterate through the array and see if there are any two adjacent numbers that are equal 
        # if equal return true.
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True

        # if we exit out of the loop without returning True, that means there were no duplicates, 
        # Hence indicating that we should return a false.
        return False        



# Solution 2: Using HashMaps ...
# So, the broad idea is that the hashmap will help us keep track of the values we have encountered while iterating through the array, by storing them as a (key, value) pair or the (num, 0).
# Now, if we encounter a number that is already in the hashmap we can return true, else return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for i in nums :
            # if i is already in the hashmap then return true ...
            if i in hashmap :
                hashmap[i] += 1
                return True

            # add the i in hashmaps as a (key, value) pair of (i, 0)
            # 0 here indicated the number of instances it has occured 
            hashmap[i] = 0

        # if we exit out of the loop without returning True, that means there were no duplicates, 
        # Hence indicating that we should return a false. 
        return False
    



# Solution3: Using HashSets ...
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        # now we can simply iterate through the array and see if there are any two adjacent numbers that are equal 
        # if equal return true.
        for i in nums:
            if i in hashset:
                # if i is already in the hashset then return true ...
                return True

            # add i to the hashset
            hashset.add(i)

        # if we exit out of the loop without returning True, that means there were no duplicates, 
        # Hence indicating that we should return a false.
        return False
         

# Solution 4: Using Python Sets ...
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)
        