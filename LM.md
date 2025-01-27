## 1. VSCode and GitHub Codespaces Setup

**Working in GitHub Codespaces:**

- Use GitHub Codespaces for development, training, and fine-tuning models.
- No local saves—models are uploaded directly to GitHub Releases.

**VSCode Setup:**

- **Install Extensions to VSCode:**
  - Install the Jupyter extension for interactive notebooks
  - Ensure Python is installed locally.
  - Connect to a configured GitHub Codespace 

- **Install Libraries:**
  - Run the following command to install required libraries:
    ```bash
    pip install jupyter transformers datasets torch markdown
    ```
  - Run the following to check libraries and save dependencies 
    ```bash
    python -c "import notebook; import transformers; import datasets; import torch; import markdown; output = f'Jupyter notebook version: {notebook.__version__}\nTransformers version: {transformers.__version__}\nDatasets version: {datasets.__version__}\nTorch version: {torch.__version__}\nMarkdown version: {markdown.__version__}'; open('dependency_versions.txt', 'w').write(output)"
    ```


## 2. Markdown Training Data

**Processing Markdown:**

- Use the markdown library to convert Markdown files into plain text for training data.
- You can directly copy paste the file path from the explorer
- Create a python script

**Example to convert Markdown:**

- How to read in a markdown file as text
```python
import markdown
with open("Datasets/Risk_Management/Operational Risk.md", "r") as f:
    html = markdown.markdown(f.read())
```
- How to sample line of text from file
```python
#Open a Markdown and and read its content
with open("Datasets/Risk_Management/Operational Risk.md", "r") as f:
    lines = f.readlines()

#Print the first 5 lines
for line in lines [:5]:
  print(line.strip()) # .strip() to remove leading/trailing whitespace or new line
```


## 3. Jupyter Notebooks Setup

**VSCode Jupyter Notebooks:**

- Open `.ipynb` files directly in VSCode to run cells interactively.
- Run the notebook to fine-tune models in real-time, track progress, and view results.

## 4. Key Libraries for Language Model Training in Python

**Libraries:**

- `transformers`: For loading and fine-tuning pre-trained models (e.g., GPT-2).
- `datasets`: For loading and processing datasets in a format suitable for model training.
- `torch`: For model training using deep learning frameworks (PyTorch).
- `jupyter`: To run code in interactive Jupyter Notebooks.
- `markdown`: To parse markdown files to plain text.

**Optional Libraries:**

- `gitpython`: For automating tasks like pushing model changes to GitHub repositories (if needed).

## 5. Saving Model to GitHub Releases (No Local Save)

**GitHub Releases Overview:**

- Use GitHub Releases to save large files (e.g., your trained model) directly to your repository as artifacts.

**Steps to Save Model to GitHub Releases:**

1. **Create a Release:**
   - In your GitHub repository, navigate to the Releases tab.
   - Click "Draft a new release"
    -Tag version, add description, attach files etc.
   - Install GitHub CLI in Codespace
   ```bash
   sudo apt update && sudo apt install gh
   ```

2. **Authenticate GitHub CLI: (optional)**
    - If the COdespace is not using an enviroment vairable for authentication
    - Create peronal access token
      - Github.com -> Settings -> Developer Settings -> Personal Access Tokens -> Tokens (classic) -> Generate new token -> Generate new token (classic) 
      - Add a note
      - Set expiration to 30 days
      - Select scopes repo, workflow, write:packages
      ```bash
      gh auth login --with--token < $GITHUB_TOKEN
      ```

3. **Upload Model to Release:**
   - Save to files in repository
   - Upload model files (e.g., `.bin`, `.json`) using GitHub UI or GitHub CLI.
   - Example with GitHub CLI:
     ```bash
     cd jupyter_notebook_models
     ```
     ```bash
     gh release create mkv1 ./jupyter_notebook_models/* --repo DarkFader13/The_Git_Good_Repo
     ```

4. **Access Model Later:**
   - The model is available for download from the release page. You can either manually download the model or use it in future projects by referencing the release URL.

## 6. Conclusion

- VSCode and GitHub Codespaces are your primary tools for development, training, and interacting with models using Jupyter Notebooks.
- Use the `transformers`, `datasets`, `torch`, and `jupyter` libraries for efficient model training.
- Markdown data can be converted and processed for use as training data.
- No local saves are needed—save the trained model directly to GitHub Releases for easy access and sharing.
