from utils.upload_video import upload_video
import os
def up(mainname,des):
    video_data = {
            "file": "12",
            "title": f"{mainname}",
            "description": f"{des} #anania",
            "keywords":"shorts,short,satsifiying",
            "privacyStatus":"public"
    }

    print(video_data["title"])
    print("Posting Video in 5 minutes...")
    upload_video(video_data)    
    os.remove('12.mp4')
    
# up("anania","belay")