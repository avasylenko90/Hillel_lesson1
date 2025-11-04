def is_palindrome(expression: str):
    expression = expression.lower()
    clear_expression = [char for char in expression if char.isdigit() or char.isalpha()]
    clear_str = "".join(clear_expression)
    if clear_str == clear_str[::-1]:
        return True
    else:
        return False


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК ✅")