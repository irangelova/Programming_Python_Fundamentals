lost_fights = int(input())
price_helmet = float(input())
price_sword = float(input())
price_shield = float(input())
price_armor = float(input())
total_expenses = 0

broken_helmet = lost_fights // 2
broken_sword = lost_fights // 3
broken_shield = lost_fights // (2 * 3)
broken_armor = broken_shield // 2

total_expenses = (broken_helmet * price_helmet) \
                 + (broken_sword * price_sword) \
                 + (broken_shield * price_shield) \
                 + (broken_armor * price_armor)

print(f"Gladiator expenses: {total_expenses:.2f} aureus")