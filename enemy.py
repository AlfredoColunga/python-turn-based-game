import random


class Enemy():
    MIN_DAMAGE = 1
    MAX_DAMAGE = 100

    def __init__(self):
        self._is_alive = True
        self._paranoid_effect = False
        self._retrogression_effect = False


    @property
    def enemy_is_alive(self) -> bool:
        """Check if the enemy is alive."""
        return self._is_alive

    @property
    def has_paranoid_effect(self) -> bool:
        """Check if the enemy has the "Paranoid" effect active."""
        return self._paranoid_effect

    @property
    def has_retrogression_effect(self) -> bool:
        """Check if the enemy has the "Retrogression" effect active."""
        return self._retrogression_effect


    def apply_paranoid_effect(self) -> None:
        """Apply the "Paranoid" effect to the enemy."""
        self._paranoid_effect = True


    def apply_retrogression_effect(self) -> None:
        """Apply the "Retrogression" effect to the enemy."""
        self._retrogression_effect = True


    def enemy_die(self) -> None:
        """Kill the enemy."""
        self._is_alive = False


    def _calculate_damage(self, player) -> int:
        """
        Calculate the damage the enemy will do in his next attack.

        Returns:
            int: 0 if the "Retrogression" effect is active,
                 100 if the player has the "Retrogression" effect active or a
                 pseudo-random number between 1 and 100.
        """
        if self._retrogression_effect:
            return 0

        if player.has_denial_effect:
            return self.MAX_DAMAGE

        return random.randint(self.MIN_DAMAGE, self.MAX_DAMAGE)


    def _can_attack(self) -> bool:
        """Check if the enemy can attack basen on his paranoid effect."""
        return not self._paranoid_effect


    def _reset_retrogression_effect(self) -> None:
        """Reset the retrogression effect if it is active."""
        if self._retrogression_effect:
            self._retrogression_effect = False


    def attack(self, player) -> None:
        """Attack the player."""
        if self._can_attack():
            damage = self._calculate_damage(player)

            print(f"The enemy has attacked you with {damage} points of damage.\n")
            player.take_damage(damage)
        else:
            print("The enemy cannot attack you, but you still have to destroy him.\n")


        self._reset_retrogression_effect()