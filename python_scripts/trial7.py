# generate_qa.py
import subprocess
import csv
import os
import re

def generate_qa(markdown_file, num_questions, focus_topic, output_folder):
    # Read the Markdown file
    with open(markdown_file, "r") as file:
        notes = file.read()

    # Prepare the prompt for Mistral 7B
    prompt = (
        f"Generate {num_questions} questions and answers based on the following notes. "
        f"Focus the questions on the topic of '{focus_topic}'. "
        "Each question should be a maximum of 2 sentences, and each answer should be less than 50 words. "
        f"Format the output as a list of questions and answers pairs, with {num_questions} pairs"
        "Here are the notes:\n\n{notes}"
    )

    # Run Ollama with Mistral 7B to generate Q&A
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )

    result.stdout = result.stdout.replace("\n\n", "\n")
    result.stdout = result.stdout.replace("Question: ", "")
    result.stdout = result.stdout.replace("Answer: ", "")

    # Parse the output into questions and answers
    qa_pairs = []
    output_lines = result.stdout.split("\n")
    for i in range(0, len(output_lines) - 1, 2):
        question = output_lines[i].strip()
        answer = output_lines[i + 1].strip() if i + 1 < len(output_lines) else ""
        qa_pairs.append((question, answer))


    qa_pairs = [(re.sub(r'^\d+\.\s*', '', q), a) for q, a in qa_pairs]

    # Save the Q&A pairs to a CSV file
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
    output_file = os.path.join(output_folder, f"qa_output_{focus_topic.replace(' ', '_')}.csv")
    
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Question", "Answer"])  # Write header
        writer.writerows(qa_pairs)  # Write Q&A pairs

    print(f"Q&A generated and saved to {output_file}")
    print(qa_pairs)

if __name__ == "__main__":
    # Inputs
    markdown_file = "/workspaces/personal_projects/Datasets/Risk_Management/Operational Risk.md" ##input("Enter the path to your Markdown file (e.g., notes.md): ")
    num_questions = 3 ##input("Enter the number of questions to generate: ")
    focus_topic = "Risk" ##input("Enter the topic to focus on for the questions: ")
    output_folder = "/workspaces/personal_projects/Questions_Answer_Bank" ##input("Enter the folder to save the output CSV file (e.g., output): ")

    # Generate Q&A
    generate_qa(markdown_file, int(num_questions), focus_topic, output_folder)