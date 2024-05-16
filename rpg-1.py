
class Character:
    def __init__(self, name, health=10, power=5): #giving health/power default numbers by adding = number 
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self, enemy):
        print(f'{self.name} attacks {enemy.name}!')
        enemy.health -= self.power
        
    def is_alive(self): #if wanting a true/false prompt method in question - is villain alive - yes/True false/Dead 
        return self.health > 0 
        
class Hero(Character): #child class
    def __init__(self, name, health, power, cape):
        super().__init__(name,health,power)
        self.cape = cape

class Villain(Character): #child class
    def __init__(self,name,health,power):
        super().__init__(name,health,power)

hero = Hero('Batman', 20, 8, True)
villain = Villain('Joker', 40 ,2) 

def play_game():
    
    while villain.health > 0 and hero.health > 0:
        print(f"You have {hero.health} health and {villain.power} power.")
        print(f"The {villain.name} has {villain.health} health and {villain.power} power.") 
        print()
        print("What do you want to do?")
        print("1. fight villains")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(villain)
            print(f"You do {hero.power} damage to {villain.name}.")
        if not villain.is_alive(): #if villain is not alive 
            print(f'The {villain.name} is dead.')
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input ")

        if villain.is_alive():
            # Goblin attacks hero
            villain.attack(hero)
            print(f"The {villain.name} does {villain.power} damage to you.")
            if not hero.is_alive():
                print("You are dead.")
play_game()