class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==-2147483648 and divisor==-1:
            return 2147483647

        if abs(divisor)>abs(dividend):
            return 0

        if divisor==1:
            return dividend

        if divisor==-1:
            return -dividend if dividend!=-2147483648 else 2147483647

        a=abs(dividend)
        b=abs(divisor)
        c=0

        while a>=b:
            temp=b
            count=1

            while a>=temp+temp:
                temp+=temp
                count+=count

            a-=temp
            c+=count

        if (dividend>0 and divisor>0) or (dividend<0 and divisor<0):
            return c
        else:
            return -c