import re  #正規表現を使用するための標準ライブラリ
from spotify_client import SpotifyClient

def is_japanese_song(track: dict, client: SpotifyClient) -> bool:
    #判定１：曲名に日本語が含まれるかどうか
    track_name = track['name']
    if re.search(r'[ぁ-ん一-龠ァ-ン]', track_name):
        return True
    
    #判定２：アーティストのジャンルが日本語系かどうか
    artist_id = track['artists'][0]['id']
    artist_genres = client.get_artist_genres(artist_id)
    jp_genres = ['j-pop', 'anime', 'vocaloid', 'j-rock', 'kayokyoku', 'j-r&b', 'j-rap', 'japanese indie']
    if any(genre for genre in artist_genres if genre in jp_genres):
        return True

    return False