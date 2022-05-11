# # A valid IP address consists of exactly four integers separated by single 
# dots.
# # Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#  
# # 
# # 
# # For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.01
# 1
# # .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses. 
# # 
# # 
# # Given a string s containing only digits, return all possible valid IP 
# # addresses that can be formed by inserting dots into s. You are not allowed 
# to reorder 
# # or remove any digits in s. You may return the valid IP addresses in any 
# order. 
# # 
# # 
# # Example 1: 
# # 
# # 
# # Input: s = "25525511135"
# # Output: ["255.255.11.135","255.255.111.35"]
# # 
# # 
# # Example 2: 
# # 
# # 
# # Input: s = "0000"
# # Output: ["0.0.0.0"]
# # 
# # 
# # Example 3: 
# # 
# # 
# # Input: s = "101023"
# # Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
# # 
# # 
# # 
# # Constraints: 
# # 
# # 
# # 1 <= s.length <= 20 
# # s consists of digits only. 
# # 
# # Related Topics String Backtracking 👍 2523 👎 621
# 


# leetcode submit region begin(Prohibit modification and deletion)
from copy import deepcopy
from typing import List
from queue import SimpleQueue as Queue


class state:
    def __init__(self, s: str):
        self.values = []
        self.others = s


class Solution:
    def check(self, node: state, num: int):
        if (3 - len(node.values)) * 3 < len(node.others) - num:
            return False
        return True

    def restoreIpAddresses(self, s: str) -> List[str]:
        qq = Queue()
        root = state(s)
        qq.put(root)
        res = set()
        while not qq.empty():
            top = qq.get()
            assert isinstance(top, state)
            if len(top.values) == 4:
                if top.others == "":
                    res.add('.'.join(top.values))
                continue
            if len(top.others) == 0:
                continue
            one = top.others[0]
            if self.check(top, 1):
                temp = state(top.others[1:])
                temp.values = deepcopy(top.values)
                temp.values.append(one)
                qq.put(temp)
            for i in range(2, 4):
                phrase = top.others[:i]
                if phrase.startswith('0') or not self.check(top,i):
                    continue
                if 0 < int(phrase) <= 255:
                    temp = state(top.others[i:])
                    temp.values = deepcopy(top.values)
                    temp.values.append(phrase)
                    qq.put(temp)
        return list(res)
# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("25525511135"))