'''COMPRESSION'''

dictionary = [chr(i) for i in range(256)]
input = open('someText.txt', 'r').read()
output = []

previous = ''
for char in input:
    if previous + char in dictionary:
        previous = previous + char
    else:
        output.append(dictionary.index(previous))
        if len(dictionary) <= 1000 and len(previous+char) <= 255:
            dictionary.append(previous + char)
        previous = char
output.append(dictionary.index(previous))

with open('encodedText.txt', 'w+') as f:
    for i in output:
        f.write(str(i) + ' ')

'''DECOMPRESSION'''

encoded = list(map(int, open('encodedText.txt', 'r').read().rstrip().split(' ')))
decodedList = []
for i in encoded:
    decodedList.append(dictionary[i])
decoded = ''.join(decodedList)
print(decoded)
with open('decodedText.txt', 'w+') as f:
    f.write(decoded)
