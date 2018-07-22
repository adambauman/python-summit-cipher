import RPi.GPIO as GPIO
import time

g_matrix_output_pins = [4,17,27,22,5]
g_matrix_input_pins = [18,23,24,25,12]

g_keep_running = True

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


def ReadAnswerMatrix(position_number):
    is_active = False
    GPIO.output(g_matrix_output_pins[position_number], GPIO.HIGH)
    if GPIO.input(g_matrix_input_pins[position_number]):
        is_active = True
    GPIO.output(g_matrix_output_pins[position_number], GPIO.LOW)
    return is_active
                  
        
print("Starting up!")
while g_keep_running:
    answer_matrix = {}
    for answer_position in range(5):
        answer_matrix[answer_position] = ReadAnswerMatrix(answer_position)

    for answer in range(5):
        if answer_matrix[answer] == True:
            print(answer, " is correct")
        else:
            print(answer, " is incorrent")

    time.sleep(3)
    print("")
    print("")
