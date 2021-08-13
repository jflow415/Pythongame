import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

class Game:

    def __init__(self):
        #game code
        self.width = 600
        self.height = 600
        self.purple_rgb = (149,79,255)

        #game screen with width of 500 and height of 600
        self.arcade_window = pygame.display.set_mode((self.width,self.height))

        self.clock = pygame.time.Clock()

        self.background = GameObject(0,0, self.width, self.height, 'assets/background.png')
        self.treasure = GameObject(280,20, 35,25, 'assets/coin2.png')

        self.player = Player(280, 500, 50, 50, 'assets/player.png', 10)
        self.enemies = [
            Enemy(20, 520, 25, 25, 'assets/imp.png', 3),
            Enemy(200, 400, 50, 50, 'assets/imp.png', 3),
            Enemy(550, 200, 50, 50, 'assets/imp.png', 3)

        ]
        self.enemy = Enemy(50, 400, 50, 50, 'assets/imp.png', 3)

  

    def game_loop(self):
        player_direction = 0
        while True:
            #event handeling 
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    #arrow key up
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    #arrow key down
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0

            #game logic
            self.move_characters(player_direction)

            #display function
            self.image_sprites()

            #check collision
            if self.check_collision():
                return


            #perform the loop 60 times per second "60 fps"
            self.clock.tick(60)
    
    def image_sprites(self):
        self.arcade_window.fill(self.purple_rgb)
        self.arcade_window.blit(self.background.image, (self.background.x, self.background.y))
        self.arcade_window.blit(self.treasure.image,(self.treasure.x, self.treasure.y))
        self.arcade_window.blit(self.player.image,(self.player.x, self.player.y))
        for enemy in self.enemies:
            self.arcade_window.blit(enemy.image,(enemy.x, enemy.y))

        pygame.display.update()

    #all character movements on the screen
    def move_characters(self, player_direction):
        self.player.move(player_direction, self.height)  
        for enemy in self.enemies: 
            enemy.move(self.width) 

    #find collision of characters/treasure and breakout
    def check_collision(self):
        for enemy in self.enemies:
            if self.detect_collision(self.player, enemy):
                return True
        if self.detect_collision(self.player, self.treasure):
                return True
        return False

    #check for overlappying
    def detect_collision(self, object_one, object_two):
        if object_one.y > (object_two.y + object_two.height):
            return False
        elif (object_one.y + object_one.height) < object_two.y:
            return False

        if object_one.x > (object_two.x + object_two.width):
            return False
        elif (object_one.x + object_one.width) < object_two.x:
            return False
        return True
    
    

    


