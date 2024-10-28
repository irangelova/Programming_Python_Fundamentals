input_numbers = list(map(int, input().split(", ")))
#index_even_numbers = [input_numbers.index(number) for number in input_numbers if number % 2 == 0]
#print(index_even_numbers)

found_indices_or_no = map(lambda x: x if input_numbers[x] % 2 == 0 else "no",
                          range(len(input_numbers)))
even_indices = list(filter(lambda a: a != "no", found_indices_or_no))
print(even_indices)