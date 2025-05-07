import requests
import json

def ask_llama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

if __name__ == "__main__":
    while True:
        user_input = input("\nyou:")
        if user_input.lower() in ["exit", "quit"]:
            break
        response=ask_llama(user_input)
        print(f"\nLlama3.2:{response}")