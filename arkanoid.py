import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (138, 149, 151)
GREEN = (   0, 255,   0)
RED = ( 255,   0,   0)
BLUE = (   0,   0, 255)

BRICK_WIDTH = 53
BRICK_HEIGHT = 20
BRICK_GAP = 3
BRICK_ROWS = 5
BRICK_COLUMNS = 10

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(pygame.image.load("C:\\Users\\Asus\\Desktop\\AgusDur0\\programacion\\python\\Proyectos\\Arkanoid\\nave_boca.png"))
        self.rect = self.image.get_rect()

    def update(self):
        self.player_x = 260
        self.player_y = 550
        self.player_speed_x = 0

class Bola(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Asus\\Desktop\\AgusDur0\\programacion\\python\\Proyectos\\Arkanoid\\bola.png")
        self.rect = self.image.get_rect()

    def update(self):
        self.bola_x = self.player_x + 65
        self.bola_y = self.player_y + 65
        self.bola_speed_x = self.player_speed_x
        self.bola_speed_y = 0


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:\\Users\\Asus\\Desktop\\AgusDur0\\programacion\\python\\Proyectos\\Arkanoid\\fondo_prueba_2.png")

class Game(object):
    def __init__(self):
        self.game_over = False

        self.score = 0
        self.bola_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        self.player = Player()
        self.bola = Bola()

        self.bola_list.add(self.bola)
        self.all_sprites_list.add(self.bola)

        self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.bola_speed_x = 0
                self.bola_speed_y = 0
            if event.key == pygame.K_LEFT:
                self.player_speed_x = -3
            if event.key == pygame.K_RIGHT:
                self.player_speed_x = 3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                self.bola_speed_x = 3
                self.bola_speed_y = -3
            if event.key == pygame.K_LEFT:
                self.player_speed_x = 0
            if event.key == pygame.K_RIGHT:
                self.player_speed_x = 0

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()
            self.meteor_hit_list = pygame.sprite.spritecollide(self.player, self.bola_list, False)

        if (self.bola_x > 556 or self.bola_x < 20):
            self.bola_speed_x *= -1
        if (self.bola_y < 15):
            self.bola_speed_y *= -1

        if player_x > 476:
            player_x = 476

        if player_x < 28:
            player_x = 28

        self.bola_x += self.bola_speed_x
        self.bola_y += self.bola_speed_y
        self.player_x += self.player_speed_x



    def display_frame(self, screen):

        self.bricks = []
        self.brick = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))
        self.brick_rect = pygame.Surface.get_rect
        self.brick.fill(GREEN)

        for row in range(BRICK_ROWS):
            for column in range(BRICK_COLUMNS):
                brick_x = 20 + column * (BRICK_WIDTH + BRICK_GAP)
                brick_y = 50 + row * (BRICK_HEIGHT + BRICK_GAP)
                self.bricks.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))    

        self.screen.fill(WHITE)
        self.screen.blit(self.background, [-200, 0])
        self.screen.blit(self.player, [self.player_x, self.player_y])
        self.screen.blit(self.bola, [self.bola_x, self.bola_y])

        pygame.draw.line(screen, GRAY, (0, 0), (0, 700), 50)
        pygame.draw.line(screen, GRAY, (800, 0), (800, 700), 447)
        pygame.draw.line(screen, GRAY, (0, 0), (800, 0), 20)
        pygame.draw.line(screen, GRAY, (0, 700), (800, 700), 20)

        pygame.display.flip()

    def main():
        pygame.init()

        screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        done = False
        clock = pygame.time.Clock()
        game = Game()

        while not done:
            done = game.process_events()
            game.run_logic()
            game.display_frame(screen)
            clock.tick(60)
        pygame.quit()

    if __name__ == "__main__":
        main()



