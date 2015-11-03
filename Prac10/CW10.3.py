inp = open('input.txt', 'r')
Words = dict()
Lines = inp.read()
Lines = Lines.replace('.', ' ')
Lines = Lines.replace('!', ' ')
Lines = Lines.replace(',', ' ')
Lines = Lines.replace('\n', ' ')
Lines = Lines.split()
Lines = [word.lower() for word in Lines]
print(Lines)
for word in Lines:
    if word in Words:
        Words[word] += 1
    else:
        Words[word] = 1
max = 1
Words = {Words[word] : word for word in Words}
print(Words)
for key in Words:
    if key > max:
        max = key
print(Words[max])
