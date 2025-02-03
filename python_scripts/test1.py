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
markdown_directory = "Datasets/Risk_Management/"
training_texts = load_markdown_files(markdown_directory)



# Print the first 5 lines of each markdown text
for text in training_texts:
    lines = text.splitlines()  # Splits the text into lines
    for line in lines[:5]:  # Adjust the number here to get more or fewer lines
        print(line.strip())  # .strip() to remove leading/trailing whitespace or new line
    print("-" * 40)  # Just a separator for clarity between texts