class Solution:
    def longestPalindrome(self, s):
        mx=0                   #mx即为当前计算回文串最右边字符的最大值
        ans=0
        po=0
        Len=[0]*10000

    ##转换字符串
        def INIT(s):
            init_s='@#'
            for x in s:
                init_s=init_s+x+'#'

            return init_s+'$',2*len(s)+1     # 字符串结尾加一个字符，防止越界 

        init_s,len_s=INIT(s)       #转换字符串
        get_po=0
        for i in range(1,len_s):
            if mx>i:
                Len[i]=min(mx-i,Len[2*po-i]) #在Len[j]和mx-i 中取小
            else:
                Len[i]=1  #如果i>mx，要从头开始匹配

            while init_s[i-Len[i]]==init_s[i+Len[i]]:
                Len[i]=Len[i]+1

            if Len[i]+i>mx:      #若新计算的回文串右端点位置大于mx，要更新po和mx的值
                mx=Len[i]+i
                po=i


            if ans<Len[i]:
                ans=Len[i]
                get_po=i


        return init_s[get_po-ans+2:get_po+ans:2]   #返回Len[i]中的最大值-1即为原串的最长回文子串额长度
