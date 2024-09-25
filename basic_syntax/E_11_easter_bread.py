budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = 0.75 * price_kg_flour
price_litre_milk = 1.25 * price_kg_flour
price_breads = 0
total_price_breads = 0
count_breads = 0
coloured_eggs = 0

while True:
    price_breads = price_pack_eggs + price_kg_flour + (price_litre_milk / 4)
    if (total_price_breads + price_breads) > budget:
        break
    else:
        total_price_breads += price_breads
    count_breads += 1
    coloured_eggs += 3

    if count_breads % 3 == 0:
        coloured_eggs -= (count_breads - 2)

print(f"You made {count_breads} loaves of Easter bread! Now you have {coloured_eggs} eggs and {(budget - total_price_breads):.2f}BGN left.")
