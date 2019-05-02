# 计算1+22+3+...+100：
sum = 0
n = 1
while n <= 100:
    sum = sum + n
    n = n + 1
print(sum) # 5050

# 计算1x2x3x...x100:
acc = 1
n = 1
while n <= 100:
    acc = acc * n
    n = n + 1
print(acc) # 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000