import pygame
class Io:
    def __init__(self, game):
        pygame.display.set_caption("Text Adventures")
        self.screen = pygame.display.set_mode((1400, 920))
        self.clock = pygame.time.Clock()
        self.input_rect = pygame.Rect(100, 800, 1200, 32)
        self.white_color = pygame.Color(255, 255, 255, 255)
        self.grey_color = pygame.Color(200, 200, 200, 200)
        self.font = pygame.font.Font(None, 30)
        self.input_text = ''
        self.text = []
        self.game = game
    def update_screen(self):
        self.screen.fill((30, 30, 30))
        txt_surface = self.font.render(self.input_text, True, self.white_color)
        txt_surface3 = self.font.render("Health: " + str(self.game.health), True, self.white_color)
        self.screen.blit(txt_surface, (self.input_rect.x+5, self.input_rect.y+5))
        self.screen.blit(txt_surface3, (self.input_rect.x+5, self.input_rect.y+40))
        y_offset = 40
        if len(self.text) > 23:
            self.text = self.text[1:]
        for i in reversed(self.text):
            if len(i.split(" ")) > 3:
                txt_surface2 = self.font.render(i, True, self.white_color)
                self.screen.blit(txt_surface2, (self.input_rect.x+5, self.input_rect.y-y_offset))
            else:
                txt_surface2 = self.font.render(i, True, self.grey_color)
                self.screen.blit(txt_surface2, (self.input_rect.x+15, self.input_rect.y-y_offset))
            y_offset += 35
        pygame.draw.rect(self.screen, self.white_color, self.input_rect, 2)

        pygame.display.flip()
        self.clock.tick(30)
