from spells import Spell


class Player():
    MAX_HEALTH = 100

    def __init__(self):
        self._health = self.MAX_HEALTH
        self._hands_status = True
        self._mouth_status = True
        self._spells = self._initialize_spells()
        self._spell_lookup = {spell.name: spell for spell in self._spells}


    def _initialize_spells(self):
        return [
            Spell(name="Agony",
                  cast_msg="You have performed a forbidden hand movement...",
                  success_msg="The enemy has split in two, and you have seen his soul slowly leave his body.",
                  failure_msg="Your hands have been destroyed. You can see your broken bones sticking out of your flesh. You will never be able to use your hands again.",
                  hands_required=True),
            Spell(name="Cadaver",
                  cast_msg='You have uttered a curse: "Arise, O sacred bones, arise! May the stony God rend the life from this body and swell his flesh with pestilence!"...',
                  success_msg="The enemy has fallen dead.",
                  failure_msg="Your mouth has rotted. You will never be able to speak again.",
                  mouth_required=True),
            Spell(name="Denial",
                  cast_msg="You have turned an hourglass of ashes...",
                  success_msg="Your health has been restored.",
                  failure_msg="Your health has been restored, but the ashes have revealed that you will not pass this foe.",
                  hands_required=True),
            Spell(name="Paranoid",
                  cast_msg="Your silver ring has sparkled after you performed a hand movement...",
                  success_msg="The enemy has become an inanimate object and will no longer be able to attack you.",
                  failure_msg="You have become a talking vase. You will never be able to use your hands again, but your voice can still be heard.",
                  hands_required=True),
            Spell(name="Retrogression",
                  cast_msg='You have recited an ancient poem backwards: "nrolrof enots elprup a egasiv htiw erehps a ecnelis ni htenrut fohnurdsorF nettogrof"...',
                  success_msg="The ancient planet is pleased and has rewarded you: The enemy's next attack will not cause damage.",
                  failure_msg="You have sung with all your might, but no one has heard you.",
                  mouth_required=True)
        ]


    @property
    def player_is_alive(self) -> bool:
        """Checks if the player is alive."""
        return self._health > 0


    @property
    def _hands_available(self) -> bool:
        """Checks if the player's hands are available."""
        return self._hands_status == True


    @property
    def _mouth_available(self) -> bool:
        """Checks if the player's mouth is available."""
        return self._mouth_status == True


    def _disable_hands(self) -> None:
        """Sets the player's hands to 'False'."""
        self._hands_status = False


    def _disable_mouth(self) -> None:
        """Sets the player's mouth to 'False'."""
        self._mouth_status = False


    def _restore_health(self) -> None:
        """Restores the player's health to maximum."""
        self._health = self.MAX_HEALTH


    def take_damage(self, damage: int) -> None:
        """Applies damage to the player"""
        if self.player_is_alive:
            self._health = max(0, self._health - damage)

            if self._health <= 0:
                self._player_die()


    def _player_die(self) -> None:
        """Kills the player."""
        self._health = 0
        print("You died!")


    def _get_spell_by_name(self, spell_name: str) -> Spell:
        """Returns a spell searched by its name."""
        return self._spell_lookup.get(spell_name)


    def _can_cast_spell(self, spell: Spell) -> bool:
        """
        Checks if the player can cast a specific spell.

        Returns:
            bool: True if the player's hands or mouth are available,
                  False if the player's hands or mouth are unavailable.
        """
        if spell.hands_required and not self._hands_available:
            print(f'You could not cast "{spell.name}" because you cannot use your hands.')
            return False

        if spell.mouth_required and not self._mouth_available:
            print(f'You could not cast "{spell.name}" because you cannot use your mouth.')
            return False

        return True


    def _apply_spell_effect(self, enemy, spell_name: str, success: bool) -> None:
        """Applies the effect of a spell based on its result."""
        if spell_name == "Agony":
            if success == True:
                enemy.enemy_die()
            else:
                self._disable_hands()

        if spell_name == "Cadaver":
            if success == True:
                enemy.enemy_die()
            else:
                self._disable_mouth()

        if spell_name == "Denial":
            if success == True:
                self._restore_health()
            else:
                self._player_die()

        if spell_name == "Paranoid":
            if success == True:
                enemy.apply_paranoid_effect()
            else:
                self._disable_hands()

        if spell_name == "Retrogression" and success == True:
            enemy.apply_retrogression_effect()


    def _view_spells(self) -> None:
        print("===< Known Spells >===")
        for spell in self._spells:
            print(f"{spell.name} -- Success rate: {int(spell.success_rate * 100)}%")


    def _view_current_health(self) -> None:
        title = "===< Current Health >==="
        str_health = str(self._health).center(len(title))
        print(title)
        print(str_health)


    def cast_spell(self, spell_name: str, enemy) -> bool:
        """Tries to cast a spell.

        Returns:
            bool: True if the spell could be cast (regardless of success),
                  False if the spell could not be cast.
        """
        spell = self._get_spell_by_name(spell_name)

        if not spell:
            print(f'The spell called "{spell_name}" is beyond your knowledge.')
            return False

        if not self._can_cast_spell(spell):
            return False

        success = spell.calculate_cast_success()
        self._apply_spell_effect(enemy, spell.name, success)
        return True


    def attack(self, enemy) -> None:
        """Allows the player to attack the enemy."""
        self._view_current_health()
        self._view_spells()

        spell_input = input("Write your attack: ").capitalize().strip()
        print("")

        self.cast_spell(spell_input, enemy)