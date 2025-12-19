print("Name: Shekhar Suman")
print("Roll No: 48")
import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    sentence_letters = set(sentence.lower())
    return alphabet <= sentence_letters

sentence = "shekhar's lazy dog jump over the quick brown fox"
result = is_pangram(sentence)

if result:
    print("The sentence is a pangram.")
else:
    print("The sentence is not a pangram.")
