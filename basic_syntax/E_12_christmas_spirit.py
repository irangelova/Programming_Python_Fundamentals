decorations_quantity = int(input())
days_to_christmas = int(input())
money_spent = 0
christmas_spirit = 0
price_ornaments = 2
price_tree_skirt = 5
price_tree_garland = 3
price_tree_lights = 15
spirit_ornaments = 5
spirit_tree_skirt = 3
spirit_tree_garland = 10
spirit_tree_lights = 17

for day in range(1, days_to_christmas + 1):
    if day % 11 == 0:
        decorations_quantity += 2
    if day % 2 == 0:
        money_spent += price_ornaments * decorations_quantity
        christmas_spirit += spirit_ornaments
    if day % 3 == 0:
        money_spent += (price_tree_skirt + price_tree_garland) * decorations_quantity
        christmas_spirit += spirit_tree_skirt + spirit_tree_garland
    if day % 5 == 0:
        money_spent += price_tree_lights * decorations_quantity
        christmas_spirit += spirit_tree_lights
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        money_spent += price_tree_skirt + price_tree_garland + price_tree_lights
if day % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmas_spirit}")