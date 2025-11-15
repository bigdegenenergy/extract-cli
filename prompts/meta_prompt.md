# Meta-Prompt: Turning Knowledge into User-Friendly CLI Tools

This meta-prompt outlines the process for turning any source of knowledge (research paper, article, documentation, etc.) into a user-friendly, production-ready command-line interface (CLI) tool.

## Phase 1: Extraction and Analysis

1.  **Identify the Source:**
    *   What is the source of knowledge? (URL, file path, etc.)
    *   What is the core idea or problem being solved?

2.  **Extract the Content:**
    *   Use tools like `pdftotext`, web scraping, or simply copy-pasting to extract the full text content of the source.

3.  **Analyze the Content with an LLM:**
    *   Use a powerful LLM to analyze the extracted text.
    *   **Prompt:** "Analyze the following text and identify the core concepts, algorithms, and methodology. Break down the process into the smallest possible atomic steps. For each step, define the inputs, outputs, and any constraints."

## Phase 2: Implementation

1.  **Design the Core Logic:**
    *   Based on the LLM's analysis, design the core software components.
    *   What are the main functions or classes needed?
    *   How will data be passed between components?

2.  **Implement the Algorithms:**
    *   Write the Python code to implement the core algorithms and logic identified in the analysis phase.
    *   Use the `templates/` directory for reusable components.

3.  **Integrate with APIs:**
    *   If the tool requires external services (like LLMs), integrate with a cost-effective API provider like OpenRouter.
    *   Implement a client to handle API calls.

## Phase 3: CLI and User Experience

1.  **Create an Interactive CLI:**
    *   Use the `templates/cli_template.py` as a starting point.
    *   The CLI should guide the user through the process with clear, simple steps.
    *   **Key features:**
        *   Task input (just describe the task)
        *   Automatic decomposition and analysis
        *   Cost estimation
        *   Confirmation before execution

2.  **Implement Cost Estimation:**
    *   Use the `templates/cost_estimator_template.py` to create a cost estimation module.
    *   Estimate the number of API calls, token usage, and total cost.
    *   Display the cost estimate to the user before they commit to running the task.

3.  **Automatic Task Decomposition:**
    *   Use an LLM to automatically decompose the user's task into the steps required by the framework.
    *   **Prompt:** "Given the user's task description, decompose it into the steps required by the implemented framework. Generate the necessary configuration and prompts."

## Phase 4: Documentation and Packaging

1.  **Write Comprehensive Documentation:**
    *   **README.md:** Overview, quick start, and example usage.
    *   **USAGE.md:** Detailed usage instructions and best practices.
    *   **[FRAMEWORK_GUIDE].md:** In-depth explanation of the concepts from the source.

2.  **Create Examples:**
    *   Provide at least one complete, runnable example that demonstrates the framework in action.

3.  **Package for Distribution:**
    *   Create a `requirements.txt` file.
    *   Add a `LICENSE` file (MIT is a good default).
    *   Create a `.gitignore` file.

## Phase 5: Deployment

1.  **Initialize a Git Repository:**
    *   `git init`
    *   `git add .`
    *   `git commit -m "Initial commit"`

2.  **Push to GitHub:**
    *   Create a new repository on GitHub.
    *   `gh repo create [repo-name] --public --source=. --push`

3.  **Deliver to User:**
    *   Provide the user with the GitHub repository link.
    *   Include a quick start guide and summary of the features.

