
import pygame
from sys import exit
pygame.init()

# color Lib
green = (51, 204, 51)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
purple = (127, 0, 255)
orange = (255, 165, 0)

screen = pygame.display.set_mode([300, 475])
pygame.display.set_caption(' Adventure Cookie Capitalist')
background = pygame.image.load('Pictures/Adventure-captitalist.png')
framerate = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()

# Game Variables
score = 0
# green
green_value = 10
draw_green = False
green_length = 0
green_speed = 5
# Managers cost
green_cost = 2500
green_owned = False
green_manager_cost = 25_000
# yellow
yellow_value = 0
draw_yellow = False
yellow_length = 0
yellow_speed = 4
# Managers cost
yellow_cost = 10_000
yellow_owned = False
yellow_manager_cost = 50_000
# red
red_value = 0
draw_red = False
red_length = 0
red_speed = 3
# Managers cost
red_cost = 35_000
red_owned = False
red_manager_cost = 90_000
# blue
blue_value = 0
draw_blue = False
blue_length = 0
blue_speed = 2
# Managers cost
blue_cost = 65_000
blue_owned = False
blue_manager_cost = 250_000
# orange
orange_value = 0
draw_orange = False
orange_length = 0
orange_speed = 1
# Managers cost
orange_cost = 125_000
orange_owned = False
orange_manager_cost = 500_000


def draw_task(color, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = pygame.draw.circle(screen, color, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, color, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, color, [70, y_coord - 15, length, 30])
    value_text = font.render(str(value), True, white)
    screen.blit(value_text, (16, y_coord - 10))
    return task, length, draw


def draw_buttons(color, x_coord, cost, owned, manager_cost):
    color_button = pygame.draw.rect(screen, color, [x_coord, 340, 50, 30])
    color_cost = font.render(str(round(cost, 2)), True, black)
    screen.blit(color_cost, (x_coord + 6, 350))
    if not owned:
        manager_button = pygame.draw.rect(screen, color, [x_coord, 405, 50, 30])
        manager_text = font.render(str(round(manager_cost, 2)), True, black)
        screen.blit(manager_text, (x_coord + 6, 410))
    else:
        manager_button = pygame.draw.rect(screen, black, [x_coord, 405, 50, 30])
    return color_button, manager_button


running = True
while running:
    timer.tick(framerate)
    if green_owned and not draw_green:
        draw_green = True
    if yellow_owned and not draw_yellow:
        draw_yellow = True
    if red_owned and not draw_red:
        draw_red = True
    if blue_owned and not draw_blue:
        draw_blue = True
    if orange_owned and not draw_orange:
        draw_orange = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_yellow = True
            if task3.collidepoint(event.pos):
                draw_red = True
            if task4.collidepoint(event.pos):
                draw_blue = True
            if task5.collidepoint(event.pos):
                draw_orange = True
            # Buy Manager
            if green_manager_buy.collidepoint(event.pos) and score >= green_manager_cost and not green_owned:
                green_owned = True
                score -= green_manager_cost
            if yellow_manager_buy.collidepoint(event.pos) and score >= yellow_manager_cost and not yellow_owned:
                yellow_owned = True
                score -= yellow_manager_cost
            if red_manager_buy.collidepoint(event.pos) and score >= red_manager_cost and not red_owned:
                red_owned = True
                score -= red_manager_cost
            if blue_manager_buy.collidepoint(event.pos) and score >= blue_manager_cost and not blue_owned:
                blue_owned = True
                score -= blue_manager_cost
            if orange_manager_buy.collidepoint(event.pos) and score >= orange_manager_cost and not orange_owned:
                orange_owned = True
                score -= orange_manager_cost
            # Buy More items
            if green_buy.collidepoint(event.pos) and score >= green_cost:
                green_value += 15
                score -= green_value
                green_cost += 25
            if yellow_buy.collidepoint(event.pos) and score >= yellow_cost and not yellow_owned:
                yellow_value += 25
                score -= yellow_value
                yellow_cost += 35
            if red_buy.collidepoint(event.pos) and score >= red_cost and not red_owned:
                red_value += 35
                score -= red_value
                red_cost += 45
            if blue_buy.collidepoint(event.pos) and score >= blue_cost and not blue_owned:
                blue_value += 45
                score -= blue_value
                blue_cost += 55
            if orange_buy.collidepoint(event.pos) and score >= orange_cost and not orange_owned:
                orange_value += 55
                score -= orange_value
                orange_cost += 65


    screen.blit(background, (0, 3))
    task1, green_length, draw_green = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
    task2, yellow_length, draw_yellow = draw_task(yellow, 110, yellow_value, draw_yellow, yellow_length, yellow_speed)
    task3, red_length, draw_red = draw_task(red, 170, red_value, draw_red, red_length, red_speed)
    task4, blue_length, draw_blue = draw_task(blue, 230, blue_value, draw_blue, blue_length, blue_speed)
    task5, orange_length, draw_orange = draw_task(orange, 290, orange_value, draw_orange, orange_length, orange_speed)
    # Manager buttons
    green_buy, green_manager_buy = draw_buttons(green, 5, green_cost, green_owned, green_manager_cost)
    yellow_buy, yellow_manager_buy = draw_buttons(yellow, 60, yellow_cost, yellow_owned, yellow_manager_cost)

    red_buy, red_manager_buy = draw_buttons(red, 115, red_cost, red_owned, red_manager_cost)
    blue_buy, blue_manager_buy = draw_buttons(blue, 170, blue_cost, blue_owned, blue_manager_cost)

    orange_buy, orange_manager_buy = draw_buttons(orange, 230, orange_cost, orange_owned, orange_manager_cost)

    # how much money are we earning
    display_score = font.render('Cash: €'+str(round(score, 2)), True, white, black)
    screen.blit(display_score, (10, 5))
    Buy_More = font.render('Buy More', True, white)
    screen.blit(Buy_More, (10, 315))
    Buy_Manager = font.render('Buy Manager', True, white)
    screen.blit(Buy_Manager, (10, 380))
    pygame.display.flip()
pygame.quit()
exit()