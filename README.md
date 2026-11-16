## Tokenization
### vocabulary-based token encoding
1. Word-level tokenization.
2. Punctuation handling.
3. Token-to-ID conversion.
### Step 1 - Set up your project
Create a folder:
```
mkdir tokenizer-project
cd tokenizer-project
```
Create a Python file:
```
tokenizer.py
```
Our project structure:
```
tokenizer-project/
│
└── tokenizer.py
```
### Step 2 - Implement basic word tokenization
```

text = "I love learning Artificial Intelligence"

tokens = text.split()

print(tokens)
print("Total tokens:", len(tokens))
```
### Step 3 - Handle Punctuation
Use Python's re module (Regular Expressions).
```

import re

text = "Hello, how are you?"

tokens = re.findall(r"\w+|[^\w\s]", text)

print(tokens)
print("Total tokens:", len(tokens))
```
### Step 4 - Convert tokens into IDs
```

import re

text = "I love AI. I love Python."

# Step 1: Tokenize
tokens = re.findall(r"\w+|[^\w\s]", text)

# Step 2: Create vocabulary
vocabulary = {}

for token in tokens:
    if token not in vocabulary:
        vocabulary[token] = len(vocabulary)

# Step 3: Convert tokens into IDs
token_ids = [vocabulary[token] for token in tokens]

print("Tokens:", tokens)
print("Vocabulary:", vocabulary)
print("Token IDs:", token_ids)
```

