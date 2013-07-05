# by Timothy Downs, inputbox2.0 written for my map editor

# This program needs a little cleaning up
# It ignores the shift key
# And, for reasons of my own, this program converts "-" to "_"

# A program to get user input, allowing backspace etc
# shown in a box in the middle of the screen
# Called by:
# import inputbox
# answer = inputbox.ask(screen, "Your name")
#
# Only near the center of the screen is blitted to

import pygame
import pygame.font
import pygame.event
import pygame.draw
import string

class inputbox():
    
    def __init__(self, screen, question, pos, color_back, color_text):
        pygame.font.init()
        self.current_string = []
        self.string = ""
        self.screen = screen
        self.question = question
        self.pos = pos
        self.color_back = color_back
        self.color_text = color_text
        self.message = self.question + ": "
        
    def update(self):
        inkey = self.get_key()
        if inkey != None:
            if inkey == pygame.K_BACKSPACE:
                self.current_string = self.current_string[0:-1]
            elif inkey == pygame.K_RETURN:
                return self.string.join(self.current_string)
            elif inkey == pygame.K_MINUS:
                self.current_string.append("_")
            elif inkey <= 127:
                self.current_string.append(chr(inkey))
            self.message = self.question + ": " + self.string.join(self.current_string)
        return ""
    
    def get_key(self):
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        elif event.type == pygame.NOEVENT:
            pass
        else:
            pygame.event.post(event)
    
    def draw(self):
        fontobject = pygame.font.Font(None,18)
        pygame.draw.rect(self.screen, self.color_back,
                       ((self.pos[0]) - 100,
                        (self.pos[1]) - 10,
                        200,20), 0)
        pygame.draw.rect(self.screen, self.color_text,
                       ((self.pos[0]) - 102,
                        (self.pos[1]) - 12,
                        204,24), 1)
        if len(self.message) != 0:
            self.screen.blit(fontobject.render(self.message, 2, self.color_text),
                    ((self.pos[0]) - 100, (self.pos[1]) - 5))
        pygame.display.flip()