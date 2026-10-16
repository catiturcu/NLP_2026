from transformers import AutoTokenizer, AutoModelForCausalLM
model_name="distilbert/distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
model = AutoModelForCausalLM.from_pretrained(model_name)

text="Artificial intelligence can help people"
inputs = tokenizer(text, return_tensors="pt")

print("Inputs:",text)
print("Token ID ",inputs["input_ids"])

outputs=model.generate(inputs["input_ids"],max_new_tokens=3,do_sample=False)

results=tokenizer.decode(outputs[0],skip_special_tokens=True)

print("Cont: ", results)
print("Text gen: ",results[len(text):])
