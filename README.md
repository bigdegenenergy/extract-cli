
# extract-cli: A Meta-Framework for Operationalizing Knowledge

This repository provides a meta-framework for turning any source of knowledge (research papers, articles, documentation, etc.) into a user-friendly, production-ready command-line interface (CLI) tool. The goal is to bridge the gap between theoretical research and practical application by providing a structured, repeatable process for operationalizing academic work.

## 🚀 The Core Idea

Sources of knowledge like research papers, articles, and documentation contain powerful ideas, algorithms, and frameworks that have the potential for significant real-world impact. However, these ideas are typically presented in a format that is not easily accessible to a broader audience. This meta-framework provides a systematic approach to:

1.  **Extracting** the core concepts from any source.
2.  **Analyzing** the methodology and algorithms.
3.  **Implementing** the concepts in a reusable software library.
4.  **Wrapping** the implementation in a user-friendly CLI.
5.  **Integrating** with cost-effective APIs (like OpenRouter) and providing cost estimation.

## The Meta-Prompt

The entire process is guided by a "meta-prompt," which is a series of steps that can be followed to replicate the process of turning a knowledge source into a CLI tool. The meta-prompt is detailed in `prompts/meta_prompt.md`.

## Repository Structure

```
extract-cli/
├── docs/                     # Detailed documentation
│   └── USAGE.md
├── examples/                 # Example implementations
│   └── maker_framework/      # The MAKER framework as a reference
├── prompts/                  # Meta-prompts and templates
│   └── meta_prompt.md        # The core meta-prompt for this process
├── templates/                # Reusable code templates
│   ├── cli_template.py
│   └── cost_estimator_template.py
├── workflow/                 # Scripts to automate the process
│   ├── 1_extract_source.py
│   ├── 2_analyze_source.py
│   └── 3_generate_cli.py
└── README.md
```

## How to Use This Meta-Framework

To use this framework to turn a new knowledge source into a CLI tool, follow these steps:

1.  **Start with the Meta-Prompt:** Open `prompts/meta_prompt.md` and use it as your guide.

2.  **Run the Workflow Scripts:** The scripts in the `workflow/` directory are designed to automate the process:
    *   `1_extract_source.py`: Takes a URL or file path to a knowledge source and extracts the full text.
    *   `2_analyze_source.py`: Uses an LLM to analyze the extracted text and identify the core concepts, algorithms, and methodology.
    *   `3_generate_cli.py`: Uses the analysis to automatically generate a user-friendly CLI, complete with cost estimation and API integration.

3.  **Use the Templates:** The `templates/` directory provides reusable code templates for common components like:
    *   An interactive CLI (`cli_template.py`)
    *   A cost estimator (`cost_estimator_template.py`)

4.  **Review the Example:** The `examples/maker_framework/` directory contains the complete implementation of the MAKER framework as a reference. Use it to see what a finished product looks like.

## Example: The MAKER Framework

This meta-framework was born out of the process of creating the MAKER framework CLI. The `examples/maker_framework/` directory shows how the principles of this meta-framework were applied to the source paper "Solving a Million-Step LLM Task with Zero Errors."

## Contributing

This is a living project, and contributions are welcome! If you use this framework to operationalize a new knowledge source, consider adding it as an example.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
