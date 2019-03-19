# 3Sum
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 : return []
        nums.sort()
        ans = []
        for index in range(len(nums)):
            second = index + 1
            last = len(nums) - 1
            if index > 0 and nums[index - 1] == nums[index]:
                continue
            if index >= len(nums) -2:
                break
            while second < last:
                if nums[second] + nums[index] + nums[last] < 0:
                    second += 1
                elif nums[second] + nums[index] + nums[last] > 0:
                    last -= 1
                elif nums[second] + nums[index] + nums[last] == 0:
                    ans.append([nums[index], nums[second], nums[last]])
                    while nums[second] == nums[second + 1] and second < len(nums) - 2:
                        second += 1
                    second += 1
                    while nums[last] == nums[last - 1] and last > 2:
                        last -= 1
                    last -= 1
        return ans

alist = [0,0,0]

solution = Solution()
print(solution.threeSum(alist))