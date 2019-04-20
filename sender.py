import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import os
import numpy as np
from tkinter.filedialog import askopenfilename


def showoptions():

    data = IntVar()
    data2 = IntVar()
    entry1 = Entry(ramka, width=5, textvariable=data)
    entry1.grid(row=0, column=0, sticky=tk.NW)
    text1 = Label(ramka, text="Długośc boku obrazu (px)")
    text1.grid(row=0, column=1)
    entry2 = Entry(ramka, width=5, textvariable=data2)
    entry2.grid(row=1, column=0, sticky=tk.NW)
    text2 = Label(ramka, text="Liczba czarnych pikseli")
    text2.grid(row=1, column=1, sticky=tk.NW)
    generuj = Button(ramka, text="Generuj obrazek", command=lambda:generateimg(data.get(), data2.get()))
    generuj.grid(row=2, column=1, sticky=tk.NW)
    ramka.grid(row=3, column=0, sticky=tk.NW)


def nooptions():
    ramka.grid_forget()


def imgfromfile():
    nooptions()
    filename = askopenfilename(initialdir="/", title="Select file")
    image = Image.open(filename).resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    global label
    label = Label(ramka6, image=photo, borderwidth=2, relief="groove")
    label.image = photo
    label.grid(column=0, row=2, sticky=tk.N)
    img = Image.open(filename).convert('L')
    np_img = np.array(img)
    np_img = ~np_img  # invert B&W
    np_img[np_img > 0] = 1
    global signal
    signal=np_img



def coloredimg():
    nooptions()
    value = []
    for i in range(250 * 250):
      value.append(0)
    global signal
    signal=value.copy()
    plt.imsave('colored_img.png', np.array(value).reshape(250,250), cmap=cm.gray)
    image = Image.open("colored_img.png").resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    label = Label(ramka6, image=photo, borderwidth=2, relief="groove")
    label.image = photo
    label.grid(column=0, row=2, sticky=tk.N)



def generateimg(first, second):
    value = []
    kontrolka = second
    for i in range(first * first):
        if (kontrolka > 0):
            value.append(0)
            kontrolka -= 1
        else:
            value.append(1)
    global signal
    signal = value.copy()
    plt.imsave('temp_img.png', np.array(value).reshape(first,first), cmap=cm.gray)
    image = Image.open("temp_img.png").resize((250, 250))
    photo = ImageTk.PhotoImage(image)
    global label
    label = Label(ramka6, image=photo,borderwidth=2, relief="groove")
    label.image = photo
    label.grid(column=0, row=2, sticky=tk.N)


def send(algorytm,stopien):
    print("=====WYSYLKA DALEJ====")
    print("Sygnal do scramblingu: ")
    print(signal)
    print("O dlugosci: "+str(len(signal)))
    if(algorytm.get()==0):
        print("Algorytm scramblowania: algorytm1")
    if (algorytm.get() == 1):
        print("Algorytm scramblowania: algorytm2")
    print("Stopien zaklocenia: "+stopien+"%")
    print("=====================")

window = tk.Tk()
window.title("Nadawca sygnału")
window.geometry("600x490")


ramka4 = tk.Frame()
version = tk.Label(ramka4, text="Scrambler sender v0.0", fg="grey", width=30, anchor="w")
version.grid(row=0, column=0, sticky=tk.NW)

author = tk.Label(ramka4, text="Karasek, Kamieniecki, Śliwka", fg="grey", anchor="e", width=30)
author.grid(row=0, column=1, sticky=tk.NW)

label1 = tk.Label(ramka4, text="Podgląd obrazu", fg="black", width=28, anchor="center", font=('Verdana', 15, 'bold'))
label1.grid(row=1, column=0)

label2 = tk.Label(ramka4, text="Zródło obrazu: ", fg="black", width=30, anchor="w", font=('Verdana', 15, 'bold'))
label2.grid(row=1, column=1, pady=20)
zrodlo = IntVar()
algorytm = IntVar()

ramka2 = tk.Frame(ramka4)
ramka = tk.Frame(ramka2)
button1 = tk.Radiobutton(ramka2, text="Obraz z pliku", variable=zrodlo, value=1, anchor="w", command=lambda:imgfromfile(),
                         height=2)
button1.grid(row=1, column=0, sticky=tk.NW)
button2 = tk.Radiobutton(ramka2, text="Obraz jednokolorowy", variable=zrodlo, value=0, anchor="w", command=lambda:coloredimg(),
                         height=2)
button2.grid(row=0, column=0, sticky=tk.NW)
button3 = tk.Radiobutton(ramka2, text="Generuj obraz", variable=zrodlo, value=2, anchor="w", command=showoptions,
                         height=2)
button3.grid(row=2, column=0, sticky=tk.NW)

labelka = tk.Label(ramka2, text="Rodzaj scramblingu: ", fg="black", width=30, anchor="w", font=('Verdana', 15, 'bold'))
labelka.grid(row=7, column=0, sticky=tk.NW, pady=20)
button11 = tk.Radiobutton(ramka2, text="Algorytm1", variable=algorytm, value=0, anchor="w", height=2)
button11.grid(row=8, column=0, sticky=tk.NW)
button12 = tk.Radiobutton(ramka2, text="Algorytm2", variable=algorytm, value=1, anchor="w", height=2)
button12.grid(row=9, column=0, sticky=tk.NW)
button13 = tk.Button(ramka2, text="Wyślij", height=3, width=15, fg="#FFFFFF", highlightbackground="#000000",command=lambda:send(algorytm,entry1.get()))
button13.grid(row=10, column=0, sticky=tk.SW, pady=20)
ramka2.grid(column=1, row=2)
ramka6 = tk.Frame(ramka4)
coloredimg()
ramka5 = tk.Frame(ramka6)
entry1 = Entry(ramka5, width=5)
entry1.grid(row=0, column=0, sticky=tk.NW)
entry1.insert(END,'0')
text1 = Label(ramka5, text="% zakłocenia sygnału")
text1.grid(row=0, column=1, sticky=tk.NW)
ramka5.grid(column=0, row=3, pady=10, sticky=tk.N)
ramka6.grid(column=0, row=2, sticky=tk.N)
ramka4.grid(column=0, row=0, sticky=tk.N)

ramka3 = tk.Frame()

ramka3.grid(column=0, row=1)


window.mainloop()