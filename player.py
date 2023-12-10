import pygame



class Player(pygame.sprite.Sprite):
    def __init__(self,pos,constraint,speed):
        super().__init__()
        self.image=pygame.image.load("../Invader/graphics/player.png").convert_alpha()
        self.rect=self.image.get_rect(midbottom=pos)
        self.speed=speed
        self.max_x_constraint=constraint
        self.laser_time=0
        self.ready=True
        self.laser_coldown=600

    # Sluzi za gledanje koje je dugme pritisnuto
    def get_input(self):
        keys=pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x+=self.speed
        elif keys[pygame.K_LEFT]:
            self.rect.x-=self.speed

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot_laser()
            self.ready=False
            self.laser_time=pygame.time.get_ticks()

    
    def recharge(self):
        if not self.ready:
            current_time=pygame.time.get_ticks()
            if current_time-self.laser_time>=self.laser_coldown:
                self.ready=True

    
    def update(self):
        self.get_input()
        self.constraint()
        self.recharge()

    def constraint(self):
        if self.rect.left<=0:
            self.rect.left=0
        if self.rect.right>=self.max_x_constraint:
            self.rect.right=self.max_x_constraint


    def shoot_laser(self):
        print("Pucamo sad")
       
