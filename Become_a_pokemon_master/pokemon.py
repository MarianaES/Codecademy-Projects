class Pokemon:
    # To create a pokemon, give it a name, type, and level.
    # Max health depends on its level, its starting health is its max health.
    # It is not knocked out at the beginning of the game.
    # If no level is given, defaul level will be 5.
    def __init__(self, name, type, level = 5):
        self.name = name
        self.level = level
        self.type = type
        self.health = level * 5
        self.max_health = level * 5
        self.is_knocked_out = False

    # If printing any pokemon, it will tell you its name, type, level and health.
    def __repr__(self):
        return f"This level {self.level} {self.name} has {self.health} hit points remaining. It is a {self.type} type Pokemon"

    # When reviving a pokemon, it's knocked out status may be changed to False.
    # The .revive() method can only be called if the pokemon has no health points.
    def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
            self.health = 1
        print(f"{self.name} was revived!")

    # When knocking out a pokemon, it's knocked out status may be changed to True.
    # The .knock_out() method if there are any health points and set them up to 0.
    def knock_out(self):
        self.in_knocked_out = True
        if self.health != 0:
            self.health = 0
        print(f"{self.name} was nocked out!")

    # Health deducted on the amount, and remaining health is printed.
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.health = 0
            self.knockout()
        else:
            print(f"{self.name} now has {self.health} health.")

    # Health added on the amountm, and current health is printed.
    def gain_health(self, amount):
        if self.health == 0:
            self.revive()
            self.health += amount
        elif self.health >= self.max_health:
            self.health = self.max_health
        print(f"{self.name} now has {self.health} health.")

    #There are a lot of types with advantages & disadvantages but this code will only include: Fire, Water and Grass.
    def attack(self, other_pokemon):
        #Make sure the pokemon is still alive.
        if self.is_knocked_out:
            print(f"{self.name} can't attack because it is knocked out!")
            return None
        # If the pokemon attacking has a disadvantage, then it deals damage equal to half its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Water") or (self.type == "Water" and other_pokemon.type == "Grass") or (self.type == "Grass" and other_pokemon.type == "Fire"):
            damage = round(self.level * 0.5)
            print(f"{self.name} attacked {other_pokemon.name} for {damage} damage.")
            print("It's not very effective")
            other_pokemon.lose_health(round(self.level * 0.5))
        # If the pokemon attacking has neither advantage or disadvantage, then it deals damage equal to its level to the other pokemon
        if (self.type == other_pokemon.type):
            print(f"{self.name} attacked {other_pokemon.name} for {self.level} damage.")
            other_pokemon.lose_health(self.level)
        # If the pokemon attacking has advantage, then it deals damage equal to double its level to the other pokemon
        if (self.type == "Fire" and other_pokemon.type == "Grass") or (self.type == "Water" and other_pokemon.type == "Fire") or (self.type == "Grass" and other_pokemon.type == "Water"):
            damage = self.level * 2
            print(f"{self.name} attacked {other_pokemon.name} for {damage} damage.")
            print(f"It's super effective")
            other_pokemon.lose_health(damage)

    # Three classes that are subclasses of Pokemon.
    # Charmander is a fire type, Squirtle is a Water type, and Bulbasaur is a Grass type.

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

class Trainer:
    # A trainer has a list of pokemon (max. 6), a number of potions and a name.
    # When the trainer gets created, the first pokemon in their list of pokemons is the active pokemon (number 0)
    # A trainer also has a “currently active Pokémon”, which we represented as a number.
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    # Prints the name of the trainer, the pokemon they currently have, and the current active pokemon.
    def __repr__(self):
        print(f"The trainer {self.name} has the following pokemon")
        for pokemon in self.pokemons:
            print(pokemon)
        return "The current active pokemon is {name}".format(name = self.pokemons[self.current_pokemon].name)

    def switch_active_pokemon(self, new_active):
        # Switches the active pokemon to the number given as a parameter
        # First checks to see the number is valid (between 0 and the length of the list)
        if new_active <= len(self.pokemons) and new_active >= 0:
            # You can't switch to a pokemon that is knocked out
            if self.pokemons[new_active].is_knocked_out:
                print("{name} is knocked out. You can't make it your active pokemon".format(name = self.pokemons[new_active].name))
            # You can't switch to your current pokemon
            elif new_active == self.current_pokemon:
                print("{name} is already your active pokemon".format(name = self.pokemons[new_active].name))
            # Switches the pokemon
            else:
                self.current_pokemon = new_active
                print("Go {name}, it's your turn!".format(name = self.pokemons[self.current_pokemon].name))

    def use_potion(self):
        # Uses a potion on the active pokemon, assuming you have at least one potion.
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemons[self.current_pokemon].name))
            # A potion restores 20 health
            self.pokemons[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        # Your current pokemon attacks the other trainer's current pokemon
        my_pokemon = self.pokemons[self.current_pokemon]
        their_pokemon = other_trainer.pokemons[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

if __name__ == '__main__':
    # Six pokemon are made with different levels.
    a = Charmander(7)
    b = Squirtle()
    c = Squirtle(1)
    d = Bulbasaur(10)
    e = Charmander()
    f = Squirtle(2)
    #Two trainers are created. The first three pokemon are given to trainer 1, the second three are given to trainer 2.
    trainer_one = Trainer([a,b,c], 3, "José")
    trainer_two = Trainer([d,e,f], 5, "Mariana")
    print(trainer_one)
    print(trainer_two)
    # Testing attacking, giving potions, and switching pokemon.
    trainer_one.attack_other_trainer(trainer_two)
    trainer_two.attack_other_trainer(trainer_one)
    trainer_two.use_potion()
    trainer_one.attack_other_trainer(trainer_two)
    trainer_two.switch_active_pokemon(0)
    trainer_two.switch_active_pokemon(1)
