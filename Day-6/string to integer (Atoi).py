class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0

        int_max = 2**31-1
        int_min = -2**31

        # whitespace
        while i<n and s[i] == ' ':
            i+=1

        # sign
        sign = 1
        if i<n and (s[i] == '-' or s[i] == '+'):
            if s[i] == '-':
                sign = -1
            i+=1

        # integer part
        res = 0
        while i<n and s[i].isdigit():
            res = res*10 + int(s[i])
            i+=1

            if sign*res >= int_max:
                return int_max

            if sign*res <= int_min:
                return int_min

        return sign*res
        