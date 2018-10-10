class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_map = {}
        result = []
        for i in strs:
            string = ''.join(sorted(i))
            if string not in strs_map:
                strs_map[string] = len(result)
                result.append([i])
            else:
                result[strs_map[string]].append(i)
        return result


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
