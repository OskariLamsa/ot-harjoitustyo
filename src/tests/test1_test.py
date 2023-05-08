"""Tämä tiedosto sisältää testejä"""
import unittest
import os
from commands import Commands
from game import Loop
from rooms import Rooms
from items import Items
from interface import Io
import random
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
        Handler = Commands(self.GAME)
        print(self.GAME.items[0])
        print(self.GAME.rooms[0])
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
    def test_use_key_west(self):
        Commands.command_handler(self.GAME, "search")
        self.GAME.position = (2,-1)
        self.assertEqual(Commands.command_handler(self.GAME, "use key"),
                         "You used the key to unlock the Bathroom")
    def test_use_key_east(self):
        Commands.command_handler(self.GAME, "search")
        self.GAME.position = (2,-3)
        self.assertEqual(Commands.command_handler(self.GAME, "use key"),
                         "You used the key to unlock the Bathroom")
    def test_use_key_north(self):
        Commands.command_handler(self.GAME, "search")
        self.GAME.position = (3,-2)
        self.assertEqual(Commands.command_handler(self.GAME, "use key"),
                         "You used the key to unlock the Bathroom")
    def test_use_key_south(self):
        Commands.command_handler(self.GAME, "search")
        self.GAME.position = (1,-2)
        self.assertEqual(Commands.command_handler(self.GAME, "use key"),
                         "You used the key to unlock the Bathroom")
    def test_command_handler_move_east(self):
        self.GAME.position = (0,0)
        self.assertEqual(Commands.command_handler(self.GAME, "move east"),
                            "There is nothing there.")

    def test_command_handler_move_north(self):
        self.assertEqual(Commands.command_handler(self.GAME, "move north"),
                         "There is nothing there.")
    def test_move_to_locked(self):
        self.GAME.position = (2,-1)
        self.assertEqual(Commands.command_handler(self.GAME, "move west"),
                         "That room is locked!")
    def test_attack_nothing(self):
        self.assertEqual(Commands.command_handler(self.GAME, "attack"),
                         "There are no enemies to attack.")
    def test_attack(self):
        "Lyo ja osu."
        random.seed(10)
        Commands.combat_start(self.GAME)
        self.assertEqual(Commands.command_handler(self.GAME, "attack"),
                         "You hit the goblin\nThe goblin hits you for 2 damage!")
    def test_attack_miss(self):
        "lyo ja huido ohi."
        random.seed(11)
        Commands.combat_start(self.GAME)
        self.assertEqual(Commands.command_handler(self.GAME, "attack"),
                         "You miss.\nThe ghost attacks you, but misses!")
    def test_invalid_two_part_input(self):
        "Varoita pelaajaa järjettomästä inputista."
        self.assertEqual(Commands.command_handler(self.GAME, "kaksi sanaa"),
                         "Check your commands, sir.")
    def test_potion(self):
        "Yritä käyttää potion-esinettä."
        self.GAME.position = (1,0)
        Commands.command_handler(self.GAME, "search")
        self.assertEqual(Commands.command_handler(self.GAME, "use potion"),
                         "You have healed for 4 health!")
    def test_no_escape(self):
        "Yritä paeta tappelusta. epäonnistu."
        random.seed(11)
        Commands.combat_start(self.GAME)
        self.GAME.in_combat = 1
        self.assertEqual(Commands.command_handler(self.GAME, "move south"),
                         "But you couldn't get away!\nThe ghost attacks you, but misses!")
    def test_escape(self):
        "Yritä paeta tappelusta. Onnistuu."
        random.seed(7)
        Commands.combat_start(self.GAME)
        self.GAME.in_combat = 1
        self.assertEqual(Commands.command_handler(self.GAME, "move south"),
                         "You managed to flee!\nYou are in a hallway. The stone bricks are withered and collecting moss.\nYou can move: north (Hospital), south (Crossroads)")
    def test_invalid_enemy_attack(self):
        "Väärän niminen vihollinen hyokkää. Mitään ei tapahdu."
        Commands.combat_start(self.GAME)
        self.assertEqual(Commands.enemy_attack(self.GAME, "Petteri"),
                         None)
    def test_defeat_the_enemies(self):
        "Päihitä vihollinen."
        random.seed(10)
        Commands.combat_start(self.GAME)
        Commands.command_handler(self.GAME, "attack")
        Commands.command_handler(self.GAME, "attack")
        Commands.command_handler(self.GAME, "attack")
        self.assertEqual(Commands.command_handler(self.GAME, "attack"),
                         "You hit and defeat the goblin and find 46 money!")
    def test_ambush(self):
        "Vihollinen hyokkää."
        self.GAME.combat_chance = 100
        random.seed(10)
        self.assertEqual(Commands.command_handler(self.GAME, "move south"),
            "You are in a hallway. The stone bricks are withered and collecting moss.\nYou have been ambushed by a goblin!")
    def test_save(self):
        "Tallenna peli"
        self.assertEqual(self.GAME.save(),
                         None)
   # def test_events(self):
    #    "Testaa events"
     #   pygame.init()
      #  IO = Io(self.GAME)
       # IO.update_screen()
        #self.assertEqual(self.GAME.events(),
         #                None)