class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        k=[]
        for i in nums1:
            if i in nums2:
                x=nums2.index(i)
                fl=0
                z=0
                for j in nums2[x+1::]:
                    if j>i:
                        fl=1
                        z=j
                        break
                if fl==1:
                    k.append(z)
                else:
                    k.append(-1)

        return k