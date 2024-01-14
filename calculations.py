import pandas as pd
import json
import time

def date():
    date = time.strftime("%Y", time.localtime())
    return date

# načtení a otevření souboru drive_data.json
# pokud v drive_data.json nic není, vytvoří se nový list s keys a prázdnými values
def first_load():
    global data
    try:
        with open("drive_data.json", "r") as file:
            print("JSON soubor téměř načten")
            content = json.load(file)
            print("JSON soubor načten")
            if content:
                data = content
                print("Data jsou načtena")
            else:
                pass
    except Exception as e:
        print(f"Chyba při načítání JSON souboru: {e}")
        data = [
            {
                "Datum": "",
                "Cena": 0,
                "Mnozstvi": 0,
                "Pocet km": 0
            }
        ]
        with open("drive_data.json", "w") as file:
            json.dump(data, file)    
#first_load()

def data_frame():
   with open("drive_data.json", "r") as file:
         content = json.load(file)
         data = content
   # vytvoření DataFrame
   df = pd.DataFrame(data)

   # Převeďte sloupec 'Datum' na typ datetime
   df['Datum'] = pd.to_datetime(df['Datum'], dayfirst=True)

   # Vytvořte sloupec 'Rok' s rokem z data
   df['Rok'] = df['Datum'].dt.year #vytvoří sloupec 'Rok'

   # Vytvoření sloupce Cena celkem
   df['Cena celkem'] = df['Cena'] * df['Mnozstvi']

   # proměnná pro konkrétní rok
   choose_year = 2024

   # Seskupení řádků podle roku 2024
   filter_year = df[df['Rok'] == choose_year] # v podstatě filtr 

   print(df)
   print(filter_year)
   print(choose_year)
   return df, filter_year, choose_year

#data_frame()
# Zápisy do proměnných
def docasna_funkce():
   cena_litr = df.get('Cena')
   mnozstvi = df.get('Mnozstvi')
   pocet_km = df.get('Pocet km')

   # Výpočty
   x = ((cena_litr)*(mnozstvi)).sum()
   print(f'Celková cena: {x}')

   y = (x/len(df)).round(2)
   print(f'Měsíční průměrná cena za celou dobu: {y}')

   # Získání součtu hodnot pro rok 2023
   suma_rok = filter_year['Cena celkem'].sum()
   print(f'Celková cena za rok {choose_year}: {suma_rok}')

   # Získání měsíčního průměru pro určitý rok
   average_monthly = (suma_rok / len(filter_year['Cena celkem'])).round(2)
   print(f'Průměrná měsíční cena v roce {choose_year}: {average_monthly}')

def calc(df, filter_year, choose_year):
    # Zápisy do proměnných
   cena_litr = df.get('Cena')
   mnozstvi = df.get('Mnozstvi')
   pocet_km = df.get('Pocet km')

   # Výpočty
   x = ((cena_litr)*(mnozstvi)).sum()
   print(f'Celková cena: {x}')

   y = (x/len(df)).round(2)
   print(f'Měsíční průměrná cena za celou dobu: {y}')

   # Získání součtu hodnot pro rok 2023
   suma_rok = filter_year['Cena celkem'].sum()
   print(f'Celková cena za rok {choose_year}: {suma_rok}')

   # Získání měsíčního průměru pro určitý rok
   average_monthly = (suma_rok / len(filter_year['Cena celkem'])).round(2)
   print(f'Průměrná měsíční cena v roce {choose_year}: {average_monthly}')

   return cena_litr, mnozstvi, pocet_km, x, y, suma_rok, average_monthly


#print(calc_instance)
#calc()
#print(df.head())

# Výpočet celkového poctu najetých km za určitý rok
#def km_year():
#      celkem_km_za_rok = filter_year['Pocet km'].sum()
#      if km_year_final not celkem_km_za_rok:
            



#print(f'Celkový počet najetých km za rok {date()}: {km_year}')


