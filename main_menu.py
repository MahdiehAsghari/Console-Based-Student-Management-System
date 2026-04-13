from rich.console import Console
from rich.prompt import Prompt
from get_info import signUp_infos
import os
console = Console()


def Menu1():
    console.print("[bold red on #FBB02D]•1: Selection[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•2: Add and Remove[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•3: Confirmation[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•4: Financial[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•5: Quit Request[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•6: About Us[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•7: Exit[/bold red on #FBB02D]\n")

def Menu2():
    console.print("[bold red on #FBB02D]•1: Selected Lessons[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•2: Financial[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•3: Quit Request[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•4: About Us[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•5: Exit[/bold red on #FBB02D]\n")

def Menu3():
    console.print("[bold red on #FBB02D]•1: About Us[/bold red on #FBB02D]\n")
    console.print("[bold red on #FBB02D]•2: Exit[/bold red on #FBB02D]\n")

def Option2():
    money = 100
    while True:
        option = Prompt.ask("[bold blue on white]Choose Number of the Option[/bold blue on white]")

        if option == "1":
            os.system("cls")
            Confirmation2()
        os.system("cls")
        Menu2()

        if option == "2":
            os.system("cls")
            money = Financial(money)
        os.system("cls")
        Menu2()

        if option == "3":
            os.system("cls")
            if Quit_Request() == 1:
                os.system("cls")
                Menu3()
                Option3()
            elif Quit_Request() == 0:
                os.system("cls")
                Menu2()

        if option == "4":
            os.system("cls")
            About_Us()
            back_menu = Prompt.ask("[bold blue on white]Enter 0 to back to main menu[/bold blue on white]")
            if back_menu == "0":
                os.system("cls")
                Menu2()

        if option == "5":
            os.system("cls")
            Exit()

def Option3():
     while True:
        option = Prompt.ask("[bold blue on white]Choose Number of the Option[/bold blue on white]")

        if option == "1":
            os.system("cls")
            About_Us2()
            back_menu = Prompt.ask("[bold blue on white]Enter 0 to back to main menu[/bold blue on white]")
            if back_menu == "0":
                os.system("cls")
                Menu3()
        if option == "2":
            os.system("cls")
            Exit()


l_infos = []
selected_l = []

def Selection():
    lessons_name = ["Math 1", "Math 2", "English", "Programming Languages", 
                    "Basic Programming", "Physics", "Basic Economy", "Literature", "Statistics", "Theology"]
    lesson_code = ["334470","334471","334472","334473","334474","334475","334476","334477","334478","334479"]
    prof_name = ["Mr. Davidson","Mr. Jackson","Ms. Sara", "Mr. Smith", "Mr. Piterson", "Ms. Swift", "Mr. Chan",
                 "Ms. Anderson", "Mr. Pitt", "Ms. Aniston"]

    while True:
        for i in range(10):
            if i in selected_l:
                console.print(f"[bold black on green]•{i+1}: Lesson's name: {lessons_name[i]} / Prof's name: {prof_name[i]} / Lesson's Code: {lesson_code[i]}[/bold black on green]\n")
            else:
                console.print(f"[bold black on #00A8E8]•{i+1}: Lesson's name: {lessons_name[i]} / Prof's name: {prof_name[i]} / Lesson's Code: {lesson_code[i]}[/bold black on #00A8E8]\n")
        
        l_num = int(Prompt.ask("[bold blue on white]Choose the Lesson's Number\nEnter 0 to Back Menu[/bold blue on white]"))
        if l_num-1 not in selected_l:
            selected_l.append(l_num-1)
        if l_num == 0:
            break
        os.system("cls")

def Add_Remove():
    lessons_name = ["Math 1", "Math 2", "English", "Programming Languages", 
                    "Basic Programming", "Physics", "Basic Economy", "Literature", "Statistics", "Theology"]
    lesson_code = ["334470","334471","334472","334473","334474","334475","334476","334477","334478","334479"]
    prof_name = ["Mr. Davidson","Mr. Jackson","Ms. Sara", "Mr. Smith", "Mr. Piterson", "Ms. Swift", "Mr. Chan",
                 "Ms. Anderson", "Mr. Pitt", "Ms. Aniston"]
    
    while True:
        for i in range(10):
            if i in selected_l:
                console.print(f"[bold black on green]•{i+1}: Lesson's name: {lessons_name[i]} / Prof's name: {prof_name[i]} / Lesson's Code: {lesson_code[i]}[/bold black on green]\n")
            else:
                console.print(f"[bold black on #00A8E8]•{i+1}: Lesson's name: {lessons_name[i]} / Prof's name: {prof_name[i]} / Lesson's Code: {lesson_code[i]}[/bold black on #00A8E8]\n")
        
        l_num = int(Prompt.ask("[bold blue on white]Choose the Lesson's Number to ADD or REMOVE\nEnter 0 to Back Menu[/bold blue on white]"))
        if l_num-1 not in selected_l:
            selected_l.append(l_num-1)
        elif l_num-1 in selected_l:
            selected_l.remove(l_num-1)
        if l_num == 0:
            break
        os.system("cls")
    
def Confirmation():
    lessons_name = ["Math 1", "Math 2", "English", "Programming Languages", 
                    "Basic Programming", "Physics", "Basic Economy", "Literature", "Statistics", "Theology"]
    lesson_code = ["334470","334471","334472","334473","334474","334475","334476","334477","334478","334479"]
    prof_name = ["Mr. Davidson","Mr. Jackson","Ms. Sara", "Mr. Smith", "Mr. Piterson", "Ms. Swift", "Mr. Chan",
                 "Ms. Anderson", "Mr. Pitt", "Ms. Aniston"]

    console.print("[bold blue on white]Your Selected Lessons[/bold blue on white]\n")
    for i in range(10):
        if i in selected_l:
            console.print(f"[bold black on green]•{i+1}: Lesson's name: {lessons_name[i]} / Prof's name: {prof_name[i]} / Lesson's Code: {lesson_code[i]}[/bold black on green]\n")
    confirm = Prompt.ask("[bold blue on white]Confirm Your Selection (1) / Back Menu (0)[/bold blue on white]")
    if confirm == "1":
        return 1
    elif confirm == "0":
        return 0

def Confirmation2():
    lessons_name = ["Math 1", "Math 2", "English", "Programming Languages", 
                    "Basic Programming", "Physics", "Basic Economy", "Literature", "Statistics", "Theology"]
    lesson_code = ["334470","334471","334472","334473","334474","334475","334476","334477","334478","334479"]
    prof_name = ["Mr. Davidson","Mr. Jackson","Ms. Sara", "Mr. Smith", "Mr. Piterson", "Ms. Swift", "Mr. Chan",
                 "Ms. Anderson", "Mr. Pitt", "Ms. Aniston"]

    console.print("[bold blue on white]Your Selected Lessons[/bold blue on white]\n")
    for i in range(10):
        if i in selected_l:
            console.print(f"[bold black on green]•{i+1}: Lesson's name: {lessons_name[i]} / Prof's name: {prof_name[i]} / Lesson's Code: {lesson_code[i]}[/bold black on green]\n")
    Prompt.ask("[bold blue on white]You Confirmed Your Selection!!!/ Back Menu (0)[/bold blue on white]")

def Financial(x):
    os.system("cls")
    while True:
            console.print(f"[bold #f4b41a on #143d59]Account balance: {x}$ [/bold #f4b41a on #143d59]\n")
            console.print("[bold #143d59 on #f4b41a]•1: Payment[/bold #143d59 on #f4b41a]\n")
            console.print("[bold #143d59 on #f4b41a]•2: Withdraw[/bold #143d59 on #f4b41a]\n")
            y = Prompt.ask("[bold #210070 on #213970]Choose the option\nEnter 0 to Back Menu[/bold #210070 on #213970]")
            if y == "0":
                break
            if y == "1":
                os.system("cls")
                payment=int(Prompt.ask("[bold #210070 on #213970]Enter the payment amount[/bold #210070 on #213970]"))
                os.system("cls")
                x += payment
            if y == "2" :
                os.system("cls")
                withdraw=int(Prompt.ask("[bold #210070 on #213970]Enter the withdraw amount[/bold #210070 on #213970]"))
                os.system("cls")
                x -= withdraw
    return x

def Quit_Request():
    Prompt.ask("[bold blue on white]Write your Quit Requist / Enter 0 to Cancel[/bold blue on white]")
    q_request = Prompt.ask("[bold blue on white]Enter 1 to Confirm your Quit Requist / Enter 0 to Cancel[/bold blue on white]")
    if q_request == "1":
        return 1
    elif q_request == "0":
        return 0
        
def About_Us():
    for key, value in signUp_infos.items():
        console.print(f"[bold black on #23C9FF]{key} : {value}[/bold black on #23C9FF]\n")

def About_Us2():
    console.print(f"[bold black on red]I'm Tired of This Life !!![/bold black on red]\n")
   
def Exit():
    exit()
