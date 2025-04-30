print('''NAMASKAR DEVIYO OR SAJJANO
KBC ME APKA SWAGAT HAI COMPUTER SCREEN PE APKA PEHLA SAWAL''')

questions = [
    ["Titanic me aisa kya lagate ki vo dubti nahi?", "3 k", "aalu", "papad", "taang", 1],
    ["Agar Superman ko bhukh lage to vo kya khayega?", "3 k", "burger", "duniya", "current", 2],
    ["Aise kaunse kapde hain jo kabhi gande nahi hote?", "3 k", "imagination", "sapne", "soch", 3],
    ["Kis chiz ka face hota hai lekin aankhen nahi?", "3 k", "coin", "clock", "map", 3]
]

levels = [10000, 20000, 30000, 40000]  # Levels should be matched to the questions
money = 0  # Starting amount

# Loop through the questions
for i in range(len(questions)):
    question = questions[i]

    # Print the question and choices
    print(f"\nQuestion for ₹{levels[i]}:")  # Display the level/prize
    print(f"Q{i + 1}: {question[0]}")  # Display the question
    print(f"a. {question[1]}")
    print(f"b. {question[2]}")
    print(f"c. {question[3]}")
    print(f"d. {question[4]}")

    # Get user's answer
    try:
        a = int(input("Enter your answer (1-4): "))  # Try to convert input to integer
        if a == question[-1]:  # Check if the answer is correct
            money = levels[i]  # Update money if correct
            print(f"Correct answer! You've won ₹{money}.")
        else:
            print("Wrong answer. Better luck next time!")
            break  # End the game if the answer is wrong
    except ValueError:  # Catch exception if user inputs something that can't be converted to an integer
        print("Invalid input. Please enter a number between 1 and 4.")
        break  # End the game on invalid input

# Final message
if money == levels[-1]:  # If the user reached the last level
    print(f"Saabash! Aap jeet chuke hai ₹{money}.")
else:
    print(f"Take your money: ₹{money}")


