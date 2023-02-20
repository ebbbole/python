import pygame  
  
pygame.init()  ## used to initialize all the required module
screen = pygame.display.set_mode((1000, 600))   ## set the window desired size

background = pygame.image.load('images/img.jpg')
pygame.display.set_caption("Twitsy")
icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(icon)

done = False  
  
while not done:  
    for event in pygame.event.get():   ## empty the event queue
        if event.type == pygame.QUIT:  
            done = True  
    pygame.draw.rect(screen, (100, 255, 0), pygame.Rect(250, 255, 0, 10)) 
    #load the fonts  
    font = pygame.font.SysFont("Acari Sans", 80)  
    font_caption = pygame.font.SysFont("Acari Sans", 20)  
    font2 = pygame.font.SysFont("Andalus", 20)  
    # Render the text in new surface  
    main_text = font.render("Twitsy", True, (255, 255, 255))
    caption = font_caption.render("Say Anything", True, (255, 255, 255))
    copyright = font2.render("Copyright. 2023", True, (255, 255, 255))
    screen.blit(background, (0,0))
    screen.blit(main_text,(main_text.get_width() //10, 100-main_text.get_height()))
    screen.blit(caption,(30+caption.get_width() //10, 75+caption.get_height()))
    screen.blit(copyright,(50-copyright.get_width() //10, 550+copyright.get_height()))

    pygame.display.flip() ## make all the changes avalible for scree