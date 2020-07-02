#In Pokemon Go, a Pokemon is defined by several different
#parameters. For simplicity in this problem, we'll say that
#every Pokemon is defined by two parameters: its name, a
#string, and its power level, an integer.
#
#Create a class called Pokemon. The Pokemon class's
#constructor should have two parameters (in addition to self):
#the Pokemon's name and the Pokemon's power. These should be
#assigned to attributes called 'name' and 'power'.
#
#The Pokemon class should also have a method called
#would_defeat. would_defeat will have one parameter: an
#instance of a _different_ Pokemon. would_defeat should
#return True if this Pokemon's power is greater than the
#other Pokemon's power, or False if not.

class Pokemon:
    def __init__(self, name, power):
        self.name = name
        self.power = power
        
    def would_defeat(self,diffPokemon):
        if self.power > diffPokemon.power: return True
        else: return False

new_pokemon_1 = Pokemon("Pikachu", 500)
print(new_pokemon_1.name)
print(new_pokemon_1.power)

new_pokemon_2 = Pokemon("Charizard", 2412)
new_pokemon_3 = Pokemon("Squirtle", 312)
print(new_pokemon_1.would_defeat(new_pokemon_2))
print(new_pokemon_1.would_defeat(new_pokemon_3))
