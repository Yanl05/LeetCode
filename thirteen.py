class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Dics = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900,
                'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        Lists = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        #print(s.split('M'))
        lens = len(s)
        count = 0
        for i in range(lens):
            if i <= lens - 2:
                temps = s[i] + s[i + 1]
            else:
                temps = ''
            if temps in Lists:
                count = count + Dics[temps]
                count = count - Dics[s[i + 1]]
                continue
            count = count + Dics[s[i]]
        return count
