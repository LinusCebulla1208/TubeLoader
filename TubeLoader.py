from pytube import YouTube

URL = input("Bitte geben sie die URL, oder Video-ID des Videos ein:") #URL abfragen
URL2 = "https://www.youtube.com/watch"+"?"+"v"+"="+URL
if URL[0]=='h':
    yt = YouTube(URL)
else:
    yt = YouTube(URL2)

jn = input(f"Video {yt.title} herunterladen? Die Datei wird im aktuellen Ordner gespeichert [J/N]")

if jn=='J':
    stream = yt.streams.first()
    stream.download()
    print("Ihr Video wurde erfolgreich heruntergeladen.")
else:
    pass