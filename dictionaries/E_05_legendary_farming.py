key_materials = {}
junk_materials = {}
legendary_item = ""
legendary_item_obtained = False

while True:
    if legendary_item_obtained:
        break
    materials = input().split()

    for index in range(0, len(materials), 2):
        if legendary_item_obtained:
            break
        if materials[index + 1].lower() == "shards" or materials[index + 1].lower() == "fragments" or materials[index + 1].lower() == "motes":
            if materials[index + 1].lower() not in key_materials.keys():
                key_materials[materials[index + 1].lower()] = 0
            key_materials[materials[index + 1].lower()] += int(materials[index])
        else:
            if materials[index + 1].lower() not in junk_materials.keys():
                junk_materials[materials[index + 1].lower()] = 0
            junk_materials[materials[index + 1].lower()] += int(materials[index])

        for material, value in key_materials.items():
            if value >= 250:
                if material == "shards":
                    legendary_item = "Shadowmourne"
                elif material == "fragments":
                    legendary_item = "Valanyr"
                elif material == "motes":
                    legendary_item = "Dragonwrath"
                legendary_item_obtained = True
                key_materials[material] -= 250
                break

print(f"{legendary_item} obtained!")
if "shards" in key_materials.keys():
    print(f"shards: {key_materials['shards']}")
else:
    print("shards: 0")
if "fragments" in key_materials.keys():
    print(f"fragments: {key_materials['fragments']}")
else:
    print("fragments: 0")
if "motes" in key_materials.keys():
    print(f"motes: {key_materials['motes']}")
else:
    print("motes: 0")

for material, value in junk_materials.items():
    print(f"{material}: {value}")

