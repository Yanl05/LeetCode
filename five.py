class Solution:
    # # 方法一： 暴力解法  超时
    # def longestPalindrome(self, s):
    #     """
    #     暴力解法
    #     最长，那就从最长的开始检验是否为回文子串
    #     :param s:
    #     :return:
    #     """
    #     if s == '':
    #         return s
    #     for i in range(len(s), 0, -1):
    #         for j in range(len(s)):
    #             if j+i>len(s):
    #                 break
    #             else:
    #                 if self.check(s[j:j+i]):
    #                     return s[j:j+i]
    #
    #
    #
    # def check(self,s):
    #     """
    #     检测该串 是否为回文子串
    #     :param s:
    #     :return:  回文子串返回true 否则为else
    #     """
    #     while len(s)>0:
    #         # 当第一个字符与最后一个字符相等时
    #         if s[0] == s[-1]:
    #             # print(s[0])
    #             s = s[1:-1]
    #             # print(s)
    #             if s == '':
    #                 return True
    #         else:
    #             return False

    # # 方法二： 中心扩散法
    # def longestPalindrome(self, s):
    #     """
    #
    #     :param s:
    #     :return:
    #     """
    #     size = len(s)
    #     if size == 0:
    #         return ''
    #
    #     # 返回的回文子串至少是1
    #     longest_palindrome = 1
    #     longest_palindrome_str = s[0]
    #
    #     for i in range(size):
    #         palindrome_odd,odd_len = self.__center_spread(s, size, i, i)
    #         palindrome_even,even_len = self.__center_spread(s, size, i, i+1)
    #
    #         # 找到当前最长回文子串
    #         cur_max_sub = palindrome_odd if odd_len>even_len else palindrome_even
    #         if len(cur_max_sub)>longest_palindrome:
    #             longest_palindrome = len(cur_max_sub)
    #             longest_palindrome_str = cur_max_sub
    #     return longest_palindrome_str
    #
    # def __center_spread(self, s, size, left, right):
    #     """
    #     left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
    #     right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
    #
    #     :param s:
    #     :param size:
    #     :param left:
    #     :param right:
    #     :return:
    #     """
    #     l = left
    #     r = right
    #
    #     while l>=0 and r<size and s[l]==s[r]:
    #         l -= 1
    #         r += 1
    #     return s[l+1:r],r-l-1

    # # 方法三 动态规划
    # def longestPalindrome(self, s: str) -> str:
    #     """
    #
    #     :param s:
    #     :return:
    #     """
    #     size = len(s)
    #     if size <= 1:
    #         return s
    #     # 创建二维dp数组
    #     dp = [[False for _ in range(size)] for _ in range(size)]
    #     longest_l = 1
    #     res = s[0]
    #
    #     for i in range(size):
    #         for j in range(i):
    #             # 状态转移方程：如果头尾都相等并且中间也是回文  或者 中间长度小于等于 1
    #             # [j + 1, i - 1] 能够形成区间，因此有 j + 1 < i - 1
    #             # [j + 1, i - 1] 不能形成区间，即 i - j <= 2
    #             if s[j] == s[i] and (i-j<=2 or dp[j+1][i-1]):
    #                 dp[j][i] = True
    #                 if i - j +1>longest_l:
    #                     longest_l = i-j+1
    #                     res = s[j:i+1]
    #     return res

    # 方法四：Manacher算法
    def longestPalindrome(self, s: str) -> str:
        """
        Manacher 算法本质上还是中心扩散法，只不过它使用了类似 KMP 算法的技巧，充分挖掘了已经进行回文判定的子串的特点，提高算法的效率。

        1.对原始字符串进行预处理（为了避免奇数长度的回文子串or偶数长度的回文子串问题）
            字符串长度 len 添加分隔符的个数 len+1  -> 最后得到的总长度 2*len+1  一定是奇数
        2.得到p数组  p -> 回文半径   能扩散的步数+1 （1为原点）  ---> 带分割符的最长子串                是       回文半径p*2-1
          得到p-1数组                                       ---> 不带分割符的最长子串 要 减去 len+1个分隔符   p*2-1 - p+1 = p
        3.p-1 数组中最大的数 就是最长回文子串

        :param s:
        :return:
        """
        size = len(s)
        if size <= 1:
            return s
        # 1.对原始字符串进行预处理
        new_s = self.addDivide(s)
        # print(new_s)
        # 2.得到p数组
        p = [1, 2]
        for i in range(2, len(new_s)):
            tag = 0
            while i - tag >= 0 and i + tag < len(new_s) and new_s[i - tag] == new_s[i + tag]:
                tag += 1
            p.append(tag)
        print(p)
        # 获得最大回文半径数字所在的index，并get 子串
        radius = max(p) # 6
        mid = p.index(radius)# 7
        new_s = new_s[mid-radius+1:mid+radius]
        print(new_s)
        palindrome = ''.join(new_s.split('#'))
        return palindrome

    def addDivide(self, s):
        """
        分隔符 #
        :param s:
        :return: 给s加上len（s）+1 个分隔符后返回
        """
        ret = '#'
        for i in range(len(s)):
            ret = ret + s[i] + '#'
        return ret

    #     mx=0                   #mx即为当前计算回文串最右边字符的最大值
    #     ans=0
    #     po=0
    #     Len=[0]*10000
    #
    # ##转换字符串
    #     def INIT(s):
    #         init_s='@#'
    #         for x in s:
    #             init_s=init_s+x+'#'
    #
    #         return init_s+'$',2*len(s)+1     # 字符串结尾加一个字符，防止越界
    #
    #     init_s,len_s=INIT(s)       #转换字符串
    #     get_po=0
    #     for i in range(1,len_s):
    #         if mx>i:
    #             Len[i]=min(mx-i,Len[2*po-i]) #在Len[j]和mx-i 中取小
    #         else:
    #             Len[i]=1  #如果i>mx，要从头开始匹配
    #
    #         while init_s[i-Len[i]]==init_s[i+Len[i]]:
    #             Len[i]=Len[i]+1
    #
    #         if Len[i]+i>mx:      #若新计算的回文串右端点位置大于mx，要更新po和mx的值
    #             mx=Len[i]+i
    #             po=i
    #
    #
    #         if ans<Len[i]:
    #             ans=Len[i]
    #             get_po=i
    #
    #
    #     return init_s[get_po-ans+2:get_po+ans:2]   #返回Len[i]中的最大值-1即为原串的最长回文子串额长度


print(Solution().longestPalindrome('abbabb'))
# print(Solution().check(''))
