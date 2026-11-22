class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=s.lower().strip()
        k=str()
        for i in range(len(l)):
            if l[i].isalpha() or l[i].isspace() or l[i].isdigit():
                k+=l[i]

        x=k.split()
        a=str()
        for i in x:
            a+=i

        if a==a[::-1]:
            return True
        else:
            return False
        

