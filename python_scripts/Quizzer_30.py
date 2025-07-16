# generate_qa.py
import subprocess
import csv
import os
import re
import time
import signal

def start_ollama():
    """Start the Ollama server."""
    print("Starting Ollama server...")
    ollama_process = subprocess.Popen(
        ["ollama", "serve"],
        stdout=subprocess.DEVNULL, #suppress standard output
        stderr=subprocess.DEVNULL #supress standard error
        )
    time.sleep(5)  # Wait for the server to start
    print("THE LLAMA IS RUNNING")
    return ollama_process

def kill_ollama(ollama_process):
    """Kill the Ollama server."""
    print("Ollama-san is taking a break")
    ollama_process.terminate()
    ollama_process.wait()

def generate_qa(markdown_file, num_questions, focus_topic, output_folder):
    # Read the Markdown file
    with open(markdown_file, "r") as file:
        notes = file.read()

    # Prepare the prompt for Mistral 7B
    prompt = (
        f"Generate {num_questions} questions and answers based on the following notes. "
        f"Focus the questions on the topic of '{focus_topic}'. "
        "Each question should be a maximum of 2 sentences, and each answer should be less than 50 words. "
        "Do NOT return JSON or structured formats. Just list the Q&A like:\n"
        "FORMAT STRICTLY like this (no intro, no numbering):\n"
        "Question: ...\nAnswer: ...\nQuestion: ...\nAnswer: ...\n\n"
        f"Format the output as a list of questions and answers pairs, with {num_questions} pairs"
        "Here are the notes:\n\n{notes}"
    )
    #Might need to update prompt with future updates

    # Run Ollama with Mistral 7B to generate Q&A
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )

    #Parse Q/A prefix
    result.stdout = result.stdout.replace("\n\n", "\n")
    result.stdout = result.stdout.replace("Question: ", "")
    result.stdout = result.stdout.replace("Answer: ", "")
    result.stdout = result.stdout.replace("Q: ", "")
    result.stdout = result.stdout.replace("A: ", "")

    # Parse the output into questions and answers
    qa_pairs = []
    output_lines = result.stdout.split("\n")
    for i in range(0, len(output_lines) - 1, 2):
        question = output_lines[i].strip()
        answer = output_lines[i + 1].strip() if i + 1 < len(output_lines) else ""
        qa_pairs.append((question, answer))

    #Remove numbering
    qa_pairs = [(re.sub(r'^\d+\.\s*', '', q), a) for q, a in qa_pairs]

    # Save the Q&A pairs to a CSV file
    os.makedirs(output_folder, exist_ok=True)  # Create the output folder if it doesn't exist
    output_file = os.path.join(output_folder, f"qa_output_{focus_topic.replace(' ', '_')}.csv")
    
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Question", "Answer"])  # Write header
        writer.writerows(qa_pairs)  # Write Q&A pairs

    print(f"Q&A generated and saved to {output_file}")
    ##print(qa_pairs)

if __name__ == "__main__":

    ollama_process = start_ollama()
    try:
        # Inputs
        markdown_file = input("Enter the path to your Markdown file (e.g., notes.md): ")
        num_questions = input("Enter the number of questions to generate: ")
        focus_topic = input("Enter the topic to focus on for the questions: ")
        output_folder = input("Enter the folder to save the output CSV file (e.g., output): ")

        # Generate Q&A
        generate_qa(markdown_file, int(num_questions), focus_topic, output_folder)
    finally:
        kill_ollama(ollama_process)

