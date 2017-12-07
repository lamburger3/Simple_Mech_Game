from random import randint
 
'''
Create a battle system based on d20s, with each fighter containing AC, and health, like in DND.
 
1.
There should be 3 presets for the user to choose, "Heavy Mech," "Light Mech," and "Medium Mech,"
all who contain unique stats, light having less AC and health than medium, and medium having less than heavy,
AC and health increasing by increments of twenty each preset, light starting at 30 HP and AC
 
2.
I should be able to choose my mech preset and have a message print to me telling me what i've chosen.
 
3.
I should then be given a "Light machinegun" if i've chosen light, an "Assaultcannon" if i've chosen medium,
and a "Heavy Blastcannon" if i've chosen heavy.
 
Light machinegun does 1d8 damage per hit, Assaultcannon does 1d12, and Heavy Blastcannon does a 1d20
 
4.
There should be an enemy generated the same way, but preset determined randomly between the 3
 
5.
I should be prompted to engage the enemy, while being told what i am seeing in-game
 
6.
If i choose to engage the enemy, combat ensues in turn order where the user starts first, and attack rate is based on a d20 roll that must pass enemy AC, describe every attack as it happens.
 
7.
Enemy must automatically attack after user has
 
8.
When a fighter looses, print the name of the winner of the battle.
'''
 
light_mech_weapon_name = "Light Machine Gun"
light_mech_weapon_die_size = 8
 
medium_mech_weapon_name = "Assault Cannon"
medium_mech_weapon_die_size = 12
 
heavy_mech_weapon_name = "Heavy Blast Cannon"
heavy_mech_weapon_die_size = 20
 
class Weapon():
  name = ""
  weapon_die_count = 1
  weapon_die_size = 6
  weapon_modifier = 0
 
  def __init__(self, name, size):
    self.name = name
    self.weapon_die_size = size
 
  def print_weapon_stats(self):
    print("This mech's weapon is called %s. It has the following attack roll:" % self.name)
    print("%dd%d + %d" % (self.weapon_die_count, self.weapon_die_size, self.weapon_modifier))
 
  def roll_attack_roll(self):
    return randint(1,20)
 
  def roll_damage_roll(self):
    sum_of_rolls = 0
    for x in range(0, self.weapon_die_count):
      sum_of_rolls += randint(1, self.weapon_die_size)
 
    return sum_of_rolls + self.weapon_modifier
 
light_mech_armor = 10
light_mech_health = 30
 
medium_mech_armor = 15
medium_mech_health = 50
 
heavy_mech_armor = 17
heavy_mech_health = 70
 
class Mech():
  #TODO: Add weapon
  armor = 0
  health = 0
  weapon = None
 
  def print_mech_stats(self):
    print("This mech has %d armor and %d health" % (self.armor, self.health))
    self.weapon.print_weapon_stats()
 
 
  def __init__(self, armor, health, weapon):
    self.armor = armor
    self.health = health
    #TODO: Verify that this is actually an instance of the Weapon class
    self.weapon = weapon
 
  def attack(self):
    print("The mech shoots its gun! It rolls a %d" % self.weapon.roll_attack_roll())
    print("If this hit, it hit for %d damage" % self.weapon.roll_damage_roll())
 
 
def get_random_mech():
  return get_mech_of_type(randint(1, 3))
 
def get_mech_of_type(mech_choice_number):
  if (int(mech_choice_number) == 1):
    weapon = Weapon(light_mech_weapon_name, light_mech_weapon_die_size)
    mech = Mech(light_mech_armor, light_mech_health, weapon)
 
  elif (int(mech_choice_number) == 2):
    weapon = Weapon(medium_mech_weapon_name, medium_mech_weapon_die_size)
    mech = Mech(medium_mech_armor, medium_mech_health, weapon)
 
  elif (int(mech_choice_number) == 3):
    weapon = Weapon(heavy_mech_weapon_name, heavy_mech_weapon_die_size)
    mech = Mech(heavy_mech_armor, heavy_mech_health, weapon)
  else:
    weapon = Weapon(light_mech_weapon_name, light_mech_weapon_die_size)
    mech = Mech(light_mech_armor, light_mech_health, weapon)
 
  return mech
 
'''
Ask the player to choose a type of mech.
'''
def let_player_choose_mech():
  #Show options
  print("Please choose a mech:")
  print("1. Light Mech")
  print("2. Medium Mech")
  print("3. Heavy Mech")
 
  #Get player input
  mech_choice_number = input("")
  player_mech = get_mech_of_type(mech_choice_number)
 
  return player_mech
 
'''
Main function.
Call everything else needed here.
'''
def main():
  print("Welcome to Jordan's MechBattler v 1.0!")
  player_mech = let_player_choose_mech()
 
  print("You got your mech! Here are its stats:")
  player_mech.print_mech_stats()
 
  print("You are going to fight the following mechs!")
 
  for x in range(20):
    mech = get_random_mech()
    mech.print_mech_stats()
    #TODO: Attack a specific target, and see it's armor value
    mech.attack()
 
#Start the program here
main()
