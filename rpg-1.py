import random

class Character:
    def __init__(self, name, health=10, power=5, coins=20):
        self.name = name
        self.health = health
        self.power = power
        self.coins = coins
        
    def attack(self, enemy):
        print(f'{self.name} attacks {enemy.name}!')
        enemy.health -= self.power
        
    def is_alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, name, health, power, cape, coins=20):
        super().__init__(name, health, power, coins)
        self.cape = cape
        
    def attack(self, enemy):
        if random.random() < 0.2:
            print(f'Critical hit! {self.name} deals double damage!')
            damage = self.power * 2
        else:
            damage = self.power
        print(f'{self.name} attacks {enemy.name} with {damage} damage!')
        enemy.health -= damage
        
    def buy(self, item):
        if self.coins >= item.cost:
            self.coins -= item.cost
            item.apply(self)
            print(f'{self.name} bought {item.__class__.__name__} for {item.cost} coins.')
        else:
            print(f'{self.name} does not have enough coins to buy {item.__class__.__name__}.')

class Villain(Character):
    def __init__(self, name, health, power, bounty=5):
        super().__init__(name, health, power)
        self.bounty = bounty

class Shadow(Character):
    def __init__(self, name, health=1, power=5, bounty=10):
        super().__init__(name, health, power)
        self.bounty = bounty

    def attack(self, enemy):
        if random.random() < 0.1:
            print(f'{self.name} avoids the attack!')
        else:
            print(f'{self.name} attacks {enemy.name}!')
            enemy.health -= self.power

class Zombie(Character):
    def __init__(self, name='Zombie', health=0, power=5, coins=0):
        super().__init__(name, health, power, coins)

    def is_alive(self):
        return self.health > 0

hero = Character('Hero', 20, 8)
zombie = Zombie()

while zombie.is_alive() and hero.is_alive():
    hero.attack(zombie)
    if not zombie.is_alive():
        print(f'{zombie.name}: YOU CANNOT KILL ME. I\'M ALREADY DEAD!')
        break

    zombie.attack(hero)
    if not hero.is_alive():
        print('The hero has fallen!')
        break

class Reaper:
    def end_game():
        return random.random() < 0.1

class Panda(Character):
    def hug(self, target):
        if target == self:
            print(f'{self.name} gave {hero.name} a hug.')
        else:
            print(f'{self.name} gave {target.name} a hug.')

class Store:
    class Item:
        def __init__(self, cost):
            self.cost = cost

        def apply(self, character):
            pass

    class Tonic(Item):
        def __init__(self):
            super().__init__(5)

        def apply(self, character):
            character.health += 2
            print(f"{character.name}'s health has increased by 2!")

    class Sword(Item):
        def __init__(self):
            super().__init__(10)

        def apply(self, character):
            character.power += 2
            print(f"{character.name}'s power has increased by 2!")

    items = [Tonic(), Sword()]

  
    def do_shopping(hero):
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
character = Zombie()

if hero.cape:
    print(f'{hero.name} has a cape.')
else:
    print('NO CAPES!')

def play_game():
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

