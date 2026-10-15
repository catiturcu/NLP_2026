#https://www.europarl.europa.eu/topics/ro/article/20200827STO85804/ce-este-inteligenta-artificiala-si-cum-este-utilizata
#https://www.europarl.europa.eu/doceo/document/TA-8-2019-0081_RO.html
from collections import Counter
from math import log
import math
import re
with open("corpus.txt", "r", encoding="utf-8") as file:
    text = file.read()

text = text.lower()
s=".,!?;:()/|`~#$%&*[]{}\"'„”–—-"
sentences = re.split(r'[.!?]+', text)

tokens = []
tokenized_sentences = []
for sentence in sentences:
    for i in s:
        sentence = sentence.replace(i, " ")

    words = sentence.split()

    if len(words) > 0:
        words = ["<s>"] + words + ["</s>"]
        tokenized_sentences.append(words)
        tokens.extend(words)

print("nr tokens:", len(tokens))
#print("primii 10:",tokens[0:10])
vocab=set(tokens)
print("dimensiunea ",len(vocab))

n=int(input("N>1 FOR N-GRAM: "))
ngrams = []

for words in tokenized_sentences:
    for i in range(len(words)-n+1):
        gram = tuple(words[i:i+n])
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

prop=input("PROP: ")
prop=prop.lower()

for i in s:
    prop=prop.replace(i, " ")
prop_tokens = prop.split()
prop_tokens = ["<s>"] + prop_tokens + ["</s>"]

if n == 1:
    prop_ngrams = []

    for word in prop_tokens[1:]:
        prop_ngrams.append((word,))
else:
    prop_ngrams = []

    for i in range(len(prop_tokens)-n+1):
        gram = tuple(prop_tokens[i:i+n])
        prop_ngrams.append(gram)

prop_prob = 1.0
log_prob = 0.0

print("\nprob cond: ")

for gram in prop_ngrams:
    context = gram[:-1]
    if gram in counts:
        count=counts[gram]
    else:
        count=0
    if n==1:
        p=(count+1)/(len(tokens)+len(vocab))
    else:
        if context in contexts:
            nr_context=contexts[context]
        else:
            nr_context=0
        p=(count+1)/(nr_context+len(vocab))

    print(gram,"->",p)
    prop_prob*=p
    log_prob+=math.log(p)

print("\nPROB PROP: ",prop_prob)
print("LOG PROP: ",log_prob)