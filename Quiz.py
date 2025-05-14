import random

# if this function is called then it will check if the user has typed yes / no
# if not then the function will ask for yes / no again!
def yes_no(question):
    """checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:

        response = input(question).lower()
        # check if the user input is yes / y
        if response == "yes" or response == "y":
            return "yes"
        # check if the user input is no / n
        elif response == "no" or response == "n":
            return "no"
        # print an error message if the user doesn't type yes / y or no / n
        else:
            print("Enter Yes / No")

# this function if called will check that the user input is a valid integer!
def int_check(question, low=None, high=None, exit_code=None):
    # this is the error area
    if low is None and high is None:
        error = "Please enter an integer"

    elif low is not None and high is None:
        error = (f"Please enter an integer the is "
                 f"more than / equal to {low}")

    else:
        error = (f"Please enter an integer the "
                 f"is between {low} and {high} (inclusive)")

    while True:
        # this is where it asks for the user input
        response = input(question).lower()

        # checks if the user typed the exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            if low is not None and response < low:
                print(error)

            elif high is not None and response > high:
                print(error)

            else:
                return response


        except ValueError:
            print(error)

# this is the function where the instructions are stored!
def instructions():
    """PRINTS INSTRUCTIONS"""

    print('''
**** Information and Instructions ****
This quiz's question's / answer's are randomly generated

To get started with the quiz follow the following steps

1) Enter the amount of questions you want to answer!
2) Work out the answer and enter it
3) Once you have answered all the questions you will be asked if 
   you want to see your history if you answer yes it will display! 

Good Luck and have fun!!!
    ''')

# this is the function where it gets the random number's that the user is asked for.
# it is also where the maths are done
def do_maths(op_type):
    # this is where the default parameters are!
    if op_type == 1 or op_type == 2:
        low_num = 1
        high_num = 1000
    else:
        low_num = 2
        high_num = 20
    # this is where the random numbers are generated.
    number1 = random.randint(low_num, high_num)
    number2 = random.randint(low_num, high_num)

    # this is where it does the math
    if op_type == 1:
        answer = number1 - number2
        unit = "-"
    elif op_type == 2:
        answer = number1 + number2
        unit = "+"
    elif op_type == 3:
        temp_ans = number1 * number2
        answer = number1
        number1 = temp_ans
        unit = "/"
    else:
        answer = number1 * number2
        unit = "*"
    # this is the question heading
    print(f"🤔🤔🤔 You are on question number {round_played} out of {max_rounds} 🤔🤔🤔")
    print(answer)
    # this is where the user is asked for there input.
    user_answer = int_check(f"{number1} {unit} {number2} ", exit_code="xxx")
    # this is where it checks if you got the right / wrong answer
    if user_answer == "xxx":
        return user_answer
    # this is where the user gets their feedback and also adds it to the quiz history
    if user_answer == answer:
        feedback = f"😃😃😃 Well Done for guessing the answer {answer} 😃😃😃"
        quiz_history.append(f"😀😀😀Question {round_played}, The question was {number1} {unit} {number2} and you guessed the correct answer which was {answer} 😀😀😀")
    else:
        feedback = f"💩💩💩 You didn't Guess the answer: {answer} 💩💩💩"
        quiz_history.append(f"💩💩💩Question {round_played}, The question was {number1} {unit} {number2} the correct answer was {answer} BUT you guessed {user_answer} 💩💩💩")
    print(feedback)
    print()
    # check user_answer against answer


# this is where the variables are initiated!
round_played = 1
max_rounds = 0
quiz_history = []

print("🎩🎩🎩 Welcome to the QUIZ! 🎩🎩🎩")

# this ask the user if they want to see the instructions!
want_instructions = yes_no("Do you want to read the instructions?  ")
# display the instructions
if want_instructions == "yes":
    instructions()

# ask the user what the max number of question's they want to answer!
max_rounds = int_check("What is the max number of questions you want to answer? (max 30) ", low=1, high=30)

while round_played <= max_rounds:
    # call the do_maths function witch is where the main part of the program is!
    math_ans = do_maths(random.randint(1, 4))
    # checks if the user typed the exit code if so the quiz will break
    if math_ans == "xxx":
        break
    # add 1 to the round's played until it is equal to max_rounds then it will stop the loop!
    round_played += 1

print("Quiz over")
print()

# this is the history part of the quiz
if round_played > 1:
    # ask the user if they want to see there history for the quiz!
    see_history = yes_no("Do you want to see your history?  ")
    print()
    # checks if the user typed yes/y if so the quiz history will display!
    if see_history.lower() == "yes" or see_history.lower() == "y":
        print("🪄🪄🪄 Quiz History 🪄🪄🪄")
        print()
        for item in quiz_history:
                print(item)

        print()
        print("Thanks for answering the quiz's question"
              "All Answer were generated of the fly!")
# this is where if the user doesn't answer any question's it will print the following!
else:
    # print a statement if that user selected infinite mode and didn't play any rounds!!!
    print("🐔🐤🐥🐔 Oops! You chickens out and didn’t play any rounds🐔🐤🐥🐔 ")