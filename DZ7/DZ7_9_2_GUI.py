# После первого запроса подгружается список досупных валют

import tkinter as tk
from tkinter.ttk import Combobox
import requests


def load():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()        
    s = [i for i in  data['Valute'].keys()]
    combo['values'] = (s)    
    if ent_valute.get() == '':
        znak = combo.get()
    else:
        znak = ent_valute.get()
    lbl_out.config(text=format(data['Valute'][znak]['Name'] + ' '+ str(data['Valute'][znak]['Value'])), font=("Arial", 20), relief=tk.RIDGE, borderwidth=10)


window = tk.Tk()
window.title("Курс валют")
frame_a = tk.Frame()
frame_b = tk.Frame(relief=tk.SUNKEN, borderwidth=10)
lbl_valute = tk.Label(master=frame_a, text="Введите или выберите валюту", font=("Arial", 20), relief=tk.RIDGE , borderwidth=10)
lbl_valute.pack(fill=tk.X, padx=5, pady=5)
ent_valute = tk.Entry(master=frame_b, bg='Azure', font=("Arial", 15), relief=tk.SUNKEN, borderwidth=10)
ent_valute.pack(fill=tk.X, side=tk.LEFT, padx=5, pady=5)
combo = Combobox(master=frame_b, font=("Arial", 20))
combo['values'] = ('USD', 'EUR', 'GBP', 'JPY')
combo.current(0)  # установите вариант по умолчанию 
combo.pack(fill=tk.X, padx=5, pady=5)
frame_a.pack(fill=tk.X)
frame_b.pack(fill=tk.X)
btn = tk.Button(text="Получить курс", font=30, command=load)
btn.pack(padx=5, pady=5)
lbl_out = tk.Label(text="Текущий курс", font=("Arial", 20), relief=tk.RIDGE, borderwidth=10)
lbl_out.pack(fill=tk.X, padx=5, pady=5)
window.mainloop()