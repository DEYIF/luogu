# 输入两个整数 a, b, 输出他们的和
# 输入以空格分隔

# My Answer
# input = str(input())
# space = -1
# for i in range(len(input)):
#     if input[i] == ' ':
#         space = i
# s1 = str(input[0])
# for i in range(1,space):
#     s1 = str(s1 + input[i])
# a = int(s1)
# s2 = str(input[space+1])
# for i in range(space+2,len(input)):
#     s2 = str(s2 + input[i])
# b = int(s2)
# print(a+b)

# Official Answer
s = input().split()
print(s)
print (int(s[0])+int(s[1]))