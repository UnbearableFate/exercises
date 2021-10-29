class my_list(list):
    def __init__(self, n):
        super().__init__(n)


test = [1,2,3]
tt = my_list(test)

print(tt)