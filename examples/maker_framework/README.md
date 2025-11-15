# Example: MAKER Framework

This directory contains a reference to the MAKER framework implementation, which was created using the extract-cli meta-framework.

## Source

**Paper:** "Solving a Million-Step LLM Task with Zero Errors"  
**arXiv:** https://arxiv.org/abs/2511.09030  
**Implementation:** https://github.com/bigdegenenergy/maker-framework

## Process Overview

The MAKER framework CLI was created by following the extract-cli process:

### Step 1: Extraction

The paper was retrieved from arXiv and the full text was extracted using `pdftotext`.

### Step 2: Analysis

An LLM analyzed the paper and identified:

- **Core Concept:** Maximal Agentic decomposition, first-to-ahead-by-K Error correction, and Red-flagging (MAKER)
- **Key Algorithms:**
  - Maximal Agentic Decomposition (MAD)
  - First-to-ahead-by-k Voting
  - Red-flagging
- **User Workflow:**
  - User describes their task
  - System decomposes task automatically
  - Cost is estimated before execution
  - User confirms and receives configuration

### Step 3: Implementation

The analysis was used to create:

1. **Interactive CLI** (`maker_cli.py`)
   - Guides users through task description
   - Shows automatic decomposition
   - Displays cost estimate
   - Generates ready-to-use configuration

2. **Core Algorithms** (`maker/algorithms.py`)
   - `generate_solution()`: Orchestrates the overall task
   - `do_voting()`: Implements first-to-ahead-by-k voting
   - `get_vote()`: Samples from LLM with red-flagging
   - `create_red_flag_checker()`: Factory for red-flag checking
   - `estimate_kmin()`: Calculates minimum k for target success rate

3. **OpenRouter Integration** (`maker/openrouter.py`)
   - Cost-effective LLM access
   - Automatic model selection
   - Cost estimation before execution

4. **Task Decomposer** (`maker/decomposer.py`)
   - Automatic task decomposition using LLM
   - Generates micro-agent prompts
   - Recommends optimal parameters

## Key Features

The MAKER framework implementation demonstrates all the principles of the extract-cli meta-framework:

✅ **Single Input Interface** - User just describes their task  
✅ **Automatic Decomposition** - LLM breaks down the task  
✅ **Cost Transparency** - Exact costs shown before execution  
✅ **API Integration** - OpenRouter for cost-effective LLM access  
✅ **Production-Ready** - Clean, documented, tested code  

## Lessons Learned

### What Worked Well

1. **Automatic decomposition** significantly improved user experience
2. **Cost estimation** gave users confidence before running expensive tasks
3. **OpenRouter integration** made the tool accessible and affordable
4. **Clear documentation** helped users understand and adapt the framework

### Challenges

1. **Prompt engineering** for automatic decomposition required iteration
2. **Cost estimation accuracy** depends on good parameter estimates
3. **Error handling** for various edge cases needed careful consideration

## Using This as a Template

If you're using extract-cli to operationalize a new knowledge source, the MAKER framework serves as an excellent reference:

- Review the repository structure
- Study the CLI implementation
- Examine how cost estimation is integrated
- Look at the documentation approach

## Repository

For the complete implementation, see:  
https://github.com/bigdegenenergy/maker-framework
