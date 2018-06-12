class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # print(len(s))
        if s == '':
            return True
        lens = len(s)
        if lens % 2 == 1:
            return False
        lists = []
        lists.append(s[0])
        i = 1
        while i < lens:
            #print(s[i], lists[-1])
            #if s[i] == lists[-1]:
            if s[i] == '}' and lists[-1] == '{' or s[i] == ')' and lists[-1] == '(' or s[i] == ']' and lists[-1] == '[' or s[i] == ' ' and lists[-1] == ' ':
                del lists[-1]
                i = i + 1
            else:
                lists.append(s[i])
                i += 1
        if len(lists) == 0:
            return True
        else:
            return False
print(Solution().isValid('{[  ]}'))
