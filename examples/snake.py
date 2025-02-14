import lighght as gh
from random import choice


poetry = "I have eaten the plums that were in the icebox and which you were probably saving for breakfast Forgive me they were delicious so sweet and so cold"
directions = [gh.LEFT, gh.RIGHT, gh.UP, gh.DOWN]
snake = []
index = 0
direction = directions[0]
food = None
game_over = False


@gh.setup
def setup():
    gh.full_screen()
    gh.no_cursor()
    gh.color_mode(gh.HSB)
    init_game()


@gh.draw
def draw():
    gh.background(' ')
    if gh.get_frame_count() % 4 == 0:
        update_snake()
    collision_detection()
    draw_snake()
    draw_food()


@gh.cursor_moved
def cursor_moved():
    global direction
    direction = gh.get_key_code()


@gh.key_typed
def key_typed():
    if game_over:
        init_game()


def init_game():
    global snake, index, direction, game_over
    game_over = False
    index = 0
    direction = choice(directions)
    x0, y0 = int(gh.get_width() / 2), int(gh.get_height() / 2)
    snake = [[x0, y0, 0]]
    generate_food()

    gh.set_cursor(x0, y0)
    gh.loop()


def draw_snake():
    for x, y, i in snake:
        h = gh.map(i, 0, len(poetry), 0, 360)
        gh.stroke(poetry[i], bg=(h, 100, 100))
        gh.point(x, y)


def draw_food():
    h = gh.map(food[2], 0, len(poetry), 0, 360)
    gh.stroke(poetry[food[2]], bg=(h, 100, 100))
    gh.point(food[0], food[1])


def update_snake():
    global game_over
    for i in range(len(snake) - 1):
        p1, p2 = snake[i], snake[i + 1]
        p1[0], p1[1] = p2[0], p2[1]

    head = snake[-1]
    x_move = 0 if direction == gh.UP or direction == gh.DOWN else 1
    y_move = 0 if direction == gh.LEFT or direction == gh.RIGHT else 1
    x_d = 1 if direction == gh.RIGHT else -1
    y_d = 1 if direction == gh.DOWN else -1
    next_x = (head[0] + x_move * x_d) % gh.get_width()
    next_y = (head[1] + y_move * y_d) % gh.get_height()

    if in_snake(next_x, next_y):
        gh.no_loop()
        game_over = True
    else:
        head[0] = next_x
        head[1] = next_y


def in_snake(x, y):
    for p in snake:
        if p[0] == x and p[1] == y:
            return True
    return False


def collision_detection():
    global snake
    head = snake[-1]
    if head[0] == food[0] and head[1] == food[1]:
        snake.append([food[0], food[1], index])
        generate_food()


def generate_food():
    global food, index, game_over
    if index == len(poetry) - 1:
        game_over = True
        gh.no_loop()
    else:
        index = index + 1
        while True:
            x = int(gh.random(gh.get_width()))
            y = int(gh.random(gh.get_height()))
            if not in_snake(x, y):
                break
        food = [x, y, index]

if __name__ == "__main__":
    gh.run()
