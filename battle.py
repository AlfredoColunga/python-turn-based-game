import os
from player import Player
from enemy import Enemy


class Battle:
    def __init__(self):
        self.player = Player()
        self.enemies = [Enemy() for _ in range(5)] # Create 5 enemies
        self.current_enemy_index = 0


    @property
    def current_enemy(self):
        if self.current_enemy_index < len(self.enemies):
            return self.enemies[self.current_enemy_index]
        return None


    def _clear_terminal(self):
        """Clean the terminal basen on the user's operating system."""
        if os.name == "nt":
            os.system("cls") # Windows
        else:
            os.system("clear") # Unix/Linux/Mac


    def _display_intro(self) -> None:
        """Print the intro messages to the terminal."""
        print(f"All your companions have died at the hands of {len(self.enemies)} enemies who broke into the wizard tower.")
        print("Lady Elianor, the plump, furry cat who leads the wizard clan, has given you only one order: Kill them all.\n")


    def _display_ending(self, player_is_alive: bool) -> None:
        """Print the ending messages to the terminal."""
        if player_is_alive:
            print("You have successfully protected Lady Elianor and the tower.")
        else:
            print("You died!\n")
            print("The enemies have reached Lady Elianor and have taken the tower.")


    def _advance_to_next_enemy(self) -> bool:
        """
        Advance the current enemy pointer to the next enemy.

        Returns:
            bool: True if successfully advanced to a next enemy,
                  False if already at the last enemy.
        """
        if self.current_enemy_index < len(self.enemies) - 1:
            self.current_enemy_index += 1
            return True
        return False


    def run(self) -> None:
        self._clear_terminal()
        self._display_intro()

        while self.player.player_is_alive and self.current_enemy:
            # Player's turn
            self.player.attack(self.current_enemy)
            print("")

            # Check if the current enemy has been defeated
            if not self.current_enemy.enemy_is_alive:
                if self._advance_to_next_enemy():
                    print("The next enemy is approaching you...\n")
                    continue
                else:
                    print("You have defeated all the enemies!")
                    break

            # Enemy's turn
            if self.current_enemy.enemy_is_alive:
                self.current_enemy.attack(self.player)

            # Check if the player has been defeated
            if not self.player.player_is_alive:
                break


        self._display_ending(self.player.player_is_alive)