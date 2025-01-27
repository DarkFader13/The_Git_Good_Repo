
# Steps to Train a Chatbot on Markdown Files

## 1. **Install Required Libraries**
Install the necessary Python libraries:
```bash
pip install torch transformers datasets markdown
```

---

## 2. **Prepare Your Markdown Data**
Convert your Markdown files into plain text and preprocess them for training.

### Example: Convert Markdown to Plain Text
```python
import markdown
import os

# Function to convert Markdown to plain text
def markdown_to_text(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    html = markdown.markdown(md_text)
    return html  # Or use a library like `html2text` to further clean the text

# Load all Markdown files from a directory
def load_markdown_files(directory):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            text = markdown_to_text(filepath)
            texts.append(text)
    return texts

# Example usage
markdown_directory = "path/to/your/markdown/files"
training_texts = load_markdown_files(markdown_directory)
```

---

## 3. **Preprocess the Data**
Tokenize the text data using a tokenizer compatible with your model (e.g., GPT-2).

### Example: Tokenize Text Data
```python
from transformers import GPT2Tokenizer

# Load the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# Tokenize the text data
def tokenize_texts(texts):
    tokenized_data = tokenizer(
        texts,
        truncation=True,
        padding="max_length",
        max_length=512,  # Adjust based on your needs
        return_tensors="pt",
    )
    return tokenized_data

tokenized_data = tokenize_texts(training_texts)
```

---

## 4. **Load a Pre-trained Model**
Load a pre-trained language model (e.g., GPT-2) for fine-tuning.

### Example: Load GPT-2 Model
```python
from transformers import GPT2LMHeadModel

# Load the GPT-2 model
model = GPT2LMHeadModel.from_pretrained("gpt2")
```

---

## 5. **Set Up Training**
Define the optimizer, loss function, and data loader.

### Example: Training Setup
```python
from torch.utils.data import DataLoader, Dataset
import torch

# Create a PyTorch Dataset
class TextDataset(Dataset):
    def __init__(self, tokenized_data):
        self.input_ids = tokenized_data["input_ids"]
        self.attention_mask = tokenized_data["attention_mask"]

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {
            "input_ids": self.input_ids[idx],
            "attention_mask": self.attention_mask[idx],
        }

# Create DataLoader
dataset = TextDataset(tokenized_data)
train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

# Define optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
```

---

## 6. **Train the Model**
Fine-tune the model on your Markdown data.

### Example: Training Loop
```python
# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Training loop
epochs = 3
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in train_loader:
        # Move batch to device
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        # Forward pass
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)
        loss = outputs.loss

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch + 1}, Loss: {total_loss / len(train_loader)}")
```

---

## 7. **Save the Fine-Tuned Model**
Save the fine-tuned model for later use.

### Example: Save the Model
```python
model.save_pretrained("fine_tuned_chatbot")
tokenizer.save_pretrained("fine_tuned_chatbot")
```

---

## 8. **Test the Chatbot**
After training, you can interact with your chatbot by generating responses.

### Example: Generate Responses
```python
from transformers import pipeline

# Load the fine-tuned model
chatbot = pipeline("text-generation", model="fine_tuned_chatbot", tokenizer=tokenizer)

# Generate a response
prompt = "What is the main topic of your notes?"
response = chatbot(prompt, max_length=100, num_return_sequences=1)
print(response[0]["generated_text"])
```

---

# Summary of Steps
1. **Install libraries**: `pip install torch transformers datasets markdown`
2. **Prepare data**: Convert Markdown files to plain text and tokenize them.
3. **Load model**: Load a pre-trained GPT-2 model.
4. **Set up training**: Define optimizer, loss function, and data loader.
5. **Train the model**: Fine-tune the model on your Markdown data.
6. **Save the model**: Save the fine-tuned model for future use.
7. **Test the chatbot**: Generate responses using the fine-tuned model.

---

# Example Code for Training a Chatbot
Here’s the complete code for training a chatbot on Markdown files:

```python
import os
import markdown
from transformers import GPT2Tokenizer, GPT2LMHeadModel, pipeline
from torch.utils.data import DataLoader, Dataset
import torch

# Step 1: Convert Markdown to plain text
def markdown_to_text(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as f:
        md_text = f.read()
    html = markdown.markdown(md_text)
    return html

def load_markdown_files(directory):
    texts = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            text = markdown_to_text(filepath)
            texts.append(text)
    return texts

# Step 2: Tokenize the text data
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

def tokenize_texts(texts):
    tokenized_data = tokenizer(
        texts,
        truncation=True,
        padding="max_length",
        max_length=512,
        return_tensors="pt",
    )
    return tokenized_data

# Step 3: Load the GPT-2 model
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Step 4: Create a PyTorch Dataset and DataLoader
class TextDataset(Dataset):
    def __init__(self, tokenized_data):
        self.input_ids = tokenized_data["input_ids"]
        self.attention_mask = tokenized_data["attention_mask"]

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        return {
            "input_ids": self.input_ids[idx],
            "attention_mask": self.attention_mask[idx],
        }

markdown_directory = "path/to/your/markdown/files"
training_texts = load_markdown_files(markdown_directory)
tokenized_data = tokenize_texts(training_texts)
dataset = TextDataset(tokenized_data)
train_loader = DataLoader(dataset, batch_size=8, shuffle=True)

# Step 5: Set up training
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Step 6: Train the model
epochs = 3
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in train_loader:
        input_ids = batch["input_ids"].to(device)
        attention_mask = batch["attention_mask"].to(device)

        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)
        loss = outputs.loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    print(f"Epoch {epoch + 1}, Loss: {total_loss / len(train_loader)}")

# Step 7: Save the fine-tuned model
model.save_pretrained("fine_tuned_chatbot")
tokenizer.save_pretrained("fine_tuned_chatbot")

# Step 8: Test the chatbot
chatbot = pipeline("text-generation", model="fine_tuned_chatbot", tokenizer=tokenizer)
prompt = "What is the main topic of your notes?"
response = chatbot(prompt, max_length=100, num_return_sequences=1)
print(response[0]["generated_text"])
```

---

This workflow will allow you to train a chatbot on your Markdown notes and generate responses based on the fine-tuned model. Adjust the parameters (e.g., `max_length`, `batch_size`, `epochs`) as needed for your specific use case.
