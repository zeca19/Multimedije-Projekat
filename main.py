import pygame, sys
from player import Player
import obstacle

class Game:

    def __init__(self):
        # Player setup
        player_sprite=Player((screen_width/2,screen_height),screen_width,5)
        self.player=pygame.sprite.GroupSingle(player_sprite)

        # Obstacle setup
        self.shape=obstacle.shape
        self.block_size=6;
        self.blocks=pygame.sprite.Group()
        self.create_multiple_obstacles(0,480,0,100,200)

    
    def create_obstacle(self,x_start,y_start,offset_x):
        for row_index, row in enumerate(self.shape):
            for col_index, col in enumerate(row):
                if col=="x":
                    x=x_start+col_index*self.block_size+offset_x
                    y=y_start+row_index*self.block_size
                    block=obstacle.Block(self.block_size,(241,79,80),x,y)
                    self.blocks.add(block)

    def create_multiple_obstacles(self,x_start,y_start,*offset):
        for x in offset:
            self.create_obstacle(x_start,y_start,x)

    def run(self):
        self.player.update()
        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        self.blocks.draw(screen)
        # Treba da azurira sve grupe
        # I treba da nacrta sve grupe
        

if __name__=="__main__":
    pygame.init()
    screen_width=600
    screen_height=600

    screen=pygame.display.set_mode((screen_width,screen_height))
    clock=pygame.time.Clock()
    game=Game()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
        screen.fill((30,30,30))
        game.run()

        pygame.display.flip()
        clock.tick(60)