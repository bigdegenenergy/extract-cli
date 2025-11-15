# extract-cli Usage Guide

This guide provides detailed instructions for using the extract-cli meta-framework to turn knowledge sources into user-friendly CLI tools.

## Overview

The extract-cli framework provides a systematic, repeatable process for operationalizing knowledge from research papers, articles, and documentation. The process consists of three main steps, each automated by a workflow script.

## Prerequisites

Before you begin, ensure you have the following installed and configured.

### System Requirements

The framework requires a Unix-like environment (Linux, macOS, or WSL on Windows) with the following tools installed:

- **Python 3.8+** with pip
- **pdftotext** (part of poppler-utils)
- **requests** library for Python

### API Access

For the analysis step, you will need an OpenRouter API key. OpenRouter provides access to multiple LLM providers through a single API, making it cost-effective and flexible.

1. Visit [OpenRouter](https://openrouter.ai/)
2. Sign up for a free account
3. Generate an API key
4. Set the environment variable:
   ```bash
   export OPENROUTER_API_KEY='your-key-here'
   ```

## Step-by-Step Process

### Step 1: Extract Source Content

The first step is to extract the text content from your knowledge source. The framework supports multiple source types including arXiv papers, web pages, and local files.

**Command:**
```bash
python workflow/1_extract_source.py <source> [--output-dir <dir>]
```

**Examples:**

Extract from an arXiv paper:
```bash
python workflow/1_extract_source.py https://arxiv.org/abs/2511.09030
```

Extract from a web page:
```bash
python workflow/1_extract_source.py https://example.com/article
```

Extract from a local PDF:
```bash
python workflow/1_extract_source.py /path/to/paper.pdf
```

**Output:**
- Creates an `extracted/` directory (or your specified output directory)
- Saves the extracted text to `extracted/source.txt`

### Step 2: Analyze Source Content

The second step uses an LLM to analyze the extracted content and identify the core concepts, algorithms, and implementation details needed to build a CLI tool.

**Command:**
```bash
python workflow/2_analyze_source.py <input_file> [--output <file>] [--api-key <key>]
```

**Example:**
```bash
python workflow/2_analyze_source.py extracted/source.txt --output analysis.json
```

**Output:**
- Creates `analysis.json` with structured information about:
  - Title and core concept
  - Key algorithms
  - User workflow
  - Cost parameters
  - Implementation notes

### Step 3: Generate CLI Tool

The final step generates a complete CLI tool from the analysis, including the interactive CLI script, documentation, and supporting files.

**Command:**
```bash
python workflow/3_generate_cli.py <analysis_file> [--output-dir <dir>]
```

**Example:**
```bash
python workflow/3_generate_cli.py analysis.json --output-dir my_cli_tool
```

**Output:**
- Creates a new directory with:
  - `cli.py`: Interactive CLI script
  - `README.md`: Documentation
  - `requirements.txt`: Python dependencies

## Complete Example

Here is a complete example of turning an arXiv paper into a CLI tool.

```bash
# Step 1: Extract the paper
python workflow/1_extract_source.py https://arxiv.org/abs/2511.09030

# Step 2: Analyze the content
python workflow/2_analyze_source.py extracted/source.txt --output maker_analysis.json

# Step 3: Generate the CLI
python workflow/3_generate_cli.py maker_analysis.json --output-dir maker_cli

# Step 4: Review and customize
cd maker_cli
cat README.md
python cli.py
```

## Customization

The generated CLI is a starting point. You will typically need to customize it to fully implement the functionality described in the source.

### Customizing the CLI

The generated `cli.py` file contains TODO comments indicating where you need to add implementation logic. Common customizations include:

1. **Implementing core algorithms**: Add the actual implementation of algorithms identified in the analysis.
2. **Adding cost estimation**: Integrate the cost estimation templates from `templates/cost_estimator_template.py`.
3. **Connecting to APIs**: Use the OpenRouter client template from `templates/openrouter_client_template.py`.
4. **Enhancing user experience**: Add progress indicators, error handling, and validation.

### Using the Templates

The `templates/` directory provides reusable components that you can copy and adapt:

- **cli_template.py**: Interactive CLI structure
- **cost_estimator_template.py**: Cost estimation logic
- **openrouter_client_template.py**: API client for OpenRouter

## Best Practices

When using the extract-cli framework, keep these best practices in mind.

### Source Selection

Choose sources that have clear, well-defined concepts and methodologies. Research papers with detailed algorithm descriptions work particularly well. Articles that are too high-level or vague may require more manual intervention.

### Analysis Review

Always review the `analysis.json` file before generating the CLI. The LLM analysis is a starting point, and you may need to refine or correct the extracted information.

### Iterative Development

The generated CLI is a scaffold. Plan to iterate on the implementation, adding functionality incrementally and testing as you go.

### Documentation

As you customize the generated CLI, update the README.md and add inline comments to explain your implementation choices.

## Troubleshooting

### "pdftotext: command not found"

Install poppler-utils:
```bash
# Ubuntu/Debian
sudo apt-get install poppler-utils

# macOS
brew install poppler
```

### "OpenRouter API key not found"

Set the environment variable:
```bash
export OPENROUTER_API_KEY='your-key-here'
```

### Analysis JSON is incomplete

The LLM may not extract all necessary information on the first try. You can:
1. Manually edit the `analysis.json` file
2. Re-run the analysis with a different model
3. Provide additional context in the source text

### Generated CLI doesn't work

The generated CLI is a template. You need to implement the core logic based on the analysis. Review the TODO comments in the generated code.

## Advanced Usage

### Custom Analysis Prompts

You can modify the analysis prompt in `workflow/2_analyze_source.py` to extract different or additional information based on your needs.

### Using Different Models

The analysis step defaults to Google Gemini 2.0 Flash, but you can specify a different model by modifying the `model` parameter in the script.

### Batch Processing

You can process multiple sources by creating a shell script that loops through a list of URLs or files:

```bash
#!/bin/bash
for url in $(cat paper_urls.txt); do
  python workflow/1_extract_source.py "$url" --output-dir "extracted_$(basename $url)"
done
```

## Contributing

If you use this framework to operationalize a new knowledge source, consider contributing your example to the repository. This helps others learn from your experience and expands the collection of reference implementations.

## Support

For questions, issues, or suggestions:
- Open an issue on GitHub
- Review the example implementations in `examples/`
- Check the meta-prompt in `prompts/meta_prompt.md`
