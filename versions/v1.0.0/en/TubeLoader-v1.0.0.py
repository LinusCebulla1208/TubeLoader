from pytube import YouTube

URL = input("Please insert the URL of the Youtube Video:") #URL abfragen
yt = YouTube(URL)
fname = yt.title + ".mp4"
jn = input(f"Do you want to download the video '{yt.title}'? The file will be saved as '{fname}' [Y/N]")
if jn=='Y':
    stream = yt.streams.first()
    stream.download()
    print("The video was succesfully downloaded!")
else:
    pass