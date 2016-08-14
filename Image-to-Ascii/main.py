import imagetoascii
import pygame

def run_program(fps):
    pygame.init()
    done = False
    p = imagetoascii.ImgtoAscii(10,'reddit.jpg')
    screen = pygame.display.set_mode((p.image.get_size()))
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill((255,255,255))
        p.create_image(screen)
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


if __name__ == '__main__':
    run_program(1)
