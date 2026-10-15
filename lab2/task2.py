#https://www.europarl.europa.eu/topics/ro/article/20200827STO85804/ce-este-inteligenta-artificiala-si-cum-este-utilizata
#https://www.europarl.europa.eu/doceo/document/TA-8-2019-0081_RO.html
from collections import Counter
with open("corpus.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()
s=".,!?;:()/|`~#$%&*[]{}\"'„”–—-"
for i in s:
    text = text.replace(i, " ")

tokens = text.split()
print("nr tokens:", len(tokens))
#print("primii 10:",tokens[0:10])
vocab=set(tokens)
print("dimensiunea ",len(vocab))

n=int(input("N>1 FOR N-GRAM: "))
ngrams=[]
for i in  range(len(tokens)-n+1):
    gram=tuple(tokens[i:i+n])
    ngrams.append(gram)
counts={}
for gram in ngrams:
    if gram in counts:
        counts[gram]+=1
    else:
        counts[gram]=1

print("Numar total de N-grame:", len(ngrams))
print("Numar de N-grame distincte:", len(counts))

contexts={}
for gram in ngrams:
    context =gram[:-1]

    if context in contexts:
        contexts[context]+=1
    else:
        contexts[context]=1

prob={}

for gram in counts:
    context=gram[:-1]
    if n==1:
        prob[gram]=counts[gram]/len(tokens)
    else:
        prob[gram]=counts[gram]/contexts[context]

lista=list(counts)

lista.sort(key=lambda gram: counts[gram], reverse=True)
print("\n FREC: ")
for i in range(5):
    gram=lista[i]
    print( gram, "| count:", counts[gram],"| probability:", round(prob[gram],2))

prob2={}
for gram in counts:
    context=gram[:-1]
    if n==1:
        prob2[gram]=(counts[gram]+1)/(len(tokens)+len(vocab))
    else :
        prob2[gram] = (counts[gram] + 1) / (contexts[context]+ len(vocab))


gram = lista[0]

print("\nVerificare smoothing:")
print("N-grama:", gram)
print("Probabilitate initiala:", prob[gram])
print("Probabilitate dupa smoothing:", prob2[gram])
