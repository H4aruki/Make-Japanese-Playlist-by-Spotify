import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#情報の取得
CLIENT_ID = "d60d3661cc3f482788ee8c55b3a1e462"
CLIENT_SECRET = "3ec43494061d498cb899a383bb9da8b7"   #公開禁止
REDIRECT_URI = "http://127.0.0.1:8888/callback"

#スコープの設定
SCOPE = "user-read-private"

auth_manager = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=SCOPE)

sp = spotipy.Spotify(auth_manager=auth_manager)

#テスト
user_info = sp.current_user()
print(user_info)