def first_word(text):
    text = text.lstrip(" ")
    text = text.lstrip(".")
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    clean_text = text.split()
    return clean_text[0]

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
