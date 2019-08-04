import pygame

def imageLoader(image, scale, clip):
    asset = pygame.image.load(image)
    playerClipped = pygame.Surface( (clip[2],clip[3]) )
    playerClipped.blit(asset, (0,0), clip)
    scaledAsset = (clip[2] * scale, clip[3] * scale)
    scaledAsset = pygame.transform.scale(playerClipped, (clip[2] * scale, clip[3] * scale))

    return scaledAsset
