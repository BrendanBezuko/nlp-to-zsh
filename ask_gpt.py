#!/usr/bin/env python3
from openai import OpenAI
import os
import sys

def ask_gpt_completions(prompt, max_tokens=100):
    """
    Returns code completion suggestions using OpenAI's API.

    :param prompt: The prompt to send to the API.
    :param max_tokens: The maximum number of tokens to generate.
    :return: The completion response from the API.
    """
    api_key = os.getenv('OPENAI_API_KEY')
    model = os.getenv('OPENAI_MODEL_NAME')
    
    if not api_key:
        return "API key not found. Please set the OPENAI_API_KEY environment variable."
    try:
        client = OpenAI(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are an assistant specializing in responding with Linux command-line solutions."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=max_tokens
        )
        if response.choices:
            return response.choices[0].message.content
        else:
            return "No response"
    except Exception as e:
        return str(e)

# Main program
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./openai_code_completion.py 'prompt'")
        sys.exit(1)

    prompt = sys.argv[1]
    print(ask_gpt_completions(prompt))

