# creating a self intro script generator project 1 

# importing date and time library 
import datetime 
# .strip()- This ensures that if the user accidentally adds spaces before or after their name, those spaces are removed.
name = input("what is your name").strip()
age = input("How old are you").strip()
city = input("Which city do you live?").strip()
proffesion =input("what is your proffesion").strip()
hobby =input("what is your hoby?").strip()

# f is formatted string - It allows you to directly insert the values of variables inside curly braces {} within the string.
intro_message = (
    f"Hello! My name is {name}, I'm {age} years old and live in {city}.\n"   # \n is used for line break 
    f"I work as a {proffesion} and I absolutely enjoy {hobby} in my free time.\n"
    "Nice to meet you!\n"
)

# getting today date using datetime module / coverting date to a string using iso 
current_date = datetime.date.today().isoformat()
intro_message += f"\n Logged on : {current_date}"

border = "*" * 80
final_output = f"{border}\n{intro_message}\n{border}"

print("\n" + final_output)


