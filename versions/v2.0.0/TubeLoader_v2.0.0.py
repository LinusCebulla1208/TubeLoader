from pytube import YouTube

def printList(l):   #Liste "geordnet" ausgeben
    for i in range(len(l)):
        print(l[i])

def urlAbfragen():
    URL = input("Bitte geben sie die URL, oder Video-ID des Videos ein:") #URL abfragen
    URL2 = "https://www.youtube.com/watch"+"?"+"v"+"="+URL
    if URL[:8]=='https://':  #wenn URL eingegeben
        global yt
        yt = YouTube(URL)
        Hauptmenue1()
    else:
        yt = YouTube(URL2)  #wenn Video-ID eingegeben

def Hauptmenue1():
    print("1: Alle Streams anzeigen.")
    print("2: Alle progressiven Streams(Bild+Ton zusammen) anzeigen(empfohlen).")
    print("3: Nur MPEG4 herunterladen(empfohlen).")
    print("4: Nur Audio herunterladen.")
    print("5: Zurück.")
    print("6: Programm schließen.")

    global o1
    o1 = input("Bitte geben sie die Zahl vor der jeweiligen Option ein:")
    
    Hauptmenue2()

def Hauptmenue2():

    if o1=='1':
        printList(yt.streams.all())
        o2 = input("Bitte geben sie die Zahl hinter 'itag=' der jeweiligen Option ein, oder 0, um zurück zum Hauptmenü zu gelangen:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Video {yt.title} herunterladen? Die Datei wird im aktuellen Ordner gespeichert [J/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()

    elif o1=='2':
        printList(yt.streams.filter(progressive=True).all())
        o2 = input("Bitte geben sie die Zahl hinter 'itag=' der jeweiligen Option ein, oder 0, um zurück zum Hauptmenü zu gelangen:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Video {yt.title} herunterladen? Die Datei wird im aktuellen Ordner gespeichert [J/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()

    elif o1=='3':
        printList(yt.streams.filter(file_extension='mp4').filter(progressive=True).all())
        o2 = input("Bitte geben sie die Zahl hinter 'itag=' der jeweiligen Option ein, oder 0, um zurück zum Hauptmenü zu gelangen:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Video {yt.title} herunterladen? Die Datei wird im aktuellen Ordner gespeichert [J/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()

    elif o1=='4':
        printList(yt.streams.filter(only_audio=True).all())
        o2 = input("Bitte geben sie die Zahl hinter 'itag=' der jeweiligen Option ein, oder 0, um zurück zum Hauptmenü zu gelangen:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Video {yt.title} herunterladen? Die Datei wird im aktuellen Ordner gespeichert [J/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()
    
    elif o1=='5':
        urlAbfragen()
    
    elif o1=='6':
        exit()
    
    else:
        print("Eingabe ungültig!")
        urlAbfragen()

print("Herzlich Willkomen bei TubeLoader!")
urlAbfragen()
Hauptmenue1()