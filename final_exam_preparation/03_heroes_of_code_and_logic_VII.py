number_of_heroes = int(input())
heroes_data = {}

for num in range(number_of_heroes):
    hero_name, hp, mp = input().split()
    heroes_data[hero_name] = {"hp": int(hp), "mp": int(mp)}

while True:
    command = input().split(" - ")
    if command[0] == "End":
        break
    elif command[0] == "CastSpell":
        current_name = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if heroes_data[current_name]["mp"] >= mp_needed:
            heroes_data[current_name]["mp"] -= mp_needed
            print(f"{current_name} has successfully cast {spell_name} and now has {heroes_data[current_name]['mp']} MP!")
        else:
            print(f"{current_name} does not have enough MP to cast {spell_name}!")
    elif command[0] == "TakeDamage":
        current_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes_data[current_name]["hp"] -= damage
        if heroes_data[current_name]["hp"] > 0:
            print(f"{current_name} was hit for {damage} HP by {attacker} and now has {heroes_data[current_name]['hp']} HP left!")
        else:
            heroes_data.pop(current_name)
            print(f"{current_name} has been killed by {attacker}!")
    elif command[0] == "Recharge":
        current_name = command[1]
        mp_amount = int(command[2])
        if (heroes_data[current_name]["mp"] + mp_amount) > 200:
            mp_recovered = 200 - heroes_data[current_name]["mp"]
        else:
            mp_recovered = mp_amount
        heroes_data[current_name]["mp"] += mp_recovered
        print(f"{current_name} recharged for {mp_recovered} MP!")
    elif command[0] == "Heal":
        current_name = command[1]
        hp_amount = int(command[2])
        if (heroes_data[current_name]["hp"] + hp_amount) > 100:
            hp_recovered = 100 - heroes_data[current_name]["hp"]
        else:
            hp_recovered = hp_amount
        heroes_data[current_name]["hp"] += hp_recovered
        print(f"{current_name} healed for {hp_recovered} HP!")

for hero, data in heroes_data.items():
    print(f"{hero}")
    print(f"HP: {data['hp']}")
    print(f"MP: {data['mp']}")
