# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests
import json

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        dict_result = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}')
        dict_result = json.loads(dict_result.content)
        if not dict_result.get('found') or not word:
            return False
        return word == self.grid
