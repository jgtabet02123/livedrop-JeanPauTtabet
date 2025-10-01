# source.py
import requests
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

console = Console()

def generate_response(api_url, user_input):
    """
    Send user input to the RAG API and get answer + sources.
    """
    payload = {
        "query": user_input,
        "prompt_key": "base_retrieval_prompt",
        "top_k": 3
    }
    try:
        r = requests.post(f"{api_url}/chat", json=payload)
        r.raise_for_status()
        data = r.json()
        return {
            "answer": data.get("answer", "No answer generated."),
            "sources": data.get("sources", [])
        }
    except Exception as e:
        return {"answer": f"Error contacting API: {str(e)}", "sources": []}

def start_chat():
    """
    Terminal chat interface. Prompts user for API URL each time.
    """
    api_url = console.input("[bold yellow]Enter your ngrok or API URL : [/]").strip()
    if not api_url:
        console.print("[red]No URL entered. Exiting.[/]")
        return

    # Test connection
    try:
        health = requests.get(f"{api_url}/health").json()
        if health.get("status") != "healthy":
            console.print(f"[red]API returned unexpected health status: {health}[/]")
            return
        console.print(f"[green]Connected to API successfully![/]")
    except Exception as e:
        console.print(f"[red]Failed to connect to API: {e}[/]")
        return

    console.print(Panel("[bold cyan]Shoplite Assistant[/] (type 'exit' to quit)", expand=False))

    while True:
        user_input = console.input("[bold green]You:[/] ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            console.print("[bold cyan]Assistant:[/] Goodbye!")
            break

        response = generate_response(api_url, user_input)
        console.print(Markdown(f"**Assistant:** {response['answer']}"))

        if response["sources"]:
            console.print(Panel(f"Sources: {', '.join(response['sources'])}", style="cyan"))

if __name__ == "__main__":
    start_chat()
