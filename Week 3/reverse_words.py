class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip(" ")
        x=s.split()
        a=""
        for b in x[::-1]:
            a=a+" "+b
        return a.strip()
