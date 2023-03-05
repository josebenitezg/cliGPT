from rich import print
from rich.console import Console
from rich.markdown import Markdown
from rich.live import Live
from utils import get_response

c = Console()
sep = Markdown("---")

while True:
    c.print("\n[bold red]User input 👤:[/] ", end="")
    
    content = input()
    response = get_response(content)
    c.print(sep)
    
    c.print(f"\n[bold yellow]GPT3.5-turbo 🤖:[/]")
    c.print(Markdown(response), sep)
    
    if content == "clear":
        c.print("Cleared the chat history")