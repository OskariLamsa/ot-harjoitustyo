import pygame
from commands import Commands

class Loop:
    def __init__(self, levels):
        self.levels = []
    def start( ):
        screen = pygame.display.set_mode((1080, 920))
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 30)
        input_rect = pygame.Rect(100, 800, 880, 32)
        color = pygame.Color(255, 255, 255, 255)
        text = ''
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        to_print = Commands.command_handler(text)
                        print(to_print)
                        text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
            screen.fill((30,30,30))
            txt_surface = font.render(text, True, color)
            #length = max(200, txt_surface.get_width()+10)
            #input_rect.w = length
            screen.blit(txt_surface, (input_rect.x+5, input_rect.y+5))
            pygame.draw.rect(screen, color, input_rect, 2)

            pygame.display.flip()
            clock.tick(30)
if __name__=="__main__":
    pygame.init()
    game = Loop.start() 