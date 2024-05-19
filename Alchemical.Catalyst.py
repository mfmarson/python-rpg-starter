import random

# Introduction function
def introduction():
    print("Welcome to: The Alchemical Catalyst!")
    print("You are Dr. Shelly Gideon, a skilled alchemist in Piltover.")
    print("Your mission is to find Mary Fisk in the underground city and take back the Alchemical Catalyst before she uses it against the city.")
    print("Your team is waiting to meet you")
    print("Good-luck, Doctor!")
    input("Press Enter to continue...")

def meet_characters():
    print("You will meet three key allies:")
    print("1. Inspector Amelia Worthington: A dedicated police inspector.")
    print("2. Professor Archibald Ravenscroft: An elderly alchemist with wisdom to share.")
    print("3. Harriet 'Hattie' Blackwood: A skilled mechanic with innovative gadgets.")
    input("Press Enter to continue...")

# Define questions and answers
questions = [
    {
        "question": "True or False: It is not possible to nest while loops in Python.",
        "options": ["1. True", "2. False"],
        "answer": "2"
    },
    {
        "question": "What does K.I.S.S stand for?",
        "options": ["1. Keep It Super Smart", "2. Keep It Super Simple", "3. Keep It Simple Stupid"],
        "answer": "3"
    },
    {
        "question": "How do you convert a String to an Integer?",
        "options": ["1. int()", "2. int():", "3. int{}"],
        "answer": "1"
    },
]

# Function to ask a question and check the answer
def ask_question(question):
    print(question["question"])
    for option in question["options"]:
        print(option)
        print("You must unlock the hints by answering these questions.")
    answer = input("Enter the number of your choice: ")
    return answer == question["answer"]

# Function to ask all questions
def ask_all_questions():
    correct_answers = 0
    for question in questions:
        if ask_question(question):
            correct_answers += 1
        else:
            print("Incorrect Answer")
    return correct_answers == len(questions)

# Journey starts here
def start_journey():
    clues = [
        "Clue 1: Look near Professor Archibald Ravenscroft's alchemical lab.",
        "Clue 2: Hattie's workshop may hold secrets.",
        "Clue 3: Detective Dupin might have critical information."
    ]
    found_clues = []
    for i in range(1, 5):
        print(f"\nStep {i}: Where do you want to go?")
        print("1. Detective Station")
        print("2. Alchemical Lab")
        print("3. Hattie's Workshop")
        choice = input("Enter the number of your choice: ")
        if choice in ["1", "2", "3"]:
            if ask_question(random.choice(questions)):
                found_clues.append(clues[int(choice) - 1])
                print(f"Correct! Found clue: {found_clues[-1]}")
            else:
                print("Incorrect answer. You didn't get the clue.")
        else:
            print("Invalid choice. You wasted time and didn't find a clue.")
    input("You have found Lucius Crow! Don't let him get away with the Catalyst! \n Press Enter to continue...")

# Battle with the villain
def battle_villain():
    hero_health = 40
    villain_health = 50
    while hero_health > 0 and villain_health > 0:
        print(f"\nYour health: {hero_health}, Lucius Crowe's health: {villain_health}")
        print("Choose your action:")
        print("1. Attack")
        print("2. Defend")
        action = input("Enter the number of your choice: ")
        if action == "1":
            damage = random.randint(10, 20)
            villain_health -= damage
            print(f"You dealt {damage} damage to Lucius Crowe!")
        elif action == "2":
            print("You defend against Lucius Crowe's attack.")
            continue
        else:
            print("Invalid choice. You missed your turn.")
            continue
        
        villain_damage = random.randint(5, 15)
        hero_health -= villain_damage
        print(f"Lucius Crowe dealt {villain_damage} damage to you!")
    
    if hero_health > 0:
        print("\nCongratulations! You have defeated Lucius Crowe and secured the Alchemical Catalyst.")
    else:
        print("\nYou have been defeated by Lucius Crowe. The Alchemical Catalyst is lost.")

# Closing commentary
def closing_commentary():
    print("\nThank you for playing! The fate of Brasshaven lies in your hands.")
    print("Whether you succeeded or failed, your efforts are appreciated.")
    print("Until next time, farewell!")

# Main function to run the game
def main():
    introduction()
    meet_characters()
    start_journey()
    while not ask_all_questions():
        print("\nYou must answer all questions correctly to proceed.")
    battle_villain()
    closing_commentary()

# Run the game
if __name__ == "__main__":
    main()
