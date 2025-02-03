import markdown
import os
from transformers import GPT2Tokenizer

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

# Example usage
markdown_directory = "Datasets/Risk_Management/"
training_texts = load_markdown_files(markdown_directory)
tokenized_data = tokenize_texts(training_texts)


# Check tokenized texts available
if len(tokenized_data["input_ids"]) > 0:
    # Decode the first document's token IDs back to text
    decoded_text = tokenizer.decode(tokenized_data["input_ids"][0])

    # Split the decoded text into lines
    lines = decoded_text.split('\n')

    # Determine the number of lines to print (up to 20)
    num_lines_to_print = min(20, len(lines))

    # Print the specified number of lines in human-readable format
    print("First 20 lines (or fewer) of the first document:")
    for i in range(num_lines_to_print):
        print(lines[i])

    # Approximation for the token IDs and attention masks for the first 20 lines
    tokens_approx = num_lines_to_print * 10
    token_ids_for_first_lines = tokenized_data["input_ids"][0][:tokens_approx]
    attention_mask_for_first_lines = tokenized_data["attention_mask"][0][:tokens_approx]

    # Print the tokenized version (token IDs) for the first 20 lines (approximation)
    print("\nTokenized version (token IDs) for the first 20 lines (approximation):")
    print(token_ids_for_first_lines)

    # Print the attention masks for the same portion
    print("\nAttention Mask for the first 20 lines (approximation):")
    print(attention_mask_for_first_lines)
else:
    print("No documents were found or tokenized.")