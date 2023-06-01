import random
import methods as m

class entity:
    def __init__(self, attack, magic, defense, resistance, speed, hp, cooldown, experience):
        self.attack = attack
        self.magic = magic
        self.defense = defense
        self.resistance = resistance
        self.speed = speed
        self.hp = hp
        self.cooldown = 0
        self.experience = 0

    def gain_experience(self, amount):
        self.experience += amount
        print("You gained", amount, "experience points.")

        if self.experience >= 100:
            self.level_up()

    #numbers for level up should definitely be considered here, so 1,2 are just placeholders :)
    def level_up(self):
        self.hp = 100
        self.attack += random.randint(1, 2)
        self.magic += random.randint(1, 2)
        self.defense += random.randint(1, 2)
        self.resistance += random.randint(1, 2)
        self.speed += random.randint(1, 2)
        self.experience = 0
        self.actions_remaining = 1 #1 is just a placeholder value, its p much everywhere bc i didnt wanna keep checking whats what while laying it out :)
        print("Nice! You leveled up. Your stats have increased.")
        #TO DO - add prompt explaining what went up and by how much

#player classes
class mage(entity):
    def __init__(self):
        super().__init__(random.randint(10, 20), random.randint(70, 100),
                         random.randint(1, 5), random.randint(7, 10),
                         random.randint(3, 6), random.randint(100, 120),
                         cooldown = 0, experience = 0)
        self.class_name = "Mage"
        self.actions_remaining = 1
        self.weaponName = 'Staff'
        self.weapon = object(random.randint(5, 10))
    def attack(self, weapon):
        damage = self.attack + weapon.damage
        return damage

class paladin(entity):
    def __init__(self):
        super().__init__(random.randint(30, 40), random.randint(50, 80),
                         random.randint(5, 9), random.randint(6, 9),
                         random.randint(3, 7), random.randint(140, 180),
                         cooldown = 0, experience = 0)
        self.class_name = "Paladin"
        self.actions_remaining = 1
        self.weaponName = 'Sword'
        self.weapon = object(random.randint(5, 10))
    def attack(self, weapon):
        damage = self.attack + weapon.damage
        return damage

class warrior(entity):
    def __init__(self):
        super().__init__(random.randint(40, 50), random.randint(10, 30),
                         random.randint(6, 10), random.randint(1, 3),
                         random.randint(5, 9), random.randint(150, 180),
                         cooldown = 0, experience = 0)
        self.class_name = "Warrior"
        self.actions_remaining = 1
        self.weaponName = 'Axe'
        self.weapon = object(random.randint(5, 10))
    def attack(self, weapon):
        damage = self.attack + weapon.damage
        return damage

class ranger(entity):
    def __init__(self):
        super().__init__(random.randint(30, 40), random.randint(30, 50),
                         random.randint(3, 6), random.randint(4, 6),
                         random.randint(7, 10), random.randint(150, 180),
                         cooldown = 0, experience = 0)
        self.class_name = "Ranger"
        self.actions_remaining = 1
        self.weaponName = 'Bow'
        self.weapon = object(random.randint(5, 10))
    def attack(self, weapon):
        damage = self.attack + weapon.damage
        return damage

    #Creatures
class goblin(entity):
    def __init__(self):
        super().__init__(random.randint(20, 30), random.randint(30, 50),
                             random.randint(3, 4), random.randint(1, 3),
                             random.randint(4, 6), random.randint(60, 100),
                        cooldown = 0, experience = 0)
        self.class_name = "Goblin"

    def attack(self, enemy):
        damage = self.attack - enemy.defense
        enemy.hp = enemy.hp - damage
        return enemy.hp

    #def sneakyStab(self, enemy):
        #self.cooldown += 3
        #if enemy.speed <= 5:
            #enemy.hp = enemy.hp - self.attack * 2
            #print("Goblin got a critical strike!")
        #else:
            #damage = self.attack - enemy.defense
            #enemy.hp = enemy.hp - damage
        #return enemy.hp



class orc(entity):
    def __init__(self):
        super().__init__(random.randint(30, 40), random.randint(30, 50),
                             random.randint(4, 6), random.randint(3, 6),
                             random.randint(3, 5), random.randint(100, 150),
                        cooldown = 0, experience = random.randint(20, 25))
        self.class_name = "Orc"

    def attack(self, enemy):
        damage = (self.attack + 5) - enemy.defense
        enemy.hp = enemy.hp - damage
        return enemy.hp

    #def savage_blows(self, enemy):
        #self.cooldown += 4
        #blows = 0
        #while blows < 3:
            #blows += 1
            #hitChance = random.randint(1,2)
            #if hitChance == 2:
                #damage = (self.attack) - enemy.defense
                #enemy.hp = enemy.hp - damage
                #print(f"Attack {blows} hit for {self.attack} damage")
            #else:
                #print(f"Attack {blows} missed")


class troll(entity):
    def __init__(self):
        super().__init__(random.randint(30, 40), random.randint(30, 50),
                             random.randint(4, 6), random.randint(3, 6),
                             random.randint(3, 5), random.randint(100, 150),
                        cooldown = 0, experience = random.randint(20, 25))
        self.class_name = "Troll"
        #self.regeneration = 10

    def attack(self, enemy):
        damage = (self.attack + 10) - enemy.defense
        enemy.hp = enemy.hp - damage
        return enemy.hp

    #def snotRocket(self, enemy):
        #self.cooldown += 4
        #if enemy.resistance <= 6:
            #enemy.speed = enemy.speed - 4
            #enemy.defense = enemy.defense - 4
            #print("the trolls snot rocket lowered your defense and speed by 4!")
        #else:
            #print("The trolls snot rocket missed")
        #return enemy


class golem(entity):
    def __init__(self):
        super().__init__(random.randint(30, 40), random.randint(30, 50),
                             random.randint(4, 6), random.randint(3, 6),
                             random.randint(3, 5), random.randint(100, 150),
                        cooldown = 0, experience = random.randint(20, 25))
        self.class_name = "Golem"
        #self.damageResist = 15
        
    def attack(self, enemy):
        damage = (self.attack + 10) - enemy.defense
        enemy.hp = enemy.hp - damage
        return enemy.hp

    #def laserEye(self, enemy):
        #self.cooldown += 1
        #damage = (self.attack + 15) - enemy.resistance
        #enemy.hp = enemy.hp - damage
        #enemy.resitance = enemy.resistance - 5
        #print("Golems laser eye lowered you defense by 4!")
        #return enemy

class dragon(entity):
    def __init__(self):
        super().__init__(random.randint(30, 40), random.randint(30, 50),
                             random.randint(4, 6), random.randint(3, 6),
                             random.randint(3, 5), random.randint(100, 150),
                        cooldown = 0, experience = random.randint(20, 25))
        self.class_name = "Dragon"
        #self.damageResist = 20
        #self.regeneration = 20

    def attack(self, enemy):
        damage = (self.attack + 20) - enemy.defense
        enemy.hp = enemy.hp - damage
        return enemy.hp

    #def fireBreath(self, enemy):
        #self.cooldown += 3
        #damage = (self.attack + 50) - enemy.resistance
        #enemy.hp -= damage
        #return enemy.hp

#Monster class creates a random monster from the ones we have above... i couldnt figure out a better way to randomize level stuff for battle & also make battle calling make sense
#this causes an error on start, i had it working but it required basically copy and pasting everything from the already defined classes above
#and surely there is a more efficient way to handle that
class monster(entity):
    def __init__(self):
        monster_type = random.choice(["Goblin", "Orc", "Troll", "Golem", "Dragon"])
        if monster_type == "Goblin":
            self.monster = goblin()
        elif monster_type == "Orc":
            self.monster = orc()
        elif monster_type == "Troll":
            self.monster = troll()
        elif monster_type == "Golem":
            self.monster = golem()
        elif monster_type == "Dragon":
            self.monster = dragon()

        self.class_name = self.monster.class_name
        self.attack = self.monster.attack
        self.magic = self.monster.magic
        self.defense = self.monster.defense
        self.resistance = self.monster.resistance
        self.speed = self.monster.speed
        self.hp = self.monster.hp
        self.cooldown = self.monster.cooldown
        self.experience = self.monster.experience

    def attack(self, enemy):
        damage = self.monster.attack - enemy.defense
        enemy.hp -= damage
        return enemy.hp



#TREASURE CLASSES
class object:
    def __init__(self, damage):
        self.damage = damage

        
class treasure:
    def __init__(self, newAction, healthRestore, actionRestore, newWeapon):
        self.newAction = newAction
        self.healthRestore = healthRestore
        self.actionRestore = actionRestore
        self.newWeapon = newWeapon


class Battle:
    def __init__(self, player, monster):
        self.player = player
        self.monster = monster

    def start_battle(self):
        print("A ", self.monster.class_name, "has appeared!")

        while True:
            print("\nYour HP:", self.player.hp)
            print("Monster HP:", self.monster.hp)
            print("\n1. Attack")
            print("2. Action")
            print("3. Inspect")
            print("4. Run")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.attack()
            elif choice == "2":
                self.use_action()
            elif choice == "3":
                self.inspect()
            elif choice == "4":
                self.run()
                break
            else:
                print("Invalid choice. Try again.")

            if self.check_game_over():
                break

    def attack(self):
        #added monster defense to the equation and specified monsters with damage resist
        if self.monster.class_name == "Golem" or self.monster.class_name == "Dragon":
            damage = self.player.attack + self.player.weapon.damage - self.monster.defense
            self.monster.hp -= damage
            #- self.monster.damageResist
            print("\nYour blow lands, dealing", damage, "damage to the monster. It now has", self.monster.hp,"HP, nice shot!")
        else:
            damage = self.player.attack + self.player.weapon.damage - self.monster.defense
            self.monster.hp -= damage
            print("\nYour blow lands, dealing", damage, "damage to the monster. It now has", self.monster.hp,"HP, nice shot!")

        if self.monster.hp >= 0:
            playerDamageFelt = (self.monster.attack - self.player.defense)
            self.player.hp -= playerDamageFelt
            print("\nThe", self.monster.class_name, "stikes you, dealing", playerDamageFelt, "damage to you. You have", self.player.hp, "HP remaining, be careful!")

        elif self.monster.hp <= 0:
            print(f"The {self.monster.class_name} has been slain, outstanding work!")

    def use_action(self):
        if self.player.actions_remaining <= 0:
            print("You have no action uses remaining.")
            return

        damage = self.player.attack + self.player.weapon.damage + self.player.action_power
        self.monster.hp -= damage
        print("You used an action and dealt", damage, "damage to the monster. It now has ", self.monster.hp, "HP.")

        self.player.actions_remaining -= 1

        if self.monster.hp <= 0:
            print("Congratulations! You defeated the monster.")

    def inspect(self):
        print("\nMonster Name:", self.monster.class_name)
        print("Monster HP:", self.monster.hp)
        print("Monster Actions:", self.monster.actions)
        print("Monster Stats: Attack =", self.monster.attack, "Defense =", self.monster.defense)

    def run(self):
        flee_chance = 30  # Percentage chance to flee - we can work in how to have speeed or something interact with this

        if random.randint(1, 100) <= flee_chance:
            print("You successfully fled from the battle.")
        else:
            print("You failed to flee and must continue the battle.")

    def check_game_over(self):
        if self.player.hp <= 0:
            print("Game over! You were defeated.")
            return True
        elif self.monster.hp <= 0:
            self.player.gain_experience(self.monster.experience)
            return True

        return False
