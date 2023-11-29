import pygame, asyncio
import button
import math
import random
from os import listdir
from os.path import isfile, join

pygame.init()
pygame.mixer.init()
game_pause = False
game_npause = False
pygame.display.set_caption("Legal Learns")

# Keyboard_click_voice = pygame.mixer.Sound(join("assets","sounds","keyboard_click.mp3"))
# Mouse_click_voice = pygame.mixer.Sound(join("assets","sounds","mouse_click.mp3"))
# Game_error_sound = pygame.mixer.Sound(join("assets","sounds","error_sound.mp3"))
# Game_lost_sound = pygame.mixer.Sound(join("assets","sounds","game_lost.mp3"))
# Game_win_sound = pygame.mixer.Sound(join("assets","sounds","win_sound.wav"))
# Game_sound = pygame.mixer.Sound(join("assets","sounds","game_song.wav"))
# Game_sound.play(loops=-1)
# Game_sound.set_volume(0.05)

WIDTH, HEIGHT = 800, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Child Right Play")
clock = pygame.time.Clock()
LETTER_FONT = pygame.font.SysFont('comicsans', 20)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)
RADIUS = 20
BUTTON_AREA = 100
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) /2)
starty = 400
a = 65
for i in range(26):
    x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(a + i), True])

images = []
for i in range(14):
    image = pygame.image.load(join("assets", "hangman_images", "images","hangman") + str(i) + ".png") 
    images.append(image)

hangman_states = 0
words = ["RIGHTS","LAW","CHILD","EDUCATION","HEALTH","WORK","PROTECTION","HARASSMENT","IDENTITY","NATIONALITY","CULTURE"]
print(len(words))
word = random.choice(words)
word_letter = random.choice(word)
guessed = []
guessed.append(word_letter)
WHITE = (255,255,255)
BLACK = (0,0,0)
resume_img = pygame.image.load(join("assets","Menu2","images","button_resume.png")).convert_alpha()
quit_img = pygame.image.load(join("assets","Menu2","images","button_quit.png")).convert_alpha()
next_img = pygame.image.load(join("assets","Menu","Buttons","Next.png")).convert_alpha()
close_img = pygame.image.load(join("assets","Menu","Buttons","Close.png")).convert_alpha()
pre_img = pygame.image.load(join("assets","Menu","Buttons","Restart.png")).convert_alpha()
resume_button = button.Button(304, 125, resume_img, 1)
quit_button = button.Button(336, 250, quit_img, 1)
next_button = button.Button(700, 400, next_img, 2)
close_button = button.Button(650, 400, close_img, 3)
pre_button = button.Button(600, 400, pre_img, 2)

def append_word(a):
    global word
    if (a==True):
        word = random.choice(words)
        word_letter = random.choice(word)
        guessed.append(word_letter)
        if(len(word) > 5):
            while True:
                word_letter = random.choice(word)
                if word_letter not in guessed:
                    guessed.append(word_letter)
                    break
    else:
        guessed.clear()
        word_letter = random.choice(word)
        guessed.append(word_letter)
        if(len(word) > 5):
            while True:
                word_letter = random.choice(word)
                if word_letter not in guessed:
                    guessed.append(word_letter)
                    break




def reset__game_again():
    global hangman_states
    hangman_states = 0
    append_word(False)
    global letters
    letters = []
    letters.clear()
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) /2)
    starty = 400
    a = 65
    for i in range(26):
        x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(a + i), True])

    image = pygame.image.load(join("assets", "hangman_images", "images","hangman0.png")) 
    images.append(image)    

def reset__game():
    global hangman_states
    hangman_states = 0
    append_word(True)
    global letters
    letters = []
    letters.clear()
    startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) /2)
    starty = 400
    a = 65
    for i in range(26):
        x = startx + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
        y = starty + ((i // 13) * (GAP + RADIUS * 2))
        letters.append([x, y, chr(a + i), True])

    image = pygame.image.load(join("assets", "hangman_images", "images","hangman0.png"))
    images.append(image)

def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    rect_area = pygame.draw.rect(window, "white", (390, 110, 407, 280))

    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 800:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def display_message(message):
    image = pygame.image.load(join("assets", "Background", "blue.png"))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    for tile in tiles:
        window.blit(image, tile)
    
    text = WORD_FONT.render(message, 1, BLACK)
    window.blit(text, ((WIDTH-200) - text.get_width()/2, (HEIGHT-450) - text.get_height()/2))
    text = "Scenario: Priya, 10, lives in a slum and works as a maid. She can't go to school, gets little food and is abused. \n\nRight: Priya deserves education, health, safety and freedom. Her parents and boss break her rights by forcing her to work. She needs legal and social help to leave and study."
    display_text(window, text, (400,120), LETTER_FONT, BLACK)
    window.blit(images[hangman_states+7], (50, 100))
    if(message != "You Lost!"):
        next_button.draw(window)
    pre_button.draw(window)
    close_button.draw(window)
    pygame.display.update()

def draw_win():
    image = pygame.image.load(join("Background", "blue.png"))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    for tile in tiles:
        window.blit(image, tile)

    text = TITLE_FONT.render("Word Hunt", 1, BLACK)
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    text = WORD_FONT.render(display_word, 1, BLACK)
    window.blit(text, (300, 200))
    
    for letter in letters:
        x, y, l, visible = letter
        if(visible and l not in guessed):
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(l, 1, BLACK)
            window.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
        else:
            letter[3] = False

    window.blit(images[hangman_states], (50, 100))
    pygame.display.update()

def draw_resume_screen():
    global game_pause
    image = pygame.image.load(join("assets", "Background", "blue.png"))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH // width + 1):
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height)
            tiles.append(pos)

    for tile in tiles:
        window.blit(image, tile)
    resume_button.draw(window)
    quit_button.draw(window)
    pygame.display.update()

append_word(True)
draw_win()
async def main():
    global game_pause, game_npause
    global hangman_states, clock
    GAME_MESSAGE = ""
    FPS = 60
    run = True
    
    while run:
        clock.tick(FPS)
        if(game_pause == True):
            draw_resume_screen()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    print(m_x, " " , m_y)
                    if(m_x >= 298 and m_x <= 491 and m_y >= 125 and m_y <= 198):
                        #Mouse_click_voice.play()
                        game_pause = False
                    elif(m_x >= 334 and m_x <= 462 and m_y >= 249 and m_y <= 324):
                        #Mouse_click_voice.play()
                        pygame.quit()
                        quit()

        elif game_npause == True:
            display_message(GAME_MESSAGE)
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    print(m_x, " " , m_y)
                    if(m_x >= 600 and m_x <= 640 and m_y >= 402 and m_y <= 442):
                        #Mouse_click_voice.play()
                        game_npause = False
                        reset__game_again()

                    elif(m_x >= 654 and m_x <= 691 and m_y >= 402 and m_y <= 442):
                        #Mouse_click_voice.play()
                        pygame.quit()
                        quit()

                    elif(m_x >= 702 and m_x <= 741 and m_y >= 402 and m_y <= 442 and GAME_MESSAGE == "You Won!!!"):
                        #Mouse_click_voice.play()
                        game_npause = False
                        reset__game()

        else:
            draw_win()
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    run = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_x, m_y = pygame.mouse.get_pos()
                    for letter in letters:
                        x, y, l, v = letter
                        if v:
                            dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                            if(dis < RADIUS):
                                #Mouse_click_voice.play()
                                letter[3] = False
                                guessed.append(l)
                                if l not in word:
                                    hangman_states += 1

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        #Keyboard_click_voice.play()
                        game_pause = True
                    else:    
                        l1 = event.unicode.upper()
                        for letter in letters:
                            x, y, l, v = letter
                            if v and l==l1:
                                #Keyboard_click_voice.play()
                                letter[3] = False
                                guessed.append(l)
                                if l not in word:
                                    hangman_states += 1
                            elif v==False and l==l1:
                                #Game_error_sound.play()
                                pass

            draw_win()
            won = True
            for let in word:
                if let not in guessed:
                    won = False
                    break
            
            if(won):
                GAME_MESSAGE = "You Won!!!"
                #Game_win_sound.play()
                game_npause = True

            if(hangman_states == 6):
                GAME_MESSAGE = "You Lost!"
                #Game_lost_sound.play()
                game_npause = True

    await asyncio.sleep(0)

asyncio.run(main())


pygame.quit()
quit()