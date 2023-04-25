"""Pelin aloittava script"""
#pylint: disable=no-member
#Yllä oleva ajaa saman asian kuin whitelistaaminen, joka ei toiminut.
import os
import pygame
from commands import Commands
from rooms import Rooms
from items import Items
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
screen = pygame.display.set_mode((1080, 920))
clock = pygame.time.Clock()
input_rect = pygame.Rect(100, 800, 880, 32)
color = pygame.Color(255, 255, 255, 255)
class Loop:
    """Peli"""

    def __init__(self):
        """
        Huoneet ovat lista huone-olioita,
        Esineet ovat lista esine-olioita.
        Player_items sisältää pelaajan omistamat esineet.
        Position ilmaisee pelaajan sijainnin. 
        """
        room_file = open(os.path.join(__location__, 'rooms.csv'), encoding="utf-8")
        item_file = open(os.path.join(__location__, 'items.csv'), encoding="utf-8")
        self.rooms = Rooms.room_decoder(self, room_file)
        self.items = Items.item_decoder(self, item_file)
        self.player_items = []
        self.position = (0,0)

    def find_adjacent_rooms(self):
        """Palauta pelaajan viereiset huoneet, ja missä suunnassa ne ovat."""
        roominfo = "You can move: "
        for i in self.rooms:
            if self.position[0] -1 == i.horizontal and self.position[1] == i.vertical:
                roominfo += f"north ({i.name}),"
            if self.position[0] +1 == i.horizontal and self.position[1] == i.vertical:
                roominfo += f"south ({i.name}),"
            if self.position[0] == i.horizontal and self.position[1] == i.vertical +1:
                roominfo += f"west ({i.name}),"
            if self.position[0] == i.horizontal and self.position[1] == i.vertical -1:
                roominfo += f"east ({i.name}),"
        return roominfo[0:-1]

    def start(self):
        """Pelin loop"""
        font = pygame.font.Font(None, 30)
        running = True
        text = ''
        print(self.rooms[0].description)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print(Commands.command_handler(self,  text))
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            screen.fill((30, 30, 30))
            txt_surface = font.render(text, True, color)
            screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
            pygame.draw.rect(screen, color, input_rect, 2)

            pygame.display.flip()
            clock.tick(30)
    def events(self):
        pass
if __name__ == "__main__":
    pygame.init()
    GAME = Loop()
    HANDLER = Commands(GAME)
    GAME.start()
