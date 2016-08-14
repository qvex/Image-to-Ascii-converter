import pygame


class ImgtoAscii():

    def __init__(self, spacing, image):
        self.spacing = spacing
        self.image = pygame.image.load(image)
        self.font_size = 20
        self.font = pygame.font.Font(None, self.font_size)

    def average_rgb(self, x, y):
        average = sum(self.image.get_at((x, y))) // len(self.image.get_at((x, y)))
        return average

    def create_image(self, surface):
        for x in range(0, self.image.get_size()[0], self.spacing):
            for y in range(0, self.image.get_size()[1], self.spacing):
                self.image.get_at((x, y))
                if self.average_rgb(x, y) > 225:
                    text = self.font.render(' ', False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                elif self.average_rgb(x, y) > 200:
                    text = self.font.render('"', False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                elif self.average_rgb(x, y) > 175:
                    text = self.font.render("░", False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                elif self.average_rgb(x, y) > 150:
                    text = self.font.render("░", False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                elif self.average_rgb(x, y) > 100:
                    text = self.font.render("@", False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                elif self.average_rgb(x, y) > 75:
                    text = self.font.render('▒', False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                elif self.average_rgb(x, y) > 25:
                    text = self.font.render('▓', False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
                else:
                    text = self.font.render('█', False, ((0, 0, 0)))
                    surface.blit(text, (x, y))
