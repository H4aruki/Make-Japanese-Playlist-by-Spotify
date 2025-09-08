from enum import unique
from hmac import new
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#情報の取得
CLIENT_ID = "d60d3661cc3f482788ee8c55b3a1e462"
CLIENT_SECRET = "3ec43494061d498cb899a383bb9da8b7"   #公開禁止
REDIRECT_URI = "http://127.0.0.1:8888/callback"

SCOPE = "user-library-read playlist-modify-private"

auth_manager = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=SCOPE)
sp = spotipy.Spotify(auth_manager=auth_manager)   

#ユーザー情報の取得
user_info = sp.current_user()
user_id = user_info['id']

playlist_id = "5DMEvbg3gUmiR5HIBWdveV"   #お気に入りプレイリストのid

result = sp.current_user_saved_tracks()
tracks = result['items']   #itemsは１曲の情報のすべてを取得するためのもの

while result['next']:
    result = sp.next(result)   # sp.next()で次のページのデータを取得
    tracks.extend(result['items'])

print(f"取得した曲数：{len(tracks)}")


artist_ids = []
for item in tracks:
    track = item['track']
    if track and track['artists']:
        artist_ids.append(track['artists'][0]['id'])

unique_artist_ids = list(set(artist_ids))
print(f"ユニークなアーティスト数：{len(unique_artist_ids)}")

target_genres = ['j-pop' , 'anime', 'vocaloid', 'j-rock', 'kayokyoku', 'j-r&b', 'j-rap', 'japanese indie']

#取得済みの情報からループ処理を実行
for item in tracks:
    track = item['track']
    if track:
        track_name = track['name']
        artist_name = track['artists'][0]['name']
        artist_id = track['artists'][0]['id']
        #print(f"{track_name} by {artist_name} artist_id : {artist_id}")

#アーティストIDとジャンルリストを紐付けるための辞書を作成
artist_genres_map = {}

# sp.artistsは一度に50件までしかIDを扱えないため、50件ずつに分割して処理
for i in range(0, len(unique_artist_ids), 50):
    # 50件ずつIDのリストを切り出す
    chunk = unique_artist_ids[i:i+50]
    
    # アーティスト情報をまとめて取得
    artists_info = sp.artists(chunk)
    
    # 取得した結果を辞書に格納していく
    for artist in artists_info['artists']:
        artist_id = artist['id']
        genres = artist['genres']
        artist_genres_map[artist_id] = genres
#print(artist_genres_map)


#プレイリストの定義と作成
#一度実行して作成完了しているため、以降はコメント化する
"""
playlist_name = 'Japanese'
playlist_discription = 'お気に入りからPythonで自動生成'
Japanese_playlist = sp.user_playlist_create(user = user_id, name = playlist_name, public = False, description = playlist_discription)   #プレイリストの作成
"""

Japanese_playlist_id = '7fKJmaE2tYXtX9hyX1opo9'
