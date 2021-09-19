# 図形を90度回転する関数
def rotate(S):
    res = [[''] * N for _ in range(N)]
    # N = 5の時を考える。
    # (0, 0)の値は(0, 4)へ移動。(0, 1)の値は(1, 4)へ移動。(0, 2)の値は(2, 4)へ移動。(0, 3)の値は(3, 4)へ移動。(0, 4)の値は(4, 4)へ移動。
    # (1, 0)の値は(0, 3)へ移動。(1, 1)の値は(1, 3)へ移動。...と続けていく。
    # 参考 : https://daeudaeu.com/2d-rotate/#i-6
    for i in range(0, N):
        for j in range(0, N):
            res[j][N - i - 1] = S[i][j]
    return res

# 初めて左上に#が現れる座標を取得する関数
def leftAndTop(S):
    for i in range(0, N):
        for j in range(0, N):
            if S[i][j] == '#':
                return i, j

# 図形が等しいかどうか検証する関数
def isSame(S, T):
    # 初めて左上に#が現れる、座標を取得する。
    sx, sy = leftAndTop(S)
    tx, ty = leftAndTop(T)
    # 座標のずれを調整するためにoffsetを設ける。
    # offsetとは? : https://wa3.i-3-i.info/word11923.html
    offsetX = tx - sx
    offsetY = ty - sy

    for i in range(0, N):
        for j in range(0, N):
            # offsetをプラスする。
            ii = i + offsetX
            jj = j + offsetY
            # 座標の値が枠の中の場合
            if 0 <= ii < N and 0 <= jj < N:
                if S[i][j] != T[ii][jj]: return False
            # 座標の値が枠の外の場合
            else:
                # 座標の値が枠の外の場合に、S[i][j] == '#'だと、#の数が一致せずに異なる図形となるため、Falseを返す。
                if S[i][j] == '#': return False
    return True

# 標準入力を受け付ける。
N = int(input())

S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(N)]

# #の数を数える。
# #の数が違うと、図形が同じであると言えないため。
sumS = 0
sumT = 0
for i in range(0, N):
    for j in  range(0, N):
        if S[i][j] == '#':
            sumS += 1
        if T[i][j] == '#':
            sumT += 1

if sumS != sumT:
    print('No')
    exit()

# range(0, 4)なのは、図形を90度回転して等しいか検証するパターンが、4種類あるため。
for i in range(0, 4):
    if isSame(S, T):
        print('Yes')
        exit()
    S = rotate(S)
print('No')
