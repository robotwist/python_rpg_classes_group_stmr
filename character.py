class Character:
    def __init__(self, name, health, level=1):
        self.name = name
        self.max_health = health
        self.health = health
        self.level = level
        self.equipped_weapon = None  # Add this to track equipped weapon

    def is_alive(self):
        """Check if still alive"""
        return self.health > 0
    
    def take_damage(self, damage):
        """Reduce Health by damage amount report result"""
        self.health = max(0, self.health - damage)
        if self.health == 0:
            return f"{self.name} takes {damage} damage and falls to his own demise!"
        else:
            return f"{self.name} takes {damage} damage and is now at {self.health} health!"
    def heal(self, amount):
        """Heal the character by the given amount.
        
        Args:
            amount (int): The amount to heal
            
        Returns:
            str: Description of the healing done
        """
        self.health = min(self.max_health, self.health + amount)
        return f"{self.name} heals for {amount}. Health is now {self.health}"
    
    def equip_weapon(self, weapon_name):
        """Equip a weapon by name.
        
        Args:
            weapon_name (str): The name of the weapon to equip
            
        Returns:
            str: Description of the weapon being equipped
        """
        self.equipped_weapon = weapon_name
        return f"{self.name} equips {weapon_name}!"
    
    def __str__(self):
        """Return a string representation of the character."""
        weapon_info = f", wielding {self.equipped_weapon}" if self.equipped_weapon else ""
        return f"{self.name} (Lvl {self.level}) - HP: {self.health}/{self.max_health}{weapon_info}" 