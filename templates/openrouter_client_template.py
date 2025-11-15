"""
OpenRouter Client Template for extract-cli Framework

This template provides a starting point for integrating with OpenRouter API.
"""

import os
from typing import Dict, List, Optional
import requests


class OpenRouterClient:
    """Client for interacting with OpenRouter API."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize OpenRouter client.
        
        Args:
            api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY env var)
        """
        self.api_key = api_key or os.getenv('OPENROUTER_API_KEY')
        if not self.api_key:
            raise ValueError(
                "OpenRouter API key not provided. "
                "Set OPENROUTER_API_KEY environment variable."
            )
        
        self.base_url = "https://openrouter.ai/api/v1"
    
    def chat_completion(
        self,
        model: str,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 1000
    ) -> str:
        """
        Call OpenRouter chat completion API.
        
        Args:
            model: Model identifier (e.g., "google/gemini-2.0-flash-001")
            messages: List of message dicts with 'role' and 'content'
            temperature: Sampling temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Generated text response
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens
        }
        
        response = requests.post(
            f"{self.base_url}/chat/completions",
            headers=headers,
            json=data
        )
        
        response.raise_for_status()
        result = response.json()
        
        return result['choices'][0]['message']['content']


# Example usage
if __name__ == '__main__':
    client = OpenRouterClient()
    
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 2+2?"}
    ]
    
    response = client.chat_completion(
        model="google/gemini-2.0-flash-001",
        messages=messages
    )
    
    print(response)
