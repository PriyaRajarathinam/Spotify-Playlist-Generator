import sys
import spotipy
import os
import spotipy.util as util

scope = 'user-library-read playlist-modify-public playlist-modify-private'


def get_user_playlists(token):
    if token:
        sp = spotipy.Spotify(auth=token)
        playlists =sp.current_user_playlists(limit=50,offset=0)
        return playlists
    else:
        print ("Can't get token for", username)
def create_playlist_from_favorites(token):
    if token:
        sp = spotipy.Spotify(auth=token)
        results = sp.current_user_saved_tracks()
        curr_user_id=sp.current_user()['id']
        print(sp.current_user()['id'])
        fav_playlist = sp.user_playlist_create(curr_user_id,"temp",public=True)
        print(fav_playlist)
        for item in results['items']:
            track = item['track']
            tracks = []
            tracks.append(track['uri'])
            print(sp.audio_analysis(track['uri']))
            temp = sp.user_playlist_add_tracks(curr_user_id,fav_playlist['id'],tracks,position=None)
            print (track['name'] + ' - ' + track['artists'][0]['name'])
    
    else:
        print ("Can't get token for", username)


if __name__ == "__main__":
    cmds=["export SPOTIPY_CLIENT_ID='0ceb01c560f34814ad5b5ae57adc0f0b'","export SPOTIPY_CLIENT_SECRET='f725256974624e968cb191cade4acd43'","export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback/'"]
    for cmd in cmds:
        print(cmd)
        os.system(cmd)
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: ",sys.argv[0], "username")
        sys.exit()

    token = util.prompt_for_user_token(username, scope)
    for item in get_user_playlists(token)['items']:
        print(item)
        print()
    #create_playlist_from_favorites(token)
    