"""
Cost Estimator Template for extract-cli Framework

This template provides a starting point for creating a cost estimation module
that calculates the expected cost of running a task before execution.
"""

from typing import Dict


# Model pricing (per 1M tokens) - Update with actual pricing
MODEL_PRICING = {
    "google/gemini-2.0-flash-001": {
        "name": "Google Gemini 2.0 Flash",
        "input_price": 0.10,  # per 1M tokens
        "output_price": 0.40,  # per 1M tokens
        "context_window": 1048576,
    },
    "meta-llama/llama-3.1-8b-instruct": {
        "name": "Meta Llama 3.1 8B",
        "input_price": 0.05,
        "output_price": 0.05,
        "context_window": 131072,
    },
    # Add more models as needed
}


def estimate_cost(
    num_steps: int,
    model: str,
    avg_prompt_tokens: int = 500,
    avg_response_tokens: int = 100,
    calls_per_step: int = 1,
    overhead_factor: float = 1.1
) -> Dict[str, float]:
    """
    Estimate the cost of running a task.
    
    Args:
        num_steps: Total number of steps in the task
        model: Model identifier
        avg_prompt_tokens: Average tokens per prompt
        avg_response_tokens: Average tokens per response
        calls_per_step: Number of LLM calls per step
        overhead_factor: Multiplier to account for overhead (e.g., retries)
        
    Returns:
        Dictionary with cost breakdown
    """
    if model not in MODEL_PRICING:
        raise ValueError(f"Unknown model: {model}")
    
    model_info = MODEL_PRICING[model]
    
    # Calculate total calls
    total_calls = num_steps * calls_per_step * overhead_factor
    
    # Calculate token usage
    total_input_tokens = total_calls * avg_prompt_tokens
    total_output_tokens = total_calls * avg_response_tokens
    
    # Calculate costs (prices are per 1M tokens)
    input_cost = (total_input_tokens / 1_000_000) * model_info['input_price']
    output_cost = (total_output_tokens / 1_000_000) * model_info['output_price']
    total_cost = input_cost + output_cost
    
    return {
        'model': model_info['name'],
        'num_steps': num_steps,
        'estimated_calls': int(total_calls),
        'input_tokens': int(total_input_tokens),
        'output_tokens': int(total_output_tokens),
        'input_cost': input_cost,
        'output_cost': output_cost,
        'total_cost': total_cost
    }


def format_cost_estimate(estimate: Dict) -> str:
    """
    Format cost estimate for display.
    
    Args:
        estimate: Cost estimate dictionary from estimate_cost()
        
    Returns:
        Formatted string
    """
    return f"""
Cost Estimate
{'='*50}
Model: {estimate['model']}
Steps: {estimate['num_steps']:,}

Estimated LLM Calls: {estimate['estimated_calls']:,}
Input Tokens: {estimate['input_tokens']:,}
Output Tokens: {estimate['output_tokens']:,}

Cost Breakdown:
  Input:  ${estimate['input_cost']:.4f}
  Output: ${estimate['output_cost']:.4f}
  ----------------------------------------
  TOTAL:  ${estimate['total_cost']:.4f}
"""


def get_recommended_model() -> str:
    """
    Get the recommended (cheapest capable) model.
    
    Returns:
        Model identifier
    """
    # Sort by total cost (input + output)
    models = sorted(
        MODEL_PRICING.items(),
        key=lambda x: x[1]['input_price'] + x[1]['output_price']
    )
    
    return models[0][0] if models else list(MODEL_PRICING.keys())[0]


# Example usage
if __name__ == '__main__':
    # Estimate cost for a 1000-step task
    estimate = estimate_cost(
        num_steps=1000,
        model="google/gemini-2.0-flash-001",
        avg_prompt_tokens=500,
        avg_response_tokens=100,
        calls_per_step=1
    )
    
    print(format_cost_estimate(estimate))
