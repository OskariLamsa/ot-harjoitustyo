"""Pelin aloittava script"""
#pylint: disable=no-member
#Yllä oleva ajaa saman asian kuin whitelistaaminen, joka ei toiminut.
import os
import pygame
from commands import Commands
from rooms import Rooms
from items import Items
from interface import Io
from enemies import Enemies
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
class Loop:
    """Peli"""

    def __init__(self):
        """
        Huoneet ovat lista huone-olioita,
        Esineet ovat lista esine-olioita.
        Player_items sisältää pelaajan omistamat esineet.
        Position ilmaisee pelaajan sijainnin.
        Health pelaajan elämäpisteet
        Combat chance on mahdollisuus tappeluun
        In_combat on moodi, joka menee päälle kun taistelu alkaa.
        Yritetään ladata tietoja save.csv tiedostosta, mikäli sellainen on. 
        """
        with open(os.path.join(__location__, 'items.csv'), encoding="utf-8") as item_file:
            self.items = Items.item_decoder(self, item_file)
        with open(os.path.join(__location__, 'rooms.csv'), encoding="utf-8") as room_file:
            self.rooms = Rooms.room_decoder(self, room_file, self.items)
        with open(os.path.join(__location__, 'enemies.csv'), encoding="utf-8") as enemy_file:
            self.enemies = Enemies.enemy_decoder(self, enemy_file)
        self.player_items = []
        try:
            with open(os.path.join(__location__, 'save.csv'), encoding="utf-8") as save_file:
                i = save_file.read()
                i = i.split(";")
                self.health = int(i[0])
                make_tuple = i[1]
                make_tuple = make_tuple[1:5]
                self.position = (int(make_tuple[0]), int(make_tuple[3]))
                make_list = i[2]
                make_list = make_list[1:-1]
                make_list = make_list.split(",")
                for i in make_list:
                    i = i.replace("'", "")
                    i = i.replace(" ", "")
                    for j in self.items:
                        if i == j.name:
                            self.player_items.append(j)

        except FileNotFoundError:
            self.position = (0,0)
            self.health = 10
        self.combat_chance = 0
        self.in_combat = 0
    def delete_save(self):
        """Poista tallennus tiedosto.
        """
        try:
            os.remove(os.path.join(__location__, 'save.csv'))
        except FileNotFoundError:
            pass

    def find_adjacent_rooms(self):
        """Palauta pelaajan viereiset huoneet, ja missä suunnassa ne ovat."""
        roominfo = "You can move: "
        for i in self.rooms:
            if self.position[0] -1 == i.horizontal and self.position[1] == i.vertical:
                roominfo += f"north ({i.name}), "
            if self.position[0] +1 == i.horizontal and self.position[1] == i.vertical:
                roominfo += f"south ({i.name}), "
            if self.position[0] == i.horizontal and self.position[1] == i.vertical +1:
                roominfo += f"west ({i.name}), "
            if self.position[0] == i.horizontal and self.position[1] == i.vertical -1:
                roominfo += f"east ({i.name}), "
        return roominfo[0:-2]

    def start(self):
        """Aloittaa pelin ja lopettaa pelin. Kun peli päätetään, kutsuu funktiota save()"""
        start_message = Commands.command_handler(self,  "look") + "\n"
        for i in start_message.splitlines():
            IO.text.append(i)
        while True:
            if GAME.events() is False:
                GAME.save()
                break
    def save(self):
        """Tallenna pelaajan edistyminen save.csv tiedostoon.
        """
        items_list = []
        for i in self.player_items:
            items_list.append(i.name)
        with open(os.path.join(__location__, 'save.csv'), "w", encoding="utf-8") as save_file:
            save_file.write(f"{self.health};{self.position};{items_list}")
    def input_entry(self):
        """Lisää pelaajan kirjoittaman tekstin ja komennon palautteen IO-tekstikenttään.
            Sitten pyyhkii input_textin.
        """
        thing = Commands.command_handler(self,  IO.input_text) + "\n"
        IO.text.append(IO.input_text)
        for i in thing.splitlines():
            IO.text.append(i)
        IO.input_text = ''
    def events(self):
        """Tämä on pelisilmukka. Kutsu input_entry aina kun pelaaja kirjoittaa enter.
        Päivittää näyton IO.update_screenillä, mutta jos pelaaja poistuu peli-ikkunasta,
        siirry suoritus takaisin start() funktioon
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    GAME.input_entry()
                elif event.key == pygame.K_BACKSPACE:
                    IO.input_text = IO.input_text[:-1]
                else:
                    IO.input_text += event.unicode
        IO.update_screen()
        return None
if __name__ == "__main__":
    pygame.init()
    GAME = Loop()
    IO = Io(GAME)
    GAME.start()
