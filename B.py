# アルファベットのリストを作成する。
alphabetList = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z',
]

# 標準入力を受け付ける。
P = list(map(int, input().split()))

ans = ''
for i in range(0, len(P)):
    # P0, P1...の値に合致するアルファベットを選択し、文字列をつなぎ合わせる。
    # -1しているのは、配列のindexが0から始まるため。
    ans = ans + alphabetList[P[i] - 1]

print(ans)
