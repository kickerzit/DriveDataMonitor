### FUEL CONSUMPTION ###

from tkinter import *
import ctypes
import time
import json
from calculations import *


# Paleta barev: #5075BF modrá, #5377A6 šedomodrá, #2E4159 tmavě modrá, #6D7E8C šedá, #D8E6F2 světlá

# Okno: Zadání údajů pro spotřebu paliva
window_drive_data = Tk()
window_drive_data.title("DriveDataMonitor"),
window_drive_data.minsize(width=800, height=600)
window_drive_data.maxsize(width=800, height=600)
window_drive_data.iconbitmap("./icons/icon.ico")
window_drive_data.resizable(False, False)

main_color = "#6D7E8C"
color_a = "#5377A6"
color_b = "#5075BF"
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

# test datového typu float
def is_flt(test_data):
    if type(test_data) is float:
        return True
    else:
        return False

def process_input(labels):
    inputs = labels(labels[0], labels[1], labels[2])
    user_input_value = inputs.user_input_price.get()
    if is_flt(user_input_value):
        print("String")
    else:
        print("Float")

# datum a čas
def date():
    date = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
    return date

# Chybová hláška: Pouze čísla
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)

def save_data(labels):
    global json_data

    inputs = labels(labels[0], labels[1], labels[2])
    # získání dat a uložení do proměnné
    user_input_price_value = inputs.user_input_price.get()
    user_input_amount_value = inputs.user_input_amount.get()
    user_input_totalkm_value = inputs.user_input_totalkm.get()
    
    formatted_date = date()
    try:
        user_input_price_value = float(user_input_price_value)
        user_input_amount_value = float(user_input_amount_value)
        user_input_totalkm_value = float(user_input_totalkm_value)

            # vytvoření JSON objektu pro aktuální záznam
        json_data = {
            "Datum": formatted_date,
            "Cena": user_input_price_value,
            "Mnozstvi": user_input_amount_value,
            "Pocet km": user_input_totalkm_value
        }
        # smažeme vstupy
        inputs.user_input_price.delete(0, END)
        inputs.user_input_amount.delete(0, END)
        inputs.user_input_totalkm.delete(0, END)

        print(json_data)

        save_list() # uloží nové hodnoty do listu
        #reload_data() 

    except:
        Mbox('Chyba řádek 96', 'Hodnoty mohou být pouze číselné!', 0)

# funkce pro uložení seznamu do souboru
def save_list():

    # otevření souboru pro čtení a uložení do listu
    with open("drive_data.json", "r") as file:
        # zápis seznamu jako JSON pole
        json_read = json.load(file)
        json_read.append(json_data)
        print(json_read)
        
    # otevření souboru pro zápis finálních dat
    with open("drive_data.json", "w") as file:  
        json.dump(json_read, file, indent=4)  # indent=4 pro přehlednější formátování


# Label: Zadej údaje pro spotřebu paliva
def labels():
    #data_frame_instance = data_frame()
    #vypocty = calc(data_frame_instance[0], data_frame_instance[1], data_frame_instance[2])
        # Nadpis 
    main_label_drive_data = Label(window_drive_data, text="Zadej údaje pro spotřebu paliva", bg=main_color, fg="white", font=(main_font, 23, "bold"))
    main_label_drive_data.grid(row=0, column=0, padx=200, pady=5, sticky=N)

        # Popisky
    label_01_drive_data = Label(window_drive_data, text="Zadej cenu za litr: ", bg=color_a, fg="white", font=(main_font, 15))
    label_02_drive_data = Label(window_drive_data, text="Zadej počet natankovaných litrů: ", bg=color_a, fg="white", font=(main_font, 15))
    label_03_drive_data = Label(window_drive_data, text="Zadej celkový počet ujetých km: ", bg=color_a, fg="white", font=(main_font, 15))
    label_04_drive_data = Label(window_drive_data, text=f"Celková cena za rok {choose_year}: ", bg=color_b, fg="white", font=(main_font, 15))
    label_05_drive_data = Label(window_drive_data, text=f"Průměrná měsíční cena v roce {choose_year}: ", bg=color_b, fg="white", font=(main_font, 15))
    label_06_drive_data = Label(window_drive_data, text="Měsíční průměrná cena za celou dobu: ", bg=color_b, fg="white", font=(main_font, 15))
    label_07_drive_data = Label(window_drive_data, text="Celková cena: ", bg=color_b, fg="white", font=(main_font, 15))



    label_01_drive_data.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    label_02_drive_data.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    label_03_drive_data.grid(row=3, column=0, padx=5, pady=5, sticky=W)
    label_04_drive_data.grid(row=5, column=0, padx=5, pady=5, sticky=W)
    label_05_drive_data.grid(row=6, column=0, padx=5, pady=5, sticky=W)
    label_06_drive_data.grid(row=7, column=0, padx=5, pady=5, sticky=W)
    label_07_drive_data.grid(row=8, column=0, padx=5, pady=5, sticky=W)

    # Výpočty (labels)
    average_consumption_label = Label(window_drive_data, text=suma_rok, bg=button_color, fg="white", font=(main_font, 15))
    average_monthly_price_label = Label(window_drive_data, text=average_monthly, bg=button_color, fg="white", font=(main_font, 15))
    average_cons_alltime_label = Label(window_drive_data, text=y, bg=button_color, fg="white", font=(main_font, 15))
    total_price_label = Label(window_drive_data, text=x, bg=button_color, fg="white", font=(main_font, 15))

    average_consumption_label.grid(row=5, column=0, padx=5, pady=5)
    average_monthly_price_label.grid(row=6, column=0, padx=5, pady=5)
    average_cons_alltime_label.grid(row=7, column=0, padx=5, pady=5)
    total_price_label.grid(row=8, column=0, padx=5, pady=5)

    # Input frame
    user_input_price = Entry(window_drive_data, width=15, borderwidth=3, font=main_font) # Entry - prvek
    user_input_price.grid(row=1, column=0, padx=5, pady=5)

    user_input_amount = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
    user_input_amount.grid(row=2, column=0, padx=5, pady=5)

    user_input_totalkm = Entry(window_drive_data, width=15, borderwidth=3, font=main_font)
    user_input_totalkm.grid(row=3, column=0, padx=5, pady=5)

    ok_button = Button(window_drive_data, text="Potvrdit a uložit", borderwidth=2, font=main_font, bg=button_color, fg="white", command=save_data)
    ok_button.grid(row=4, column=0, padx=5, pady=5)

    return user_input_price, user_input_amount, user_input_totalkm



def reload_data():
        print("reload_data started")
        with open('drive_data.json', 'r') as file:
            data = json.load(file)
            print("json file loaded")
            print(data)
            print(suma_rok)
            print(average_monthly)
            print(y)
            print(x)
            calc()
            print("konec reload_data")
            '''average_consumption_label.set
            average_monthly_price_label.set(average_monthly)
            average_cons_alltime_label.set(y)
            total_price_label.set(x)'''

            '''average_consumption_label = Tk.StringVar()
            average_monthly_price_label = Tk.StringVar()
            average_cons_alltime_label = Tk.StringVar()
            total_price_label = Tk.StringVar()'''

            '''suma_rok = float(suma_rok)
            average_monthly = float(average_monthly)
            y = float(y)
            x = float(x)     
            average_consumption_label = Label(window_drive_data, text=suma_rok, bg=button_color, fg="white", font=(main_font, 15))
            average_monthly_price_label = Label(window_drive_data, text=average_monthly, bg=button_color, fg="white", font=(main_font, 15))
            average_cons_alltime_label = Label(window_drive_data, text=y, bg=button_color, fg="white", font=(main_font, 15))
            total_price_label = Label(window_drive_data, text=x, bg=button_color, fg="white", font=(main_font, 15))

            average_consumption_label.grid(row=5, column=0, padx=5, pady=5)
            average_monthly_price_label.grid(row=6, column=0, padx=5, pady=5)
            average_cons_alltime_label.grid(row=7, column=0, padx=5, pady=5)
            total_price_label.grid(row=8, column=0, padx=5, pady=5)'''


# Hlavní cyklus

labels()
window_drive_data.mainloop()


'''# pokud se v souboru nic nenachází, vytvoří se nový list
def json_list():
    global json_read    
    with open("drive_data.json", "r") as file:
            try:
                json_read = json.load(file)
                json_read = []
            except json.JSONDecodeError:
                # Pokud je obsah neplatný JSON, vytvoříme prázdný seznam
                json_read = []
                # Uložení prázdného seznamu, pokud soubor byl prázdný
                with open("drive_data.json", "w") as file:
                    json.dump(json_read, file) '''          
