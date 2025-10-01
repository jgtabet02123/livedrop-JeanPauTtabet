from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

import requests

API_URL = "http://127.0.0.1:5000/get_response"  #

import requests

PUBLIC_URL = "https://collectedly-intercuspidal-allegra.ngrok-free.dev"  # replace with printed URL
CHAT_ENDPOINT = f"{PUBLIC_URL}/chat"

def generate_response(user_input):
    payload = {
        "query": user_input,
        "prompt_key": "base_retrieval_prompt",
        "top_k": 3
    }
    try:
        r = requests.post(CHAT_ENDPOINT, json=payload)
        r.raise_for_status()
        data = r.json()
        return {
            "answer": data.get("answer", "No answer generated."),
            "sources": data.get("sources", [])
        }
    except Exception as e:
        return {"answer": f"Error contacting API: {str(e)}", "sources": []}


def chat_with_model():
    print(Panel("[bold cyan]Shoplite Assistant[/] (type 'exit' to quit)", expand=False))

    while True:
        user_input = console.input("[bold green]You:[/] ")
        if user_input.lower() in ["exit", "quit", "bye"]:
           print("[bold cyan]Assistant:[/] Goodbye!")
            break

        try:
            response = generate_response(user_input)
            answer = response.get("answer", "No answer generated.")
            sources = response.get("sources", [])

            
            print(Markdown(f"**Assistant:** {answer}"))

            if sources:
                print(Panel(f"Sources: {', '.join(sources)}", style="cyan"))
        except Exception as e:
           print(f"[red] Error:[/] {str(e)}")

chat_with_model()
