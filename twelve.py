class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        i = 0
        listn = []
        Dic = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C',
               500: 'D', 1000: 'M', 4:'IV', 9:'IX', 40:'XL', 90:'XC',
               400:'CD', 900:'CM'}
        num = int(str(num))
        while num:
            cal = num % 10
            listn.append(cal)
            num = num // 10
        counts = []
        for i in range(len(listn)):
            cal = listn[i] * (10 ** i)  # 4  90 900 1000 i = 0 1 2 3
            if cal == 4 \
                    or cal == 9 or cal == 40 \
                    or cal == 90 or cal == 400 or cal == 900:
                counts.append(Dic[cal])
            else:
                if i == 0:
                    if cal >= 5:
                        counts.append((cal-5)*Dic[1])
                        counts.append(Dic[5])
                    else:
                        counts.append(cal * Dic[1])
                if i == 1:
                    if cal >= 50:
                        counts.append((cal-50)//10 * Dic[10])
                        counts.append(Dic[50])
                    else:
                        counts.append(cal//10 * Dic[10])
                if i == 2:
                    if cal >= 500:
                        counts.append((cal-500)//100 * Dic[100])
                        counts.append(Dic[500])
                    else:
                        counts.append(cal//100 * Dic[100])
                if i == 3:
                    counts.append(cal//1000 * Dic[1000])
        return "".join(counts[::-1])
