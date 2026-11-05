# Emma Jackson
# mod_2_case_study.py
# This app will inform students whether or not they made the deans list or honor roll by allowing them to input their GPA's through a series of prompts.

while True:
    last_name = input("please enter your last name: ")
    if last_name.upper() == "ZZZ":
        break
    else:
        first_name = input("please enter your first name: ")
        gpa = float(input("please enter your GPA: "))
        if gpa >= 3.5:
            print(f"Congratulations {first_name} {last_name}, you made the Dean's List!")
        elif gpa >= 3.25:
            print(f"Congratulations {first_name} {last_name}, you made the Honor Roll!")
        else:
            print(f"Sorry {first_name} {last_name}, you did not make the Dean's List or Honor Roll.")
