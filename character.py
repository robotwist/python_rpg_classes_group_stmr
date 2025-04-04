class Character:
    def __init__(self, name, health, mana=50, level=1):
        self.name = name
        self.max_health = health
        self.health = health
        self.max_mana = mana
        self.mana = mana
        self.level = level
        self.equipped_weapon = None  # Track equipped weapon
        self.gold = 0  # Gold for shopping
        self.inventory = []  # Inventory for items
        self.known_spells = []  # Spells the character knows

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
        original_health = self.health
        self.health = min(self.max_health, self.health + amount)
        actual_healing = self.health - original_health
        return f"{self.name} heals for {actual_healing}. Health is now {self.health}/{self.max_health}"
    
    def equip_weapon(self, weapon_name):
        """Equip a weapon by name.
        
        Args:
            weapon_name (str): The name of the weapon to equip
            
        Returns:
            str: Description of the weapon being equipped
        """
        self.equipped_weapon = weapon_name
        return f"{self.name} equips {weapon_name}!"
    
    def learn_spell(self, spell):
        """Learn a new spell.
        
        Args:
            spell: The spell to learn
            
        Returns:
            str: Description of learning the spell
        """
        self.known_spells.append(spell)
        return f"{self.name} learns {spell.name}!"
    
    def cast_spell(self, spell_name, target):
        """Cast a known spell on a target.
        
        Args:
            spell_name (str): The name of the spell to cast
            target: The target of the spell
            
        Returns:
            str: Result of casting the spell
        """
        # Find the spell by name
        spell = next((s for s in self.known_spells if s.name == spell_name), None)
        
        if not spell:
            return f"{self.name} doesn't know the spell {spell_name}!"
        
        # Check if enough mana
        if self.mana < spell.mana_cost:
            return f"{self.name} doesn't have enough mana to cast {spell_name}!"
        
        # Deduct mana and cast the spell
        self.mana -= spell.mana_cost
        result = spell.cast(self, target)
        
        return result
    
    def use_item(self, item_name):
        """Use an item from the inventory.
        
        Args:
            item_name (str): The name of the item to use
            
        Returns:
            str: Result of using the item
        """
        # Find the item by name
        item = next((i for i in self.inventory if i.name == item_name), None)
        
        if not item:
            return f"{self.name} doesn't have {item_name} in inventory!"
        
        # Use the item
        result = item.use(self)
        
        # Remove consumable items after use (like potions)
        if hasattr(item, 'effect_type'):  # It's a potion
            self.inventory.remove(item)
            
        return result
    
    def attack(self, target):
        """Attack a target with the equipped weapon.
        
        Args:
            target: The target to attack (Monster or Character)
            
        Returns:
            str: Result of the attack
        """
        # Check if we have a weapon equipped
        if not self.equipped_weapon:
            base_damage = 5  # Default unarmed damage
            attack_text = f"{self.name} attacks with bare hands"
        else:
            # Find the equipped weapon in inventory
            weapon = next((item for item in self.inventory if item.name == self.equipped_weapon and hasattr(item, 'damage')), None)
            
            if weapon:
                base_damage = weapon.damage
                attack_text = f"{self.name} attacks with {self.equipped_weapon}"
            else:
                # Weapon name is set but not found in inventory
                base_damage = 5  # Default unarmed damage
                attack_text = f"{self.name} attacks with {self.equipped_weapon}"
        
        # Add level bonus
        damage = base_damage + (self.level - 1) * 2
        
        # Apply critical hit chance (10% chance)
        import random
        if random.random() < 0.1:  # 10% chance
            damage = int(damage * 1.5)
            attack_text += " (Critical Hit!)"
            
        # Apply damage based on target type
        if hasattr(target, 'take_damage'):  # Character object
            result = target.take_damage(damage)
            return f"{attack_text} for {damage} damage! {result}"
        elif hasattr(target, 'health'):  # Monster object
            target.health -= damage
            result = f"{attack_text} for {damage} damage!"
            if target.health <= 0:
                result += f" {target.monster_type} has been defeated!"
            else:
                result += f" {target.monster_type} health: {target.health}"
            return result
        else:
            return f"{attack_text}, but it has no effect!"
    
    def __str__(self):
        """Return a string representation of the character."""
        weapon_info = f", wielding {self.equipped_weapon}" if self.equipped_weapon else ""
        return f"{self.name} (Lvl {self.level}) - HP: {self.health}/{self.max_health} - MP: {self.mana}/{self.max_mana}{weapon_info}" 