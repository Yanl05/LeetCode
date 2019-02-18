class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        # 击败46%
        res = []
        i = 0
        # print(len(words))
        while i < len(words):
            begin = i
            cursize = 0
            row_space = 0
            front_space = 0
            # 将下标为i的单词加入后该行单词的长度
            while i < len(words):
                if cursize == 0:
                    newsize = len(words[i])
                else:
                    newsize = cursize + len(words[i]) + 1
                if newsize <= maxWidth:
                    cursize = newsize
                else:
                    break
                i = i+1
            # 计算改行需要补的空格数
            space_num = maxWidth - cursize
            if i - begin - 1 > 0 and i < len(words):# i - begin - 1 为改行空格个数
                row_space = space_num // (i-begin-1)
                # 该行每个单词之间需要补充的空格数
                front_space = space_num % (i-begin-1)
                # 不能刚好整除时，剩余的空格数量，前front_space个间隔需要再多补一个空格
            else:
                # 不需要补额外的空格
                row_space = 0
            j = begin
            while j < i:
                # 若是该行的首个单词
                if j == begin:
                    tmp = words[j]
                else:
                    tmp += " "*(row_space + 1)
                    if front_space > 0 and i < len(words):
                        tmp += " "
                        front_space -= 1
                    tmp += words[j]
                j += 1
            # tmp += " "*front_space
            if len(tmp) != maxWidth:
                tmp += " "*(maxWidth-len(tmp))
            res.append(tmp)
        print(res)
        return res


        # 100%
        # cur, res, len_str =


# print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
if __name__ == '__main__':
    S = Solution()
    words = ["a", "b", "c", "d", "e"]
    # words1 = ["a"]
    # words2 = ["This", "is", "an","example", "of", "text","justification.","This", "is", "an","example", "of", "text","justification."]
    # words3 = [""]

    maxWidth = 3
    S.fullJustify(words, maxWidth)