class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        '''
        group

是将所有匹配符合条件的字符串，打包成一个组，即group。
其中编号为0的group，即group(0)表示匹配的整个字符串。
其他编号分别为1,2,3，…的表示匹配成功返回的组中的每个字符串。

s 匹配的表达式  p 是匹配的正则表达式

re.match(pattern, string, flags=0)
函数参数说明：

参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串
        '''
        x = (re.match(p, s))
        if x == None:
            return False
        if x.group() != s:
            return False
        return True
