#assignment 1 question 3 auto tokenizer
from transformers import AutoTokenizer, AutoModelForCausalLM
from collections import Counter

# Load your desired tokenizer
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-2")
model = AutoModelForCausalLM.from_pretrained("microsoft/phi-2")

# Read the text document
with open("M:\WEDS01\Semester 3 2023\HIT137\Assignment 2\csv1.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Tokenize the text using the autotokenizer
tokens = tokenizer.tokenize(tokenizer.decode(tokenizer.encode(text)))

# Count the occurrences of each token
token_counts = Counter(tokens)

# Display the top 30 words
top_30_words = token_counts.most_common(30)
for word, count in top_30_words:
    print(f"{word}: {count}")