Dict = open('en-ru.txt', 'r')
inp = open('input.txt', 'r')
out = open('output.txt', 'w')
Dictionary = dict()
Lines = Dict.readlines()
Lines = [line.split() for line in Lines]
print(Lines)
for line in Lines:
    enword, ruword = line.split('\t-\t')
    Dict[enword] = ruword
Textlines = inp.readlines()
for i in range(len(Textlines)):
    Textlines[i] = Textlines[i].split()
for i in range(len(Textlines)):
    for j in range(len(Textlines[i])):
        if Textlines[i][j] in Dictionary:
            Textlines[i][j] = Dictionary[Textlines[i][j]]
for i in range(len(Textlines)):
    for j in range(len(Textlines[i])):
        print(Textlines[i][j], end = ' ', file = 'out')