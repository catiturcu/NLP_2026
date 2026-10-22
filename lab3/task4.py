G=[  #gram
    ("S",["NP","VP"],0.8),
    ("S",["AUX","NP","VP"],0.1),
    ("S",["VP"],0.1),
    ("NP",["PRON"],0.2),
    ("NP",["PROPER-NOUN"],0.2),
    ("NP",["DET","NOMINAL"],0.6),
    ("NOMINAL",["NOUN"],0.3),
    ("NOMINAL",["NOMINAL","NOUN"],0.2),
    ("NOMINAL",["NOMINAL","PP"],0.5),
    ("VP",["VERB"],0.2),
    ("VP",["VERB","NP"],0.5),
    ("VP",["VP","PP"],0.3),
    ("PP",["PREP","NP"],1.0),

    #lexical
    ("DET",["the"],0.6),
    ("DET",["a"],0.2),
    ("DET", ["that"], 0.1),
    ("DET", ["this"], 0.1),

    ("NOUN", ["book"], 0.1),
    ("NOUN", ["flight"], 0.5),
    ("NOUN", ["meal"], 0.2),
    ("NOUN", ["money"], 0.2),

    ("VERB", ["book"], 0.5),
    ("VERB", ["include"], 0.2),
    ("VERB", ["prefer"], 0.3),

    ("PRON", ["I"], 0.5),
    ("PRON", ["he"], 0.1),
    ("PRON", ["she"], 0.1),
    ("PRON", ["me"], 0.3),

    ("PROPER-NOUN", ["Houston"], 0.8),
    ("PROPER-NOUN", ["NWA"], 0.2),

    ("AUX", ["does"], 1.0),
    ("PREP", ["from"], 0.25),
    ("PREP", ["to"], 0.25),
    ("PREP", ["on"], 0.1),
    ("PREP", ["near"], 0.2),
    ("PREP", ["through"], 0.2)
]
sum={}
for left,right,probability in G:
    print(left,"->"," ".join(right),probability)
    if left not in sum:
        sum[left]=0
    sum[left]+=probability

for symbol,total in sum.items():
    print(symbol,"=",round(total,3))

def transf(G):
    new_G=[]
    count=1

    for left,right,probability in G:
        if len(right)<=2:
            new_G.append((left,right,probability))
        else:
            while(len(right)>2):
                new_S="X"+str(count)
                count+=1
                new_G.append((left,[right[0],new_S],probability))
                left=new_S
                right=right[1:]
                probability=1.0
            new_G.append((left,right,probability))

    return new_G

def transf2(G):
    neterm = set()

    for left, right, probability in G:
        neterm.add(left)

    reg_u = {}
    reg_n = []

    for left, right, probability in G:
        if len(right) == 1 and right[0] in neterm:
            if left not in reg_u:
                reg_u[left] = []

            reg_u[left].append((right[0], probability))
        else:
            reg_n.append((left, right, probability))
    rez = {}

    for A in neterm:
        rez[A] = {}

        def caut(B, probability, vizit):
            for left, right, p in reg_n:
                if left == B:
                    regula = (A, tuple(right))

                    if regula not in rez[A]:
                        rez[A][regula] = 0.0

                    rez[A][regula] += probability * p

            if B in reg_u:
                for C, p in reg_u[B]:
                    if C not in vizit:
                        caut(C, probability * p, vizit | {C})

        caut(A, 1.0, {A})

    G_nou = []

    for A in rez:
        for (left, right), p in rez[A].items():
            G_nou.append((left, list(right), p))

    return G_nou


print("---------------------GRAMMAR CNF--------------------------")
cnf=transf(G)
cnf=transf2(cnf)
for left,right,probability in cnf:
    print(left,"->"," ".join(right),round(probability,2))


def verif_CNF(G):
    neterminale = {left for left, right, p in G}

    for left, right, p in G:
        if len(right) == 1 and right[0] in neterminale:
            print("Regula unitara:", left, "->", right)
            return False

        if len(right) > 2:
            print("Prea multe simboluri:", left, "->", right)
            return False

    print("Toate regulile respecta CNF!")
    return True


def verifica_probabilitati(G):
    sume = {}

    for left, right, p in G:
        sume[left] = sume.get(left, 0) + p

    for left, suma in sorted(sume.items()):
        print(left, "=", round(suma, 6))
        if abs(suma - 1.0) > 1e-6:
            print("Atentie: probabilitatile nu insumeaza 1 pentru", left)

print("---------------------VERIFIC CNF G --------------------------")
verif_CNF(G)

print("---------------------VERIFIC CNF GCNF--------------------------")
verif_CNF(cnf)

print("---------------------VERIFIC PROB G --------------------------")
verifica_probabilitati(G)

print("---------------------GRAMMAR PROB GCNF--------------------------")
verifica_probabilitati(cnf)
