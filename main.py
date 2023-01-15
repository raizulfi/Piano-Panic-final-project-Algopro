import pygame
import random 
import json
from variables import Block


# Initializing Pygame and font
pygame.init()
clock = pygame.time.Clock()
score_font = pygame.font.Font('Fonts/Futura condensed.ttf', 32)

# Color
WHITE = (255,255,255)

# Size of the window application
screen = width, height = 324, 700
block_width = width // 4  # Creating 4 blocks for 4 lanes
block_height = 130

# Displaying the game with no frame
window = pygame.display.set_mode(screen, pygame.NOFRAME)
pygame.display.set_caption("Piano Panic!")

# Images
bg_image = pygame.image.load('images/background1.png') # Background image
play_image = pygame.image.load('images/playbutton.png')
play_rect = play_image.get_rect(center = (width//2, height-80)) #becomes centered and a possible button
reply_rect = play_image.get_rect(center = (width//2,height-80))
gameover_image = pygame.image.load('images/gameover.png')

# FPS and speed
clock = pygame.time.Clock()
fps = 30

# Functions
def grow_speed(score):
    return 200 + 5 * score      # The speed of the block increases as the score increases

with open('notes.json') as file:
    notes_dict = json.load(file)

# Music & sound effect
buzzer_fx = pygame.mixer.Sound('piano/buzzer.mp3')
pygame.mixer.music.load('piano/bg_music.mp3') 
pygame.mixer.music.set_volume (0.5)
pygame.mixer.music.play(-1)

# BLOCK GROUP and stats 
block_group = pygame.sprite.Group()

score = 0
no_block = 0  
speed = 2

pos = None  # Position is None, use case is for the mouse since it's our main input

#pages
home_page = True
Music_page = False
game_page = False
game_over = False


running = True
while running:
    pos = None  # When it loops complete, it'll reset due to the loop
    window.blit(bg_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Will stop the game if you press esc or quit  
        if event.type == pygame.QUIT:
            running = False
        # will stop the game if you press esc or quit  
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        #if the mouse is being clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
    

    # block_group chcekcing colision mouse click and if the block reaches the bottom of the screen


    if home_page:
        window.blit(play_image, play_rect)
        # If you click on play it go on to the game page
        if pos and play_rect.collidepoint(pos):
            home_page = False
            game_page = True

            pos = None #reset

            x = random.randint(0, 3)  # It will randomly create a block from either 4 lanes
            b = Block(x * block_width, block_height, window)  # Creates the block
            block_group.add(b)

            # you can change which song you want by changing the number depending on the notes file
            notes_list = notes_dict['2']
            notes_count = 0


    if game_page:
        pygame.mixer.music.set_volume (0.1) #lower the background muisc when playing 
        for block in block_group:
            block.update(speed)
            img1 = score_font.render(f'Score : {score}', True, WHITE)
            window.blit(img1, (70 - img1.get_width() / 2, 10))

            if pos: # it checks if the position of the mouse  clicked the block
                if block.rect.collidepoint(pos):
                    block.alive = False
                    score += 1
                    pos = None

                    note = notes_list[notes_count]
                    pygame.mixer.Sound(f'piano/{note}.mp3').play()
                    notes_count = (notes_count + 1) % len(notes_list) # once it reaches at the end of the song the length will be the same amount of keynotes which means it leads back into the starting note esentially repeating the song and keys



            # basically when the bottom of the rectangle/block goes beyond the height of the window
            if block.rect.bottom >= height and block.alive:
                block.kill() # so its stop going down
                buzzer_fx.play() 
                game_over = True

        
        if pos: #if didn't click the the blocks it plays a buzzer sound effect and it's game over
            buzzer_fx.play() 
            game_over = True


        if len(block_group) > 0: #if there is a block present
            b = block_group.sprites()[-1] #gets the last block also becomes a list 
            if  b.rect.top + speed >= 0:
                x = random.randint(0,3) # it will randomly create a block from either 4 lanes
                y = - block_height - (0 - b.rect.top)
                b = Block( x * block_width, y, window) #creates the block
                block_group.add(b)
                no_block += 1 
                
        
         #speed to increase by score
        speed = int(grow_speed(score) * (fps/1000)) 

        if game_over:
            speed = 0
            window.blit(gameover_image,(0,0))
            img1 = score_font.render(f'Score : {score}', True, WHITE)
            window.blit(img1, (img1.get_width(), 350))
            
            img2 = score_font.render(f'PRESS ESC TO EXIT :(',True, WHITE)
            window.blit(img2, (50, 400))
            

 

            



    clock.tick(fps)
    pygame.display.update()

pygame.quit()