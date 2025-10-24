def say_hi(name,age, a="Hi. My name is", b="and I'm ", c="years old"):
    return f"{a} {name} {b} {int(age)} {c}"

print(say_hi(name="Frank",age=68))