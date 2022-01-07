from rich.console import Console
from rich.theme import Theme


theme = Theme(
    {
        "parsers": "#ffdf76",
        "tools": "#4c86ea",
        "vba": "#127c44",
        "docs": "#d5282d",
        "iso": "#ab53d2",
    }
)

console = Console(theme=theme)
