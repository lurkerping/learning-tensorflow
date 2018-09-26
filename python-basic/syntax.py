#!/usr/bin/python3
# comment
print("comment using #")
'''
comment using triple '
'''
print("comment using '''")
"""
comment using triple "
"""
print('comment using """')

# Indentation
if True:
    print("True")
    print("true")

# multi line
total = 1 + 2 + \
        3 + 4 + \
        5 + 6
print(total)

# basic type
# int/bool/float/complex
# triple ''' makes paragraph
paragraph = """many many years ago, there's a boy
name batman. he is handsome!
"""
print(paragraph)
# escape character \
# using r makes escape not working
print(r"new line \n?")
# concatenation
print("you're " "really " "good")
print("you're " + "really " + "good")
# substring
print("batman"[3:])

# code group
a = 10
if a > 5:
    print("a > 5")
else:
    print("a <= 5")

# print without new line
print("this is ok", end="")
print()

# import and from...import
