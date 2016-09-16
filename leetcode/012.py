class Solution(object):
    ROMANS = 'IVXLCDM'
    def intToRoman(self, num):
        i = 0
        result = []
        while num:
            n = (num % 10)
            if 0 < n < 4:
                result.append(self.ROMANS[i] * n)
            elif n == 4:
                result.append(self.ROMANS[i] + self.ROMANS[i+1])
            elif n == 5:
                result.append(self.ROMANS[i+1])
            elif 5 < n < 9:
                result.append(self.ROMANS[i+1] + self.ROMANS[i] * (n - 5))
            elif n == 9:
                result.append(self.ROMANS[i] + self.ROMANS[i+2])
            num /= 10
            i += 2
        return ''.join(reversed(result))


print Solution().intToRoman(3999)
