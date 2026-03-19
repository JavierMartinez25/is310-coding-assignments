from rich.console import Console
from rich.table import Table
from pathlib import Path
import json

console = Console()
console.print("Here is some initial data:", style="bold cyan")

table = Table(title="Star Wars Movies")
table.add_column("Released", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right")
table.add_row("Dec 20, 2019", "Star Wars: The Rise of Skywalker", "$952,110,690")
table.add_row("May 25, 2018", "Solo: A Star Wars Story", "$393,151,347")
table.add_row("Dec 15, 2017", "Star Wars Ep. VIII: The Last Jedi", "$1,332,539,889")
console.print(table)

movies = [
    {
        "Released": "Dec 20, 2019",
        "Title": "Star Wars: The Rise of Skywalker",
        "Box Office": "$952,110,690"
    },
    {
        "Released": "May 25, 2018",
        "Title": "Solo: A Star Wars Story",
        "Box Office": "$393,151,347"
    },
    {
        "Released": "Dec 15, 2017",
        "Title": "Star Wars Ep. VIII: The Last Jedi",
        "Box Office": "$1,332,539,889"
    }
]

while True:
    movie_title = input("Enter the title of the movie: ")
    release_date = input("Enter the release date of the movie: ")
    box_office = input("Enter the box office earnings of the movie: ")

    console.print("\nHere is your entry:", style="bold cyan")
    console.print(f"Title: {movie_title}")
    console.print(f"Release Date: {release_date}")
    console.print(f"Box Office: {box_office}")

    confirm = input("Is this correct? (yes/no): ").strip().lower()

    if confirm == "yes":
        movies.append({
            "Released": release_date,
            "Title": movie_title,
            "Box Office": box_office
        })
    else:
        console.print("Please re-enter the movie information.", style="bold red")
        continue

    another = input("Do you want to enter another movie? (yes/no): ").strip().lower()
    if another != "yes":
        break

file_path = Path("movie_data.json")
file_path.write_text(json.dumps(movies, indent=4), encoding="utf-8")

console.print("\nThe data has been saved to a file.", style="bold green")
console.print(f"Full path: {file_path.resolve()}")