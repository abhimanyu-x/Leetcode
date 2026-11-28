class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        mp={}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=[]
            mp[nums[i]].append(i)

        fl=0
        for i in mp.values():
            for j in range(1,len(i)):
                if i[j]-i[j-1]<=k:
                    fl=1
                    break

        if fl==0:
            return False
        else:
            return True