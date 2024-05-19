import random

class AlchemicalCatalystGame:
    def __init__(self):
        self.hero_health = 40
        self.villain_health = 50
        self.questions = [
            {
                "question": "True or False: It is not possible to nest while loops in Python.\n",
                "options": ["1. True\n", "2. False\n"],
                "answer": "2"
            },
            {
                "question": "What does K.I.S.S stand for?\n",
                "options": ["1. Keep It Super Smart\n", "2. Keep It Super Silly\n", "3. Keep It Simple Stupid\n"],
                "answer": "3"
            },
            {
                "question": "How do you convert a String to an Integer?\n",
                "options": ["1. int()\n", "2. int():\n", "3. int{}\n"],
                "answer": "1"
            },
        ]
        self.clues = [
            "Look near Professor Ravenscroft's alchemical lab.\\n",
            "Hattie's workshop may hold secrets.\\n",
            "Detective Dupin might have critical information.\n"
        ]
        self.found_clues = []

    def introduction(self):
        print("\nWelcome to: The Alchemical Catalyst!\n")
        print("You are Dr. Shelly Gideon, a skilled alchemist in Piltover.\n")
        print("Your mission is to find Mary Fisk in the underground city and take back the Alchemical Catalyst before she uses it against the city.\n")
        print("Your team is waiting to meet you\n")
        print("Good-luck, Doctor!\n")
        input("Press Enter to continue...\n")

    def meet_characters(self):
        print("Meet your team:\n")
        print("Detective Dupin: A dedicated police detective.\n")
        print("Professor Ravenscroft: An elderly alchemist with wisdom to share.\n")
        print("Amelia Jones: A skilled mechanic with innovative gadgets.\n")
        input("Press Enter to continue...\n")

    def ask_question(self, question):
        print(question["question"])
        for option in question["options"]:
            print(option)
        answer = input("Enter the number of your choice: \n")
        return answer == question["answer"]

    def ask_all_questions(self):
        correct_answers = 0
        for question in self.questions:
            if self.ask_question(question):
                correct_answers += 1
            else:
                print("Incorrect Answer\n")
        return correct_answers == len(self.questions)

    def start_journey(self):
        num_steps = min(3,len(self.questions))
        
        for i in range(num_steps):
            print(f"\nWhere do you want to go?\n")
            print("1. Detective Dupin's Station\n")
            print("2. Professor Ravenscroft's Alchemical Lab\n")
            print("3. Amelia's Workshop\n")
            choice = input("Enter the number of your choice:\n ")
            if choice in ["1", "2", "3"]:
                question = self.questions[i]
                if self.ask_question(question):
                    self.found_clues.append(self.clues[int(choice) - 1])
                    print(f"Correct! Found clue: {self.found_clues[-1]}\n")
                    if i == num_steps -1:
                        break
                else:
                    print("Incorrect answer. You didn't get the clue.\n")
            else:
                print("Invalid choice. You wasted time and didn't find a clue.\n")
        
        input("WAIT! STOP! \nTHERE IS MARY FISK!\n \nDON'T LET HER GET AWAY WITH THE CATALYST! \n\n Press Enter to continue...\n")
        self.battle_villain()
     
    def battle_villain(self):
        while self.hero_health > 0 and self.villain_health > 0:
            print(f"\nYour health: {self.hero_health},\n Mary Fisk's health: {self.villain_health}\n")
            print("Choose your action:\n")
            print("1. ATTACK\n")
            print("2. Defend\n")
            action = input("Enter the number of your choice: \n")
            if action == "1":
                damage = random.randint(10, 20)
                self.villain_health -= damage
                print(f"You dealt {damage} damage to Mary Fisk!\n")
            elif action == "2":
                print("You defend against Mary Fisk's attack.\n")
                continue
            else:
                print("Invalid choice. You missed your turn.\n")
                continue

            villain_damage = random.randint(5, 15)
            self.hero_health -= villain_damage
            print(f"Mary Fisk dealt {villain_damage} damage to you!\n")

        if self.hero_health > 0:
            print("\nCongratulations, team! \n\nYou all have defeated Mary Fisk and secured the Alchemical Catalyst! \n\nYou have saved Piltover! \nHead back to The Heart of Gold and celebrate!\n")
        else:
            print("\nYou have been defeated by Mary Fisk. \n\nThe Alchemical Catalyst has been lost. \nLet's get the team together and regroup.\n\n We move at dawn.\n")
            
        

    def play_game(self):
        self.introduction()
        self.meet_characters()
        self.start_journey()
      
        
if __name__ == "__main__":
    game = AlchemicalCatalystGame()
    game.play_game()
