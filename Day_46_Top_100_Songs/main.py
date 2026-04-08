from bs4 import BeautifulSoup
import requests
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery


def authentication():
    """Authenticate the user and create a YouTube API client."""
    global youtube
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "credentials.json"

    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server(port=9090)
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)


def playlist_creation():
    """Create a new YouTube playlist."""
    global playlist_id

    request_to_create_playlist = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"Top 100 songs of {user_choosen_date}",
                "description": f"This playlist contains the top 100 songs of {user_choosen_date}.",
                "tags": [
                    "sample playlist",
                    "API call"
                ],
                "defaultLanguage": "en"
            },
            "status": {
                "privacyStatus": "private"
            }
        }
    )

    response_for_playlist_creation = request_to_create_playlist.execute()
    playlist_id = response_for_playlist_creation["id"]


def search_videos(each_song_title):
    """"Search for a video on YouTube using the song title and returns the video ID."""

    request_to_search_for_videos_using_title = youtube.search().list(
        part="snippet",
        maxResults=1,
        q=each_song_title
    )

    response_for_video_search = request_to_search_for_videos_using_title.execute()

    try:
        global video_id
        video_id = response_for_video_search["items"][0]["id"]["videoId"]

    except:
        return "No video found"


def add_video_to_playlist_using_video_id():
    """Add a video to the created playlist using the video ID."""

    request_to_add_video_to_playlist_using_video_id = youtube.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": playlist_id,
                "position": 0,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    )

    response_for_adding_video_to_playlist = request_to_add_video_to_playlist_using_video_id.execute()


# Asks user for date input and scrapes the Billboard website for the top 100 songs and their artists on that date.

user_choosen_date = input(
    "Which date do you want for the top 100 songs? Type in this format YYYY-MM-DD:    ")
URL = f"https://www.billboard.com/charts/hot-100/{user_choosen_date}"


response = requests.get(URL)
website_html = response.text


# Using soup to parse the HTML and extract the song titles and artist names. The song titles are stored in a list called top_100_songs_for_date and the artist names are stored in a list called list_of_artist_names.

soup = BeautifulSoup(website_html, "html.parser")
song_titles = soup.select("li ul li h3")
finding_artists_names = soup.find_all(class_="c-label a-no-trucate a-font-secondary u-font-size-15 u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px a-children-link-color-black a-children-link-color-brand-secondary:hover lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max")
artist_names = [each_artist_name.get_text(strip=True).replace('Featuring', ' ').replace(
    '&', ' ').replace(',', ' ') for each_artist_name in finding_artists_names]
top_100_songs_for_date = [each_song_title.getText().strip()
                          for each_song_title in song_titles]
song_search_title = [top_100_songs_for_date[index] + " " +
                     artist_names[index] for index in range(len(artist_names))]


# Authenticate the user, create a new playlist on YouTube, search for each song on YouTube using the song title and artist name, and add the found video to the created playlist. If a video is not found for a song, it will skip that song and move on to the next one.

authentication()
playlist_creation()

for each_song_title in song_search_title:
    search_videos(each_song_title)
    if search_videos(each_song_title) == "No video found":
        break
    else:
        add_video_to_playlist_using_video_id()
