'''
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，分别表示工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)。
接下来的N行每行包含两个正整数，分别表示该项工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)。
接下来的一行包含M个正整数，分别表示M个小伙伴的能力值Ai(Ai<=1000000000)。
保证不存在两项工作的报酬相同。

输出描述:
对于每个小伙伴，在单独的一行输出一个正整数表示他能得到的最高报酬。一个工作可以被多个人选择。

输入例子1:
3 3
1 100
10 1000
1000000000 1001
9 10 1000000000

输出例子1:
100
1000
1001
'''
import sys
# 工作的数量N(N<=100000)和小伙伴的数量M(M<=100000)
T = input()
b = T.split(" ")
N = int(b[0])
if N >= 100000:
    print("数据超出题限范围，结束程序")
    sys.exit()
M = int(b[1])
if N >= 100000:
    print("数据超出题限范围，结束程序")
    sys.exit()
# input 默认接受str,所以要转型为int

# 工作的难度Di(Di<=1000000000)和报酬Pi(Pi<=1000000000)
t = []
Di = []
Pi = []
for i in range(N):
    a = input()
    t.append(a)
    b = t[i].split(" ")

    Di.append(int(b[0]))
    Pi.append(int(b[1]))
#print(Di, Pi)
# 能力值Ai(Ai<=1000000000)
Ai = []
t = []
a = input()
a = a.split(" ")
for i in range(M):
    Ai.append(int(a[i]))
#print(Ai)

#判断每个人的能力与工作难度
for i in Ai:
    sum1 = 0
    for j in range(len(Di)):
        if i >= Di[j]:
            if sum1 < Pi[j]:
                sum1 = Pi[j]
    print(sum1)

'''
您的代码已保存
请检查是否存在语法错误或者数组越界非法访问等情况
case通过率为20.00%
Traceback (most recent call last):
File "a.py3", line 46, in 
Di.append(int(b[0]))
ValueError: invalid literal for int() with base 10: ''
'''
