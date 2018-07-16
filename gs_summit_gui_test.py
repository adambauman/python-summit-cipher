import tkinter
import tkinter.font
import sys  

#Window Configuration
window = tkinter.Tk()
window.title("GS Summit Test")
window_font_main = tkinter.font.Font(family = "Helvetica", size = 12, weight = "bold")
window.configure(background = "#FFFFFF")
window.attributes("-zoomed", True)
window.attributes("-fullscreen", True)

def ExitButton():
    window.destroy()

#Main Program Loop

    #Cipher Panel Configuration
light_panel_color = '#251400'
dark_panel_color = '#180c00'
panel_1_image = tkinter.PhotoImage(file="./panel1.png")
panel_2_image = tkinter.PhotoImage(file="./panel2.png")
panel_3_image = tkinter.PhotoImage(file="./panel3.png")
panel_4_image = tkinter.PhotoImage(file="./panel4.png")
panel_5_image = tkinter.PhotoImage(file="./panel5.png")

panel_1_label = tkinter.Label(
    window,
    background = light_panel_color,
    image = panel_1_image,
    height = 1080, width = 384)
panel_1_label.grid(row = 0, column = 0, sticky = tkinter.W)

panel_2_label = tkinter.Label(
    window,
    background = dark_panel_color,
    image = panel_2_image,
    height = 1080, width = 384)
panel_2_label.grid(row = 0, column = 1, sticky = tkinter.W)

panel_3_label = tkinter.Label(
    window,
    background = light_panel_color,
    image = panel_3_image,
    height = 1080, width = 384)
panel_3_label.grid(row = 0, column = 2, sticky = tkinter.W)

panel_4_label = tkinter.Label(
    window,
    background = dark_panel_color,
    image = panel_4_image,
    height = 1080, width = 384)
panel_4_label.grid(row = 0, column = 3, sticky = tkinter.W)

panel_5_label = tkinter.Label(
    window,
    background = light_panel_color,
    image = panel_5_image,
    height = 1080, width = 384)
panel_5_label.grid(row = 0, column = 4, sticky = tkinter.W)
    
   
#test_button = tkinter.Button(
#    window,
#    text="EXIT",
#    font = window_font_main,
#    command = ExitButton,
#    bg = "bisque2",
#    height = 500, width = 500)
#cat_image = tkinter.PhotoImage(file="./cat.png")
#test_button["image"] = cat_image
#test_button.grid(row=0, sticky = tkinter.E)

tkinter.mainloop()
