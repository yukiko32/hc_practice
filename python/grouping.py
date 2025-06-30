import random

# メンバーをリストに定義する
members = ["A", "B", "C", "D", "E", "F"]

# グループの分け方を設定
split_patterns = [(3, 3), (2, 4)]

# グループの分け方をランダムに決める
split_pattern = random.choice(split_patterns)

# メンバーリストをランダムに並び替える
random.shuffle(members)

# グループを2つに分けてアルファベット順に並び替える
split_idx = split_pattern[0]
first_group = sorted(members[:split_idx])
second_group = sorted(members[split_idx:])

# 結果を表示する
print(first_group)
print(second_group)
