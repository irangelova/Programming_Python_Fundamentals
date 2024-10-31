number_of_electrons = int(input())
no_more_electrons_left = False
shells_occupied = []
current_shell = 0

while True:
    current_shell += 1
    current_electrons = 2 * (current_shell ** 2)
    if number_of_electrons < current_electrons and number_of_electrons != 0:
        current_electrons = number_of_electrons
        shells_occupied.append(current_electrons)
        break
    elif number_of_electrons == 0:
        break
    else:
        shells_occupied.append(current_electrons)
        number_of_electrons -= current_electrons

print(shells_occupied)