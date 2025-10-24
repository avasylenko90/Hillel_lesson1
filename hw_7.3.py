def second_index(text, some_str):
    first_index = text.find(some_str)
    second_outcome = text.find(some_str, first_index + len(some_str))
    if second_outcome == -1:
        return None
    else:
        return (second_outcome)
    print(second_outcome)

print(second_index("Hello, hello", "lo"))
print("ОК")
