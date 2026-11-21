class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dict={}
        for i in range(len(nums)):
            reqd=target-nums[i]

            if reqd in dict:
                return [dict[reqd],i]

            dict[nums[i]]=i