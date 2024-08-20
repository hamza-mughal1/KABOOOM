import pygame
import csv

pygame.init()
window_size = (1100,900)
root = pygame.display.set_mode(window_size)
run = True
clock = pygame.time.Clock()
fps = 60
grid = []

with open('my_data.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      grid.append(row)



class MainPlayer:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jump_height = 20
        self.gravity = 1
        self.jump_velocity = self.jump_height
        self.movement_velocity = 5
        self.move_left = False
        self.move_right = False
        self.move_jump = False

    def player_rect(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return rect

    def move(self, x, y):
        self.x += x
        self.y += y

    def jump(self):
        self.y -= self.jump_velocity
        self.jump_velocity -= self.gravity
        if abs(self.jump_velocity) > self.jump_height:
            self.move_jump = False
            self.jump_velocity = self.jump_height

    def control_movement(self, run, rects):

        if self.move_left:
            self.move(-self.movement_velocity,0)
        elif self.move_right:
            self.move(self.movement_velocity,0)
        if self.move_jump:
            self.jump()

        if (self.move_jump == False):
            self.y += 11
            
        rect = self.player_rect()
        for i in rects:
            if (rect.colliderect(i[0]) and i[1] == (0,0,0)):
                # print("bottom : ",i[0].bottom, "\ntop : ",rect.top, "\ny-value : ",self.y)
                if (i[0].bottom >= rect.top) and ( rect.bottom > i[0].bottom):
                    self.y = i[0].bottom
                    
                    
                elif (rect.bottom >= i[0].top):
                    self.y = i[0].top - self.height 
                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move_left = True
                elif event.key == pygame.K_RIGHT:
                    self.move_right = True
                elif event.key == pygame.K_UP:
                    self.move_jump = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.move_left = False
                elif event.key == pygame.K_RIGHT:
                    self.move_right = False


        return run

class Level:
    def __init__(self, window_height, window_width, block_size, grid):
        self.height = window_height
        self.width = window_width
        self.block_size = block_size
        self.grid = grid
        self.all_rects = []


    def create_rects(self,color=(0,255,0)):
        pos1 = 0
        for i in range(0,self.width,self.block_size):
            pos2 = 0
            for j in range(0,self.height,self.block_size):
                if pos1 >=45:
                    break

                if self.grid[pos1][pos2] == "0":
                    self.all_rects.append((pygame.Rect(j,i,self.block_size,self.block_size),color))
                else:
                    self.all_rects.append((pygame.Rect(j,i,self.block_size,self.block_size),(0,0,0)))
                pos2 +=1
            pos1 +=1
                

    def draw_level(self,surface):
        for i in self.all_rects:
            pygame.draw.rect(surface,i[1],i[0],9)

            
player = MainPlayer(window_size[0]/2,(window_size[1]/2)+50,50,50)
level = Level(window_height=window_size[0],window_width=window_size[1],block_size=20,grid=grid)
level.create_rects()

while run:
    clock.tick(fps)
    root.fill((255,255,255))
    level.draw_level(root)
    rect = player.player_rect()
    run = player.control_movement(run, level.all_rects)
    
    pygame.draw.rect(root,(0,0,255),rect)
    pygame.display.update()


pygame.quit()



