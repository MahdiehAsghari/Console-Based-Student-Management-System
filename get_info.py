from rich.prompt import Prompt
from rich.console import Console

signUp_infos = {}

def GetInfo():
    Console().print("[bold blue on white]Sign Up[/bold blue on white]\n")
    signUp_infos["First Name"] = Prompt.ask("[bold red on yellow]1.Enter your firts name[/bold red on yellow]")
    signUp_infos["Last Name"] = Prompt.ask("[bold red on yellow]2.Enter your last name[/bold red on yellow]")

    g = Prompt.ask("[bold red on yellow]3.Choose your gender ~> Male(m) / Female(f)[/bold red on yellow]")
    if g == 'm':
        signUp_infos["Gender"] = "Male"
    elif g == 'f':
        signUp_infos["Gender"] = "Female"

    m = Prompt.ask("[bold red on yellow]4.Single(s) / Married(m)[/bold red on yellow]")
    if m == 's':
        signUp_infos["Marital Status"] = "Single"
    elif m == 'm':
        signUp_infos["Marital Status"] = "Married"

    signUp_infos["Phone Number"] = Prompt.ask("[bold red on yellow]5.Enter your Phone Number[/bold red on yellow]")
    signUp_infos["Father's Name"] = Prompt.ask("[bold red on yellow]6.Enter your Father's name[/bold red on yellow]")
    signUp_infos["Mother's Name"] = Prompt.ask("[bold red on yellow]7.Enter your Mother's name[/bold red on yellow]")
    signUp_infos["ID Number"] = Prompt.ask("[bold red on yellow]8.Enter your ID Number[/bold red on yellow]")
    signUp_infos["Student ID Number"] = Prompt.ask("[bold red on yellow]9.Enter your Student ID Number[/bold red on yellow]")
    signUp_infos["Home Address"] = Prompt.ask("[bold red on yellow]10.Enter your Home Address[/bold red on yellow]")

    c = Prompt.ask("[bold red on yellow]11.Daily Course(d) / Evening Course(e)[/bold red on yellow]")
    if c == 'd':
        signUp_infos["Type of Course"] = "Daily Course"
    elif c == 'e':
        signUp_infos["Type of Course"] = "Evening Course"

    signUp_infos["Faculty"] = Prompt.ask("[bold red on yellow]12.Enter your Faculty[/bold red on yellow]")
    signUp_infos["Field"] = Prompt.ask("[bold red on yellow]13.Enter your Field[/bold red on yellow]")

