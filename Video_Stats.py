import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Set up OAuth2 credentials
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    "client_secret.json", scopes
)
credentials = flow.run_console()

# Build the YouTube API client
youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

# Enter the ID of the YouTube video you want to get a summary for
video_id = "nGUMw5an7rg"

# Get the video details
video_response = youtube.videos().list(
    part="snippet,statistics",
    id=video_id
).execute()

# Extract the relevant information from the video response
video_details = video_response["items"][0]["snippet"]
video_statistics = video_response["items"][0]["statistics"]
view_count = video_statistics["viewCount"]
like_count = video_statistics["likeCount"]
comment_count = video_statistics["commentCount"]
title = video_details["title"]
description = video_details["description"]
channel_title = video_details["channelTitle"]
published_at = video_details["publishedAt"]

# Print the summary of the video
print(f"Title: {title}")
print(f"Description: {description}")
print(f"Channel: {channel_title}")
print(f"Published At: {published_at}")
print(f"Views: {view_count}")
print(f"Likes: {like_count}")
print(f"Comments: {comment_count}")
