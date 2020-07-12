class Solution:
    def reverseBits(self, n: int) -> int:
        a='{0:032b}'.format(n)
        a=a[::-1]
        return int(a,2)
