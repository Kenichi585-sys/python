import random

#A~Fまでの６人がいるリストを用意する
gr = ['A', 'B', 'C', 'D', 'E', 'F']
#リストから3 人、または 2 人をランダムに取り出す
n = random.choice([2, 3])
r = random.sample(gr, n)
#２人が取り出された場合、他の４人を取り出す
if n == 2:
    others = [p for p in gr if p not in r]
#２人以外が取り出された場合、他の３人を取り出す
else:
    others = [p for p in gr if p not in r]
#グループごとに分けて出力する
print(r)
print(others)
