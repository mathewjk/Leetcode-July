class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n==1:
            c=1
        else:
            c=0
        for i in range(1,n):
            s=int(i*(i+1)/2)
            if(s<=n):
                c+=1
            else:
                break
        return c
        
