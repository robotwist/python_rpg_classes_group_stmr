import random

dialog = {
    'initiate_battle': [
        "As you press on, a fearsome {monster} materializes from the gloom!",
        "You turn towards a shadowy figure, and as the light hits it, you see a {monster}, eyes glowing with malice.",
        "You ready your weapon, preparing for the confrontation ahead.",
        "The air thickens with tension as the {monster} lunges at you.",
        "You brace yourself for the battle of your life.",
        "With a triumphant cry, you charge at the {monster}, your weapon raised high.",
        "The {monster} roars, ready to strike."
    ],
    'monster_attack': [
        "The {monster} lunges at you, its claws slashing through the air.",
        "You dodge to the side, narrowly avoiding its deadly strike.",
        "The {monster} snarls, its eyes burning with fury.",
        "It lunges again, but you are ready this time.",
        "You counterattack, striking the {monster} with all your might."
    ],
    'player_attack': [
        "You swing your weapon, striking the {monster} with a powerful blow.",
        "The {monster} howls in pain, staggering back from the force of your attack.",
        "You press the advantage, launching a flurry of strikes.",
        "With each blow, you feel the tide of battle turning in your favor.",
        "The {monster} roars in defiance, but you are undeterred."
    ]
}

class Battle:
    def __init__(self, player_character, monster):
        self.player_character = player_character
        self.monster = monster

    def start_battle(self):
        init_msg = random.choice(dialog['initiate_battle'])
        print(init_msg.format(monster=self.monster.name, player=self.player_character.name))
        
        if self.roll_initiative():
            print(f"{self.player_character.name} seizes the initiative!")
            attacker = 'player'
        else:
            print(f"{self.monster.name} moves swiftly, claiming the initiative!")
            attacker = 'monster'
        
        while self.player_character.is_alive() and self.monster.is_alive():
            if attacker == 'player':
                self.player_attack()
                attacker = 'monster'
            else:
                self.monster_attack()
                attacker = 'player'
        
        if self.player_character.is_alive():
            print(f"With a final, resounding blow, you have vanquished the {self.monster.name}!")
            return True
        else:
            print("Defeat overwhelms you as you collapse to the cold, unyielding stone. Darkness claims your vision...")
            return False

    def roll_initiative(self):
        player_roll = random.randint(1, 20) + self.player_character.initiative
        monster_roll = random.randint(1, 20) + self.monster.initiative
        return player_roll >= monster_roll

    def monster_attack(self):
        msg = random.choice(dialog['monster_attack'])
        print(msg.format(monster=self.monster.name, player=self.player_character.name))
        self.monster.attack(self.player_character)

    def player_attack(self):
        msg = random.choice(dialog['player_attack'])
        print(msg.format(monster=self.monster.name, player=self.player_character.name))
        self.player_character.attack(self.monster)

    def __str__(self):
        return f"Battle between {self.player_character.name} and {self.monster.name}"
