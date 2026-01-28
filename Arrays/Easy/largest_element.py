# Problem: Find the largest element in the array
# Description: Given an array of integers, return the largest value present in the array.

'''
Approach 1: Sorting (Brute Force)

Sort the array and return the last element.
This works but requires unnecessary sorting.

Time Complexity: O(n log n)
Space Complexity: O(1)
'''
class Solution:
  def largest_element(self, nums):
    nums.sort()
    return nums[-1]

'''
Approach 2: Linear Scan (Optimal)

Iterate through the array while tracking the maximum value found so far.

Time Complexity: O(n)
Space Complexity: O(1)
'''
class Solution:
  def largest_element(self, nums):
    largest = nums[0]
    for num in nums:
      if num > largest:
        largest = num
    return largest
