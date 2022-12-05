from pytube import YouTube
from sys import argv

'''
USAGE: python download_yt_vids.py YOUTUBE_LINK
       python download_yt_vids.py https://www.youtube.com/watch?v=qpyRz5lkRjE&ab_channel=LowLevelLearning

'''

link = argv[1]
yt_link = YouTube(link)

print("Title: ", yt_link.title)
print("Total view: ", yt_link.views)

yt_download = yt_link.streams.get_highest_resolution()
yt_download.download("/Users/sweth/Videos/cybersecurity")