import re

racer_dictionary = {}

racers = input().split(", ")

while True:
    text = input()
    racer_name = ""
    racer_distance = 0

    if text == "end of race":
        break

    pattern1 = r"[A-Za-z]+"
    match_name = re.findall(pattern1, text)
    for element in match_name:
        racer_name += element

    pattern2 = r"\d"
    match_distance = re.findall(pattern2, text)
    for distance in match_distance:
        racer_distance += int(distance)

    if racer_name in racers:
        if racer_name not in racer_dictionary.keys():
            racer_dictionary[racer_name] = int(racer_distance)
        else:
            racer_dictionary[racer_name] += int(racer_distance)

sorted_dictionary = dict(sorted(racer_dictionary.items(), key=lambda item: item[1], reverse=True))
results = list(sorted_dictionary.keys())
print(f"1st place: {results[0]}")
print(f"2nd place: {results[1]}")
print(f"3rd place: {results[2]}")
