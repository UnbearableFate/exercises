import functools
from typing import List


def compare(a, b):
    if a[1] == b[1]:
        if a[0] >= b[0]:
            return -1
        else:
            return 1
    else:
        return b[1] - a[1]


def solution(n, logs):
    # write your code in Python
    countMap = dict()
    for log in logs:
        log = log.split()
        ip = log[0]
        stateCode = log[1]
        url = log[2]
        if stateCode == "200":
            if url in countMap:
                countMap[url] += 1
            else:
                countMap[url] = 1
    result = []
    for url, ct in countMap.items():
        result.append((url, ct))
    result.sort(key=functools.cmp_to_key(compare))
    realRes = []
    index = 0
    while index < n and index < len(result):
        realRes.append(result[index][0])
    return realRes

    pass


if __name__ == '__main__':
    print(solution(3))
