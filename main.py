from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image

celcius = 0
fahrenheit = 32
kelvin = round(273.15)


def update_elements(celcius,fahrenheit,kelvin):
    labelV1.config(text=f"{int(celcius)}°C")
    labelV2.config(text=f"{int(fahrenheit)}°F")
    labelV3.config(text=f"{round(float(kelvin))}°K")
    scale['value'] = celcius
    scalef['value'] = (fahrenheit / 212) * 100
    scalek['value'] = (kelvin / 373.15) * 100


def celcius_to_other(value):
    global celcius
    celcius = scale.get()
    fahrenheit = (celcius * 9/5) + 32
    kelvin  = celcius + 273
    update_elements(celcius,fahrenheit,kelvin)


def fahrenheit_to_other(value):
    global fahrenheit
    fahrenheit = scalef.get()
    celcius = (fahrenheit -32) * 5/9
    kelvin = (fahrenheit -32) * 5/9 + 273.15
    update_elements(celcius,fahrenheit,kelvin)


def kelvin_to_other(value):
    global kelvin
    kelvin = scalek.get() + 1
    celcius = (kelvin - 273.15)
    fahrenheit = (((kelvin - 273.15) * 9/5) + 32)
    update_elements(celcius, fahrenheit, kelvin)


root = Tk()
root.title("Temperature Converter")
root.minsize(450,600)
root.maxsize(450,600)
root.configure(background='#FFE98F')
i = Image.open("logo.png")
rimg = i.resize((350,150))
img = ImageTk.PhotoImage(rimg)
logo_label = Label(root,image=img,background="#FFE98F")
logo_label.pack()


#               ---------------------- CELCIUS ----------------------

label0 = Label(root,text="Celcius",fg="#FF0000",bg="#FFE98F",font=('verdana',24))
label0.pack(pady=10)


thermometerimg = Image.open("thermometer.png")
resizethermometer = thermometerimg.resize((400,50))
thermometer = ImageTk.PhotoImage(resizethermometer)
thermometer_label1 = Label(root,image=thermometer,background="#FFE98F")
thermometer_label1.pack()

scale = ttk.Scale(root,orient='horizontal',from_=-200,to=200,command=celcius_to_other,length=260)
scale.place(x=50,y=230)


labelV1 = Label(root,text=f"{celcius}°C",fg="#FF0000",bg="#FFE98F",font=('verdana',24,'bold'))
labelV1.place(x=340,y=185)


#               ---------------------- Fahrenheit ----------------------

label1 = Label(root,text="Fahrenheit",fg="#FF0000",bg="#FFE98F",font=('verdana',24))
label1.pack(pady=10)


thermometerimg1 = Image.open("thermometer.png")
resizethermometer1 = thermometerimg1.resize((400,50))
thermometer1 = ImageTk.PhotoImage(resizethermometer1)
thermometer_label2 = Label(root,image=thermometer1,background="#FFE98F")
thermometer_label2.pack()

scalef = ttk.Scale(root,orient='horizontal',from_=-200,to=300,command=fahrenheit_to_other,length=260)
scalef.place(x=50,y=346)

labelV2 = Label(root,text=f"{fahrenheit}°F",fg="#FF0000",bg="#FFE98F",font=('verdana',24,'bold'))
labelV2.place(x=335,y=285)


#               ---------------------- Kelvin ----------------------

label2 = Label(root,text="Kelvin",fg="#FF0000",bg="#FFE98F",font=('verdana',24))
label2.pack(pady=10)

thermometerimg2 = Image.open("thermometer.png")
resizethermometer2 = thermometerimg2.resize((400,50))
thermometer2 = ImageTk.PhotoImage(resizethermometer2)
thermometer_label3 = Label(root,image=thermometer2,background="#FFE98F")
thermometer_label3.pack()

scalek = ttk.Scale(root,orient='horizontal',from_=-300,to=400,command=kelvin_to_other,length=260)
scalek.place(x=50,y=455)

labelV3 = Label(root,text=f"{kelvin}°K",fg="#FF0000",bg="#FFE98F",font=('verdana',24,'bold'))
labelV3.place(x=300,y=400)

root.mainloop()
