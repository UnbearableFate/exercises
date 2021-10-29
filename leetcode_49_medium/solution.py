from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resDict = dict()
        for word in strs :
            ss = tuple(sorted(word))
            if ss not in resDict:
                resDict[ss] = []
                resDict[ss].append(word)
            else:
                resDict[ss].append(word)
        return [ww for ww in resDict.values()]

if __name__ == '__main__':
    ss = Solution()
    print( ss.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) )
