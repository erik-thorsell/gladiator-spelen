from os import system


#rensar skärmen och lägger till en tom rad för att det ser bättre ut
def clear_screen() -> None:
    system("cls")
    print("\n"*1)