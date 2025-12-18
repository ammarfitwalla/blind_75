"""
152. Maximum Product Subarray (Medium)

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

(take max and min.)
"""

class Solution:
    def max_prod_subarray(self, nums: list[int]) -> int:
        max_prod = nums[0]
        curr_max = curr_min = nums[0]

        for n in nums[1:]:
            if n < 0:
                curr_max, curr_min = curr_min, curr_max  # swap when negative

            curr_max = max(n, curr_max * n)
            curr_min = min(n, curr_min * n)

            max_prod = max(max_prod, curr_max)

        return max_prod

sol = Solution()
print(sol.max_prod_subarray([2,3,-2,4]))