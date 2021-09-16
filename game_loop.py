import snake_asset as snk
import pygame as pg

clock = pg.time.Clock()
running = True
window = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
snake_block1 = snk.SnakeBlock(5, 5, "E")
snake_block2 = snk.SnakeBlock(4, 5, "E")
snake_block3 = snk.SnakeBlock(3, 5, "E")
snake_list = [snake_block1, snake_block2, snake_block3]
add = False
add_block = None


pos_loc = []
for x in range(10):
    for y in range(10):
        for snake_block in snake_list:
            if snake_block.get_pos() != (x, y):
                pos_loc.append((x, y))

apple = snk.AppleBlock(pos_loc)

i = 0


def has_collided():
    pos = []
    for snake_block in snake_list:
        pos.append(snake_block.get_pos())
    return len(set(pos)) != len(snake_list)


def change_direction():
    if len(snake_list) > 1:
        for i in range(len(snake_list)-1, 0, -1):
            snake_list[i].direction = snake_list[i-1].direction


while running:
    events = pg.event.get()
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                if snake_list[0].direction != "E":
                    snake_list[0].direction = "W"
            elif event.key == pg.K_RIGHT:
                if snake_list[0].direction != "W":
                    snake_list[0].direction = "E"
            elif event.key == pg.K_UP:
                if snake_list[0].direction != "S":
                    snake_list[0].direction = "N"
            elif event.key == pg.K_DOWN:
                if snake_list[0].direction != "N":
                    snake_list[0].direction = "S"

        if event.type == pg.QUIT:
            running = False

    if i % 18 == 0:
        window.fill((0, 0, 0))
        possible_locations = []
        for x in range(10):
            for y in range(10):
                color = (255, 255, 255)
                for snake_block in snake_list:
                    if apple is not None:
                        if snake_list[0].get_pos() == apple.location():
                            add_block = snake_list[-1].create_copy()
                            add = True
                            apple = None
                    if x == snake_block.x and y == snake_block.y:
                        color = (0, 255, 0)
                    else:
                        possible_locations.append((x, y))
                    if apple is not None:
                        if x == apple.x and y == apple.y:
                            color = (255, 0, 0)
                pg.draw.rect(window, color, (30*x + 1, 30*y + 1, 29, 29))
        if apple is None:
            apple = snk.AppleBlock(possible_locations)
        for snake_block in snake_list:
            snake_block.update_position()
        change_direction()
        if add:
            snake_list.append(add_block)
            add = False

        if snake_list[0].has_collided():
            running = False

        if has_collided():
            running = False

    i += 1
    clock.tick(60)
    pg.display.flip()

print("Score:", str(len(snake_list)))