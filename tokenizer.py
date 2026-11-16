## Implement basic word tokenization
# text = "I love learning Artificial Intelligence"
# tokens = text.split()

# print(tokens)
# print("Total Tokens:", len(tokens))


## Handle Puncuation
# import re
# text = "Hello, how are you?"

# tokens = re.findall(r"\w+|[^\w\s]",text)
# print(tokens)
# print("Total Tokens", len(tokens))


## Convert token into IDs
# import re
# text = "I love AI. I love Python."

# # Step 1 Tokenize
# tokens = re.findall(r"\w+|[^\w\s]",text)
# # Step 2 Create Vocabulary
# vocabulary = {}
# for token in tokens:
#     if token not in vocabulary:
#         vocabulary[token] = len(vocabulary)

# # Step 3 Convert tokens into IDs
# token_ids = [vocabulary[token] for token in tokens]
# print("Tokens:",tokens)
# print("Vocabulary:",vocabulary)
# print("Token IDs:",token_ids)


import re
# Accept a sentence using input()
sentence = input("Enter a Sentence: ")

# Convert the sentence to lowercase.
lowercase_sentence = sentence.lower()

# Separate words and punctuation.
tokens = re.findall(r"\w+|[^\w\s]",lowercase_sentence)

# Generate a vocabulary.
vocabulary = {}
for token in tokens:
    if token not in vocabulary:
        vocabulary[token] = len(vocabulary)

# Assign unique token IDs.
token_ids = [vocabulary[token] for token in tokens]

# Display the total number of tokens.
print("Total Number of Token:", len(tokens))
print("Tokens:",tokens)
print("Vocabulary:",vocabulary)
print("Token IDs:",token_ids)

