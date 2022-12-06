from pytube import YouTube
from uploader import up
link = "https://www.youtube.com/shorts/PvgEdEstumI"
def down(link):
	yt = YouTube(link)
	ys= yt.streams.filter(progressive=True).get_highest_resolution()
	name = f"{yt.title} #shorts"
	desc = yt.description
	ys.download(output_path='/home/hackeranania/Desktop/programming languages/python/AutoTube', filename="12") 
	up(name,desc)