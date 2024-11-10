def check_ticket(ticket: str) -> str:
    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ["@", "#", "$", "^"]
    first_half = ticket[:10]
    second_half = ticket[10:]
    for current_symbol in winning_symbols:
        for uninterrupted_match in range(10, 5, -1):
            winning_symbol_repetition = current_symbol * uninterrupted_match

            if winning_symbol_repetition in first_half and winning_symbol_repetition in second_half:
                if uninterrupted_match == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match}{current_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match}{current_symbol}'
    return f'ticket "{ticket}" - no match'


all_tickets = input().split(", ")
for current_ticket in all_tickets:
    ticket_to_check = current_ticket.strip()
    result = check_ticket(ticket_to_check)
    print(result)
