"""
347. Top K Frequent Elements (Medium)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""


from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                print(res, n)
                res.append(n)
                if len(res) == k:
                    return res
        
                
# sol = Solution()
# print(sol.topKFrequent([5, 5, 5, 5, 5, 5, 5, 1,1,1,2,2,3], k = 2))


from collections import Counter

def find_most_popular(purchases):
    if not purchases:
        return None
    
    # Counter creates a hash map of counts automatically
    counts = Counter(purchases)
    print(counts)
    
    # .most_common(1) returns a list like [('ItemA', 10)]
    most_popular = counts.most_common()

    temp = []
    for item, count in most_popular:
        if count == target:
            break
        temp.append((item, count))
        
    return temp

# Example Usage
stream = [5, 5, 5, 5, 5, 5, 5, 1,1,1,2,2,3]
target = 2
print(find_most_popular(stream))
# Output: 5