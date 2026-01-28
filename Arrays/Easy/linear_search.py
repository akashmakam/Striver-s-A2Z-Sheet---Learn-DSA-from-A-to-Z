# Problem: Linear Search
# Description: Given an array of numbers and a target, check whether the target number is present in the array.

'''
Approach: 
Iterate through the array. If a match is found, return 1. Otherwise, after searching through the array, if the element is not found, return -1.
Time complexity: O(n)
Space complexity: O(1)
'''
class Solution:
    def linearSearch(self, nums, target):
        for num in nums:
            if num == target:
                return 1
        return -1
