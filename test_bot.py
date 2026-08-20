import os
import json
import time
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()
client = genai.Client()

def summarize_text(text_to_analyze):
    prompt = f"Analyze the following text and return a short summary with the top 3 key points in English:\n\n{text_to_analyze}"
    

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.6-flash",
                contents=prompt,
            )
            return response.text
        except Exception as e:
            if attempt < 2:
                console.print("[dim yellow]API busy (503). Retrying in 3 seconds...[/dim yellow]")
                time.sleep(3)
            else:
                return f"Error: Gemini API is currently unavailable. Please try again later. ({e})"

def load_history(filename="ai_summary.json"):
    """Loads existing history or returns an empty list if file doesn't exist."""
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return data
        except json.JSONDecodeError:
            return []
    return []

def save_history(history, filename="ai_summary.json"):
    """Saves the cumulative list of queries to the JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    console.print(Panel.fit("[bold cyan]=== AI TEXT SUMMARIZER BOT ===[/bold cyan]\n[dim]Type 'exit' or 'quit' to close the program.[/dim]"))
    
    history = load_history()

    while True:
        user_input = console.input("\n[bold yellow]Paste or type the text you want to summarize:[/bold yellow]\n> ")
        
        if user_input.strip().lower() in ["exit", "quit"]:
            console.print("\n[bold red]Exiting... See you next time![/bold red]")
            break
            
        if not user_input.strip():
            console.print("[bold italic red]You did not enter any text. Try again.[/bold italic red]")
            continue

        with console.status("[bold green]Processing with Gemini...[/bold green]", spinner="dots"):
            summary = summarize_text(user_input)

        md_summary = Markdown(summary)
        console.print(Panel(md_summary, title="[bold green]GENERATED SUMMARY[/bold green]", border_style="green"))

        entry = {
            "input": user_input,
            "summary": summary
        }
        history.append(entry)
        save_history(history)
        
        console.print("[dim green]✔ History updated in ai_summary.json[/dim green]")