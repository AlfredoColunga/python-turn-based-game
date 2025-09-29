import random


class Spell:
    DEFAULT_SUCCESS_RATE = 0.5
    MIN_SUCCESS_RATE = 0.1
    MAX_SUCCESS_RATE = 0.9
    SUCCESS_INCREMENT = 0.1
    FAILURE_DECREMENT = 0.1

    def __init__(
            self,
            name: str,
            cast_msg: str,
            success_msg: str,
            failure_msg: str,
            hands_required: bool = False,
            mouth_required: bool = False
    ):
        self.name = name
        self.cast_msg = cast_msg
        self.success_msg = success_msg
        self.failure_msg = failure_msg
        self.hands_required = hands_required
        self.mouth_required = mouth_required

        self.success_rate = self.DEFAULT_SUCCESS_RATE


    def _update_success_rate(self, success: bool) -> None:
        """Update the success rate based on the spell result."""
        if success:
            self.success_rate = min(
                self.MAX_SUCCESS_RATE,
                self.success_rate + self.SUCCESS_INCREMENT
            )
        else:
            self.success_rate = max(
                self.MIN_SUCCESS_RATE,
                self.success_rate - self.FAILURE_DECREMENT
            )


    def _print_cast_result(self, success: bool) -> None:
        """Print the cast and output message based on the spell output."""
        print(f"{self.cast_msg}\n")
        if success:
            print(self.success_msg)
        else:
            print(self.failure_msg)


    def calculate_cast_success(self) -> bool:
        """
        Cast a spell and returns if it was successful.

        Generate a pseudo-random number between 0.0 and 1.0

        Returns:
            bool: True if the cast was successful,
                  False if the cast was unsuccessful.
        """
        success = random.random() <= self.success_rate

        self._update_success_rate(success)
        self._print_cast_result(success)


        return success
