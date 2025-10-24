def correct_sentence(text):
    new_text = text[0].upper() + text[1:]
    if not text.endswith("."):
        new_text += "."
    return new_text

print(correct_sentence("Greetings, friends."))