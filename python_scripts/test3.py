import markdown
import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from torch.utils.data import DataLoader, Dataset
import torch

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

# Load the GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
# Set the tokenizer's pad token to the EOS token
tokenizer.pad_token = tokenizer.eos_token


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

# Load in training data (tokenise) and pre-trained model
markdown_directory = "Datasets/Risk_Management/"
training_texts = load_markdown_files(markdown_directory)
tokenized_data = tokenize_texts(training_texts)
model = GPT2LMHeadModel.from_pretrained("gpt2")

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
