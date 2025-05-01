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

while True:
    want_instructions = yes_no("Do you want to read the instructions?  ")
    print(want_instructions)