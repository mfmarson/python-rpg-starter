import random #randomize for Reaper and double damage

class Character: #blueprint
    def __init__(self, name, health=10, power=5, coins=20): #constructor and default params
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        #assigning values passed into attributes
        
    def attack(self, enemy): #method inside Character class self (ie attacker) 
        print(f'{self.name} attacks {enemy.name}!')
        enemy.health -= self.power #reduce enemy health and attacker power
        
    def is_alive(self): #method returns attackers new health confirming alive
        return self.health > 0

class Hero(Character): #new class inherits Character class attributes and methods
    def __init__(self, name, health, power, cape, coins=20): #constructor of class Hero
        super().__init__(name, health, power, coins) #inherited constructor from Character class
        self.cape = cape #assign value of cape attribute
        
    def attack(self, enemy): #attach method WITHIN HERO class - overrides inherited Character
        if random.random() < 0.2: #adds 20% probability of double damage from attacker/self
            print(f'Critical hit! {self.name} deals double damage!')
            damage = self.power * 2
        else: #if no critical hit, damage is equal to hero/self.power
            damage = self.power
        print(f'{self.name} attacks {enemy.name} with {damage} damage!')
        enemy.health -= damage #reduces enemy health by calculated damage
        
    def buy(self, item): #method within Hero class allowing an item param for hero to buy
        if self.coins >= item.cost: #checks to verify hero has enough coins
            self.coins -= item.cost #subtracts item coins from hero coins
            item.apply(self) #applying the purchase
            print(f'{self.name} bought {item.__class__.__name__} for {item.cost} coins.')
        else: #if line 33 is false
            print(f'{self.name} does not have enough coins to buy {item.__class__.__name__}.')

class Villain(Character): #new class inherits Character class attributes and methods
    def __init__(self, name, health, power, bounty=5): #initialize new attributes
        super().__init__(name, health, power) #inherited from Character 
        self.bounty = bounty

class Shadow(Character): #new class inherits Character class attributes and methods
    def __init__(self, name, health=1, power=5, bounty=10): #initialize new attributes
        super().__init__(name, health, power) #inherits from Character
        self.bounty = bounty

    def attack(self, enemy): #attack WITHIN SHADOW 
        if random.random() < 0.1: #10% chance to avoid attack
            print(f'{self.name} avoids the attack!') #Shadow avoids attack
        else: #Shadow attacks hero
            print(f'{self.name} attacks {enemy.name}!')
            enemy.health -= self.power #hero health - Shadow power

class Zombie(Character): #new class inherits Character class attributes and methods
    def __init__(self, name='Zombie', health=0, power=5, coins=0): #zombie attributes
        super().__init__(name, health, power, coins)

    def is_alive(self): #is this needed? override Character method?
        return self.health > 0

hero = Character('Hero', 20, 8) #same as parent objects
zombie = Zombie()

#while loop shows if zombie dead regardless
while zombie.is_alive() and hero.is_alive():
    hero.attack(zombie)
    if not zombie.is_alive():
        print(f'{zombie.name}: YOU CANNOT KILL ME. I\'M ALREADY DEAD!')
        break

    zombie.attack(hero)
    if not hero.is_alive(): #zombie attack hero
        print('The hero has fallen!')
        break

class Reaper: #class of its own - stands alone - "static?" when endgame returns true (10% chance) the game ends
    def end_game():
        return random.random() < 0.1

class Panda(Character):
    def hug(self, target):
        if target == self: #Po the panda gives hero a hug
            print(f'{self.name} gave {hero.name} a hug.')
        else: #Po the panda gives target-villain a hug
            print(f'{self.name} gave {target.name} a hug.')

class Store: # class for store holding (nesting) different items for purchase
    class Item: #initializing the future item costs
        def __init__(self, cost):
            self.cost = cost

        def apply(self, character): #added so specific item characters can be added
            pass #allows any item

    class Tonic(Item): #subclass of Item
        def __init__(self):
            super().__init__(5) #5 coins from inherited class Item self.cost

        def apply(self, character):
            character.health += 2 #adds 2 health to hero
            print(f"{character.name}'s health has increased by 2!")

    class Sword(Item):
        def __init__(self):
            super().__init__(10) #10 coins from inherited class Item self.cost

        def apply(self, character):
            character.power += 2 #adds 2 to hero power
            print(f"{character.name}'s power has increased by 2!")

    items = [Tonic(), Sword()] #holds all item instances (listed items)

  
    def do_shopping(hero): #shopping with hero parameter 
        print(f'Welcome to the store! You have {hero.coins} coins.')
        print('Available items:')
        for i, item in enumerate(Store.items):
            print(f'{i + 1}. {item.__class__.__name__} - {item.cost} coins')
        print('What would you like to buy?')
        try:
            choice = int(input('Enter the item number: ')) - 1
            if 0 <= choice < len(Store.items):
                hero.buy(Store.items[choice])
            else:
                print('Invalid choice')
        except ValueError:
            print('Invalid input. Please enter a number.')

hero = Hero('Hercules', 20, 8, False)
villain = Villain('Hades', 40, 2)
panda = Panda('Po')


if hero.cape:
    print(f'{hero.name} has a cape.')
else:
    print('NO CAPES!')

def play_game(): #player input selections outcomes
    while villain.health > 0 and hero.health > 0:
        print(f'You have {hero.health} health and {hero.power} power.')
        print(f'{villain.name} has {villain.health} health and {villain.power} power.')
        print()
        print('What do you want to do?')
        print(f'1. Fight {villain.name}')
        print('2. Do nothing')
        print('3. Run away')
        print(f'4. Attack zombie')
        print('5. Hug a panda')
        print(f'6. Give {villain.name} a panda hug')
        print('7. Visit the store')
        print('> ', end='')
        user_input = input()

        if user_input == '1':
            hero.attack(villain)
            if not villain.is_alive():
                print(f' {villain.name} is dead.')
                break
        elif user_input == '2':
            print('Have you thought this through...')
        elif user_input == '3':
            print('Goodbye.')
            break
        elif user_input == '4':
            print('YOU CANNOT KILL ME, I AM ALREADY DEAD!')
        elif user_input == '5':
            panda.hug(panda)
        elif user_input == '6':
            panda.hug(villain)
        elif user_input == '7':
            Store.do_shopping(hero)
        else:
            print('Invalid input')
        
        if Reaper.end_game():
            print('DUN, DUN, DUN! THE REAPER HAS SPOKEN. GAME OVER.')
            break

        if villain.is_alive():
            villain.attack(hero)
            print(f'{villain.name} does {villain.power} damage to you.')
            if not hero.is_alive():
                print('You are dead.')
                break

play_game()

