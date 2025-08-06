import random

#A~Fまでの６人がいるリストを用意する
friends = ['A', 'B', 'C', 'D', 'E', 'F']
#リストから3 人、または 2 人をランダムに取り出す
group_choice = random.choice([2, 3])
group_first = random.sample(friends, group_choice)
#２人が取り出された場合、他の４人を取り出す
group_second = [p for p in friends if p not in group_first]
# グループごとに分けて出力する
print(group_first)
print(group_second)
