user_languages = {}
user_points = {}

while True:
    entry = input()

    if entry == "exam finished":
        break

    if len(entry.split("-")) == 2:
        banned_name = entry.split("-")[0]
        del user_points[banned_name]
    else:
        username = entry.split("-")[0]
        language = entry.split("-")[1]
        points = entry.split("-")[2]

        if language not in user_languages.keys():
            user_languages[language] = 0
            user_points[username] = 0
        if username not in user_points.keys():
            user_points[username] = int(points)
        if int(points) > user_points[username]:
            user_points[username] = int(points)
        user_languages[language] += 1

print("Results:")
for user, result in user_points.items():
    print(f"{user} | {result}")
print("Submissions:")
for language, submission in user_languages.items():
    print(f"{language} - {submission}")
