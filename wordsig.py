def reverse(word):
    return word[::-1] + " "
words = 'these are words i wrote'
for word in words.split(" "):
    print(reverse(word), end="")