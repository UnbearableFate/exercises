import math
from collections import OrderedDict


def add2Number(str):
    nums = str.split(',')
    a = int(nums[0], 2)
    b = int(nums[1], 2)
    return bin(a + b)[2:]


def lemon(bills):
    valueNameDict2 = {
        0.01: "PENNY",
        0.05: "NICKEL",
        0.10: "DIME",
        0.25: "QUARTER",
        0.50: "HALF DOLLAR",
        1.00: "ONE",
        2.00: "TWO",
        5.00: "FIVE",
        10.00: "TEN",
        20.00: "TWENTY",
        50.00: "FIFTY"
    }
    valueNameDict = {
        1: "PENNY",
        5: "NICKEL",
        10: "DIME",
        25: "QUARTER",
        50: "HALF DOLLAR",
        100: "ONE",
        200: "TWO",
        500: "FIVE",
        1000: "TEN",
        2000: "TWENTY",
        5000: "FIFTY"
    }
    valueNameDict = dict(sorted(valueNameDict.items(), reverse=True))
    result = []
    for bill in bills:
        words = bill.split(';')
        diff = int(float(words[1])*100) - ((float(words[0]))*100)
        if diff == 0:
            result.append("ZERO")
            continue
        if diff < 0:
            result.append("ERROR")
            continue
        line = ""
        while diff > 0:
            for value, name in valueNameDict.items():
                if value <= diff:
                    diff -= value
                    line += "," + name
                    break
        result.append(line[1:])
    return result

if __name__ == '__main__':
    print(lemon(["9;10","9;10.83"]))
