import pygame
import time

g_cipher_panels = []

def LoadCipherPanels():
    g_cipher_panels.append(
        {'active_image': pygame.image.load("red_plate_active.png"),
         'inactive_image': pygame.image.load("red_plate_inactive.png"),
         'is_active': False,
         'starting_pos': (0,0)
         })
    g_cipher_panels.append(
        {'active_image': pygame.image.load("orange_plate_active.png"),
         'inactive_image': pygame.image.load("orange_plate_inactive.png"),
         'is_active': False,
         'starting_pos': (384,0)
         })
    g_cipher_panels.append(
        {'active_image': pygame.image.load("green_plate_active.png"),
         'inactive_image': pygame.image.load("green_plate_inactive.png"),
         'is_active': False,
         'starting_pos': (768,0)
         })
    g_cipher_panels.append(
        {'active_image': pygame.image.load("blue_plate_active.png"),
         'inactive_image': pygame.image.load("blue_plate_inactive.png"),
         'is_active': False,
         'starting_pos': (1152,0)
         })
    g_cipher_panels.append(
        {'active_image': pygame.image.load("purple_plate_active.png"),
         'inactive_image': pygame.image.load("purple_plate_inactive.png"),
         'is_active': False,
         'starting_pos': (1536,0)
         })

def DrawCipherPanels(pygame_screen):  
    for single_panel in g_cipher_panels:
        if single_panel['is_active'] == True:
            pygame_screen.blit(single_panel['active_image'], single_panel['starting_pos'])
        else:
            pygame_screen.blit(single_panel['inactive_image'], single_panel['starting_pos'])
        pygame.display.flip()  


def ResetCipherPanels(pygame_screen):
    for single_panel in g_cipher_panels:
        single_panel['is_active'] = False
        pygame_screen.blit(single_panel['inactive_image'], single_panel['starting_pos'])
        pygame.display.flip()



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
    ResetCipherPanels(screen)

    running = True
    while running:
##        for panel in g_cipher_panels:
##            panel_area = (panel['starting_pos'][0],
##                          panel['starting_pos'][1],
##                          panel['active_image'].get_width(),
##                          panel['active_image'].get_height())
##            
##            pygame.draw.rect(screen,(0,0,0),panel_area)
##            pygame.display.flip()
        ResetCipherPanels(screen)
        time.sleep(2)
        g_cipher_panels[0]['is_active'] = True
        g_cipher_panels[2]['is_active'] = True
        g_cipher_panels[4]['is_active'] = True
        DrawCipherPanels(screen)
        time.sleep(0.5)

        HandleQuit(pygame)

if __name__ == "__main__":
    main()
