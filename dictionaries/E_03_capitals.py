countries_dictionary = input().split(", ")
capitals_dictionary = input().split(", ")

information = dict(zip(countries_dictionary, capitals_dictionary))

for country, capital in information.items():
    print(f"{country} -> {capital}")
