def password_validator(password: str) -> str:
    error_messages = []
    count_numbers = 0
    if len(password) < 6 or len(password) > 10:
        error_messages.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        error_messages.append("Password must consist only of letters and digits")
    for element in password:
        if element.isdigit():
            count_numbers += 1
    if count_numbers < 2:
        error_messages.append("Password must have at least 2 digits")
    if not error_messages:
        return "Password is valid"
    return "\n".join(error_messages)


password_to_check = input()
result = password_validator(password_to_check)
print(result)
