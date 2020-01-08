from pytube import YouTube

URL = input("Bitte fügen sie die Video-URL ein:") #URL abfragen
yt = YouTube(URL)
jn = input(f"Video {yt.title} herunterladen? Die Datei wird im Ordner TubeLoader gespeichert [J/N]")
if jn=='J':
    stream = yt.streams.first()
    stream.download()
    print("Ihr Video wurde erfolgreich heruntergeladen.")
else:
    pass