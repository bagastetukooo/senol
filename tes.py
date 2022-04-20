from youtube_comment_scraper_python import *
import pandas as pd

link = 'https://www.youtube.com/watch?v=T2-s6yY9yoI'
saved = 'dataset_1.csv'
youtube.open(link)

all_data = []
for i in range(0, 5): # It will scroll 10 times
    response = youtube.video_comments()
    data = response['body']
    all_data.extend(data)
df = pd.DataFrame(data)
df.to_csv(saved)