"""Tämä tiedosto sisältää testejä"""
import unittest
from commands import Commands
import pygame

class TestCommands(unittest.TestCase):
    """Luokka testeille"""

    def setUp(self):
        """Tämä oli pakollinen"""

    def test_move(self):
        """Yritä move -komentoa"""
        self.assertEqual(Commands.move("west"),
                         "This is where you would move west!")

    def test_command_handler_move(self):
        """Yritä move -konmentoa command handlerin kautta"""
        self.assertEqual(Commands.command_handler("move west"),
                         "This is where you would move west!")
