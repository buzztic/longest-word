
from longest_word.game import Game
import string
import pytest

# tests/test_game.py
class TestGame:
    def test_game_initialization(self):
            game = Game()
            grid = game.grid
            assert type(grid) == list
            assert len(grid) == 9
            for letter in grid:
                assert letter in string.ascii_uppercase

    def test_is_valid(self):
        game = Game()
        assert game.is_valid(game.grid)

    def test_is_valid(self):
        game = Game()
        invalid_word = game.grid[0:8]
        assert game.is_valid(invalid_word) == False

    def test_is_no_input(self):
        game = Game()
        assert game.is_valid('') == False

    def test_unknown_word_is_invalid(self):
        """A word that is not in the english directory should no be valid"""
        new_game = Game()
        new_game.grid = 'KWIENFUQW' # Force the grid to a test case:
        assert new_game.is_valid('KWIENFUQW') is False
