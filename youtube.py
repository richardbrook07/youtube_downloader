from pytube import YouTube
import pytube
try:
    video_url = 'https://www.youtube.com/watch?v=mUs97qXjw1M'
    youtube = pytube.YouTube(video_url)
    video = youtube.streams.first()
    video.download('E:\youtube-download')
    print("Download Successfull !!")
except:
    print("Something Went Wrong !!")
