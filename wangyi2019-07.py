'''
牛牛总是睡过头，所以他定了很多闹钟，只有在闹钟响的时候他才会醒过来并且决定起不起床。
从他起床算起他需要X分钟到达教室，上课时间为当天的A时B分，请问他最晚可以什么时间起床
输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个正整数，表示闹钟的数量N(N<=100)。
接下来的N行每行包含两个整数，表示这个闹钟响起的时间为Hi(0<=A<24)时Mi(0<=B<60)分。
接下来的一行包含一个整数，表示从起床算起他需要X(0<=X<=100)分钟到达教室。
接下来的一行包含两个整数，表示上课时间为A(0<=A<24)时B(0<=B<60)分。
数据保证至少有一个闹钟可以让牛牛及时到达教室。
输出描述:
输出两个整数表示牛牛最晚起床时间。
输入例子1:
3
5 0
6 0
7 0
59
6 59
输出例子1:
6 0

'''
import sys
N = sys.stdin.readline()
time = []
end =[]
for i in range(int(N)):
    clock = sys.stdin.readline()
    Hi, Mi = (map(int, clock.split()))
    time.append((Hi,Mi))

time=sorted(time, key=lambda s: s[1])
time=sorted(time, key=lambda s: s[0])
X = int(sys.stdin.readline())
cla = sys.stdin.readline()
A, B = map(int, cla.split())
for i in range(len(time)):

    fen = time[i][1]+X
    xs =time[i][0]
    if fen >= 60:
        xs=time[i][0]+(fen//60)
        fen = fen%60


        # time[i]=time[i]+1
        # time[i+1]=time[i+1]-60

    if xs<A or (xs==A and fen<=B):
        end.append(time[i][0])
        end.append(time[i][1])

print(end[-2], end[-1])




