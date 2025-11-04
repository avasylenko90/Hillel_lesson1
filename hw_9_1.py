def popular_words(text:str, words:list):
    processed_text = text.lower().split()
    new_dict = {}
    for word in words:
        new_dict[word] = processed_text.count(word)
    return new_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')