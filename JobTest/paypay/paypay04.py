def solution(a):
    countMap = {
        '0': 0,
        '1': 0,
        '2': 0,
        '3': 0,
        '4': 0,
        '5': 0,
        '6': 0,
        '7': 0,
        '8': 0,
        '9': 0,
    }
    for num in a:
        numStr = str(num)
        for c in numStr:
            countMap[c]+=1
    resultMap = sorted(countMap.items(),key= lambda x:x[1],reverse = True)
    maxValue = resultMap[0][1]
    result = []
    for resultCp in resultMap:
        if resultCp[1] == maxValue:
            result.append(int(resultCp[0]))
        else:
            break
    return result

if __name__ == '__main__':
    print(solution([25, 2, 3, 57, 38, 41]))

