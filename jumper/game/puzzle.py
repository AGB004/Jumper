import random


class Puzzle:
    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self.word_list = ["smile", "laugh", "funny"]
        self._word_selected = ""
        self._word_guess = ["_ "] * len(self._word_selected)
        self.letter_guess = ""
       
    def _select_word(self):
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        self._word_selected = random.choice(self._word_list)

    def draw_word_guess(self):
        """Moves to the given location.

        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        pass

    def process_guess(self, guess_letter):
        """
        
        """
        self.letter_guess = guess_letter

    def can_keep_guessing(self):
        """
        
        """
        pass
