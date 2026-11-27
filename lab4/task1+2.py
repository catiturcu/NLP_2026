
import torch
import requests
import logging

logging.disable(logging.WARNING)
logging.getLogger("transformers.modeling_utils").setLevel(logging.ERROR)

from transformers import AutoTokenizer, AutoModelForQuestionAnswering

model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

model.eval()

print("Enter context:\n")

context_lines = []

while True:
    line = input()

    if line.strip() == "END":
        break

    context_lines.append(line)

context = "\n".join(context_lines)

print("\nEnter questions:\n")

questions = []

while True:
    question = input()

    if question.strip() == "END":
        break

    questions.append(question)


for i, question in enumerate(questions, start=1):

    inputs = tokenizer(
        question,
        context,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    start_logits = outputs.start_logits
    end_logits = outputs.end_logits

    start_probs = torch.softmax(start_logits, dim=1)
    end_probs = torch.softmax(end_logits, dim=1)

    start_index = torch.argmax(start_probs, dim=1).item()
    end_index = torch.argmax(end_probs, dim=1).item()

    answer_tokens = inputs["input_ids"][0][start_index:end_index + 1]

    answer = tokenizer.decode(
        answer_tokens,
        skip_special_tokens=True
    )

    score = (
        start_probs[0, start_index] *
        end_probs[0, end_index]
    ).item()

    print("\n" + "=" * 60)
    print(f"Question {i}: {question}")
    print("Answer:", answer)
    print("Confidence score:", score)

    try:
        response = requests.get(
            "https://api.mymemory.translated.net/get",
            params={
                "q": answer,
                "langpair": "en|ro"
            },
            timeout=10
        )

        response.raise_for_status()

        translation = response.json()["responseData"]["translatedText"]

        print("Romanian:", translation)

    except Exception as e:
        print("Translation error:", e)

