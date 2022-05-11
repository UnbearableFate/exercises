def numberOfItems(s, startIndices, endIndices):
    result = []
    for i in range(len(startIndices)):
        #subStr = s[startIndices[i] - 1:endIndices[i]]
        beg = s.find('|',startIndices[i] - 1,endIndices[i])
        end = s.rfind('|',startIndices[i] - 1,endIndices[i])
        if beg == -1 or end == -1:
            result.append(0)
            continue
        ct = s.count('*',beg+1,end)
        result.append(ct)
    return result
    # Write your code here


def numberOfItems2(s, startIndices, endIndices):
    result = []
    for i in range(len(startIndices)):
        subStr = s[startIndices[i]-1:endIndices[i]]
        parts = subStr.split('|')[1:-1]
        ct = 0
        for p in parts:
            ct+=len(p)
        result.append(ct)
    return result
if __name__ == '__main__':
    print(numberOfItems("*|*|",[1,1],[1,3]))
    #print(numberOfItems("|**|*|*", [1, 1], [5, 6]))