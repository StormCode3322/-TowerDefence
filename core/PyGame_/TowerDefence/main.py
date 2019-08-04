import pygame, sys
from pygame.locals import *
from gameobjects import *
from imageloader import *

pygame.init()
music = pygame.mixer.Sound("audio/music.wav")
explosion = pygame.mixer.Sound("audio/explosion.wav")
nextWave = pygame.mixer.Sound("audio/next-wave.wav")
#music.play(-1)

clock = pygame.time.Clock()
screen = pygame.display.set_mode( (800,600) )

gameObjects = []

background = Background("images/Nebula1.bmp", screen.get_width(), screen.get_height())

player = Player("images/Hunter1.bmp", 2, (25, 1, 23, 23), explosion)
gameObjects.append(player)
playerRotated = pygame.transform.rotate(player.image, 30)

waveManager = WaveManager(nextWave)
enemies = []
for i in range(3):
    enemy = Enemy("images/SpacStor.bmp", 1, (101,13,91,59), (screen.get_width() + 91, screen.get_height() + 59), player, waveManager)
    enemies.append(enemy)
    gameObjects.append(enemy)
    player.collisionGroup.append(enemy)

asteroids = []
for i in range(5):
    asteroid = Asteroid("images/Rock2a.bmp", 1, (6,3,80,67), (screen.get_width() + 80, screen.get_height() + 67))
    asteroids.append(asteroid)
    gameObjects.append(asteroid)
    #player.collisionGroup.append(asteroid)

scoreBoardFrames = []
numbersWidth = 30
for i in range(0,10):
    scoreBoardFrames.append(imageLoader("images/numbers.bmp", 1, (numbersWidth * i,0, 30,49)))
    scoreBoardFrames[i].set_colorkey( (0,0,0) )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    #Update Wave Manager
    waveManager.update()

    #Update Objec ts
    for gameObject in gameObjects:
        gameObject.update()

    #Render
    if player.collision:
        screen.fill( (30,0,0) )
    else:
        screen.blit(background.image, (0,0))
    for gameObject in gameObjects:
        screen.blit(gameObject.image, (gameObject.rect.x, gameObject.rect.y))

    #Render Out Score
    firstDigit = waveManager.score % 10
    secondDigit = waveManager.score % 100 - firstDigit
    thirdDigit = waveManager.score % 1000 - firstDigit - secondDigit
    screen.blit(scoreBoardFrames[firstDigit], (64,0))
    screen.blit(scoreBoardFrames[secondDigit / 10], (32,0))
    screen.blit(scoreBoardFrames[thirdDigit / 100], (0,0))
    #Render Out Current Wave
    firstDigit = waveManager.currentWave % 10
    secondDigit = waveManager.currentWave % 100 - firstDigit
    thirdDigit = waveManager.currentWave % 1000 - firstDigit - secondDigit
    screen.blit(scoreBoardFrames[firstDigit], ((800 - 30),0))
    screen.blit(scoreBoardFrames[secondDigit / 10], ((800 - 30) - 32,0))
    screen.blit(scoreBoardFrames[thirdDigit / 100], ((800 - 30) - 64,0))

    pygame.display.flip()

    #Waste Extra Work
    clock.tick(60)
