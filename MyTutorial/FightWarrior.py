import random
import math


class Warrior:
    def __init__(self, name="warrior", health=0, attack_max=0, block_max=0):
        self.name = name
        self.health = health
        self.attack_max = attack_max
        self.block_max = block_max

    def attack(self):
        attack_amt = self.attack_max * (random.random() + .5)
        return attack_amt

    def block(self):
        block_amt = self.block_max * (random.random() + .5)
        return block_amt


class Battle:
    def start_fight(self, warrior1, warrior2):
        while True:
            if self.get_attack_result(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.get_attack_result(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break

    @staticmethod
    def get_attack_result(warriorA, warriorB):
        warrior_a_attack_amt = warriorA.attack()
        warrior_b_block_amt = warriorB.block()
        damage_2_warrior_b = math.ceil(warrior_a_attack_amt - warrior_b_block_amt)
        warriorB.health -= damage_2_warrior_b
        print("{} attacks {} and deals {} damage".format(warriorA.name, warriorB.name, damage_2_warrior_b))
        print("{} is down to {} health".format(warriorB.name, warriorB.health))
        if warriorB.health <= 0:
            print("{} has died and {} is victorious".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight Again"


def main():
    thor = Warrior("Thor", 50, 20, 10)
    loki = Warrior("Loki", 50, 20, 10)
    battle = Battle()
    battle.start_fight(thor, loki)


main()

