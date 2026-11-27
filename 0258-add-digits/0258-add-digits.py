class Solution:
    def addDigits(self, num: int) -> int:
        if num<10:
            return num
        while num>=10:
            s=sum(int(i) for i in str(num))
            num=s

        return num