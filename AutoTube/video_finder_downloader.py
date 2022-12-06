import scrapetube
from random import randint
from short_downloader import down
videos = scrapetube.get_channel("UCDss5ff8hMkvYiY0VzuLTJQ")
lists_of_videos = []
print('starting append')
for video in videos:
    lists_of_videos.append(video['videoId'])
print('appeding finished')
    
print(len(lists_of_videos))
channel_id = lists_of_videos[randint(0,len(lists_of_videos))]

down(f"https://www.youtube.com/shorts/{channel_id}")
