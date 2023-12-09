import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image=pygame.image.load("../Invader/graphics/player.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom=pos)
        self.speed=5

    # Sluzi za gledanje koje je dugme pritisnuto
    def get_input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x-=self.speed

    
    def update(self):
        self.get_input()