import string
from string import punctuation, whitespace

hash_tag1 = input("Please create the new hashtag ")
hash_tag2 = hash_tag1.title()
for char in hash_tag2:
    if char in punctuation or char in whitespace:
        hash_tag2 = hash_tag2.replace(char, "")
hash_tag3 = hash_tag2
if len(hash_tag3)>140:
    hash_tag3 = hash_tag3[:140]

hash_tag4 = "#" + hash_tag3
print(hash_tag4)
