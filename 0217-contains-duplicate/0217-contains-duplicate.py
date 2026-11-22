class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s=set()
        fl=1
        for i in nums:
            if i not in s:
                s.add(i)
            else:
                fl=0
        if fl==0:
            return True
        else:
            return False