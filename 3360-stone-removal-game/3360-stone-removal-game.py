class Solution:
    def canAliceWin(self, n: int) -> bool:
        for i in range(10,0,-1):
            if n-i<0 and i%2==0:
                return False
            elif n-i<0 and i%2==1:
                return True
            n-=i

        