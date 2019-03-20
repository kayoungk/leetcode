class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        changed = False
        while i - 1 >= 0:
            if nums[i] > nums[i - 1]:
                # find next bigger number's index
                nextbig = self.nextBiggerIndex(nums[i-1:]) + i -1
                # swap the identified "to-be-swapped" number and its next bigger number
                nums[i -1], nums[nextbig] = nums[nextbig], nums[i-1]
                changed = True
                break
            i -= 1
        if changed is False:
            # if no numbers are swapped, it means the list is in decreasing order in the first place,
            # reverse the whole list
            self.swapList(nums, 0)
        else:
            self.swapList(nums, i)

    def nextBiggerIndex(self, nums):
        for index in reversed(range(1,len(nums))):
            if nums[0] < nums[index]:
                return index

    # swap the list, make it increasing order
    def swapList(self, nums, start):
        last = len(nums) - 1
        while last >= 1 and start < last:
            nums[start], nums[last] = nums[last], nums[start]
            start += 1
            last -= 1

aList = [1,3,2]
# [2,1,3]
sol = Solution()
sol.nextPermutation(aList)
print(aList)

