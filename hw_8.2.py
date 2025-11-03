def palindrome():
    expression = input("please enter expression:")
    expression = expression.lower()
    clear_expression = [char for char in expression if char.isdigit() or char.isalpha()]
    clear_str = "".join(clear_expression)
    if clear_str == clear_str[::-1]:
        return True
    else:
        return False
        print(clear_str)
result = palindrome()
print(result)