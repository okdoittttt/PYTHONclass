from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pytz
from timezonefinder import TimezoneFinder
from datetime import datetime
from geopy.geocoders import Nominatim

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
# root.configure(bg='black')
root.resizable(False, False)

def getWeather():
    try:
        city = textfield.get()
        api = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=6fe6f8dc606fd5d52f7429fbeca908a8"

        # 날씨 정보 출력하기
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # t.config(text=(temp, "℃"))
        c.config(text=(condition, "|", "FEELS", "LIKE", temp, "℃"))

        if temp >= 0 and temp <= 15:
            t = Label(font=("arial", 70, "bold"), fg="white")
            t.config(text=(temp, "℃"))
            t.place(x=370, y=150)
        elif temp >= 16 and temp <= 30:
            t = Label(font=("arial", 70, "bold"), fg="green")
            t.config(text=(temp, "℃"))
            t.place(x=370, y=150)
        elif temp >= 31:
            t = Label(font=("arial", 70, "bold"), fg="#ee666d")
            t.config(text=(temp, "℃"))
            t.place(x=370, y=150)

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception:
        messagebox.showerror("정확한")
        textfield.focus()


# 검색 박스
Search_image=PhotoImage(file="search.png")
myimage=Label(image=Search_image)
myimage.place(x=200, y=20)

# 검색 박스에 Entry 부여
border_color = Frame(root, background="red")
textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#101010", border=0, fg="white")
textfield.place(x=290, y=40)
textfield.focus()

Search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=630, y=31)

# 하단 박스
Frame_image = PhotoImage(file="box.png")
frame_image = Label(image=Frame_image)
frame_image.pack(padx=5, pady=5, side=BOTTOM)

# 기온 이미지

# Label 부여하기
label_wind = Label(root, text="WIND", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_wind.place(x=120, y=400)
label_hum = Label(root, text="HUMIDITY", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_hum.place(x=250, y=400)
label_des = Label(root, text="DESCRIPTION", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_des.place(x=430, y=400)
label_press = Label(root, text="PRESSURE", font=("Helvetica", 15, 'bold'), fg="white", bg="#1ab5ef")
label_press.place(x=650, y=400)

# t = Label(font=("arial", 70, "bold"), fg="#ee666d")
# t.place(x=370, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=370, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()
