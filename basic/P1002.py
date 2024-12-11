# https://www.luogu.com.cn/problem/P1002
'''My first answer, correct but time limit exceeded'''
# def path_count(i, j, cp):
#     if [i,j] in cp:
#         return 0
#     elif i==0 and j==1:
#         return 1
#     elif i==1 and j==0:
#         return 1
#     elif i==0 and j==0:
#         return 0
#     elif i==0:
#         return path_count(i,j-1,cp)
#     elif j==0:
#         return path_count(i-1,j,cp)
#     elif i>0 and j>0:
#         return path_count(i-1,j,cp)+path_count(i,j-1,cp)

# input = input().split()
# B = [int(input[0]),int(input[1])]
# h = [int(input[2]),int(input[3])]
# cp = [[h[0],h[1]],
#       [h[0]+2,h[1]+1],
#       [h[0]+1,h[1]+2],
#       [h[0]-1,h[1]+2],
#       [h[0]-2,h[1]+1],
#       [h[0]-2,h[1]-1],
#       [h[0]-1,h[1]-2],
#       [h[0]+1,h[1]-2],
#       [h[0]+2,h[1]-1]]
# answer = path_count(B[0],B[1],cp)
# print(answer)

'''optimized using dynamic programming'''
input = input().split()
B = [int(input[0]),int(input[1])]
h = [int(input[2]),int(input[3])]
# initialize a 2-D arrary (n+1)*(m+1)
dp = [[0]*(B[1]+1) for _ in range(B[0]+1)]  # _ means we don't care about it
# initialize the control points
cp = set()
cp.add((h[0],h[1]))
moves = [
    (2,1),(1,2),(-2,-1),(-1,-2),
    (2,-1),(1,-2),(-2,1),(-1,2)
]
for dx,dy in moves:
    x=h[0]+dx
    y=h[1]+dy
    if 0<=x<=B[0] and 0<=y<=B[1]:
        cp.add((x,y))

if (0,0) not in cp:
    dp[0][0]=1

for i in range(B[0]+1):
    for j in range(B[1]+1):
        if (i,j) in cp:
            dp[i][j] = 0
        elif i==0 and j>0:
            dp [i][j] = dp [i][j-1]
        elif i>0 and j==0:
            dp [i][j] = dp [i-1][j]
        elif i>0 or j>0:
            dp [i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[B[0]][B[1]])


        