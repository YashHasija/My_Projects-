# creating a self intro script generator project 1 

# .strip()- This ensures that if the user accidentally adds spaces before or after their name, those spaces are removed.
import datetime
name = input("what is your name").strip()
age = input("How old are you").strip()
city = input("Which city do you live?").strip()
proffesion = ("what is your proffesion").strip()
hobby = ("what is your hoby?").strip()

intro_message = (
    f"Hello! My name is {name} , I'm {age} years old and
    live in {city}"
    f"I work as a {proffesion} and i absolutely enjoy {hobby} 
    in my free time"
    f"Nice to meet you!\n" # \n is used for new line 
    )

current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on : {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)
