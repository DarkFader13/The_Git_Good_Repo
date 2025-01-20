## 1. VSCode and GitHub Codespaces Setup

**VSCode Setup:**

- **Install Extensions:**
  - Install the Jupyter extension for interactive notebooks.
  - Ensure Python is installed.

- **Install Libraries:**
  - Run the following command to install required libraries:
    ```bash
    pip install jupyter transformers datasets torch
    ```

**Working in GitHub Codespaces:**

- Use GitHub Codespaces for development, training, and fine-tuning models.
- No local saves—models are uploaded directly to GitHub Releases.

## 2. Markdown Training Data

**Processing Markdown:**

- Use the markdown library to convert Markdown files into plain text for training data.

**Example to convert Markdown:**
```python
import markdown
with open("your_file.md", "r") as f:
    html = markdown.markdown(f.read())
```

## 3. Jupyter Notebooks Setup

**VSCode Jupyter Notebooks:**

- Open `.ipynb` files directly in VSCode to run cells interactively.
- Run the notebook to fine-tune models in real-time, track progress, and view results.
