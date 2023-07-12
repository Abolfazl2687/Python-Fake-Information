from faker import Faker
from pymsgbox import alert
from pymsgbox import confirm
from pymsgbox import prompt

faker = Faker("fa_IR")

name = faker.name()

username = faker.user_name()

password = faker.password()

gmail = faker.email()

address = faker.address()

txt = " : "

ttl = "Dark-Programmer"

title = "Dark-Programmer"

text = "Type: 1 for name,2 for user name, 3 for email, 4 for adress, 5 for password, || <q> for exit /\ <h> for help"

titl = "Dark-Programmer"

teext = "Are you sure do you want to exit ? "

wrong = "enter 1,2,3,4,5 or <q> or <h> !"

alert(text = text, title = title)

while 1:

    a = prompt(text = txt , title = ttl)

    if a == "1":
        alert(text = name, title = title)
    elif a == "2":
        alert(text = username, title = title)
    elif a == "3":
        alert(text = gmail, title = title)
    elif a == "4":
        alert(text = address, title = title)
    elif a == "5":
        alert(text = password, title = title)

    elif a == "q":
        output = confirm(text = teext, title = titl, buttons = ("Yes", "No"))
        if output == "Yes":
            break
    elif a == "h":
        alert(text = text, title = title)
    else:
        alert(text = wrong, title = title)
