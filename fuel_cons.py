### FUEL CONSUMPTION ###

from tkinter import *

# Paleta barev: #5075BF modrá, #5377A6 šedomodrá, #2E4159 tmavě modrá, #6D7E8C šedá, #D8E6F2 světlá


# Okno: Zadání údajů pro spotřebu paliva
window_drive_data = Tk()
window_drive_data.title("DriveDataMonitor"),
window_drive_data.minsize(width=800, height=600)
window_drive_data.maxsize(width=800, height=600)
window_drive_data.iconbitmap(".\icons\icon.ico")
window_drive_data.resizable(False, False)

main_color = "#6D7E8C"
color_a = "#5377A6"
main_font = "Calibri"

window_drive_data.config(bg=main_color)

""" 
# Framy - záleží na uspořádání z vrchu dolů (sestupně)
input_frame = Frame(window_drive_data, bg=main_color)
text_frame = Frame(window_drive_data, bg=main_color)
button_frame = Frame(window_drive_data, bg=main_color)
main_label_frame = Frame(window_drive_data, bg=main_color)
main_label_frame.pack()
button_frame.pack()
input_frame.pack()
text_frame.pack(anchor="w") # w - zarovnání framu doleva """


# Label: Zadej údaje pro spotřebu paliva
    # Nadpis 
main_label_drive_data = Label(window_drive_data, text="Zadej údaje pro spotřebu paliva", bg=main_color, fg="white", font=(main_font, 23, "bold"))
main_label_drive_data.grid(row=0, column=0, padx=200, pady=5, sticky=N)

    # Popisky
label_01_drive_data = Label(window_drive_data, text="Zadej cenu za litr: ", bg=color_a, fg="white", font=(main_font, 15))
label_02_drive_data = Label(window_drive_data, text="Zadej počet natankovaných litrů: ", bg=color_a, fg="white", font=(main_font, 15))
label_03_drive_data = Label(window_drive_data, text="Zadej celkový počet ujetých km: ", bg=color_a, fg="white", font=(main_font, 15))

label_01_drive_data.grid(row=1, column=0, padx=5, pady=5, sticky=W)
label_02_drive_data.grid(row=2, column=0, padx=5, pady=5, sticky=W)
label_03_drive_data.grid(row=3, column=0, padx=5, pady=5, sticky=W)

# Input frame
user_input_price = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
user_input_price.grid(row=1, column=0, padx=5, pady=5)

user_input_amount = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
user_input_amount.grid(row=2, column=0, padx=5, pady=5)

user_input_totalkm = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
user_input_totalkm.grid(row=3, column=0, padx=5, pady=5)




# Hlavní cyklus
window_drive_data.mainloop()
