import pygame
import time

g_cipher_panels = []

def LoadCipherPanels():
    g_cipher_panels.append(
        {'image': pygame.image.load("panel1.png"),
         'is_active': False,
         'starting_pos': (0,0)
         })
    g_cipher_panels.append(
        {'image': pygame.image.load("panel2.png"),
         'is_active': False,
         'starting_pos': (384,0)
         })
    g_cipher_panels.append(
        {'image': pygame.image.load("panel3.png"),
         'is_active': False,
         'starting_pos': (768,0)
         })
    g_cipher_panels.append(
        {'image': pygame.image.load("panel4.png"),
         'is_active': False,
         'starting_pos': (1152,0)
         })
    g_cipher_panels.append(
        {'image': pygame.image.load("panel5.png"),
         'is_active': False,
         'starting_pos': (1536,0)
         })

def DrawCipherPanels(pygame_screen):
    for single_panel in g_cipher_panels:
        pygame_screen.blit(single_panel['image'], single_panel['starting_pos'])

def HandleQuit(pygame):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

     
def main():
    pygame.init()
    pygame.display.set_caption("GS Summit Cipher")
    screen = pygame.display.set_mode((1920, 900))
    screen.fill((0,128,128))

    LoadCipherPanels()
    DrawCipherPanels(screen)
    pygame.display.flip()

    running = True
    while running:
        for panel in g_cipher_panels:
            panel_area = (panel['starting_pos'][0],
                          panel['starting_pos'][1],
                          panel['image'].get_width(),
                          panel['image'].get_height())
            
            pygame.draw.rect(screen,(0,0,0),panel_area)
            pygame.display.flip()
            time.sleep(0.5)

        DrawCipherPanels(screen)
        pygame.display.flip()
        time.sleep(0.5)

        HandleQuit(pygame)

if __name__ == "__main__":
    main()
