'''
https://leetcode.com/problems/string-to-integer-atoi/
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()

        if not s:
            return 0

        LOWER, UPPER = -(2**31), (2**31)-1
        
        sign = 1
        if s[0] == '-' or s[0] == '+':
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        output = '0'
        for xter in s:
            if not xter.isnumeric():
                break

            output += xter

        output = sign * int(output)


        if output < LOWER:
            output = LOWER

        if output > UPPER:
            output = UPPER

        return output

s = '-42'
obj = Solution()
print(obj.myAtoi(s))