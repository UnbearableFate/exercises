from typing import List


def stringSplit(words: str, step: int) -> list:
    result = []
    if len(words) % step != 0:
        return []
    for i in range(0, len(words), step):
        result.append(words[i:i + step])
    return result


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if len(words) == 0:
            return []
        wordLength = len(words[0])
        numOfwords = len(words)
        step = wordLength * numOfwords
        beg = 0
        wordCountMaxMap = dict()
        for w in words:
            if w in wordCountMaxMap.keys():
                wordCountMaxMap[w] += 1
            else:
                wordCountMaxMap[w] = 1

        while beg <= len(s) - wordLength * numOfwords:
            possbileWordList = stringSplit(s[beg:beg + step], wordLength)
            ok = True
            for w in possbileWordList:
                if not (w in wordCountMaxMap.keys() and possbileWordList.count(w) < wordCountMaxMap[w]):
                    ok = False
                    break
            if ok:
                res.append(beg)
            beg += 1
        return res

if __name__ == '__main__':
    ss = Solution()
    print(ss.findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake",
                           ["fooo","barr","wing","ding","wing"]))