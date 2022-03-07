from tkinter import *
import tkinter
import json
from tkinter import font
import requests
from ttkthemes import themed_tk as tk
from tkinter import ttk

def update():
    
        res = requests.get("https://freecurrencyapi.net/api/v2/latest?apikey=5f880ac0-9921-11ec-8d8a-a5086e90d9d6",params={"base-currency":"USD"})
        datafromserver = res.json()
        BHD = datafromserver['data']['BHD']
       
        OMR= datafromserver['data']['OMR']
     
        JOD= datafromserver['data']['JOD']
     
        GBP= datafromserver['data']['GBP']
        
        KYD= datafromserver['data']['KYD']
      
        EUR= datafromserver['data']['EUR']
      
        CHF = datafromserver['data']['CHF']
        
        INR = datafromserver['data']['INR']
        
        currencies=[BHD,OMR,JOD,GBP,KYD,EUR,CHF,INR]
       
        print(currencies)
        
        E1.delete(0,END)
        E1.insert(0,BHD)
        
        E2.delete(0, END)
        E2.insert(0, OMR)
        
        E3.delete(0,END)
        E3.insert(0,JOD)
        
        E4.delete(0, END)
        E4.insert(0, GBP)
        
        E5.delete(0,END)
        E5.insert(0,KYD)
        
        E6.delete(0,END)
        E6.insert(0,EUR)
        
        E7.delete(0, END)
        E7.insert(0, CHF)
        
     
        E8.delete(0,END)
        E8.insert(0,INR)
       
        
        window.after(1000,update)
      

window = tk.ThemedTk()
window.get_themes()
window.set_theme("plastik")
window.title("CURRENCY DASHBOARD")
window.geometry('800x500')

mainlabel = ttk.Label(window, text="Currency Dashboard",font=("Arial", 30))
mainlabel.grid(row=0,columnspan=5)

L1 = ttk.Label(window, text="BHD",font=("Arial",15))
L1.grid(row=1, column=1, padx=80, pady=25)
E1 = ttk.Entry(window,font=("Arial", 15))
E1.grid(row=2,column=1,padx=80)


L2 = ttk.Label(window, text="OMR",font=("Arial",15))
L2.grid(row=3, column=1, padx=80, pady=25)
E2 = ttk.Entry(window,font=("Arial", 15))
E2.grid(row=4,column=1,padx=80)


L3 = ttk.Label(window, text="JOD",font=("Arial",15))
L3.grid(row=5, column=1, padx=80, pady=25)
E3 = ttk.Entry(window,font=("Arial", 15))
E3.grid(row=6,column=1,padx=80)


L4 = ttk.Label(window, text="GBP",font=("Arial",15))
L4.grid(row=7,column=1,padx=80, pady=25)
E4 = ttk.Entry(window,font=("Arial", 15))
E4.grid(row=8, column=1, padx=80)


L5 = ttk.Label(window, text="KYD", font=("Arial", 15))
L5.grid(row=1,column=2,padx=80, pady=25)
E5 = ttk.Entry(window,font=("Arial", 15))
E5.grid(row=2, column=2, padx=80)


L6 = ttk.Label(window, text="EUR", font=("Arial", 15))
L6.grid(row=3,column=2,padx=80, pady=25)
E6 = ttk.Entry(window,font=("Arial", 15))
E6.grid(row=4, column=2, padx=80)


L7 = ttk.Label(window, text="CHF", font=("Arial", 15))
L7.grid(row=5,column=2,padx=80, pady=25)
E7 = ttk.Entry(window,font=("Arial", 15))
E7.grid(row=6, column=2, padx=80)


L8 = ttk.Label(window, text="INR", font=("Arial", 15))
L8.grid(row=7, column=2, padx=80, pady=25)
E8 = ttk.Entry(window,font=("Arial", 15))
E8.grid(row=8, column=2, padx=80)

update()

window.mainloop()


