## udělat sázku na červenou a černou, zadat, kolik si přeje vsadit, potom na co se vsází
import random

def get_value():
    gen = random.randint(1,37)
    if gen >=1 and gen <=18:
        return "Red"
    elif gen >=19 and gen <=36:
        return "Black"
    if gen==37:
        return "Green"

startMoney = 1000
print("Welcome in casino! :)")
print("You have to choose one of this color: Red, Green, or Black, Green color is bad for you, because you will lose everything.")
print("You have start money, 1000$, and you cant bet more than 1000$ every time.")

while startMoney > 0:
## sorry lukáši, pořádně nevím, jak funguje kasíno, jestli má vyhrát, když padne černá, nebo ne, takže vyhrává, jen když padne červená :D
    enterMon = int(input("Enter money to casino: "))
    if enterMon>1000:
        print("You cant bet more than 1000")
        continue
    print("You entered ", enterMon)
    enterCol = str(input("Enter color: "))
    if enterCol != "Black" & "Red":
        print("Green, so choose color again.")
        continue
    value = get_value()
    print(value)
    if value == enterCol: 
        startMoney += enterMon
        print("Congratz, you won, your money is", startMoney)
    else:
        startMoney -= enterMon
        print("OoOh, you lost, try it again :-), your money is", startMoney)
        if startMoney <= 0:
            print("Sorry, you cant play more, your money are gone")
            break
    if startMoney <= 0:
        print("Sorry, you cant play more, your money are gone.")
        break
    