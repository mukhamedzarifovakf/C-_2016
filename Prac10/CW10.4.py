text=open('en-ru.txt')
ourWords={}
for line in text:
    line=line.replace('\t-\t','-').replace('\n','').split('-')


    ourWords[line[0]]=line[1]
text.close()

EnglishText=open('EnglishText.txt')
TranslatedText=open('TranslatedText.txt','w')
trans=[]
for line in  EnglishText.read().split():
     line=line.replace('.','').replace(',',' ')
     line=line.lower()
     if line.lower() in ourWords:
         trans.append(ourWords[line])
     else:
         trans.append(line)

for elem in trans:
    print(elem, end=' ')
    TranslatedText.write(elem)
    TranslatedText.write(' ')
TranslatedText.close()