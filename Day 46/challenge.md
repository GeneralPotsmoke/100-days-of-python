#### Day 46: Create a Spotify Playlist using the Musical Time Machine
**Challenge:** Create a program that generates a Spotify playlist based on top songs from a given year.

```python
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private"))

year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{year}")
soup = BeautifulSoup(response.content, "html.parser")
song_titles = [song.getText().strip() for song in soup.find_all("span", class_="chart-element__information__song")]

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{year} Billboard 100", public=False)

track_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year.split('-')[0]}", type="track")
    try:
        track_uri = result["tracks"]["items"][0]["uri"]
        track_uris.append(track_uri)
    except IndexError:
        print(f"{song} not found on Spotify. Skipped.")

sp.playlist_add_items(playlist_id=playlist["id"], items=track_uris)
```


