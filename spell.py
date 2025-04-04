from character import Character
from monster import Monster

class Spell:
    """A magical spell that can deal damage and optionally apply a special effect."""
    def __init__(self, name, damage, mana_cost=0, effect=None):
        self.name = name
        self.damage = damage
        self.mana_cost = mana_cost
        self.effect = effect  # Optional: e.g., 'burn', 'freeze'
    
    def cast(self, caster, target):
        """Cast the spell from a character to a target.
        
        Args:
            caster: The character casting the spell
            target: The target of the spell (Character or Monster)
            
        Returns:
            str: Result of casting the spell
        """
        # Handle damage based on target type
        if hasattr(target, 'take_damage'):  # Character object
            result = target.take_damage(self.damage)
            effect_msg = f" {target.name} is affected by {self.effect}!" if self.effect else ""
            return f"{caster.name} casts {self.name} on {target.name}!{effect_msg} {result}"
        elif hasattr(target, 'health'):  # Monster object
            target.health -= self.damage
            effect_msg = f" {target.monster_type} is affected by {self.effect}!" if self.effect else ""
            return f"{caster.name} casts {self.name} on {target.monster_type} for {self.damage} damage!{effect_msg}"
        else:
            return f"{caster.name} casts {self.name}, but it has no effect!"
    
    def __str__(self):
        effect_info = f", Effect: {self.effect}" if self.effect else ""
        return f"Spell: {self.name} (Damage: {self.damage}, Mana: {self.mana_cost}{effect_info})"

# Example usage if this script is run directly
if __name__ == "__main__":
    # Import necessary classes for testing
    from character import Character
    
    # Create a character and a spell
    wizard = Character("Gandalf", 100)
    fireball = Spell("Fireball", 30, mana_cost=15, effect="burn")
    
    # Create a target
    goblin = Monster("Goblin", 50)
    
    # Cast the spell
    result = fireball.cast(wizard, goblin)
    print(result)
    print(f"Goblin health after spell: {goblin.health}")