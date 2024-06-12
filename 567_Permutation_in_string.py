class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        
        s1_count, s2_count = [0]*26, [0]*26
        for i in range(len(s1)):
            s1_count[ord(s1[i])-ord('a')] += 1
            s2_count[ord(s2[i])-ord('a')] += 1

        MATCHES = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                MATCHES += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if MATCHES == 26:
                return True

            idx = ord(s2[r])-ord('a')
            s2_count[idx] += 1
            if s1_count[idx] == s2_count[idx]:
                MATCHES += 1
            elif s1_count[idx] == s2_count[idx] - 1:
                MATCHES -= 1

            idx = ord(s2[l])-ord('a')
            s2_count[idx] -= 1
            if s1_count[idx] == s2_count[idx]:
                MATCHES += 1
            elif s1_count[idx] == s2_count[idx] + 1:
                MATCHES -= 1

            l += 1    
        return MATCHES == 26

            





#---------------------- Testing ----------------------
if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    solution = Solution()
    print(solution.checkInclusion(s1, s2))  # True

    s1 = "ab"
    s2 = "eidboaoo"
    solution = Solution()
    print(solution.checkInclusion(s1, s2))  # False