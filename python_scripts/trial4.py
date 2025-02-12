# generate_qa.py
import subprocess

def generate_qa(markdown_file, num_questions, focus_topic):
    # Read the Markdown file
    with open(markdown_file, "r") as file:
        notes = file.read()

    # Prepare the prompt for Mistral 7B
    prompt = (
        f"Generate {num_questions} questions and answers based on the following notes. "
        f"Focus the questions on the topic of '{focus_topic}'. Here are the notes:\n\n{notes}"
    )

    # Run Ollama with Mistral 7B to generate Q&A
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )

    # Save the output to a file
    output_file = f"qa_output_{focus_topic.replace(' ', '_')}.md"
    with open(output_file, "w") as output_file:
        output_file.write(result.stdout)

    print(f"Q&A generated and saved to {output_file}")

if __name__ == "__main__":
    # Inputs
    markdown_file = input("Enter the path to your Markdown file (e.g., notes.md): ")
    num_questions = input("Enter the number of questions to generate: ")
    focus_topic = input("Enter the topic to focus on for the questions: ")

    # Generate Q&A
    generate_qa(markdown_file, int(num_questions), focus_topic)