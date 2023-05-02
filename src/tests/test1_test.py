"""Tämä tiedosto sisältää testejä"""
import unittest
import os
from commands import Commands
from game import Loop
from rooms import Rooms
from items import Items
from interface import Io
import pygame
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
__location__ = __location__[0:-6] 
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
        self.GAME.delete_save()

        """
        Tämä ei toimi. Se luo save tiedoston, jotta se voi yrittää pelin mahdollisuutta
        lukea save tiedostoja. Konstruktroi antaa virhettä. Hassua on se, että jos ottaa pois päältä
        tuon self.GAME.delete_save() osan setUpissa, niin tämän testin luoma save tiedosto jää
        src kansioon. Pelin voi käynnistää, ja huomata, miten sen konstruktori luki tämän funktion
        luoman save tiedoston oikein.
    def test_save_file_read(self):
        pygame.init()
        with open(os.path.join( __location__, 'save.csv'), "w", encoding="utf-8") as save_file:
            save_file.write("10;(0, 0);['key', 'potion']")
            self.GAME2 = Loop()
            print(self.GAME2.player_items)
        """
    def test_IO(self):
        pygame.init()
        IO = Io(self.GAME)
        IO.update_screen()
    def test_command_handler_move_south(self):
        """Yritä move -komentoa command handlerin kautta, onnistuu."""
        self.assertEqual(Commands.command_handler(self.GAME, "move south"),
                         "You are in a hallway. The stone bricks are withered and collecting moss.\nYou can move: north (Hospital), south (Crossroads)")
        
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
        
    def test_use_item_wrong(self):
        """Yritä käyttää esinettä, jota pelaajalla ei ole."""
        self.assertEqual(Commands.command_handler(self.GAME, "use Excalibur"),
                         "You don't have an item by that name.")
    def test_use_key_wrong(self):
        """Yritä käyttää avainta, väärä paikka."""
        Commands.command_handler(self.GAME, "search")
        self.assertEqual(Commands.command_handler(self.GAME, "use key"),
                         "Nothing to unlock here.")
    def test_command_handler_move_east(self):
        self.GAME.position = (0,0)
        self.assertEqual(Commands.command_handler(self.GAME, "move east"),
                            "There is nothing there.")

    def test_command_handler_move_north(self):
        self.assertEqual(Commands.command_handler(self.GAME, "move north"),
                         "There is nothing there.")
