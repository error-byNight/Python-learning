from pytube import YouTube

# Get the YouTube video link
video_link = input("Enter the YouTube video link: ")

# Create a YouTube object
yt = YouTube(video_link)

# Get the highest resolution video stream
stream = yt.streams.get_highest_resolution()

# Download the video
stream.download()

print("Video downloaded successfully!")
