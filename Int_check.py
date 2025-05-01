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
while True:
    int_1 = int_check("What is the max number of questions you want to answer? (max 30) ", low=1, high=30)
    print(int_1)