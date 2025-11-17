def text(screen, font, msg, x, y, color=(255,255,255)):
    surf = font.render(msg, True, color)
    screen.blit(surf, (x, y))
