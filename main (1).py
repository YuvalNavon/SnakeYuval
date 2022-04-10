import pygame
import random
from constants import *
import time




# Just some stuff pygame needs
class Game():
    def __init__(self):
        self.start_menu()
    def pygame_init(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
        game_screen = pygame.Surface(screen.get_size())
        game_screen.convert()

        return clock, screen, game_screen

    # Draw on screen a rectangle for every snake square
    def draw_snake(self,game_screen, snake_locations, apple_loc):
        for i in range(len(snake_locations)):
            # The game screen, X, Y, Width, Height
            pygame.draw.rect(game_screen, SNAKE_COLOR, (
            snake_locations[i][0] * GRID_SIZE, snake_locations[i][1] * GRID_SIZE, GRID_SIZE - 1 / (i + 1),
            GRID_SIZE - 1 / (i + 1)), 0)
            pygame.draw.rect(game_screen, (255, 8, 0),
                             (apple_loc[0] * GRID_SIZE, apple_loc[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

    def turn(self,event):
        new_direction = DIRECTION_DICT[RIGHT]
        if event.key == pygame.K_DOWN:
            new_direction = DIRECTION_DICT[DOWN]
        elif event.key == pygame.K_UP:
            new_direction = DIRECTION_DICT[UP]
        elif event.key == pygame.K_LEFT:
            new_direction = DIRECTION_DICT[LEFT]
        elif event.key == pygame.K_RIGHT:
            new_direction = DIRECTION_DICT[RIGHT]
        return new_direction

    def move(self,snake_locations, snake_direction):
        templocations = [(snake_locations[0][0] + snake_direction[0], snake_locations[0][1] + snake_direction[1])]
        for i in range(len(snake_locations) - 1):
            templocations.append(snake_locations[i])
        snake_locations = templocations
        return snake_locations

    def gen_apple(self,snake_locations):
        while True:
            apple_loc = (
            random.randrange(round((SCREEN_WIDTH / 2 - 300) / GRID_SIZE), round((SCREEN_WIDTH / 2 + 300)) / GRID_SIZE),
            random.randrange(round((SCREEN_HEIGHT / 2 - 300) / GRID_SIZE),
                             round((SCREEN_HEIGHT / 2 + 300)) / GRID_SIZE))
            if apple_loc not in snake_locations:
                print(apple_loc)
                return apple_loc

    def start_menu(self):
        clock, screen, game_screen = self.pygame_init()
        start = False
        while start == False:
            screen.blit(game_screen, (0, 0))
            game_screen.fill(START_BACKGROUND_COLOR)
            pygame.display.set_caption('Snake Game')
            font = pygame.font.Font('freesansbold.ttf', 64)
            text = font.render('S N A K E', True, (0, 255, 0), START_BACKGROUND_COLOR)
            textRect = text.get_rect()
            textRect.center = (300, 100)
            game_screen.blit(text, textRect)
            font = pygame.font.Font('freesansbold.ttf', 20)
            text = font.render('PRESS SPACE TO PLAY', True, (255, 255, 255), START_BACKGROUND_COLOR)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH / 2, 300)
            game_screen.blit(text, textRect)
            text = font.render('PRESS BACKSPACE FOR AI PLAY', True, (255, 255, 255), START_BACKGROUND_COLOR)
            textRect = text.get_rect()
            textRect.center = (SCREEN_WIDTH / 2, 400)
            game_screen.blit(text, textRect)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.main_game()

                    elif event.key == pygame.K_BACKSPACE:
                        return 0

    def main_game(self):
        apples = 0
        snake_direction = DIRECTION_DICT[RIGHT]
        clock, screen, game_screen = self.pygame_init()
        # All of the snake's locations.
        snake_locations = [SNAKE_STARTING_LOC, (10, 9), (10, 8)]
        apple_loc = (0, 0)
        player_pressed_esc = False
        game_over = False
        is_apple = False
        start = False

        speed = GAME_SPEED
        while not player_pressed_esc and not game_over:
            # Moving the clock
            clock.tick(speed)
            # Creating the current screen
            screen.blit(game_screen, (0, 0))
            # Filing the screen with the color
            game_screen.fill(BACKGROUND_COLOR)
            blockSize = GRID_SIZE  # Set the size of the grid block
            for x in range(round(SCREEN_WIDTH / 2 - 300), round(SCREEN_WIDTH / 2 + 300), blockSize):
                for y in range(round(SCREEN_HEIGHT / 2 - 300), round(SCREEN_HEIGHT / 2 + 300), blockSize):
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    pygame.draw.rect(game_screen, (10, 10, 10), rect, 1)

            if snake_locations[0] in snake_locations[1:-1] or snake_locations[0][0] < round(
                    (SCREEN_WIDTH / 2 - 300) / GRID_SIZE) or snake_locations[0][1] < round(
                    (SCREEN_HEIGHT / 2 - 300) / GRID_SIZE) or \
                    snake_locations[0][0] >= round((SCREEN_WIDTH / 2 + 300) / GRID_SIZE) or \
                    snake_locations[0][1] >= round((SCREEN_HEIGHT / 2 + 300) / GRID_SIZE):
                print("GAME OVER")
                snake_locations = [SNAKE_STARTING_LOC, (10, 9), (10, 8)]
                apple_loc = (0, 0)
                game_over = True

            if snake_locations[0] == apple_loc:
                is_apple = False
                snake_locations.append((snake_locations[-1][0] - 1, snake_locations[-1][1]))
                apples += 1
                print("apples:", apples, "speed:", speed)

            if not is_apple:
                apple_loc = self.gen_apple(snake_locations)
                is_apple = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    player_pressed_esc = True
                elif event.type == pygame.KEYDOWN:
                    snake_direction = self.turn(event)
            snake_locations = self.move(snake_locations, snake_direction)

            self.draw_snake(game_screen, snake_locations, apple_loc)
            # Updating the screen after we've draw something on it
            pygame.display.update()

g = Game()
pygame.quit()
