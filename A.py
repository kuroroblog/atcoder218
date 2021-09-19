# 標準入力を受け付ける。
N = int(input())
# 文字列Sを1文字単位に分割し、リストに格納する。
S = list(input())

# リスト内のN - 1番目の値を取り出す。
# -1しているのは、配列のindexが0から始まるため。
ans = S[N - 1]

# 'o'なら'Yes'、'x'なら'No'を出力する。
if ans == 'o':
    print('Yes')
else:
    print('No')
