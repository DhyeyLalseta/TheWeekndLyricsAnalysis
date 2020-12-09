from secrets import *
from lyricsgenius import Genius

genius = Genius(client_access_token)

def get_artist_lyrics(artist_name: str):
    if not artist_name:
        raise ValueError("No artist name")
    genius.remove_section_headers = True
    genius.excluded_terms = ["Remix", "Live"]
    artist = genius.search_artist(artist_name)
    artist.save_lyrics("_".join((artist_name.lower()).split()) + ".json")

if __name__ == "__main__":
    get_artist_lyrics("The Weeknd")
