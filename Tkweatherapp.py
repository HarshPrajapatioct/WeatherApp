from tkinter import *
from tkinter import ttk
import requests

def  data_get():
        API_key = ''#Add your Open weather app api key here
        city = city_name.get()
        data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={API_key}").json()
        w_label1.config(text=data["weather"][0]["main"])
        wb_label1.config(text=data["wind"]["speed"])
        temp_label1.config(text=data["main"]["temp"])
        press_label1.config(text=data["main"]["pressure"])
        humidity_label1.config(text=str(data["main"]["humidity"]))
    
    
win = Tk()
win.title("Weather app")
win.config(bg = "skyblue")
win.geometry("500x500")

name_label = Label(win,text="Weather App", font=("Time New Roman",40,"bold"),bg="skyblue",fg="blue")
name_label.place(x=25,y=45,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Mumbai","Ahmedabad","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
comm = ttk.Combobox(win,text="Weather App", values=list_name,font=("Time New Roman",25),textvariable=city_name)
comm.place(x=50,y=120,height=50,width=400)

button1 = ttk.Button(win,text="Search",command=data_get)
button1.place(x=200,y=180,height=30,width=100)

w_label = Label(win,text="Weather : ", font=("Time New Roman",15),bg="skyblue",fg="blue")
w_label.place(x=110,y=220,height=30,width=150)

w_label1 = Label(win,text="", font=("Time New Roman",15),bg="skyblue",fg="blue")
w_label1.place(x=230,y=220,height=30,width=110)

wb_label = Label(win,text="Wind : ", font=("Time New Roman",15),bg="skyblue",fg="blue")
wb_label.place(x=100,y=250,height=30,width=150)

wb_label1 = Label(win,text="", font=("Time New Roman",15),bg="skyblue",fg="blue")
wb_label1.place(x=200,y=250,height=30,width=150)



temp_label = Label(win,text="Temprature(F): ", font=("Time New Roman",15),bg="skyblue",fg="blue")
temp_label.place(x=92,y=280,height=30,width=150)

temp_label1 = Label(win,text="", font=("Time New Roman",15),bg="skyblue",fg="blue")
temp_label1.place(x=230,y=280,height=30,width=110)

press_label = Label(win,text="Pressure : ", font=("Time New Roman",15),bg="skyblue",fg="blue")
press_label.place(x=100,y=310,height=30,width=150)

press_label1 = Label(win,text="", font=("Time New Roman",15),bg="skyblue",fg="blue")
press_label1.place(x=230,y=310,height=30,width=110)

humidity_label = Label(win,text="Humidity : ", font=("Time New Roman",15),bg="skyblue",fg="blue")
humidity_label.place(x=100,y=340,height=30,width=150)

humidity_label1 = Label(win,text="", font=("Time New Roman",15),bg="skyblue",fg="blue")
humidity_label1.place(x=230,y=340,height=30,width=110)

win.mainloop()