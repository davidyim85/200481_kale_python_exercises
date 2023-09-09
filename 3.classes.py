
# Go back to Alex's lesson on Wednesday August 30th as a guide

# 1. Create a class called Wolf. When this class is instantiated it takes in a name and age. 
# the class is also to have a method called bark which will print its name and 'Ahhhoooo'

class Wolf:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f'{self.name} Ahhooooo')

# 2. Instantiate: Create an Object from the Wolf class and use the bark method
wolf_instance = Wolf('BigBadWolf', 5)

# the print when running this file is coming from this line below:
wolf_instance.bark()


# 3. Create a class called Dog. This class will Inherit from the class Wolf. 
# Please define a method called 'fetch' and have it print 'who is a good boy'

class Dog(Wolf):
    def fetch(self):
        print('who is a good boy')

# 4. Instantiate: Create an Object from the Dog class and try the bark method

dog_i = Dog('Spike', 2)
dog_i.bark()
dog_i.fetch()


# 5. Remember the class Fighter from Aug 30th.
# Change the attack method. 
# In the attack method, damage is strength subtracted by defense. 
# This needs change to: Any integer value between zero and strength subtracted by defense.
# Look up how to generate random number python
# Look up how to round to nearest integer in python

# 6. Change ryu and ken to have the same stats. Fight until ken win 2 times
# While the advantage will still be on the first attacker's side the result should be closer to 50/50
# I like an even match

import random

class Fighter:
    def __init__(self, name, hp, strength, defence):
        self.name = name
        self.hp = hp
        self.strength = strength
        self.defence = defence
        
    def attack(self, opponent):

        # self.strength time random.random generates a value from 0 to self.strenght BUT this is not a whole number
        # in order to round to the nearest integer we use the round method
        damage = round(self.strength * random.random()) - opponent.defence
        if (damage < 0):
            damage = 0
        opponent.hp -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage")
        
ryu = Fighter("Ryu", 100, 10, 5)
ken = Fighter("Ken", 100, 10, 5)

while(True):
    ryu.attack(ken)
    
    if (ken.hp <= 0):
        print(f"{ryu.name} wins!")
        break
        
    ken.attack(ryu)
    
    if (ryu.hp <= 0):
        print(f"{ken.name} wins!")
        break
