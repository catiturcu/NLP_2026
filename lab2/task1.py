#task1
corpus = ["low","new","lowest","newest","widest","lower"]
dict={}
vocab = []
sect=[]
for i in corpus:
    dict[i]=list(i)

for i in corpus:
    for c in i:
        if c not in vocab:
            vocab.append(c)

print("CORPUS:",dict)
print("VOCAB:",vocab)

def count_pairs(dict):
    pairs={}
    for i in dict:
        split=dict[i]
        for j in range(len(split)-1):
            pair=(split[j],split[j+1])
            if pair not in pairs:
                pairs[pair]=1
            else:
                pairs[pair]+=1
    return pairs


def merge_pairs(a, b, dict):
    for i in dict:
        split = dict[i]
        new = []
        k = 0

        while k < len(split):
            if k < len(split) - 1 and split[k] == a and split[k+1] == b:
                new.append(a + b)
                k = k + 2
            else:
                new.append(split[k])
                k = k + 1

        dict[i] = new

    return dict

for i in range(5):
    pairs = count_pairs(dict)
    best = None
    count = 0

    for p in pairs:
        if pairs[p] > count:
            count = pairs[p]
            best = p

    a = best[0]
    b = best[1]
    merged = a + b

    sect.append((a, b, merged))
    dict = merge_pairs(a, b, dict)

    if merged not in vocab:
        vocab.append(merged)

    print("\nMerge", i + 1, ":", best, "->", merged)
    print("Count:", count)
    print("Corpus:", dict)
    print("Vocabulary:", vocab)

word = list("slowest")

for a, b, merged in sect:
    new_word = []
    k = 0

    while k < len(word):
        if k < len(word) - 1 and word[k] == a and word[k + 1] == b:
            new_word.append(merged)
            k += 2
        else:
            new_word.append(word[k])
            k += 1

    word = new_word

print("\nUnseen word: slowest")
print("BPE tokens:", word)