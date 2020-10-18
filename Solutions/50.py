"""
      50. Program to Find the Frequency of Characters in a String
"""

def frequency(sentence, ch):
    freq = 0
    for i in sentence:
        if i.lower() == ch:
            freq += 1
    return freq


sentence = raw_input("Enter a sentence: ")
ch = raw_input("Enter character to count frequency: ")

print "Frequency: of \'{}\': {}".format(ch,frequency(sentence,ch))