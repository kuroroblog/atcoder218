# 標準入力を受け付ける。
N = int(input())
# 重複の削除 + set型を利用する。 ⏩ in句を利用する際に、探索を高速化するため。
# なぜset型を利用すると高速になるのか? : https://qiita.com/kitadakyou/items/6f877edd263f097e78f4
points = set(tuple(map(int, input().split())) for _ in range(N))

ans = 0
for p1 in points:
    for p2 in points:
        # 1点を固定(p1とする)して、もう一点をp2とする場合、p1のx座標 < p2のx座標かつp1のy座標 < p2のy座標の場合の長方形を探す。
        if not(p1[0] < p2[0] and p1[1] < p2[1]):
            continue

        # 2点の情報から残りの2点の座標を洗い出す。
        r = (p2[0], p1[1])
        q = (p1[0], p2[1])

        # 残りの2点の情報が標準入力内に含まれるか、確認する。
        if r in points and q in points:
            ans += 1

print(ans)
