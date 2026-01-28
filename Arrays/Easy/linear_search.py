# Linear Search
# Time complexity: O(n)
# Space complexity: O(1)

# Approach 1: 
# 1. Iterate through the array
#    a. return 1 if the target is found. 
# 2. After searching the array, if the target is not found, return -1.
class Solution:
    def linearSearch(self, nums, target):
        for num in nums:
            if num == target:
                return 1
        return -1
