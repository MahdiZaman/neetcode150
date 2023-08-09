class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = {}
        l = 0 # sliding window left pointer

        maxcount = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            # print(max(count.values()))
            
            maxcount = max(maxcount, count[s[r]])
            if (r - l + 1) - maxcount > k :
            # if (r - l + 1) - max(count.values()) > k :
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
'''    
**Objective: Maximize the length of substring where
(length of substring - most_popular_letter_count_in_that_substring) = k**

- keep the counts of the letters in a dictionary **(fast look up, fast retrieval)**
- **sliding windows** can help
	- move right pointer for each letter in given string
		- move left pointer when/if the (length of substring - most_popular_letter_count) > k 

- the dictionary can be as large as 26 keys (for 26 english block letters). Look up in that dictionary can be O(26n) time. 
- One way of optimizing that is to avoid looking up for each right-pointer-letter by keeping a maxCount.
- **The unintuitive trick is** that when moving the left pointer, decreasing the count can keep track of original count, but that does not affect the result at all. Because when maxCount is itstored separately and not decreased, we are essentially overestimating the maxCount, but the `length_of_substring` would only be updated if it is larger than our last seen longest `length_of_substring`. So although that shorter substring is a valid one, it does not alter the returning result. So we can avoid the lookup altogether by only keeping count of `max(maxCount, letter_at_right_pointer)`. *Thanks to neetcode for teaching this*
'''
