from pytube import YouTube

def printList(l):   #Liste "geordnet" ausgeben
    for i in range(len(l)):
        print(l[i])

def urlAbfragen():
    URL = input("Please enter the URL, or the Video-ID of the Video you want to download:") #URL abfragen
    URL2 = "https://www.youtube.com/watch"+"?"+"v"+"="+URL
    if URL[:8]=='https://':  #wenn URL eingegeben
        global yt
        yt = YouTube(URL)
        Hauptmenue1()
    else:
        yt = YouTube(URL2)  #wenn Video-ID eingegeben

def Hauptmenue1():
    print("1: Show all - not recommended.")
    print("2: Show only progressive(audio+video in one file) - recommended.")
    print("3: Show only MPEG4 - recommended.")
    print("4: Show only audio - recommended.")
    print("5: Back.")
    print("6: Quit.")

    global o1
    o1 = input("Please enter the Number of the option you want to run:")
    
    Hauptmenue2()

def Hauptmenue2():

    if o1=='1':
        printList(yt.streams.all())
        o2 = input("Please enter the number behind the 'itag=' of the respectiveo option, or enter 0, to go back to the main menu:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Do you want to download the video '{yt.title}'? The file will be saved in the current folder [Y/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()

    elif o1=='2':
        printList(yt.streams.filter(progressive=True).all())
        o2 = input("Please enter the number behind the 'itag=' of the respectiveo option, or enter 0, to go back to the main menu:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Do you want to download the video '{yt.title}'? The file will be saved in the current folder [Y/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()

    elif o1=='3':
        printList(yt.streams.filter(file_extension='mp4').filter(progressive=True).all())
        o2 = input("Please enter the number behind the 'itag=' of the respectiveo option, or enter 0, to go back to the main menu:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Do you want to download the video '{yt.title}'? The file will be saved in the current folder [Y/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()

    elif o1=='4':
        printList(yt.streams.filter(only_audio=True).all())
        o2 = input("Please enter the number behind the 'itag=' of the respectiveo option, or enter 0, to go back to the main menu:")
        if o2=='0':
            Hauptmenue1()
        stream = yt.streams.get_by_itag(o2)
        jn = input(f"Do you want to download the video '{yt.title}'? The file will be saved in the current folder [Y/N]")
        if jn.lower()=='j':
            stream.download()
        else:
            Hauptmenue1()
    
    elif o1=='5':
        urlAbfragen()
    
    elif o1=='6':
        exit()
    
    else:
        print("You entered an invalid numer/charakter!")
        Hauptmenue1()

print("Welcome to TubeLoader!")
urlAbfragen()
Hauptmenue1()