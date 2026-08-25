import os
import json
import time
from google import genai
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.table import Table

console = Console()
client = genai.Client()

def call_gemini(prompt):

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
                return f"Error: Gemini API currently unavailable. ({e})"

def load_history(filename="ai_summary.json"):
    if os.path.exists(filename):
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            return []
    return []

def save_history(history, action_type, user_input, result, filename="ai_summary.json"):
    entry = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "action": action_type,
        "input": user_input[:50] + "..." if len(user_input) > 50 else user_input,
        "result": result
    }
    history.append(entry)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
    console.print("[dim green]✔ History updated in ai_summary.json[/dim green]")

def show_history_table(history):
    if not history:
        console.print("[bold yellow]History is empty.[/bold yellow]")
        return
    
    table = Table(title="Query History", border_style="cyan")
    table.add_column("Timestamp", style="dim", width=19)
    table.add_column("Action", style="bold cyan", width=18)
    table.add_column("Input (Snippet)", style="white")

    for item in history:
        table.add_row(
            item.get("timestamp", "N/A"),
            item.get("action", "Summary"),
            item.get("input", "")
        )
    console.print(table)

if __name__ == "__main__":
    history = load_history()

    while True:
        console.print("\n" + "="*50)
        console.print(Panel.fit("[bold cyan]=== AI MULTI-TOOL BOT ===[/bold cyan]\n[dim]1. Summarize text\n2. Summarize .txt file\n3. Explain code\n4. View history\n5. Exit[/dim]"))
        
        option = console.input("\n[bold yellow]Select an option (1-5):[/bold yellow] ").strip()

        if option == "5" or option.lower() in ["exit", "quit"]:
            console.print("\n[bold red]Exiting program![/bold red]")
            break

        elif option == "1":
            text = console.input("\n[bold yellow]Enter the text to summarize:[/bold yellow]\n> ").strip()
            if not text:
                console.print("[bold red]Input cannot be empty.[/bold red]")
                continue
            
            prompt = f"Analyze the following text and return a short summary with the top 3 key points in English:\n\n{text}"
            with console.status("[bold green]Processing summary...[/bold green]", spinner="dots"):
                res = call_gemini(prompt)
            
            console.print(Panel(Markdown(res), title="[bold green]GENERATED SUMMARY[/bold green]", border_style="green"))
            save_history(history, "Text Summary", text, res)

        elif option == "2":
            file_path = console.input("\n[bold yellow]Enter .txt file path (e.g., errors.txt):[/bold yellow]\n> ").strip()
            if not os.path.exists(file_path):
                console.print("[bold red]File does not exist.[/bold red]")
                continue
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            prompt = f"Summarize the main content of this file in English:\n\n{content}"
            with console.status("[bold green]Reading and analyzing file...[/bold green]", spinner="dots"):
                res = call_gemini(prompt)

            console.print(Panel(Markdown(res), title=f"[bold green]SUMMARY OF: {file_path}[/bold green]", border_style="green"))
            save_history(history, "File Summary", file_path, res)

        elif option == "3":
            code = console.input("\n[bold yellow]Paste the code to explain:[/bold yellow]\n> ").strip()
            if not code:
                console.print("[bold red]Input cannot be empty.[/bold red]")
                continue

            prompt = f"Explain step-by-step how this code works in English:\n\n```\n{code}\n```"
            with console.status("[bold green]Analyzing code...[/bold green]", spinner="dots"):
                res = call_gemini(prompt)

            console.print(Panel(Markdown(res), title="[bold green]CODE EXPLANATION[/bold green]", border_style="green"))
            save_history(history, "Code Explanation", code, res)

        elif option == "4":
            show_history_table(history)

        else:
            console.print("[bold red]Invalid option. Please try again.[/bold red]") 