class Solution(object):
    def plusOne(self, digits): #19
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        last_digit = digits[-1] #9
        res = []

        if last_digit < 9 :
            last_digit += 1
            return digits[:-1] + [last_digit]

        # if all digits have to update
        last_digit += 1 
        
        quo = last_digit // 10
        digits[-1] = last_digit % 10
        for i in range(len(digits)-2, -1, -1):
            digits[i] = digits[i] + quo
            quo = digits[i] // 10
            if quo > 0 :
                digits[i] = digits[i] % 10
        if quo != 0:
            res = [quo] + digits
            return res
        else:
            return digits
        
    
if __name__ == "__main__":
    sol = Solution()
    digits = [1,9] # [9,9,9]
    print(sol.plusOne(digits)) # Expected: 4 for [1,2,3,4]