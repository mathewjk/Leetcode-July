class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        h=float(hour*5+float(minutes*5/60))
        if(h>=60):
            h-=60
        dif=abs(h-minutes)
        dif=dif*6
        if(dif>180):
            k=dif-180
            dif=180-k
        return dif
