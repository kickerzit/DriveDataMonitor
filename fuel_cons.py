### FUEL CONSUMPTION ###

from tkinter import *
import ctypes

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
button_color = "#2E4159"
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

# Funkce
def is_int(test_data):
    if type(test_data) is int:
        return True
    else:
        return False

def process_input():
    user_input_value = user_input_price.get()
    if is_int(user_input_value):
        print("String")
    else:
        print("Integer")


def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
    
def save_data():
    # získání dat a uložení do proměnné
    user_input_price_value = user_input_price.get()
    user_input_amount_value = user_input_amount.get()
    user_input_totalkm_value = user_input_totalkm.get()

    # kontrola typu a převod na integer
    if is_int(user_input_price_value) and is_int(user_input_amount_value) and is_int(user_input_totalkm_value):
        pass
    else:
        try:
            user_input_price_value = int(user_input_price_value)
            user_input_amount_value = int(user_input_amount_value)
            user_input_totalkm_value = int(user_input_totalkm_value)
            print(is_int(user_input_price_value))
            print(is_int(user_input_amount_value))
            print(is_int(user_input_totalkm_value))
            # uložení souboru
            with open("drive_data.txt", "w") as file:
                file.write(f"{user_input_price_value}\n")
                file.write(f"{user_input_amount_value}\n")
                file.write(f"{user_input_totalkm_value}")    
        except:  
            Mbox('Chyba', 'Hodnoty mohou být pouze číselné!', 0)

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
user_input_price = Entry(window_drive_data, width=15, borderwidth=3, font=main_font) # Entry - prvek
user_input_price.grid(row=1, column=0, padx=5, pady=5)

user_input_amount = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
user_input_amount.grid(row=2, column=0, padx=5, pady=5)

user_input_totalkm = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
user_input_totalkm.grid(row=3, column=0, padx=5, pady=5)

ok_button = Button(window_drive_data, text="Potvrdit a uložit", borderwidth=2, font=main_font, bg=button_color, fg="white", command=save_data)
ok_button.grid(row=4, column=0, padx=5, pady=5)

# Hlavní cyklus
window_drive_data.mainloop()
