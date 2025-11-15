#!/usr/bin/env python3
"""
Step 2: Analyze Source Content

This script uses an LLM to analyze the extracted content and identify:
- Core concepts and algorithms
- Methodology and implementation details
- User-facing functionality
- Cost estimation parameters
"""

import argparse
import json
import os
import sys


ANALYSIS_PROMPT = """Analyze the following source content and extract information needed to build a user-friendly CLI tool.

Source Content:
{content}

Please provide a JSON response with the following structure:
{{
  "title": "Short title of the concept/framework",
  "core_concept": "One-paragraph explanation of the main idea",
  "key_algorithms": [
    {{
      "name": "Algorithm name",
      "description": "What it does",
      "inputs": ["input1", "input2"],
      "outputs": ["output1"],
      "complexity": "Time/space complexity if applicable"
    }}
  ],
  "user_workflow": {{
    "input_required": "What the user needs to provide",
    "steps": ["Step 1", "Step 2", ...],
    "output_generated": "What the user receives"
  }},
  "cost_parameters": {{
    "typical_steps": "Estimated number of steps for typical use case",
    "llm_calls_per_step": "Number of LLM calls per step (if applicable)",
    "avg_tokens_per_call": "Average tokens per LLM call (if applicable)"
  }},
  "implementation_notes": [
    "Key implementation detail 1",
    "Key implementation detail 2"
  ]
}}

Focus on information that would be useful for building a practical CLI tool."""


def analyze_content(content: str, api_key: str, model: str = "google/gemini-2.0-flash-001") -> dict:
    """
    Analyze source content using an LLM.
    
    Args:
        content: Extracted text content
        api_key: OpenRouter API key
        model: Model to use for analysis
        
    Returns:
        Analysis dictionary
    """
    import requests
    
    prompt = ANALYSIS_PROMPT.format(content=content[:10000])  # Limit content length
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are an expert at analyzing technical content and extracting implementation details."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    response.raise_for_status()
    result = response.json()
    
    response_text = result['choices'][0]['message']['content']
    
    # Extract JSON from response
    response_clean = response_text.strip()
    if response_clean.startswith("```json"):
        response_clean = response_clean[7:]
    if response_clean.startswith("```"):
        response_clean = response_clean[3:]
    if response_clean.endswith("```"):
        response_clean = response_clean[:-3]
    
    return json.loads(response_clean.strip())


def main():
    parser = argparse.ArgumentParser(
        description='Analyze source content using LLM'
    )
    parser.add_argument(
        'input_file',
        help='Path to extracted text file'
    )
    parser.add_argument(
        '--output',
        default='./analysis.json',
        help='Path to save analysis JSON'
    )
    parser.add_argument(
        '--api-key',
        help='OpenRouter API key (or set OPENROUTER_API_KEY env var)'
    )
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('OPENROUTER_API_KEY')
    if not api_key:
        print("❌ Error: OpenRouter API key required")
        print("Set OPENROUTER_API_KEY environment variable or use --api-key")
        return 1
    
    # Read content
    print(f"Reading content from {args.input_file}...")
    with open(args.input_file, 'r') as f:
        content = f.read()
    
    # Analyze
    print("Analyzing content with LLM...")
    analysis = analyze_content(content, api_key)
    
    # Save analysis
    with open(args.output, 'w') as f:
        json.dump(analysis, f, indent=2)
    
    print(f"✅ Analysis saved to: {args.output}")
    print(f"\nTitle: {analysis.get('title', 'Unknown')}")
    print(f"Core Concept: {analysis.get('core_concept', 'Unknown')[:100]}...")
    
    return 0


if __name__ == '__main__':
    sys.exit(main())
