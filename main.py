import os
import rich
import get_info
import main_menu
from rich.console import Console
from rich.prompt import Prompt
from first_frame import FirstFrame

money = 100
console = Console()

os.system("cls")

console.print(FirstFrame(["Welcome", "mahdieh Asghari","14016321902", "Press Enter to continue..."], c="█"))

input()

os.system("cls")

get_info.GetInfo()

C2 = Prompt.ask("\n[bold blue on white]Enter (f) for Finish / Enter (r) for restarting the sign up[/bold blue on white]")

while True:
    if C2 == 'r':
        os.system("cls")
        get_info.GetInfo()
        C2 = Prompt.ask("\n[bold blue on white]Enter (f) for Finish / Enter (r) for restarting the sign up[/bold blue on white]")
    else:
        break
    
os.system("cls")

console.print("[bold blue on white]Contents!\n[/bold blue on white]")

main_menu.Menu1()

#______________________________________________________________________

while True:
    option = Prompt.ask("[bold blue on white]Choose Number of the Option[/bold blue on white]")
    
    if option == "1":
        os.system("cls")
        main_menu.Selection()
    os.system("cls")
    main_menu.Menu1()

    if option == "2":
        os.system("cls")
        main_menu.Add_Remove()
    os.system("cls")
    main_menu.Menu1()

    if option == "3":
        os.system("cls")
        if main_menu.Confirmation() == 1:
            os.system("cls")
            main_menu.Menu2()
            main_menu.Option2()

    if option == "4":
        os.system("cls")
        money = main_menu.Financial(money)
    os.system("cls")
    main_menu.Menu1()
    
    if option == "5":
        os.system("cls")
        if main_menu.Quit_Request() == 1:
            os.system("cls")
            main_menu.Menu3()
            main_menu.Option3()
        elif main_menu.Quit_Request() == 0:
            os.system("cls")
            main_menu.Menu1()

    if option == "6":
        os.system("cls")
        main_menu.About_Us()
        back_menu = Prompt.ask("[bold blue on white]Enter 0 to back to main menu[/bold blue on white]")
        if back_menu == "0":
            os.system("cls")
            main_menu.Menu1()

    if option == "7":
        os.system("cls")
        main_menu.Exit()
