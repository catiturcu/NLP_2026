#   Visiting professors can be annoying
#   adj/verb subst     modal verb adj
"""
Visiting professors
can be annoying

P -> NP VP

NP -> Adj N
NP -> GER
NP -> N

GER -> G NP

VP -> Modal VP
VP -> V Adj

Adj -> 'visiting' | 'annoying'
G -> 'visiting'
N -> 'professors'
Modal -> 'can'
V -> 'be'


 # OLD MEN AND WOMEN WERE WAITING OUTSIDE
   ADJ N   CON N     AUX  VERB     ADV

OLD MEN AND WOMEN -NP / WERE WAITING OUTSIDE -VP

P-> NP VP
NP-> NP C NP
NP->ADJ N
VP-> AUX VB ADV

NP-> N

ADJ->'OLD'
N->'WOMEN'
N->'MEN'
C->'AND'
AUX->'WERE'
VB->'WAITING'
ADV->'OUTSIDE'




  #The reporter interviewed the actor with the camera near the entrance
   D     N          V           NP      P     NP       P      NP


P-> NP VP

NP -> Det N
NP -> NP PP

VP -> V NP
VP -> VP PP

PP -> P NP

Det -> 'the'
N -> 'reporter' | 'actor' | 'camera' | 'entrance'
V -> 'interviewed'
P -> 'with' | 'near'

"""


import nltk
from nltk import CFG
from nltk.parse import ChartParser
grammar = CFG.fromstring("""
S -> NP VP

NP -> D N
NP -> GER
NP -> NP C NP
NP -> NP PP
NP -> N
NP -> ADJ NP
GER -> G NP

VP -> M VP
VP -> V NP
VP -> V ADJ
VP -> AUX VBB
VP -> AUX VBB ADV
VP -> VP PP

PP -> P NP

D -> 'the'
N -> 'professors' | 'men' | 'women' | 'reporter' | 'actor' | 'camera' | 'entrance'
ADJ -> 'visiting' | 'old' | 'annoying'
G -> 'visiting'
M -> 'can'
AUX -> 'be' | 'were'
V -> 'interviewed' | 'be'
VBB -> 'waiting'
ADV -> 'outside'
C -> 'and'
P -> 'with' | 'near'


""")

print(grammar)

parse=ChartParser(grammar)

text=["Visiting professors can be annoying.","Old men and women were waiting outside.","The reporter interviewed the actor with the camera near the entrance."]
for i in text:
    words=i.lower().replace("."," ").split()
    print("TEXT-PROP: ",text)
    trees=list(parse.parse(words))

    print("NR: ",len(trees))
    for tree in trees:
        print(tree)
        tree.pretty_print()





