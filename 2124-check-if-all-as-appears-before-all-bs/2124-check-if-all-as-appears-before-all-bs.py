class Solution:
    def checkString(self, s: str) -> bool:
        x=s.count('a')
        a=s[0:x]
        b=s[x::]
        if 'a' in b or 'b' in a:
            return False
        else:
            return True
            