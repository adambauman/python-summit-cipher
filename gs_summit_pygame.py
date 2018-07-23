import pygame
import RPi.GPIO as GPIO
import time

# NOTE: (Adam) Setup
g_answer_count = 5
g_screen_resolution = (1920,1080)
g_fullscreen = False
g_matrix_output_pins = [4,17,27,22,5]
g_matrix_input_pins = [18,23,24,25,12]
g_cipher_panels = []

# NOTE: (Adam) Initialize GPIO
try:
    GPIO.setmode(GPIO.BCM)
    for output_pin in g_matrix_output_pins:
        GPIO.setup(output_pin, GPIO.OUT)
        GPIO.output(output_pin, GPIO.LOW)

    for input_pin in g_matrix_input_pins:
        GPIO.setup(input_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

except:
    print("GPIO setup error, exiting")
    GPIO.cleanup()
    quit()
    

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

# IN pygame.display pygame_screen
def DrawCipherPanels(pygame_screen):  
    for single_panel in g_cipher_panels:
        if single_panel['is_active'] == True:
            pygame_screen.blit(single_panel['active_image'], single_panel['starting_pos'])
        else:
            pygame_screen.blit(single_panel['inactive_image'], single_panel['starting_pos'])
    pygame.display.flip()

# IN pygame.display pygame_screen
def ResetCipherPanels(pygame_screen):
    for single_panel in g_cipher_panels:
        single_panel['is_active'] = False
        pygame_screen.blit(single_panel['inactive_image'], single_panel['starting_pos'])
    pygame.display.flip()

# IN int position_number
# RETURN bool is_active
def ReadAnswerMatrix(position_number):
    is_active = False
    GPIO.output(g_matrix_output_pins[position_number], GPIO.HIGH)
    if GPIO.input(g_matrix_input_pins[position_number]):
        is_active = True
    GPIO.output(g_matrix_output_pins[position_number], GPIO.LOW)
    return is_active

# IN pygame pygame
# RETURN bool quit_requested
def CheckForQuit(pygame):
    quit_requested = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_requested = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            quit_requested = True
    return quit_requested



     
def main():
    pygame.init()
    pygame.display.set_caption("GS Summit Cipher")
    if g_fullscreen:
        screen = pygame.display.set_mode(g_screen_resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(g_screen_resolution)

    LoadCipherPanels()
    ResetCipherPanels(screen)

    quit_requested = False
    while quit_requested == False:
        for answer_position in range(5):
            g_cipher_panels[answer_position]['is_active'] = ReadAnswerMatrix(answer_position)
            
        DrawCipherPanels(screen)
        time.sleep(0.2)
        quit_requested = CheckForQuit(pygame)

    # NOTE: (Adam) Clean-up
    pygame.quit()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
