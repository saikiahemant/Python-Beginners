"""
41. program to Reverse a Sentence Using Recursion
"""

def reverse(sentence):
    if len(sentence) == 1:
        return sentence
    rev = reverse(sentence[1:])+sentence[0]
    return rev

s =raw_input("Enter your sentence: ")
print("Sentence in reverse is ",reverse(s))