import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]
        self.name = name

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        self.hp = max(0, self.hp)

    def heal(self, heal):
        self.hp += heal
        self.hp = min(self.hp, self.maxhp)

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost
        self.mp = max(0, self.mp)

    def choose_action(self):
        i = 1
        print("\n" + "\t" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "\tACTIONS" + bcolors.ENDC)
        for item in self.actions:
            print("\t\t", str(i) + ".", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "\tMAGIC" + bcolors.ENDC)
        for spell in self.magic:
            print("\t\t", str(i) + ".", spell.name, "(cost:", str(spell.cost) + ")")
            i += 1

    def choose_item(self):
        i = 1

        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "\tITEMS" + bcolors.ENDC)
        for item in self.items:
            print("\t\t", str(i) + ".", item["item"].name + ":", item["item"].description,
                  " (x" + str(item["quantity"]) + ")")
            i += 1


    def get_stats(self):
        print("\t\t\t\t\t   _________________________\t\t\t   __________")
        print(bcolors.BOLD + self.name + "\t\t"
              + str(self.hp) + "/" + str(self.maxhp) + " |" + bcolors.OKGREEN + "██████████               " + bcolors.ENDC + bcolors.BOLD + "|\t\t"
              + str(self.mp) + "/" + str(self.maxmp) + " |" + bcolors.OKBLUE + "██████████" + bcolors.ENDC + "|")