import random

def main():
    """
    set min and max constant to help a computer to select random numbers for addition between 10 and 99
    input from user the result of addition
    create while loop (which will check the addition)
        if correct, the program will print output correct and run one more time until correct_attempt != 4
        if user input is not correct correct_attempts will need to restart with 1 again.
        if user did addition correctly 3 times, write a message "Congratulation" message outside while loop
        program will stop running after 3 correct answers
    """
    random_addition()

def random_addition():
    correct_attempt = 1
    while correct_attempt != 4:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)

        total = num1 + num2
        print("What is " + str(num1) + " + " + str(num2) + "?")
        user_answer = int(input("Your Answer: "))
        if user_answer != total:
            print("Incorrect.  The expected answer is " + str(total))
            correct_attempt = 1
        if user_answer == total:
            print("Correct! You've gotten " + str(correct_attempt) + " correct in a row.")
            correct_attempt += 1
    print("Congratulations!  You mastered addition.")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
