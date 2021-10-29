char2num = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
}



class longlongInt :
    def __init__(self, nums = '', size = 0):
        self.num = []
        if nums != '':
            for n in reversed(nums) :
                self.num.append(char2num[n])
            return
        if size != 0 :
            self.num = [0 for _ in range(size)]

    def deleteHeading0(self):
        while len(self.num) >1 and self.num[len(self.num)-1] == 0:
            self.num = self.num[:len(self.num)-1]


    def output(self):
        self.deleteHeading0()
        res = ''
        for n in reversed(self.num) :
            res += (list(char2num.keys())[n])
        return res

    def multi10(self, times):
        for i in range(times) :
            self.num.insert(0,0)
        return self

    def __add__(self, other):
        result = longlongInt(size = max(len(self.num),len(other.num))+1)
        if len(self.num) < len(other.num):
            self.num = self.num+[0 for _ in range(len(other.num)-len(self.num))]
        else:
            other.num = other.num+[0 for _ in range(len(self.num)-len(other.num))]

        for i in range(len(self.num)):
            sumI = self.num[i] + other.num[i] + result.num[i]
            result.num[i] = sumI % 10
            result.num[i+1] += int(sumI / 10)
        #result.deleteHeading0()
        return result

    def __mul__(self, other):
        result = longlongInt(size=len(self.num)+ len(other.num))
        short = None
        long = None
        if len(self.num) < len(other.num) :
            short = self
            long = other
        else:
            short = other
            long = self

        for i in range(len(short.num)) :
            midRes = longlongInt(size=len(long.num)+1)
            for j in range(len(long.num)) :
                m1 = short.num[i] * long.num[j]
                midRes.num[j] = midRes.num[j] + m1% 10
                midRes.num[j+1] = int(m1 / 10)
            result = result+midRes.multi10(i)

        return result


class Solution:
   def multiply(self, num1: str, num2: str) -> str:
       n1 = longlongInt(nums= num1)
       n2 = longlongInt(nums= num2)

       return (n1*n2).output()

if __name__ == '__main__':
    ss = Solution()
    print(ss.multiply("123",'456'))

