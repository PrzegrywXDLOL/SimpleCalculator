from tkinter import *
wyswietlacz = [] #tablica działająca jako wyświetlacz kalkulatora

liczba = None #liczba zapamiętywana w "pamięci" kalkulatora

dzialanie = "" #zmienna pomagająca określić jakie działanie jest wykonywane

#określenie ile jest liczb w wyświtlaczu przed przecinkiem
def liczbyprzed():
    i = 0
    while i < len(wyswietlacz):
            if wyswietlacz[i] == ".":
                break
            else:
                i = i + 1
    if wyswietlacz.count("-") > 0:
        i = i - 1
    return i

#określenie sprawdzanmie czy po przecinku jest tylko 0
def czyjest0(ciag):
    i = 0
    while i < len(ciag):
        i = i + 1
        if ciag[i] == ".":
            i = i + 1
            y = 0
            while i < len(ciag):
                if ciag[i] == "0":  
                    i = i + 1
                else:
                    y = y + 1
                    i = i + 1
    if y > 0:
        return False    
    else:
        return True

#określenie ile liczb jest w wyświetlaczu i odjęcie od nich znaków ("." i "-")
def liczenieliczb():
    i = 0
    y = 0
    while i < len(wyswietlacz):
            if wyswietlacz[i] == "." or wyswietlacz[i] == "-":
                y = y + 1
                i = i + 1
            else:
                i = i + 1
    z = len(wyswietlacz) - y
    return z

#wyswietlanie całej liczby z listy
def wyswietlanie():
    global x
    x = ""
    if liczenieliczb()<=8:  #wyświetlanie liczb mieszczących się w limicie znakowym
        for i in wyswietlacz:
            y = str(i)
            x = x+y
        wyswietl.set(x)
    elif liczenieliczb()>8 and czyjest0(wyswietlacz) == False: #liczby powyżej 8 znaków sązaokrąglane do maksywalnie 3 liczb po przecinku
        for i in wyswietlacz:
            y = str(i)
            x = x+y
        if liczbyprzed() <= 5:
            x = round(float(x), 3)
            wyswietl.set(x)
        elif liczbyprzed() == 6:
            x = round(float(x), 2)
            wyswietl.set(x)
        elif liczbyprzed() == 7:
            x = round(float(x), 1)
            wyswietl.set(x)
        elif liczbyprzed() >= 8:
            wyswietl.set("ERROR!!!")
            wyswietlacz.clear()
    elif liczenieliczb()>8 and czyjest0(wyswietlacz) == True: #dla liczb całkowitych o większej liczbie znaków niż 8 występuje błąd
        wyswietl.set("ERROR!!!")
        wyswietlacz.clear()     

#funkcje dla przycisków:

#dodawnie liczb do wyświetlacza
def plus(liczba):
    if liczenieliczb()<8:
        wyswietlacz.append(liczba)
        wyswietlanie()

#dodawanie przecinka do liczb w wyświetlaczu
def przecinek():
    l = wyswietlacz.count(".")    
    if l < 1:
        wyswietlacz.append(".")
        wyswietlanie()

#kasowanie wszystkich danych z wyswietlacza i z zapamiętanej liczby
def kasuj():
    global liczba
    wyswietlacz.clear()
    liczba = None
    wyswietlanie()

#zmiana znaku podanej liczby
def zmiana_znaku():
    l = wyswietlacz.count("-")    
    if l > 0:
        wyswietlacz.remove("-")
    else:
        wyswietlacz.insert(0, "-")
    wyswietlanie()

#cofnięcie ostatniej liczby bądź znaku
def cofnij():
    if x != "-":
        wyswietlacz.pop()
        wyswietlanie()

#funkcja odpowiadająca za dodawanie liczb
def dodaj():
    global liczba
    global dzialanie
    global x
    if liczba == None:
        liczba = float(x)
        dzialanie = "+"
        wyswietlacz.clear()
        wyswietlanie()
    else:
        liczba = liczba + float(x)
        wyswietlacz.clear()
        if czyjest0(str(liczba)) == True:
            liczba = int(liczba)
        for i in str(liczba):
            wyswietlacz.append(i)
        wyswietlanie()

#funkcja odpowiadająca za odejmowanie liczb
def minus():
    global liczba
    global dzialanie
    global x
    if liczba == None:
        liczba = float(x)
        dzialanie = "-"
        wyswietlacz.clear()
        wyswietlanie()
    else:
        liczba = liczba - float(x)
        wyswietlacz.clear()
        if czyjest0(str(liczba)) == True:
            liczba = int(liczba)
        for i in str(liczba):
            wyswietlacz.append(i)
        wyswietlanie()

#funkcja odpowiadająca za mnożenie liczb
def razy():
    global liczba
    global dzialanie
    global x
    if liczba == None:
        liczba = float(x)
        dzialanie = "*"
        wyswietlacz.clear()
        wyswietlanie()
    else:
        liczba = liczba * float(x)
        wyswietlacz.clear()
        if czyjest0(str(liczba)) == True:
            liczba = int(liczba)
        for i in str(liczba):
            wyswietlacz.append(i)
        wyswietlanie()

#funkcja odpowiadająca za dzielenie liczb
def podzielic():
    global liczba
    global dzialanie
    global x
    if liczba == None:
        liczba = float(x)
        dzialanie = "/"
        wyswietlacz.clear()
        wyswietlanie()
    else:
        if float(x) == 0:
            wyswietl.set("ERROR!!!")
            wyswietlacz.clear()
        else:
            liczba = liczba / float(x)
            wyswietlacz.clear()
            if czyjest0(str(liczba)) == True:
                liczba = int(liczba)
            for i in str(liczba):
                wyswietlacz.append(i)
            wyswietlanie()

#funkcja odpowiadająca za działanie znakku równa się
def rownasie():
    global dzialanie
    global liczba
    match dzialanie:
        case "":
            dzialanie = ""
        case "+":
            liczba = liczba + float(x)
            wyswietlacz.clear()
            if czyjest0(str(liczba)) == True:
                liczba = int(liczba)
            for i in str(liczba):
                wyswietlacz.append(i)
            wyswietlanie()
            liczba = None
            dzialanie = ""
        case "-":
            liczba = liczba - float(x)
            wyswietlacz.clear()
            if czyjest0(str(liczba)) == True:
                liczba = int(liczba)
            for i in str(liczba):
                wyswietlacz.append(i)
            wyswietlanie()
            liczba = None
            dzialanie = ""
        case "/":
            if float(x) == 0:
                wyswietl.set("ERROR!!!")
                dzialanie = ""
                wyswietlacz.clear()
            else:
                liczba = liczba / float(x)
                wyswietlacz.clear()
                if czyjest0(str(liczba)) == True:
                    liczba = int(liczba)
                for i in str(liczba):
                    wyswietlacz.append(i)
                wyswietlanie()
                liczba = None
                dzialanie = ""
        case "*":
            liczba = liczba * float(x)
            wyswietlacz.clear()
            if czyjest0(str(liczba)) == True:
                liczba = int(liczba)
            for i in str(liczba):
                wyswietlacz.append(i)
            wyswietlanie()
            liczba = None
            dzialanie = ""


#wygląd okienka kalkulatora + przyciski:

kalk = Tk()
wyswietl = StringVar()
frame = Frame(kalk, bg="Black")
photo = PhotoImage(file = "Kalkulator.png")
kalk.iconphoto(False, photo)
kalk.title("Kalkulator")
kalk.geometry("340x365")
kalk.resizable(0, 0)
kalk.config(bg="Black")
frame2 = Frame(kalk)
frame2.pack(side=TOP)
wysw = Entry(frame2, font=('arial', 50), textvariable=wyswietl, width=50, justify=RIGHT, state="disabled")
wysw.pack()
Button(frame, text="7", command=lambda: plus(7), width=8, height=4, background="SkyBlue3").grid(column=1, row=1)
Button(frame, text="4", command=lambda: plus(4), width=8, height=4, background="SkyBlue3").grid(column=1, row=2)
Button(frame, text="1", command=lambda: plus(1), width=8, height=4, background="SkyBlue3").grid(column=1, row=3)
Button(frame, text="+/-", command=zmiana_znaku, width=8, height=4, background="LightCyan3").grid(column=1, row=4)
Button(frame, text="8", command=lambda: plus(8), width=8, height=4, background="SkyBlue3").grid(column=2, row=1)
Button(frame, text="5", command=lambda: plus(5), width=8, height=4, background="SkyBlue3").grid(column=2, row=2)
Button(frame, text="2", command=lambda: plus(2), width=8, height=4, background="SkyBlue3").grid(column=2, row=3)
Button(frame, text="0", command=lambda: plus(0), width=8, height=4, background="SkyBlue3").grid(column=2, row=4)
Button(frame, text="9", command=lambda: plus(9), width=8, height=4, background="SkyBlue3").grid(column=3, row=1)
Button(frame, text="6", command=lambda: plus(6), width=8, height=4, background="SkyBlue3").grid(column=3, row=2)
Button(frame, text="3", command=lambda: plus(3), width=8, height=4, background="SkyBlue3").grid(column=3, row=3)
Button(frame, text=".", command=przecinek, width=8, height=4, background="LightCyan3").grid(column=3, row=4)
Button(frame, text="C", command=kasuj, width=9, height=4, background="Orange3").grid(column=4, row=1)
Button(frame, text="*", command=razy, width=9, height=4, background="LightCyan3").grid(column=4, row=2)
Button(frame, text="/", command=podzielic, width=9, height=4, background="LightCyan3").grid(column=4, row=3)
Button(frame, text="=", command=rownasie, width=19, height=4, background="Orange3").grid(column=4, row=4, columnspan=2)
Button(frame, text="<-", command=cofnij, width=9, height=4, background="Orange3").grid(column=5, row=1)
Button(frame, text="+", command=dodaj, width=9, height=4, background="LightCyan3").grid(column=5, row=2)
Button(frame, text="-", command=minus, width=9, height=4, background="LightCyan3").grid(column=5, row=3)
frame.pack(side=BOTTOM)
kalk.mainloop()