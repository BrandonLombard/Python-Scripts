import random

run = True  # Set run to true
score = 0  # Keep track of how many questions the user gets right

# Tell user one way to exit program
print('Type e to exit')

# While run is true, continue program
while run:
    # Set up random numbers between 0 and 12 with randint
    first_number = random.randint(0, 12)
    second_number = random.randint(0, 12)

    # Have user input their answer
    answer = input(str(first_number) + "*" + str(second_number) + "=")

    # If user gets the answer right, tell them they were correct
    if answer == str(first_number * second_number):
        score = score + 1
        if (first_number >= 7) and (second_number >= 7): # Give extra point if numbers are larger than 6
            score = score + 1
        print('Correct! Your score is ' + str(score))
    elif answer != str(first_number * second_number):
        print("Incorrect, the answer is: " + str(first_number * second_number))
    # Else tell the user they were wrong and give them correct answer
    else:
        print("Error")

