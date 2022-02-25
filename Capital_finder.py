text = input().split(" ")

n = len(text)

words = {}
for i in range(n-1):
    if text[i+1][0].isupper():
        if text[i][-1] != '.':
            trimmed_word = text[i+1].strip(".,")
            words.update({i+2: trimmed_word})

if len(words.keys()) == 0:
    print("None")
else:
    for index in words.keys():
        print("{}:{}".format(index, words.get(index)))