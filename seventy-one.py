class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # pathlist = path.split("/")
        # pl1 = []
        # ret = []
        # for iter in pathlist:
        #     if iter != '':
        #         pl1.append(iter)
        # for iter in pl1:
        #     if iter == ".":
        #         continue
        #     elif iter == "..":
        #         if len(ret) != 0:
        #             ret.pop()
        #     else:
        #         ret.append(iter)
        #
        #
        #
        # return "/"+"/".join(ret)

        # 最优解
        res = []
        path = path.split('/')
        path = [i for i in path if i!='' and i!='.']
        for i in path:
            if i != '..':
                res.append(i)
            elif res:
                res.pop()
        return '/' + '/'.join(res)

print(Solution().simplifyPath("/a//b////c/d//././/.."))
# print(Solution().simplifyPath("/a/../../b/../c//.//"))