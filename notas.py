from datetime import datetime
import json
import os
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class Notas:
    def __init__(self, titulo, contenido, fecha=None):
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.titulo = titulo
        self.contenido = contenido

    def to_dict(self):
        return {
            "fecha": self.fecha,
            "titulo": self.titulo,
            "contenido": self.contenido
        }

class NotasBook:
    def __init__(self, filename="mis_notas.json"):
        self.filename = filename
        self.notas = self.load_notas()

    def load_notas(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    return data if isinstance(data, list) else []
            except json.JSONDecodeError:
                return []
        return []

    def save_notas(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.notas, f, indent=4, ensure_ascii=False)

    def add_notas(self, nueva_nota):
        self.notas.append(nueva_nota.to_dict())
        self.save_notas()
        console.print("[bold green]✔ Nota agregada con éxito.[/bold green]")

    def list_notas(self):
        if not self.notas:
            console.print("[bold yellow]No hay notas guardadas.[/bold yellow]")
            return

        table = Table(title=" TUS NOTAS", style="cyan")
        table.add_column("#", style="dim", width=4)
        table.add_column("Fecha", style="magenta", width=20)
        table.add_column("Título", style="bold white", width=20)
        table.add_column("Contenido", style="green")

        for i, nota in enumerate(self.notas, 1):
            table.add_row(str(i), nota['fecha'], nota['titulo'], nota['contenido'])

        console.print(table)

    def search_book(self, query):
        resultados = [
            n for n in self.notas 
            if query.lower() in n['titulo'].lower() or query.lower() in n['contenido'].lower()
        ]
        
        if not resultados:
            console.print(f"[bold red]No se encontraron notas con: '{query}'[/bold red]")
            return

        table = Table(title=f" RESULTADOS PARA '{query}'", style="yellow")
        table.add_column("Fecha", style="magenta", width=20)
        table.add_column("Título", style="bold white", width=20)
        table.add_column("Contenido", style="green")

        for nota in resultados:
            table.add_row(nota['fecha'], nota['titulo'], nota['contenido'])

        console.print(table)

def main():
    libro = NotasBook()

    while True:
        menu_text = (
            "[bold cyan]1.[/bold cyan] Agregar nota\n"
            "[bold cyan]2.[/bold cyan] Mirar notas\n"
            "[bold cyan]3.[/bold cyan] Buscar nota\n"
            "[bold cyan]4.[/bold cyan] Salir"
        )
        console.print(Panel(menu_text, title=" GESTOR DE NOTAS", border_style="bold blue"))
        
        option = input("Selecciona una opción: ").strip()

        if option == "1":
            titulo = input("Título: ").strip()
            contenido = input("Contenido: ").strip()

            if titulo:
                new_nota = Notas(titulo, contenido)
                libro.add_notas(new_nota)
            else:
                console.print("[bold red]Error: El título es requerido[/bold red]")

        elif option == "2":
            libro.list_notas()

        elif option == "3":
            query = input("Ingresa el término a buscar: ").strip()
            libro.search_book(query)

        elif option == "4":
            console.print("[bold green]¡Hasta luego![/bold green]")
            break

        else:
            console.print("[bold red]Realice una opción válida.[/bold red]")

if __name__ == "__main__":
    main()