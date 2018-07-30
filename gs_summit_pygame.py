import pygame
import RPi.GPIO as GPIO
import time

# NOTE: (Adam) Setup
g_answer_count = 5
g_screen_resolution = (1920,1080)
g_fullscreen = True
g_matrix_output_pins = [4,17,27,22,5]
g_matrix_input_pins = [18,23,24,25,12]
g_cipher_panels = []
g_sound_library = {}

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


def LoadSounds():
    g_sound_library["success"] = pygame.mixer.Sound("success_trimmed.ogg")
    g_sound_library["yay"] = pygame.mixer.Sound("yay.ogg")
   

def LoadCipherPanels():
    g_cipher_panels.append(
        {"active_image": pygame.image.load("red_plate_active.png"),
         "inactive_image": pygame.image.load("red_plate_inactive.png"),
         "is_active": False,
         "past_state": False,
         "starting_pos": (0,0)
         })
    g_cipher_panels.append(
        {"active_image": pygame.image.load("orange_plate_active.png"),
         "inactive_image": pygame.image.load("orange_plate_inactive.png"),
         "is_active": False,
         "past_state": False,
         "starting_pos": (384,0)
         })
    g_cipher_panels.append(
        {"active_image": pygame.image.load("green_plate_active.png"),
         "inactive_image": pygame.image.load("green_plate_inactive.png"),
         "is_active": False,
        "past_state": False,
         "starting_pos": (768,0)
         })
    g_cipher_panels.append(
        {"active_image": pygame.image.load("blue_plate_active.png"),
         "inactive_image": pygame.image.load("blue_plate_inactive.png"),
         "is_active": False,
         "past_state": False,
         "starting_pos": (1152,0)
         })
    g_cipher_panels.append(
        {"active_image": pygame.image.load("purple_plate_active.png"),
         "inactive_image": pygame.image.load("purple_plate_inactive.png"),
         "is_active": False,
         "past_state": False,
         "starting_pos": (1536,0)
         })


# IN pygame.mixer.Sound sound
def PlaySound(sound):
    #clock = pygame.time.Clock()
    sound.play()
    # NOTE: (Adam) Before adding pre-init this helped with panel activated/sound sync
    #while pygame.mixer.get_busy():
        #clock.tick(60)


# IN pygame.display pygame_screen, IN g_cipher_panels single_panel
# RETURN bool panel_was_activated
def DrawCipherPanelAction(pygame_screen, single_panel):
    panel_was_activated = False
    panel_was_deactivated = False
    if single_panel["past_state"] == False and single_panel["is_active"] == True:
        panel_was_activated = True
    elif single_panel["past_state"] == True and single_panel["is_active"] == False:
        panel_was_deactivated = True

    if panel_was_activated:
        pygame_screen.blit(single_panel["active_image"], single_panel["starting_pos"])
    elif panel_was_deactivated:
        pygame_screen.blit(single_panel["inactive_image"], single_panel["starting_pos"])

    single_panel["past_state"] = single_panel["is_active"]
    return panel_was_activated
    
    
# IN pygame.display pygame_screen
def DrawCipherPanels(pygame_screen):
    play_success_sound = False
    for single_panel in g_cipher_panels:
        panel_was_activated = DrawCipherPanelAction(pygame_screen, single_panel)
        if panel_was_activated == True:
            play_success_sound = True
        
    if play_success_sound == True:
        PlaySound(g_sound_library["success"])
        
    pygame.display.flip()


# IN pygame.display pygame_screen
def ResetCipherPanels(pygame_screen):
    for single_panel in g_cipher_panels:
        single_panel["is_active"] = False
        pygame_screen.blit(single_panel["inactive_image"], single_panel["starting_pos"])
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
    print("Pygame initializing, please wait...")
    try:
        pygame.display.init()
        pygame.mixer.pre_init(frequency=44100, size=-16, channels=1)
        pygame.mixer.init()
    except:
        print("Pygame failed to initialize...")
        quit()
    print("Pygame initialization successful!")
    
    pygame.display.set_caption("GS Summit Cipher")
    pygame.mouse.set_visible(False)
    if g_fullscreen:
        screen = pygame.display.set_mode(g_screen_resolution, pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode(g_screen_resolution)

    LoadCipherPanels()
    LoadSounds()
    ResetCipherPanels(screen)
    #NOTE: (Adam) Have had this issue before, need to prime with a single sound before mixer functions
    PlaySound(g_sound_library["yay"])

    quit_requested = False
    while quit_requested == False:
        for answer_position in range(g_answer_count):
            g_cipher_panels[answer_position]["is_active"] = ReadAnswerMatrix(answer_position)
            
        DrawCipherPanels(screen)
        #NOTE: (Adam) Might not need delay to stop GPIO hammering with pygame in play
        time.sleep(0.2)
        quit_requested = CheckForQuit(pygame)
        


    # NOTE: (Adam) Clean-up
    pygame.quit()
    GPIO.cleanup()

if __name__ == "__main__":
    main()
