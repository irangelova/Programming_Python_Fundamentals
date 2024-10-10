def loading_bar(number: int) -> str:
    if number == 100:
        return f"{number}% Complete!\n[%%%%%%%%%%]"
    count_percentage = number // 10
    count_dots = 10 - count_percentage
    return f"{number}% [{'%' * count_percentage}{'.'* count_dots}]\nStill loading..."


current_number = int(input())
print(loading_bar(current_number))
