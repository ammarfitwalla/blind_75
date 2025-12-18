"""
15. 3Sum (Medium)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array which sum up to zero.

        Parameters:
        nums (List[int]): The input list of integers.

        Returns:
        List[List[int]]: A list of lists, where each inner list contains three integers that sum to zero.
        """
        nums.sort()
        n = len(nums)
        outs = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, h = i+1 , n-1

            while l < h:
                summ = nums[i] + nums[l] + nums[h]
                if summ == 0:
                    outs.append([nums[i], nums[l], nums[h]])
                    l += 1
                    h -= 1
                    while l < h and l > i+1 and nums[l] == nums[l-1]:
                        l += 1
                    while l < h and h < n-1 and nums[h] == nums[h+1]:
                        h -= 1
                elif summ < 0:
                    l += 1
                else:
                    h -= 1
        return outs
    
sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,1,1]))
print(sol.threeSum([0,0,0]))
                