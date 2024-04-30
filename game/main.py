import asyncio
import sys

import pygame


COLORS = [
    ['aqua', 'azure', 'coral'],
    ['crimson', 'cyan', 'indigo'],
]
FPS = 25

async def main():
    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode((1200, 800))
    clock = pygame.time.Clock()

    color_index_x = 0
    color_index_y = 0

    def change_color(change_x, change_y):
        nonlocal color_index_x, color_index_y
        color_index_x = (color_index_x + change_x) % len(COLORS[0])
        color_index_y = (color_index_y + change_y) % len(COLORS)
        new_color = COLORS[color_index_y][color_index_x]
        screen.fill(new_color)
        pygame.display.update()

    while True: # EVENT LOOP
        for event in pygame.event.get():
            if not event.type == pygame.KEYUP:
                continue

            if event.key == pygame.K_d:
                change_color(1, 0)

            if event.key == pygame.K_a:
                change_color(-1, 0)

            if event.key == pygame.K_w:
                change_color(0, -1)

            if event.key == pygame.K_s:
                change_color(0, 1)

            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        clock.tick(FPS) # Frames per second. 25 fps
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
