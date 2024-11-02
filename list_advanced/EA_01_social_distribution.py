population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
no_equal_distribution_possible = False

for wealth in population:
    wealth_index = population.index(wealth)
    max_wealth = max(population)
    max_wealth_index = population.index(max_wealth)
    if wealth < minimum_wealth:
        if max_wealth - (minimum_wealth - wealth) >= minimum_wealth:
            max_wealth -= (minimum_wealth - wealth)
            population.insert(max_wealth_index, max_wealth)
            population.pop(max_wealth_index + 1)
            wealth += (minimum_wealth - wealth)
            population.insert(wealth_index, wealth)
            population.pop(wealth_index + 1)
        else:
            print("No equal distribution possible")
            no_equal_distribution_possible = True
            break

if not no_equal_distribution_possible:
    print(population)
