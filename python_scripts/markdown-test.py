#Open a Markdown and and read its content
with open("Datasets/Risk_Management/Operational Risk.md", "r") as f:
    lines = f.readlines()

#Print the first 5 lines
for line in lines [:10]:
  print(line.strip()) # .strip() to remove leading/trailing whitespace or new line