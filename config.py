#情報の取得
import os

# GitHub Secretsから環境変数を読み込む
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:8888/callback"   #自身を表す世界共通のアドレス

SCOPE = "user-library-read playlist-read-private playlist-read-public playlist-modify-private playlist-modify-public"

playlist_id = os.getenv("PLAYLIST_ID")   #お気に入りプレイリストのid
Japanese_playlist_id = os.getenv("JAPANESE_PLAYLIST_ID")   #日本語曲専用のプレイリストid
