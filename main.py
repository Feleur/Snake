import pygame
import time
import random

pygame.init()

wh = (255, 255, 255)     # White
ye = (255, 255, 102)     # Yellow
bk = (0, 0, 0)           # Black
re = (213, 50, 80)       # Red
gr = (0, 255, 0)         # Green
bl = (50, 153, 213)      # Blue

screenWidth = 600
screenHeight = 400

display = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

snakeSize = 10
snakeSpeed = 10

fontS = pygame.font.SysFont("bahnschrift", 25)
score = pygame.font.SysFont("comicsansms", 35)


def yourScore(score):
    value = fontS.render("Your score = " + str(score), True, ye)
    display.blit(value, [0, 0])


def snake(snakeSize, snakeList):
    for tmp in snakeList:
        pygame.draw.rect(display, bk, [tmp[0], tmp[1], snakeSize, snakeSize])


def msg(msgs, color):
    message = fontS.render(msgs, True, color)
    display.blit(message, [int(screenWidth/6), int(screenHeight/3)])


def game():
    gameOver = False
    gameClose = False

    x = screenWidth / 2
    y = screenHeight / 2

    xMove = 0
    yMove = 0

    snakeList = []
    length = 1

    pointX = round(random.randrange(0, screenWidth - snakeSize) / 10.0) * 10.0
    pointY = round(random.randrange(0, screenHeight - snakeSize) / 10.0) * 10.0

    while not gameOver:
        while gameClose:
            display.fill(bl)
            msg("You lost. Press N to play one more time or Q to quit.", re)
            yourScore(length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_n:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOver = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    xMove = -snakeSize
                    yMove = 0
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    xMove = snakeSize
                    yMove = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    xMove = 0
                    yMove = -snakeSize
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    xMove = 0
                    yMove = snakeSize
        if x >= screenWidth or x < 0 or y >= screenHeight or y < 0:
            gameClose = True
        x += xMove
        y += yMove
        display.fill(bl)
        pygame.draw.rect(display, gr, [int(pointX), int(pointY), int(snakeSize), int(snakeSize)])
        snakeHead = []
        snakeHead.append(x)
        snakeHead.append(y)
        snakeList.append(snakeHead)

        if len(snakeList) > length:
            del snakeList[0]

        for tmp in snakeList[:-1]:
            if tmp == snakeHead:
                gameClose = True

        snake(snakeSize, snakeList)
        yourScore(length - 1)

        pygame.display.update()

        if x == pointX and y == pointY:
            pointX = round(random.randrange(0, screenWidth - snakeSize) / 10.0) * 10.0
            pointY = round(random.randrange(0, screenHeight - snakeSize) / 10.0) * 10.0
            length += 1
            print("X")

        clock.tick(snakeSpeed)

    pygame.quit()
    quit()


def main():
    game()


main()
