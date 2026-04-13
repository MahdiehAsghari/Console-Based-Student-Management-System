def FirstFrame(lst, c):
    text = "[#EC4067]"
    text += f"{c * 50}\n"

    for i in lst:
        text += f"{c}{int((48-len(i))/2)*' '}[bold #AFCBFF]{i}[/bold #AFCBFF]{int((48-len(i))/2)*' '}{' ' if len(i)%2 else ''}{c}\n"
        text += f"{c}{48 * ' '}{c}\n"

    text += c*50
    text += "\n"
    text += "[/#EC4067]"
    return text
