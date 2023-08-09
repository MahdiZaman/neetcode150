class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
             
            if total_t <= h: 
                # means Koko can (possibly) relax and eat slower
                r = k - 1
                res = min(k, res)
            else: 
                # means Koko needs to eat faster. So look for larger banana/hr
                l = k + 1
        return res