
import spacy

nlp = spacy.load("en_core_web_sm")

sentences = [
    "Visiting professors can be annoying.",
    "Old men and women were waiting outside.",
    "The reporter interviewed the actor with the camera near the entrance."
]

for sentence in sentences:
    doc = nlp(sentence)

    print("\nSentence:", sentence)
    print("Token\tPOS\tDependency\tHead")

    for token in doc:
        print(
            token.text,
            "\t", token.pos_,
            "\t", token.dep_,
            "\t", token.head.text
        )
