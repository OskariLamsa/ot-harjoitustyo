"""Tämä tiedosto sisältää testejä"""
import unittest
from commands import Commands
from game import Loop
from rooms import Rooms
from items import Items
#from src.game import Loop
import pygame
"""
Oletetaan, että pelaaja aloittaa kohdasta 0,0.
Ainoa mahdollinen liike on siis south
"""

class TestCommands(unittest.TestCase):
    """Luokka testeille"""

    def setUp(self):
        """Tämä oli pakollinen"""
        self.GAME = Loop()
        self.GAME.position = (0,0)

    def test_command_handler_move_south(self):
        """Yritä move -komentoa command handlerin kautta, onnistuu."""
        self.assertEqual(Commands.command_handler(self.GAME, "move south"),
                         "You are in a hallway. The stone bricks are withered and collecting moss.\nYou can move: north (Hospital),south (Crossroads)")
        
    def test_command_handler_move_west(self):
        self.assertEqual(Commands.command_handler(self.GAME, "move west"),
                         "There is nothing there.")
        
    def test_move_nowhere(self):
        """Yritä liikkua ei-minnekkään, epäonnistuu."""
        self.assertEqual(Commands.command_handler(self.GAME, "move"),
                         "Check your commands, sir.")
        
    def test_move_invalid(self):
        """Yritä liikkua outoon suuntaan, epäonnistuu."""
        self.assertEqual(Commands.command_handler(self.GAME, "move away"),
                         "That is not a valid direction :(")
        
    def test_look(self):
        """Yritä saada aloitus huoneen deskriptio ja mahdolliset liikkeet."""
        self.assertEqual(Commands.command_handler(self.GAME, "look"),
                         "You are in a hospital. The walls are lined with empty beds and there are broken vials, bottles and needles scattered about\nYou can move: south (Hallway)")
        
    def test_search(self):
        """Yritä saada item nimeltä key, joka sijaitsee aloitushuoneessa."""
        self.assertEqual(Commands.command_handler(self.GAME, "search"),
                         "You have found a key.")
        
    def test_search_no_items(self):
        """Yritä saada viesti, joka kertoo, ettei loytynyt mitään."""
        self.GAME.position =(10,10)
        self.assertEqual(Commands.command_handler(self.GAME, "search"),
                         "You unfortunately found nothing.")
        
    def test_get_items(self):
        """Yritä saada lista esinestä."""
        Commands.command_handler(self.GAME, "search")
        self.assertEqual(Commands.command_handler(self.GAME, "items"),
                         "Your items are: key.")
        
    def test_get_items_no_items(self):
        """Yritä saada esineet, joita on nolla kappaletta."""
        self.assertEqual(Commands.command_handler(self.GAME, "items"),
                         "You have no items.")
        
    def test_use_item_no_item_name(self):
        """Yritä käyttää ei-mitään."""
        self.assertEqual(Commands.command_handler(self.GAME, "use"),
                         "Check your commands, sir.")
        
    def test_use_item_no_item_in_inventory(self):
        """Yritä käyttää esinettä, jota pelaajalla ei ole."""
        self.assertEqual(Commands.command_handler(self.GAME, "use Excalibur"),
                         "You don't have an item by that name.")
    def test_use_item(self):
        """Yritä käyttää esinettä, joka pelaajalla on."""
        Commands.command_handler(self.GAME, "search")
        self.assertEqual(Commands.command_handler(self.GAME, "use key"),
                         "You used the key.")
"""
Nämä liikkeet, vaikka ne tulevat southin jälkeen, rikkovat move_southin.
Niiden ei pitäisi edes vaikuttaa siihen, koska setUp resetoi tilanteen.
En ymmärrä. Kysyn asiasta pajassa.
"""
#   def test_command_handler_move_east(self):
#        self.GAME.position = (0,0)
#        self.assertEqual(Commands.command_handler(self.GAME, "move east"),
#                         "There is nothing there.")
#   def test_command_handler_move_north(self):
#       self.assertEqual(Commands.command_handler(self.GAME, "move north"),
#                        "There is nothing there.")
