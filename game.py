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
            self.player.move(player_direction, self.height)   
            self.enemy.move(self.width) 

            #display function
            self.image_sprites()


            #perform the loop 60 times per second "60 fps"
            self.clock.tick(60)
    
    def image_sprites(self):
        self.arcade_window.fill(self.purple_rgb)
        self.arcade_window.blit(self.background.image, (self.background.x, self.background.y))
        self.arcade_window.blit(self.treasure.image,(self.treasure.x, self.treasure.y))
        self.arcade_window.blit(self.player.image,(self.player.x, self.player.y))
        self.arcade_window.blit(self.enemy.image,(self.enemy.x, self.enemy.y))

        pygame.display.update()


