import random

def main():
    # random_addition()
    # random_substaction()
    # random_multiplication()
    random_division()

# def random_addition():
#     correct_attempt = 1
#     while correct_attempt != 4:
#         num1 = random.randint(10, 99)
#         num2 = random.randint(10, 99)

#         total = num1 + num2
#         print("What is " + str(num1) + " + " + str(num2) + "?")
#         user_answer = int(input("Your Answer: "))
#         if user_answer != total:
#             print("Incorrect.  The expected answer is " + str(total))
#             correct_attempt = 1
#         if user_answer == total:
#             print("Correct! You've gotten " + str(correct_attempt) + " correct in a row.")
#             correct_attempt += 1
#     print("Congratulations!  You mastered addition.")
#     print("The next step is learn how to subtract!")

# def random_substaction():
#     correct_attempt = 1
#     while correct_attempt != 4:
#         num1 = random.randint(10, 99)
#         num2 = random.randint(10, 99)

#         total = num1 - num2
#         print("What is " + str(num1) + " - " + str(num2) + "?")
#         user_answer = int(input("Your Answer: "))
#         if user_answer != total:
#             print("Incorrect.  The expected answer is " + str(total))
#             correct_attempt = 1
#         if user_answer == total:
#             print("Correct! You've gotten " + str(correct_attempt) + " correct in a row.")
#             correct_attempt += 1
#     print("Congratulations!  You mastered substraction.\n")
#     print("Next step is to learn multiplication!\n")


# def random_multiplication():
#     correct_attempt = 1
#     while correct_attempt != 4:
#         num1 = random.randint(10, 99)
#         num2 = random.randint(0, 10)

#         total = num1 * num2
#         print("What is " + str(num1) + " * " + str(num2) + "?")
#         user_answer = int(input("Your Answer: "))
#         if user_answer != total:
#             print("Incorrect.  The expected answer is " + str(total))
#             correct_attempt = 1
#         if user_answer == total:
#             print("Correct! You've gotten " + str(correct_attempt) + " correct in a row.")
#             correct_attempt += 1
#     print("Congratulations!  You mastered multiplication\n.")
#     print("Next step is to learn division!\n")
    
def random_division():
    correct_attempt = 1
    while correct_attempt != 4:
        num1 = random.randint(0, 10)
        num2 = random.randint(10, 99)

        total = num2 // num1
        print("What is " + str(num2) + " // " + str(num1) + "?")
        user_answer = float(input("Your Answer: "))
        if user_answer != total:
            print("Incorrect.  The expected answer is " + str(total))
            correct_attempt = 1
        if user_answer == total:
            print("Correct! You've gotten " + str(correct_attempt) + " correct in a row.")
            correct_attempt += 1
    print("Congratulations!  You mastered addition.")
    print("The next step is learn how to subtract!")
# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
